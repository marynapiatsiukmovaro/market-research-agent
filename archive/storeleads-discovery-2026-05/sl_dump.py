#!/usr/bin/env python3
"""
Store Leads Stage-0 dump via the logged-in JSON API (gentle, session fetch).
Pilot recipe: Shopify + Active + US + Home&Garden/Kitchen&Dining, then client-side
filters (created>=2020, monthly est revenue <= $1M, avg price <= $350). Paginates via
the discovered cursor key. Saves full JSON to logs/storeleads/ + prints a compact table.

Run on VPS: python3 scripts/sl_dump.py [want_survivors]
"""
import json, sys, re, time
from playwright.sync_api import sync_playwright

BASE = '/opt/market-research-agent'
STATE = f'{BASE}/cookies/storeleads_state.json'
OUT = f'{BASE}/logs/storeleads'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')

WANT = int(sys.argv[1]) if len(sys.argv) > 1 else 200
BASEQ = {"f:p": "1", "f:ds": "1", "f:cc": "US", "f:cat": "/Home & Garden/Kitchen & Dining"}
CURSOR_KEYS = ["c", "next_cursor", "cursor", "sa", "after", "sc"]

FETCH = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/);
  const h={'Content-Type':'application/json'}; if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  const map=d=>({id:d.id,name:d.name,merch:d.merchantName||d.cn,cc:d.countryCode,cat:d.cat,
    apf:d.apf,erf:d.erf,er:d.er,ap:d.ap,created:d.createdAt,pc:d.pc,
    rev:(d.combrs||d.tprs||null),mrpp:(d.mrpp&&d.mrpp.published_at)||null,plan:d.plan,
    fbpx:(Array.isArray(d.tech)?d.tech.some(t=>/facebook pixel/i.test(t.name||'')):false)});
  return {status:r.status, total:j&&j.totalHits, next:j&&j.next_cursor,
          domains:((j&&j.domains)||[]).map(map)};
}"""


def num(s):
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return float(s)
    m = re.findall(r'[\d.]+', str(s).replace(',', ''))
    return float(m[0]) if m else None


def keep(d):
    yr = None
    if d.get('created'):
        try:
            yr = int(str(d['created'])[:4])
        except Exception:
            yr = None
    if yr is not None and yr < 2020:
        return False
    rev = d.get('er')  # monthly revenue (cents-ish int); erf is formatted
    if rev is None:
        rev = num(d.get('erf'))
    # er appears to be monthly*100; erf formatted = monthly $. use erf number.
    rev_m = num(d.get('erf'))
    if rev_m is not None and rev_m > 1_000_000:
        return False
    price = num(d.get('apf'))
    if price is not None and price > 350:
        return False
    return True


with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={'width': 1400, 'height': 1000})
    pg = ctx.new_page()
    pg.goto('https://storeleads.app/dashboard/domains', wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(2500)

    page1 = pg.evaluate(FETCH, json.dumps(BASEQ))
    total = page1.get('total')
    seen = {}
    raw = []
    for d in page1['domains']:
        if d['id'] not in seen:
            seen[d['id']] = 1; raw.append(d)
    first_id = page1['domains'][0]['id'] if page1['domains'] else None

    # discover cursor key
    cur_key = None
    nxt = page1.get('next')
    if nxt:
        for k in CURSOR_KEYS:
            body = dict(BASEQ); body[k] = nxt
            r = pg.evaluate(FETCH, json.dumps(body))
            ds = r.get('domains') or []
            if ds and ds[0]['id'] != first_id:
                cur_key = k
                # ingest this page
                for d in ds:
                    if d['id'] not in seen:
                        seen[d['id']] = 1; raw.append(d)
                nxt = r.get('next')
                break
            time.sleep(0.8)
    print(f'total_hits={total} | cursor_key={cur_key} | after-discovery raw={len(raw)}')

    survivors = [d for d in raw if keep(d)]
    pages = 2
    while cur_key and nxt and len(survivors) < WANT and pages < 25:
        body = dict(BASEQ); body[cur_key] = nxt
        r = pg.evaluate(FETCH, json.dumps(body))
        ds = r.get('domains') or []
        new = 0
        for d in ds:
            if d['id'] not in seen:
                seen[d['id']] = 1; raw.append(d); new += 1
        nxt = r.get('next')
        survivors = [d for d in raw if keep(d)]
        pages += 1
        if not new:
            break
        time.sleep(1.0)

    survivors = survivors[:WANT]
    with open(f'{OUT}/kd_us_raw.json', 'w') as f:
        json.dump(raw, f)
    with open(f'{OUT}/kd_us_survivors.json', 'w') as f:
        json.dump(survivors, f)

    print(f'pages_fetched={pages} | raw_collected={len(raw)} | survivors(after client filters)={len(survivors)}')
    print('\n# | domain | merchant | est$/mo | avgPrice | created | reviews | #prod | FBpx')
    for i, d in enumerate(survivors[:30], 1):
        rev = d.get('rev') or {}
        rv = f"{rev.get('review_count','')}/{rev.get('avg_rating','')}" if rev else '-'
        print(f"{i:>2} | {str(d.get('name'))[:30]:<30} | {str(d.get('merch'))[:18]:<18} | "
              f"{str(d.get('erf'))[:14]:<14} | {str(d.get('apf'))[:10]:<10} | "
              f"{str(d.get('created'))[:10]} | {rv:<10} | {str(d.get('pc'))[:6]:<6} | {d.get('fbpx')}")
    b.close()
print('\n=== SL DUMP DONE ===')
