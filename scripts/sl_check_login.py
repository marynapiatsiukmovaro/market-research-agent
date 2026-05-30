#!/usr/bin/env python3
"""
Verify the imported Store Leads session works on the VPS (headless Playwright).

Usage (on VPS):
    python3 /opt/market-research-agent/scripts/sl_check_login.py [url]

Loads cookies/storeleads_state.json into a headless context, navigates to the given
Store Leads URL (default the app home), screenshots it, and dumps the visible text so we
can confirm we are LOGGED IN (not bounced to a Sign-in page). Screenshot + text go to
logs/storeleads/ for scp-back review. Read-only — changes nothing in the account.
"""
import os
import sys
from playwright.sync_api import sync_playwright

STATE = '/opt/market-research-agent/cookies/storeleads_state.json'
OUT = '/opt/market-research-agent/logs/storeleads'
URL = sys.argv[1] if len(sys.argv) > 1 else 'https://storeleads.app/'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')

os.makedirs(OUT, exist_ok=True)
if not os.path.exists(STATE):
    print('ERROR: no storeleads_state.json — run set_storeleads_cookies.py first.')
    raise SystemExit(1)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA,
                        viewport={'width': 1440, 'height': 1600}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.goto(URL, wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(3000)
    final_url = pg.url
    shot = os.path.join(OUT, 'sl_login_check.png')
    pg.screenshot(path=shot, full_page=True)
    text = pg.evaluate('document.body.innerText') or ''
    low = text.lower()

    logged_out = any(s in low for s in ['sign in with google', 'log in', 'sign in', 'create account'])
    logged_in = any(s in low for s in ['log out', 'logout', 'sign out', 'account', 'dashboard',
                                       'searches', 'credits', 'subscription', 'my lists'])
    print('URL requested :', URL)
    print('URL final     :', final_url)
    print('screenshot    :', shot)
    print('logged_in hints:', logged_in, '| logged_out hints:', logged_out)
    print('--- first 1500 chars of visible text ---')
    print(text[:1500])
    b.close()
print('=== SL LOGIN CHECK DONE ===')
