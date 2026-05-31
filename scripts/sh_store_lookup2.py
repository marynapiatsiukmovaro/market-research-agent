#!/usr/bin/env python3
# Cross-dept ENRICHMENT lookup: find a Store Leads finalist in ShopHunter, WITH domain verification
# (the Explore page keeps a default shop card when a search returns nothing -> must verify the opened
# shop's shown domain actually matches the query, per SH interface-guide). Ladder of search terms.
# Usage: python3 sh_store_lookup2.py domain1 [domain2 ...]
import sys, os, re, json
from playwright.sync_api import sync_playwright
OUT='/opt/market-research-agent/logs/shophunter'; os.makedirs(OUT, exist_ok=True)
domains=[d.strip() for d in sys.argv[1:] if d.strip()]

def bare(d): return re.sub(r'^https?://','',d).strip('/').split('/')[0]
def nowww(d): return re.sub(r'^www\.','',bare(d))
def core(d):  return re.sub(r'[^a-z0-9]','', nowww(d).rsplit('.',1)[0].lower())  # 'stoov', 'maskingmaster'
def brandwords(d): return re.sub(r'[-_.]',' ', nowww(d).rsplit('.',1)[0])
def search_terms(d):
    b=nowww(d)
    out=[brandwords(d), b]           # brandwords/bare actually filter; full-URL returns junk default set
    seen=set(); return [x for x in out if not (x in seen or seen.add(x))]
def itext(page,n=6000):
    try: return page.eval_on_selector('body',"e=>e.innerText")[:n]
    except Exception as e: return f'(innerText err {e})'
def visible_search(page):
    loc=page.get_by_placeholder('Search Shops')
    for i in range(loc.count()):
        if loc.nth(i).is_visible(): return loc.nth(i)
    return loc.first

results=[]
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(
        user_data_dir='/opt/market-research-agent/cookies/shophunter_profile', headless=True,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1440,'height':1600})
    page=ctx.new_page()
    for dom in domains:
        print(f'\n================= {dom} =================')
        ck=core(dom); hit=None
        for term in search_terms(dom):
            try:
                page.goto('https://app.shophunter.io/explore/shops',wait_until='domcontentloaded',timeout=60000)
                page.wait_for_timeout(2500)
                if '/login' in page.url:
                    print('!!! SESSION DROPPED'); ctx.close(); sys.exit(2)
                inp=visible_search(page)
                inp.click(); inp.fill(''); inp.type(term, delay=50); page.wait_for_timeout(1300)
                inp.press('Enter'); page.wait_for_timeout(5500)
                hrefs=page.eval_on_selector_all('a[href*="/shops/"]',
                    "els=>Array.from(new Set(els.map(e=>e.getAttribute('href')))).filter(h=>/\\/shops\\/[0-9]+$/.test(h)).slice(0,6)")
                # try each candidate shop, verify domain matches query core
                for href in hrefs:
                    url='https://app.shophunter.io'+href
                    page.goto(url,wait_until='domcontentloaded',timeout=60000); page.wait_for_timeout(3500)
                    head=itext(page,1200).lower()
                    # the shop page shows its domain near the top; verify core token present
                    if ck and ck in re.sub(r'[^a-z0-9]','',head):
                        hit=(term,href,url); break
                if hit: print(f'  VERIFIED via "{term}" -> {hit[1]}'); break
                else: print(f'  no-match "{term}" (hrefs={hrefs})')
            except Exception as e:
                print(f'  err "{term}": {e!r}')
        if not hit:
            print('  NOT_FOUND'); results.append({'domain':dom,'found':False}); continue
        term,href,url=hit
        page.goto(url,wait_until='domcontentloaded',timeout=60000); page.wait_for_timeout(4500)
        for y in (800,1700,2700,3700,4800): page.evaluate(f'window.scrollTo(0,{y})'); page.wait_for_timeout(600)
        page.evaluate('window.scrollTo(0,0)'); page.wait_for_timeout(400)
        body=itext(page)
        safe=core(dom)
        open(f'{OUT}/sl_{safe}.txt','w').write(body)
        page.screenshot(path=f'{OUT}/sl_{safe}.png', full_page=True)
        print('  SHOP_URL:', page.url, '| via:', term)
        print('  --- shop page (top) ---')
        print('  '+body[:1500].replace('\n','\n  '))
        results.append({'domain':dom,'found':True,'via':term,'url':page.url})
    ctx.close()
ok=sum(1 for r in results if r.get('found'))
print(f'\n===== LOOKUP DONE: {ok}/{len(results)} verified =====')
print(json.dumps([{k:r.get(k) for k in ("domain","found","url")} for r in results],ensure_ascii=False))
