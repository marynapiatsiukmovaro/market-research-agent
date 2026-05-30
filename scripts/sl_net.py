#!/usr/bin/env python3
"""
Capture the data API behind the Store Leads dashboard (logged-in) + probe frames/shadow DOM.
Logs JSON/XHR responses (url, status, top-level keys / length) so we learn how to scrape
cleanly. Screenshots the page too.

Usage (on VPS): python3 /opt/market-research-agent/scripts/sl_net.py [url]
"""
import os, sys, json
from playwright.sync_api import sync_playwright

BASE = '/opt/market-research-agent'
STATE = f'{BASE}/cookies/storeleads_state.json'
OUT = f'{BASE}/logs/storeleads'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
URL = sys.argv[1] if len(sys.argv) > 1 else 'https://storeleads.app/dashboard/domains'
os.makedirs(OUT, exist_ok=True)

records = []

def on_response(resp):
    try:
        ct = resp.headers.get('content-type', '')
        rt = resp.request.resource_type
        if 'application/json' in ct or rt in ('xhr', 'fetch'):
            rec = {'url': resp.url, 'status': resp.status, 'method': resp.request.method,
                   'rtype': rt, 'ct': ct[:40]}
            if 'application/json' in ct and resp.status == 200:
                try:
                    data = resp.json()
                    if isinstance(data, dict):
                        rec['keys'] = list(data.keys())[:15]
                        # peek at a list-ish field
                        for k, v in data.items():
                            if isinstance(v, list):
                                rec[f'len_{k}'] = len(v)
                                if v and isinstance(v[0], dict):
                                    rec[f'sample_{k}_keys'] = list(v[0].keys())[:25]
                                break
                    elif isinstance(data, list):
                        rec['list_len'] = len(data)
                        if data and isinstance(data[0], dict):
                            rec['item_keys'] = list(data[0].keys())[:25]
                except Exception:
                    rec['json'] = 'unreadable'
            records.append(rec)
            # save full body of promising data calls
            if 'application/json' in ct and resp.status == 200 and any(
                    s in resp.url for s in ('domain', 'search', 'query', 'result', 'list')):
                try:
                    fn = f"{OUT}/api_{abs(hash(resp.url))%10000}.json"
                    with open(fn, 'w') as f:
                        f.write(resp.text()[:200000])
                    rec['saved'] = fn
                except Exception:
                    pass
    except Exception:
        pass

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA,
                        viewport={'width': 1600, 'height': 1600})
    pg = ctx.new_page()
    pg.on('response', on_response)
    pg.goto(URL, wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(6000)
    pg.screenshot(path=f'{OUT}/net_page.png', full_page=True)

    # frame + shadow probe
    frames = [{'url': f.url, 'name': f.name} for f in pg.frames]
    shadow_hosts = pg.evaluate("""() => {
        let n = 0; const tags = new Set();
        const walk = (root) => { root.querySelectorAll('*').forEach(el => {
            if (el.shadowRoot) { n++; tags.add(el.tagName.toLowerCase()); walk(el.shadowRoot); }
        }); };
        walk(document); return {count:n, tags:[...tags].slice(0,15)};
    }""")
    body_len = len(pg.evaluate('document.body.innerText') or '')

    print('URL        :', pg.url)
    print('frames     :', frames)
    print('shadowDOM  :', shadow_hosts)
    print('body.innerText length:', body_len)
    print(f'\n--- {len(records)} JSON/XHR responses captured ---')
    for r in records:
        print(json.dumps(r, ensure_ascii=False))
    b.close()
print('\n=== SL NET DONE ===')
