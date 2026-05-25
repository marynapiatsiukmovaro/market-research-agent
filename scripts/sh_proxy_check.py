#!/usr/bin/env python3
# Proxy health-check. Exit 0 + "PROXY_OK <ip>" if proxy works; exit 1 + "PROXY_FAIL ..." otherwise.
import sys
from playwright.sync_api import sync_playwright
creds = {}
for line in open('/opt/market-research-agent/cookies/proxy.creds'):
    if '=' in line:
        k, v = line.strip().split('=', 1)
        creds[k] = v
proxy = {'server': 'http://%s:%s' % (creds['PROXY_HOST'], creds['PROXY_PORT']),
         'username': creds['PROXY_USER'], 'password': creds['PROXY_PASS']}
try:
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=['--no-sandbox'], proxy=proxy)
        pg = b.new_context().new_page()
        pg.goto('https://api.ipify.org?format=json', timeout=20000)
        ip = pg.eval_on_selector('body', 'e=>e.innerText')[:60]
        b.close()
    print('PROXY_OK', ip)
    sys.exit(0)
except Exception as e:
    print('PROXY_FAIL', type(e).__name__, str(e)[:80])
    sys.exit(1)
