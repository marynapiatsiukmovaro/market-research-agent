#!/usr/bin/env python3
# Debug ShopHunter shop search: target the VISIBLE Search Shops input, search a term, dump real results.
import json
from playwright.sync_api import sync_playwright
TERM="stoov"
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1440,'height':1600})
    pg=ctx.new_page()
    pg.goto('https://app.shophunter.io/explore/shops',wait_until='domcontentloaded',timeout=60000); pg.wait_for_timeout(4000)
    print('URL:',pg.url)
    # how many Search Shops inputs, which visible?
    loc=pg.get_by_placeholder('Search Shops')
    cnt=loc.count(); print('Search-Shops inputs:',cnt)
    vis_idx=-1
    for i in range(cnt):
        try:
            v=loc.nth(i).is_visible()
            print(f'  input[{i}] visible={v}')
            if v and vis_idx<0: vis_idx=i
        except Exception as e: print('  vis err',i,e)
    use=loc.nth(vis_idx if vis_idx>=0 else 0)
    use.click(); use.fill(''); use.type(TERM, delay=60); pg.wait_for_timeout(1500)
    use.press('Enter'); pg.wait_for_timeout(7000)
    print('URL after search:',pg.url)
    links=pg.eval_on_selector_all('a[href*="/shops/"]',
        "els=>els.map(e=>((e.innerText||'').replace(/\\n/g,' ').trim().slice(0,55)+' || '+e.getAttribute('href'))).slice(0,15)")
    print('SHOP_LINKS after search for "%s":'%TERM)
    for l in links: print('  ',l)
    body=pg.eval_on_selector('body','e=>e.innerText')
    print('BODY_SLICE:', body[:500].replace(chr(10),' / '))
    pg.screenshot(path='/opt/market-research-agent/logs/shophunter/dbg_search.png',full_page=True)
    ctx.close()
print('PROBE DONE')
