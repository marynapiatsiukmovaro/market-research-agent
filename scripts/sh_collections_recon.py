#!/usr/bin/env python3
# RECON: map the Shop Collections UI (My ShopHunter -> Shop Collections) + the "add to collection" control.
# Read-only exploration: dumps nav links, screenshots, page text. Does NOT add/remove anything.
import os, json, re
from playwright.sync_api import sync_playwright
OUT = '/opt/market-research-agent/logs/shophunter'; os.makedirs(OUT, exist_ok=True)
def links(page):
    return page.evaluate("""()=>Array.from(document.querySelectorAll('a[href]')).map(a=>({t:(a.innerText||'').trim().slice(0,40),h:a.getAttribute('href')})).filter(x=>x.h&&!x.h.startsWith('http')&&x.h!=='#')""")
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1600,'height':1400})
    page=ctx.new_page()
    page.goto('https://app.shophunter.io/explore/shops',wait_until='domcontentloaded',timeout=60000)
    page.wait_for_timeout(6000)
    if '/login' in page.url:
        print('SESSION_DROPPED'); ctx.close(); raise SystemExit
    page.screenshot(path=f'{OUT}/recon_01_explore.png')
    # unique internal nav links seen on explore
    seen=set(); navlinks=[]
    for x in links(page):
        k=(x['h'],x['t'])
        if k not in seen: seen.add(k); navlinks.append(x)
    print('=== INTERNAL LINKS on /explore/shops ===')
    for x in navlinks:
        if any(w in (x['h']+x['t']).lower() for w in ['collection','track','my','shop','product','staff']):
            print('  ', x['h'], '|', x['t'])
    # try opening the "My Shophunter" top-nav dropdown
    print('=== try My Shophunter dropdown ===')
    try:
        page.get_by_text(re.compile('My Shophunter',re.I)).first.click()
        page.wait_for_timeout(1500)
        page.screenshot(path=f'{OUT}/recon_02_mymenu.png')
        for x in links(page):
            if any(w in (x['h']+x['t']).lower() for w in ['collection','track','watch']):
                print('  MENU:', x['h'], '|', x['t'])
    except Exception as e:
        print('  dropdown fail:', type(e).__name__, e)
    # inspect an Explore-Shops shop CARD for an add-to-collection control
    print('=== shop card buttons/aria (add-to-collection?) ===')
    try:
        btns=page.evaluate("""()=>Array.from(document.querySelectorAll('button,[role=button],svg[aria-label],[title]')).map(b=>({t:(b.innerText||b.getAttribute('aria-label')||b.getAttribute('title')||'').trim().slice(0,30)})).filter(x=>x.t).slice(0,40)""")
        labs=sorted({b['t'] for b in btns})
        for l in labs: print('   btn/label:', l)
    except Exception as e:
        print('  btn scan fail:', e)
    # open first shop detail, look for add control there too
    try:
        first=page.evaluate("""()=>{const a=document.querySelector('a[href^=\"/shops/\"]'); return a?a.getAttribute('href'):null}""")
        if first:
            page.goto('https://app.shophunter.io'+first, wait_until='domcontentloaded', timeout=45000)
            page.wait_for_timeout(4000)
            page.screenshot(path=f'{OUT}/recon_03_shopdetail.png', full_page=True)
            det=page.evaluate("""()=>Array.from(document.querySelectorAll('button,[role=button],[title],[aria-label]')).map(b=>(b.innerText||b.getAttribute('aria-label')||b.getAttribute('title')||'').trim()).filter(t=>t).slice(0,50)""")
            print('=== shop DETAIL buttons (look for Add to Collection / Track) ===')
            for t in sorted(set(det)): print('   ', t[:40])
    except Exception as e:
        print('  detail fail:', type(e).__name__, e)
    ctx.close()
print('RECON_DONE')
