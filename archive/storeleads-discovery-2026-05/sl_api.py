#!/usr/bin/env python3
"""
Capture the Store Leads data-API QUERY SCHEMA (request bodies) + key response bodies,
so we can drive store discovery via the JSON API instead of the Shadow-DOM UI.

Saves: request payloads (printed) + full responses for domains / dashboard-load / platforms.
Usage (on VPS): python3 /opt/market-research-agent/scripts/sl_api.py [url]
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

reqs = []
SAVE = {'domains': 'domains', 'dashboard-load': 'dashboard_load', 'domains/platforms': 'platforms'}

def on_request(req):
    try:
        if '/json/auth/' in req.url and req.method == 'POST':
            reqs.append({'url': req.url, 'post': req.post_data})
    except Exception:
        pass

def on_response(resp):
    try:
        if '/json/auth/' in resp.url and resp.status == 200 and 'json' in resp.headers.get('content-type', ''):
            for key, tag in SAVE.items():
                if resp.url.endswith('/json/auth/' + key):
                    with open(f'{OUT}/full_{tag}.json', 'w') as f:
                        f.write(resp.text())
    except Exception:
        pass

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={'width': 1600, 'height': 1600})
    pg = ctx.new_page()
    pg.on('request', on_request)
    pg.on('response', on_response)
    pg.goto(URL, wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(6000)
    b.close()

print(f'--- {len(reqs)} POST /json/auth/ request bodies ---')
for r in reqs:
    print('\nURL:', r['url'])
    print('POST:', (r['post'] or '')[:1500])
print('\nsaved response bodies: full_domains.json / full_dashboard_load.json / full_platforms.json')
print('=== SL API DONE ===')
