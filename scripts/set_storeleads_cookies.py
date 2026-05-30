#!/usr/bin/env python3
"""
Import an already-logged-in Store Leads (storeleads.app) browser session onto the VPS
WITHOUT ever putting the secret in chat or git.

Marina logs into Store Leads via "Sign in with Google" — Google OAuth cannot be driven
headless from a server IP, so instead we transplant her existing logged-in cookies into a
Playwright storage_state the VPS browser reuses (same approach as the FB department).

Run interactively on the VPS (needs a TTY):
    ssh -i ~/.ssh/market_research_vps -t root@5.78.217.133 \
        'python3 /opt/market-research-agent/scripts/set_storeleads_cookies.py'

It reads the COOKIE HEADER STRING with getpass (hidden — not echoed, not in shell history,
not in chat). How to get that string:
    Chrome → storeleads.app (logged in) → F12 DevTools → Network tab → click any
    storeleads.app request → Headers → Request Headers → Cookie → copy the WHOLE value
    (looks like  name1=value1; name2=value2; ...).

Output: cookies/storeleads_state.json  (Playwright storage_state, chmod 600, gitignored).
Only cookie NAMES + a count are printed back — never the values.
"""
import getpass
import json
import os
import time
import urllib.parse

CRED_DIR = '/opt/market-research-agent/cookies'
STATE_PATH = os.path.join(CRED_DIR, 'storeleads_state.json')
DOMAIN = '.storeleads.app'

os.makedirs(CRED_DIR, exist_ok=True)

print('=== Store Leads session import → VPS only (gitignored, chmod 600) ===')
print('Paste the Cookie header string from a logged-in storeleads.app request.')
print('(input is hidden, like a password)')
cookie_str = getpass.getpass('  Cookie string: ').strip()

if not cookie_str or '=' not in cookie_str:
    print('ERROR: empty or invalid cookie string. Nothing saved.')
    raise SystemExit(1)

# tolerate "Cookie: " prefix if pasted by mistake
if cookie_str.lower().startswith('cookie:'):
    cookie_str = cookie_str.split(':', 1)[1].strip()

expires = time.time() + 365 * 24 * 3600  # extend locally so they persist across runs
cookies = []
for pair in cookie_str.split(';'):
    pair = pair.strip()
    if '=' not in pair:
        continue
    name, value = pair.split('=', 1)
    name = name.strip()
    value = urllib.parse.unquote(value.strip())
    if not name:
        continue
    cookies.append({
        'name': name,
        'value': value,
        'domain': DOMAIN,
        'path': '/',
        'expires': expires,
        'httpOnly': False,
        'secure': True,
        'sameSite': 'Lax',
    })

if not cookies:
    print('ERROR: parsed 0 cookies. Nothing saved.')
    raise SystemExit(1)

state = {'cookies': cookies, 'origins': []}
with open(STATE_PATH, 'w') as f:
    json.dump(state, f, indent=2)
os.chmod(STATE_PATH, 0o600)

print(f'\nSaved {len(cookies)} cookies → {STATE_PATH} (chmod 600).')
print('Cookie NAMES (values never shown):')
print('  ' + ', '.join(c['name'] for c in cookies))
print('Done. Values were not displayed.')
