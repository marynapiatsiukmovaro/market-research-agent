#!/usr/bin/env python3
"""
Crack the /json/auth/domains filter payload format using the logged-in session.
Replays a list of candidate filter bodies via the page's own fetch() (so cookies + any
CSRF are exactly as the app sends them) and prints totalHits + parsed-request echo +
a 2-store sample. Gentle: small list, 1.5s apart.

Run on VPS: python3 scripts/sl_query.py
"""
import json, time
from playwright.sync_api import sync_playwright

BASE = '/opt/market-research-agent'
STATE = f'{BASE}/cookies/storeleads_state.json'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')

TESTS = [
    {"f:p": "1", "f:ds": "1", "f:cc": "US", "f:cat": "/Home & Garden/Kitchen & Dining"},
    {"f:p": "1", "f:ds": "1", "f:cc": "GB", "f:cat": "/Home & Garden/Kitchen & Dining"},
    {"f:p": "1", "f:ds": "1", "f:cc": "US", "f:cat1": "Home & Garden"},
    {"f:p": "1", "f:ds": "1", "f:cc": "US,GB", "f:cat1": "Home & Garden"},
    {"f:p": "1", "f:ds": "1", "f:cat1": "Home & Garden", "f:cc": "US,GB,DE,CA,AU,NZ"},
]

JS = """async (bodyStr) => {
  const m = document.cookie.match(/X-CSRF-TOKEN=([^;]+)/);
  const headers = {'Content-Type':'application/json'};
  if (m) headers['X-CSRF-TOKEN'] = decodeURIComponent(m[1]);
  const r = await fetch('/json/auth/domains', {method:'POST', headers, body:bodyStr, credentials:'include'});
  let j=null; try{ j = await r.json(); }catch(e){}
  return {status:r.status, totalHits:j&&j.totalHits, request:j&&j.request,
          next:(j&&j.next_cursor)?String(j.next_cursor).slice(0,16):null,
          sample:((j&&j.domains)||[]).slice(0,2).map(d=>({n:d.name, cat:d.cat, apf:d.apf, erf:d.erf, created:d.createdAt}))};
}"""

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={'width': 1400, 'height': 1000})
    pg = ctx.new_page()
    pg.goto('https://storeleads.app/dashboard/domains', wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(3000)
    for body in TESTS:
        bs = json.dumps(body)
        try:
            res = pg.evaluate(JS, bs)
        except Exception as e:
            res = {'error': f'{type(e).__name__}: {e}'}
        print('\nBODY:', bs)
        print('  status:', res.get('status'), '| totalHits:', res.get('totalHits'), '| next:', res.get('next'))
        print('  request-echo:', json.dumps(res.get('request'), ensure_ascii=False)[:500])
        print('  sample:', json.dumps(res.get('sample'), ensure_ascii=False)[:400])
        time.sleep(1.5)
    b.close()
print('\n=== SL QUERY DONE ===')
