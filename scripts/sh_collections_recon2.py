#!/usr/bin/env python3
# RECON2: open Shop Collections (/collections/shops), find Marina's collection, map Shops + Products(Newest First) tabs,
# and find the "add to collection" control on a shop detail. Read-only.
import os, re
from playwright.sync_api import sync_playwright
OUT='/opt/market-research-agent/logs/shophunter'
def dump_links(page,filt=None):
    xs=page.evaluate("""()=>Array.from(document.querySelectorAll('a[href]')).map(a=>({t:(a.innerText||'').trim().slice(0,45),h:a.getAttribute('href')})).filter(x=>x.h)""")
    out=[]; seen=set()
    for x in xs:
        if x['h'].startswith('http') or x['h'] in ('#',''): continue
        k=(x['h'],x['t'])
        if k in seen: continue
        seen.add(k)
        if filt is None or filt(x): out.append(x)
    return out
def btns(page):
    return sorted(set(page.evaluate("""()=>Array.from(document.querySelectorAll('button,[role=button],[aria-label],[title]')).map(b=>(b.innerText||b.getAttribute('aria-label')||b.getAttribute('title')||'').trim()).filter(t=>t&&t.length<40)""")))
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1600,'height':1400})
    page=ctx.new_page()
    page.goto('https://app.shophunter.io/collections/shops',wait_until='domcontentloaded',timeout=60000)
    page.wait_for_timeout(6000)
    if '/login' in page.url: print('SESSION_DROPPED'); ctx.close(); raise SystemExit
    page.screenshot(path=f'{OUT}/recon_coll_01_list.png', full_page=True)
    print('URL:', page.url)
    print('=== /collections/shops body (first 1500 chars) ===')
    print(page.eval_on_selector('body','e=>e.innerText')[:1500])
    print('=== links here (collection / shop) ===')
    for x in dump_links(page, lambda x: any(w in x['h'].lower() for w in ['collection','/shops/'])):
        print('  ',x['h'],'|',x['t'])
    print('=== buttons/tabs here ===')
    for b in btns(page): print('   ',b)
    # try clicking a Products tab if present
    try:
        page.get_by_text(re.compile(r'^Products$',re.I)).first.click(); page.wait_for_timeout(3500)
        page.screenshot(path=f'{OUT}/recon_coll_02_products.png', full_page=True)
        print('=== after clicking Products tab: body (first 1200) ===')
        print(page.eval_on_selector('body','e=>e.innerText')[:1200])
        print('=== filters/buttons on Products ===')
        for b in btns(page): print('   ',b)
    except Exception as e:
        print('Products tab click fail:', type(e).__name__, e)
    # add-to-collection control on a shop detail
    try:
        page.goto('https://app.shophunter.io/shops/62198349877',wait_until='domcontentloaded',timeout=45000)
        page.wait_for_timeout(4500)
        page.screenshot(path=f'{OUT}/recon_coll_03_shopdetail.png', full_page=True)
        print('=== shop DETAIL buttons (add to collection / track?) ===')
        for b in btns(page): print('   ',b)
    except Exception as e:
        print('detail fail:', type(e).__name__, e)
    ctx.close()
print('RECON2_DONE')
