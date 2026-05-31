#!/usr/bin/env python3
"""
Recon the Store Leads LOGIN page (no auth, no secrets) to learn the sign-in mechanism:
email field? code vs magic-link? Google-only? Lists inputs/buttons + screenshots.

Usage (on VPS): python3 /opt/market-research-agent/scripts/sl_login_recon.py
"""
import os
from playwright.sync_api import sync_playwright

OUT = '/opt/market-research-agent/logs/storeleads'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
CANDIDATES = [
    'https://storeleads.app/',
    'https://storeleads.app/app',
    'https://storeleads.app/login',
    'https://storeleads.app/signin',
    'https://storeleads.app/sign-in',
]
os.makedirs(OUT, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(user_agent=UA, viewport={'width': 1440, 'height': 1400}, device_scale_factor=2)
    pg = ctx.new_page()
    for url in CANDIDATES:
        tag = url.rstrip('/').split('/')[-1] or 'home'
        try:
            pg.goto(url, wait_until='networkidle', timeout=45000)
            pg.wait_for_timeout(2500)
        except Exception as e:
            print(f'\n=== {url} -> ERR {type(e).__name__}')
            continue
        final = pg.url
        title = pg.title()
        inputs = pg.evaluate("""() => Array.from(document.querySelectorAll('input')).map(i => ({
            type: i.type, name: i.name, placeholder: i.placeholder, id: i.id, autocomplete: i.autocomplete}))""")
        buttons = pg.evaluate("""() => Array.from(document.querySelectorAll('button, a[role=button], input[type=submit]'))
            .map(b => (b.innerText||b.value||'').trim()).filter(t => t.length>0 && t.length<40).slice(0,30)""")
        body = (pg.evaluate('document.body.innerText') or '')
        low = body.lower()
        hints = {
            'google': 'google' in low,
            'magic/link': ('magic' in low) or ('link to' in low) or ('login link' in low) or ('email you a link' in low),
            'code/otp': ('code' in low) or ('one-time' in low) or ('verification' in low) or ('otp' in low),
            'password': 'password' in low,
            'check your email': 'check your email' in low or 'sent you' in low,
        }
        pg.screenshot(path=f'{OUT}/sl_login_{tag}.png', full_page=True)
        print(f'\n=== {url}  ->  {final}')
        print('title   :', title)
        print('inputs  :', inputs)
        print('buttons :', buttons)
        print('hints   :', {k: v for k, v in hints.items() if v})
        print('text[:400]:', body[:400].replace('\n', ' '))
    b.close()
print('\n=== SL LOGIN RECON DONE ===')
