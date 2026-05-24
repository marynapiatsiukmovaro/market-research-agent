#!/usr/bin/env python3
"""
Securely store ShopHunter credentials ON THE VPS — never in chat, never in git.

Run interactively on the VPS (needs a TTY):
    ssh -i ~/.ssh/market_research_vps -t root@5.78.217.133 \
        'python3 /opt/market-research-agent/scripts/set_shophunter_creds.py'

The password is read with getpass (hidden — not echoed to screen, not in shell
history when typed at the prompt). Output file is chmod 600 and lives under
cookies/ which is gitignored. Nothing here is ever committed or printed back.
"""
import getpass
import json
import os

CRED_DIR = '/opt/market-research-agent/cookies'
CRED_PATH = os.path.join(CRED_DIR, 'shophunter.creds')

os.makedirs(CRED_DIR, exist_ok=True)

print('=== ShopHunter credentials → VPS only (gitignored, chmod 600) ===')
url = input('  Login URL [https://app.shophunter.io]: ').strip() or 'https://app.shophunter.io'
email = input('  Email / login: ').strip()
pw = getpass.getpass('  Password (hidden, will not display): ')

if not email or not pw:
    print('ERROR: email and password are required. Nothing saved.')
    raise SystemExit(1)

with open(CRED_PATH, 'w') as f:
    json.dump({'url': url, 'email': email, 'password': pw}, f)
os.chmod(CRED_PATH, 0o600)

print(f'\nSaved to {CRED_PATH} (chmod 600).')
print('Password was not displayed and is not in this terminal\'s output.')
