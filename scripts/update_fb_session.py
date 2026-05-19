#!/usr/bin/env python3
"""
Cookie → fb_session.json converter.
Usage: python3 scripts/update_fb_session.py "<cookie_string>"
Creates /tmp/fb_session_new.json in the format expected by check_session.py
Format: {"cookies": [...]} — do NOT change this, check_session.py requires dict with 'cookies' key.
"""
import json, sys, urllib.parse

if len(sys.argv) > 1:
    cookie_str = sys.argv[1]
else:
    cookie_str = sys.stdin.read().strip()

cookies = []
for pair in cookie_str.split('; '):
    if '=' in pair:
        name, value = pair.split('=', 1)
        name = name.strip()
        value = urllib.parse.unquote(value.strip())
        cookies.append({
            "name": name,
            "value": value,
            "domain": ".facebook.com",
            "path": "/",
            "httpOnly": name in ("xs", "fr", "datr", "sb", "c_user"),
            "secure": True,
            "sameSite": "None"
        })

session = {"cookies": cookies}
out = '/tmp/fb_session_new.json'
with open(out, 'w') as f:
    json.dump(session, f, indent=2)

names = [c["name"] for c in cookies]
required = ["c_user", "xs", "fr", "datr", "sb"]
missing = [r for r in required if r not in names]
if missing:
    print(f"ERROR: Missing: {missing}", file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(cookies)} cookies → {out}")
