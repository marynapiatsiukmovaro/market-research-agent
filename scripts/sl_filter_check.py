#!/usr/bin/env python3
"""Store Leads — apply a Platform+Status filter and read back the matching store count (S-pivot).

Stage A of the universe export: confirm the filter is correct and capture the exact target
row-count BEFORE firing the big export. Read-only (applies UI filters, exports nothing).

Usage (on VPS):  python3 scripts/sl_filter_check.py <platform> <status>
  e.g. python3 scripts/sl_filter_check.py Shopify Active
Outputs: logs/storeleads/sl_filter_check.png + console (URL, counts, sidebar text).
"""
import os, sys, re
from playwright.sync_api import sync_playwright

STATE = '/opt/market-research-agent/cookies/storeleads_state.json'
OUT = '/opt/market-research-agent/logs/storeleads'
URL = 'https://storeleads.app/dashboard/domains'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
PLATFORM = sys.argv[1] if len(sys.argv) > 1 else 'Shopify'
STATUS = sys.argv[2] if len(sys.argv) > 2 else 'Active'

os.makedirs(OUT, exist_ok=True)


def click_filter(pg, label):
    """Click a filter option in the left sidebar by its visible label (scoped to avoid table rows)."""
    for sel in [f'aside >> text="{label}"', f'[class*="filter"] >> text="{label}"',
                f'[class*="sidebar"] >> text="{label}"', f'text="{label}"']:
        try:
            el = pg.locator(sel).first
            if el.count() > 0 and el.is_visible():
                el.click(timeout=6000)
                print(f'  clicked filter "{label}" via {sel}')
                return True
        except Exception as ex:
            print(f'  filter "{label}" sel {sel} failed: {str(ex)[:70]}')
    print(f'  !! filter "{label}" not clicked')
    return False


with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA,
                        viewport={'width': 1600, 'height': 1500}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.goto(URL, wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(6000)

    print(f'applying Platform={PLATFORM}, Status={STATUS}')
    click_filter(pg, PLATFORM)
    pg.wait_for_timeout(3500)   # let results refresh
    click_filter(pg, STATUS)
    pg.wait_for_timeout(4000)

    print('final URL    :', pg.url)
    pg.screenshot(path=os.path.join(OUT, 'sl_filter_check.png'), full_page=True)
    print('screenshot   : sl_filter_check.png')

    body = pg.evaluate('document.body.innerText') or ''
    # look for any "N stores"/"N results"/"N matching" count
    hits = re.findall(r'([\d,]{4,})\s*(stores|results|matching|domains)', body, re.I)
    print('count-like matches:', hits[:10])
    # also print the sidebar region around Platform/Status for context
    for kw in ['Platform', 'Status']:
        i = body.find(kw)
        if i >= 0:
            print(f'--- around "{kw}" ---')
            print(body[i:i + 200].replace(chr(10), ' | '))
    b.close()
print('=== SL FILTER CHECK DONE ===')
