#!/usr/bin/env python3
# TEST: add 2 shops to the collection via the shop-detail "Add/Remove from Collection" button.
# Screenshots every step so the flow is transparent. Verifies they appear in /collections/shops.
import os, re, time
from playwright.sync_api import sync_playwright
OUT='/opt/market-research-agent/logs/shophunter'
SHOPS=[('65261240483','nulooa'),('79040676086','hago')]
def btns(page):
    return sorted(set(page.evaluate("""()=>Array.from(document.querySelectorAll('button,[role=button],[role=menuitem],a')).map(b=>(b.innerText||'').trim()).filter(t=>t&&t.length<45)""")))
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1600,'height':1400})
    page=ctx.new_page()
    for sid,tag in SHOPS:
        print('==== SHOP',tag,sid,'====')
        page.goto(f'https://app.shophunter.io/shops/{sid}',wait_until='domcontentloaded',timeout=60000)
        page.wait_for_timeout(4500)
        if '/login' in page.url: print('SESSION_DROPPED'); ctx.close(); raise SystemExit
        try:
            page.get_by_text(re.compile('Add/Remove from Collection',re.I)).first.click()
            page.wait_for_timeout(2000)
            page.screenshot(path=f'{OUT}/add_dialog_{tag}.png')
            print('  dialog open. buttons/options:')
            for b in btns(page): print('     ',b)
            # in the dialog: tick the collection checkbox (collection shown as "Shops") + confirm
            done=False
            for label in ['Shops','Add','Save','Confirm','Done','Add to Collection']:
                try:
                    loc=page.get_by_text(re.compile('^'+re.escape(label)+'$',re.I))
                    if loc.count()>0:
                        loc.first.click(); page.wait_for_timeout(1200); print('     clicked:',label); done=True
                except Exception as ex:
                    print('     click fail',label,type(ex).__name__)
            page.wait_for_timeout(1500)
            page.screenshot(path=f'{OUT}/add_after_{tag}.png')
            print('  after-add screenshot saved; clicked-something=',done)
        except Exception as e:
            print('  ADD FAIL:',type(e).__name__,e)
    # verify
    page.goto('https://app.shophunter.io/collections/shops',wait_until='domcontentloaded',timeout=60000)
    page.wait_for_timeout(5000)
    page.screenshot(path=f'{OUT}/coll_after_add.png', full_page=True)
    names=page.evaluate("""()=>Array.from(document.querySelectorAll('a[href^=\"/shops/\"]')).map(a=>a.getAttribute('href')).filter(h=>/^\\/shops\\/\\d+$/.test(h))""")
    uniq=sorted(set(names))
    print('==== COLLECTION shop links now:',len(uniq),'====')
    for h in uniq: print('   ',h)
    ctx.close()
print('ADD_TEST_DONE')
