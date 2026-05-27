#!/usr/bin/env python3
# Deeper proxy diagnostic: tests the proxy against the REAL workload (Shopify /products.json)
# AND multiple IP-echo endpoints, with retries + timing — to tell apart "proxy down" from
# "one test endpoint (ipify) is flaky". Mirrors sh_enrich_final.py settings (30s, retry).
import sys, time
from playwright.sync_api import sync_playwright
creds = {}
for line in open('/opt/market-research-agent/cookies/proxy.creds'):
    if '=' in line:
        k, v = line.strip().split('=', 1); creds[k] = v
PROXY = {'server': 'http://%s:%s' % (creds['PROXY_HOST'], creds['PROXY_PORT']),
         'username': creds['PROXY_USER'], 'password': creds['PROXY_PASS']}

TARGETS = [
    ('ipify (old check endpoint)', 'https://api.ipify.org?format=json'),
    ('ifconfig.me (alt IP echo)', 'https://ifconfig.me/ip'),
    ('Shopify products.json (REAL workload)', 'https://uahpet.com/products.json?limit=3'),
    ('Shopify products.json #2', 'https://waggingrightsusa.com/products.json?limit=3'),
]

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'], proxy=PROXY)
    for label, url in TARGETS:
        ok = False
        for attempt in range(1, 4):
            t0 = time.time()
            try:
                ctx = b.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0 Safari/537.36')
                pg = ctx.new_page()
                pg.goto(url, wait_until='domcontentloaded', timeout=30000)
                body = pg.eval_on_selector('body', 'e=>e.innerText')[:120]
                dt = time.time() - t0
                print('OK   [%s] try%d %.1fs :: %s' % (label, attempt, dt, body.replace(chr(10), ' ')[:90]))
                ctx.close(); ok = True; break
            except Exception as e:
                dt = time.time() - t0
                print('FAIL [%s] try%d %.1fs :: %s %s' % (label, attempt, dt, type(e).__name__, str(e)[:60]))
                try: ctx.close()
                except Exception: pass
                time.sleep(2)
        if not ok:
            print('   -> %s UNREACHABLE after 3 tries' % label)
    b.close()
print('=== DIAG DONE ===')
