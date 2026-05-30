#!/usr/bin/env python3
"""
Passwordless EMAIL login to Store Leads on the VPS (Marina's idea).

storeleads.app/login is passwordless: enter email -> Store Leads emails a CODE or a
magic LINK -> complete the login. This drives that flow in ONE persistent browser on the
VPS, so whatever the email contains (code or link) finishes in the same session.

Run interactively on the VPS (needs a TTY):
    ssh -i ~/.ssh/market_research_vps -t root@5.78.217.133 \
        'python3 /opt/market-research-agent/scripts/sl_email_login.py'

You will be asked for: (1) your Store Leads email, then (2) the CODE or the full LINK
from the email. Nothing is printed back except cookie NAMES + a logged-in check.
Session is saved to a persistent profile + cookies/storeleads_state.json (gitignored).
"""
import os
from playwright.sync_api import sync_playwright

BASE = '/opt/market-research-agent'
PROFILE = f'{BASE}/cookies/storeleads_profile'
STATE = f'{BASE}/cookies/storeleads_state.json'
OUT = f'{BASE}/logs/storeleads'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
os.makedirs(OUT, exist_ok=True)
os.makedirs(PROFILE, exist_ok=True)


def dump(pg, tag):
    inputs = pg.evaluate("""() => Array.from(document.querySelectorAll('input')).map(i => ({
        type:i.type, name:i.name, placeholder:i.placeholder, id:i.id, vis:!!(i.offsetParent)}))""")
    buttons = pg.evaluate("""() => Array.from(document.querySelectorAll('button,a[role=button],input[type=submit]'))
        .map(b => (b.innerText||b.value||'').trim()).filter(t => t && t.length<40).slice(0,20)""")
    body = (pg.evaluate('document.body.innerText') or '')
    pg.screenshot(path=f'{OUT}/sl_{tag}.png', full_page=True)
    print(f'  [{tag}] url={pg.url}')
    print(f'  [{tag}] inputs={inputs}')
    print(f'  [{tag}] buttons={buttons}')
    print(f'  [{tag}] text[:300]={body[:300].strip()}')
    return inputs, body


with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        PROFILE, headless=True, user_agent=UA,
        viewport={'width': 1440, 'height': 1400}, args=['--no-sandbox'])
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()

    print('Opening login page...')
    pg.goto('https://storeleads.app/login', wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(2000)

    email = input('  Your Store Leads email: ').strip()
    if not email:
        print('ERROR: no email. Aborting.')
        raise SystemExit(1)

    pg.fill('input[name="email"]', email)
    # click the Sign in button (try a few robust ways)
    for sel in ['button:has-text("Sign in")', 'input[type=submit]', 'button[type=submit]']:
        try:
            if pg.locator(sel).count():
                pg.locator(sel).first.click()
                break
        except Exception:
            pass
    pg.wait_for_timeout(5000)
    print('\n--- after submitting email (check your inbox) ---')
    inputs_after, _ = dump(pg, 'after_email')

    print('\nNow open the email from Store Leads.')
    resp = input('  Paste the CODE, or the full login LINK (https://...): ').strip()

    if resp.lower().startswith('http'):
        print('Opening the login link in the same browser...')
        pg.goto(resp, wait_until='networkidle', timeout=60000)
        pg.wait_for_timeout(5000)
    else:
        # find a code field = first visible input that is not the email one
        code_sel = None
        for i in inputs_after:
            if i.get('vis') and i.get('name') != 'email' and i.get('type') in ('text', 'tel', 'number', ''):
                code_sel = (f"input[name=\"{i['name']}\"]" if i.get('name')
                            else (f"#{i['id']}" if i.get('id') else None))
                break
        if not code_sel:
            code_sel = 'input:not([name="email"])'
        try:
            pg.fill(code_sel, resp)
        except Exception as e:
            print(f'  WARN: could not fill code field ({code_sel}): {e}')
        # submit: try buttons, else Enter
        clicked = False
        for sel in ['button:has-text("Sign in")', 'button:has-text("Verify")',
                    'button:has-text("Continue")', 'button[type=submit]', 'input[type=submit]']:
            try:
                if pg.locator(sel).count():
                    pg.locator(sel).first.click()
                    clicked = True
                    break
            except Exception:
                pass
        if not clicked:
            try:
                pg.keyboard.press('Enter')
            except Exception:
                pass
        pg.wait_for_timeout(6000)

    print('\n--- after completing login ---')
    _, body = dump(pg, 'after_login')
    low = body.lower()
    logged_out = any(s in low for s in ['log in with email', 'sign in', 'create an account'])
    logged_in = any(s in low for s in ['log out', 'logout', 'sign out', 'dashboard', 'searches',
                                       'credits', 'subscription', 'my lists', 'saved'])

    cookies = ctx.cookies()
    state = {'cookies': cookies, 'origins': []}
    with open(STATE, 'w') as f:
        import json
        json.dump(state, f, indent=2)
    os.chmod(STATE, 0o600)

    print(f'\nlogged_in hints: {logged_in} | logged_out hints: {logged_out}')
    print(f'saved {len(cookies)} cookies -> {STATE}')
    print('cookie names:', ', '.join(sorted({c["name"] for c in cookies})))
    ctx.close()
print('=== SL EMAIL LOGIN DONE ===')
