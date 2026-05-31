#!/usr/bin/env python3
"""Stage-1 table builder. Dump a subcategory (term filters), extract the agreed fields,
client-filter Created>=2020, sort by Est Visits desc. Saves full JSON + prints sample.
Usage: python3 scripts/sl_dump2.py "<cat path>" [pages]"""
import json, sys, re, time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
CAT=sys.argv[1] if len(sys.argv)>1 else "/Home & Garden/Home Improvement"
PAGES=int(sys.argv[2]) if len(sys.argv)>2 else 20
FETCH="""async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {total:j&&j.totalHits, next:j&&j.next_cursor, domains:(j&&j.domains)||[]};
}"""
def social(ids, kind):
    for it in ids or []:
        u=(it.get('full_value') or it.get('value') or '')
        if kind in str(u).lower(): return u
    return ''
def row(d):
    ids=d.get('identifiers')
    return {"domain":d.get('name') or d.get('tld1'),"merchant":d.get('merchantName'),
        "country":d.get('countryCode'),"created":str(d.get('createdAt') or '')[:10],
        "visits":d.get('mvis'),"pageviews":d.get('mpv'),"sales":d.get('erf'),
        "avg_price":d.get('apf'),"min_price":d.get('minpf'),"max_price":d.get('maxpf'),
        "app_spend":d.get('masf'),"rank":d.get('rank'),"prank":d.get('prank'),
        "lang":d.get('langn'),"loc":d.get('loc'),"theme":d.get('themeName'),"theme_vendor":d.get('themeVendor'),
        "meta_desc":(d.get('md') or '')[:160],
        "reviews":d.get('combrs') or d.get('tprs'),
        "fb":social(ids,'facebook'),"ig":social(ids,'instagram'),"tiktok":social(ids,'tiktok')}
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    base={"f:p":"1","f:ds":"1","f:cat":CAT}
    r=pg.evaluate(FETCH,json.dumps(base)); total=r.get("total")
    seen={}; rows=[]
    def ingest(ds):
        for d in ds:
            i=d.get("id")
            if i not in seen: seen[i]=1; rows.append(row(d))
    ingest(r.get("domains") or []); nxt=r.get("next")
    for _ in range(PAGES-1):
        if not nxt: break
        r=pg.evaluate(FETCH,json.dumps({**base,"cursor":nxt})); time.sleep(0.8)
        ds=r.get("domains") or []
        if not ds: break
        ingest(ds); nxt=r.get("next")
    b.close()
def yr(s):
    try: return int(str(s)[:4])
    except: return 0
g=[x for x in rows if yr(x["created"])>=2020]
g.sort(key=lambda x:(x["visits"] or 0),reverse=True)
json.dump(g,open(f"{OUT}/himprov_table.json","w"),ensure_ascii=False)
print(f"category total(hits)={total} | collected(by rank)={len(rows)} | >=2020={len(g)} (saved himprov_table.json)")
print(f"\n{'#':>2} {'domain':28} {'visits':>8} {'sales/mo':>13} {'avgP':>7} {'created':>10} {'rank':>6}  social")
for i,x in enumerate(g[:25],1):
    soc=''.join(['F' if x['fb'] else '-','I' if x['ig'] else '-','T' if x['tiktok'] else '-'])
    print(f"{i:>2} {str(x['domain'])[:28]:28} {str(x['visits']):>8} {str(x['sales'])[:13]:>13} {str(x['avg_price'])[:7]:>7} {x['created']:>10} {str(x['rank']):>6}  {soc}")
print("=== DUMP2 DONE ===")
