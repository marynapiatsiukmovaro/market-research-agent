#!/usr/bin/env python3
# Explore Shops category dump (generalized from sh_hg_dump.py). Scroll-to-exhaustion, incremental save.
# Usage: sh_cat_dump.py "<Category Label>" <dest_basename> [target] [sentinel_basename]
import os, json, sys, re
from playwright.sync_api import sync_playwright
OUT = '/opt/market-research-agent/logs/shophunter'; os.makedirs(OUT, exist_ok=True)
CAT = sys.argv[1] if len(sys.argv) > 1 else 'Baby & Toddler'
DEST = f"{OUT}/{sys.argv[2] if len(sys.argv) > 2 else 'bt_shops.json'}"
TARGET = int(sys.argv[3]) if len(sys.argv) > 3 else 3000
SENT = f"{OUT}/{sys.argv[4] if len(sys.argv) > 4 else 'cat_dump.done'}"
HARVEST_JS = r'''
() => {
  const out=[];
  const links=Array.from(document.querySelectorAll('a[href]')).filter(a=>/^\/shops\/\d+$/.test(a.getAttribute('href')||''));
  for (const a of links){
    let el=a;
    for(let i=0;i<10&&el;i++){const t=el.innerText||'';
      if(t.includes('Shop Ads')&&t.includes('SKU Count')&&(t.split('SKU Count').length-1)===1)break; el=el.parentElement;}
    if(el) out.push({id:a.getAttribute('href').split('/').pop(), text:el.innerText});
  }
  return out;
}'''
def parse(txt):
    L=[l.strip() for l in txt.split('\n') if l.strip()]
    def af(label,n=1):
        for i,x in enumerate(L):
            if x==label and i+n<len(L): return L[i+n]
        return ''
    return {'name':L[0] if L else '','domain':L[1] if len(L)>1 else '',
            'shop_ads':af('Shop Ads'),'rev_day':af('Day'),'rev_week':af('Week'),'rev_week_chg':af('Week',2),
            'fb':af('Facebook Followers'),'ig':af('Instagram Followers'),
            'country':af('Shop Country'),'sku':af('SKU Count'),'currency':af('Currency')}
store={}
with sync_playwright() as p:
    ctx=p.chromium.launch_persistent_context(user_data_dir='/opt/market-research-agent/cookies/shophunter_profile',
        headless=True, user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        viewport={'width':1600,'height':1400})
    page=ctx.new_page()
    page.goto('https://app.shophunter.io/explore/shops',wait_until='domcontentloaded',timeout=60000)
    page.wait_for_timeout(6000)
    if '/login' in page.url:
        open(SENT,'w').write('SESSION_DROPPED'); print('SESSION_DROPPED'); ctx.close(); raise SystemExit
    try:
        page.get_by_text(CAT,exact=True).first.evaluate("e=>{let r=e.closest('div'); let cb=r.querySelector('input[type=checkbox]'); if(cb)cb.click();}")
        print('CATEGORY_CLICKED:', CAT, flush=True)
    except Exception as ex:
        print('CATEGORY_CLICK_FAIL:', type(ex).__name__, ex, flush=True)
    page.wait_for_timeout(800)
    page.get_by_role('button',name='Search',exact=True).first.click()
    page.wait_for_timeout(5000)
    body=page.eval_on_selector('body',"e=>e.innerText")
    mc=re.search(r'([\d,]+)\s+(?:results|shops|stores)',body,re.I)
    print('RESULT_COUNT_TEXT:', mc.group(0) if mc else 'none-visible', flush=True)
    stall=0; prev=0
    for it in range(600):
        for c in page.evaluate(HARVEST_JS):
            if c['id'] not in store: store[c['id']]=parse(c['text'])
        n=len(store)
        if n>=TARGET: print('REACHED_TARGET',n,flush=True); break
        if n==prev:
            stall+=1
            if stall>=12: print('EXHAUSTED at',n,'(no new for 12 scrolls)',flush=True); break
        else: stall=0
        prev=n
        if n and n%50<3: json.dump([dict(shop_id=k,**v) for k,v in store.items()],open(DEST,'w'),ensure_ascii=False)
        page.evaluate('window.scrollBy(0,1500)'); page.wait_for_timeout(1200)
        if it%25==0: print('  ...',n,'stores @ iter',it,flush=True)
    rows=[dict(shop_id=k,**v) for k,v in store.items()]
    json.dump(rows,open(DEST,'w'),ensure_ascii=False,indent=1)
    open(SENT,'w').write('done %d cat=%s' % (len(rows),CAT))
    print('FINAL_STORES',len(rows),'| saved:',DEST,flush=True)
    ctx.close()
print('DONE')
