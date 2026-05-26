#!/usr/bin/env python3
# Bulk-add shops to the (single) collection via shop-detail "Add/Remove from Collection" -> "Add".
# Usage: sh_collection_add.py <shop_id> [<shop_id> ...]
# Safe for shops NOT already in the collection (Add/Remove is a TOGGLE).
import sys, re
from playwright.sync_api import sync_playwright
IDS=sys.argv[1:]
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1600,'height':1400})
    page=ctx.new_page()
    for sid in IDS:
        try:
            page.goto(f'https://app.shophunter.io/shops/{sid}',wait_until='domcontentloaded',timeout=60000)
            page.wait_for_timeout(4000)
            if '/login' in page.url: print('SESSION_DROPPED'); ctx.close(); raise SystemExit
            page.get_by_text(re.compile('Add/Remove from Collection',re.I)).first.click()
            page.wait_for_timeout(1800)
            page.get_by_text(re.compile(r'^Add$',re.I)).first.click()
            page.wait_for_timeout(1500)
            print('ADDED', sid)
        except Exception as e:
            print('FAIL', sid, type(e).__name__, str(e)[:60])
    # verify
    page.goto('https://app.shophunter.io/collections/shops',wait_until='domcontentloaded',timeout=60000)
    page.wait_for_timeout(5000)
    names=page.evaluate("""()=>Array.from(document.querySelectorAll('a[href^=\"/shops/\"]')).map(a=>a.getAttribute('href')).filter(h=>/^\\/shops\\/\\d+$/.test(h))""")
    uniq=sorted(set(names))
    print('=== COLLECTION now has', len(uniq), 'shops ===')
    for h in uniq: print('  ',h)
    ctx.close()
print('BULK_ADD_DONE')
