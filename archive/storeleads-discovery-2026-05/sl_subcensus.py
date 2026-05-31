#!/usr/bin/env python3
"""Full L2 subcategory tree per kept L1 (Shopify+Active), with totals. Run on VPS."""
import json, time
from playwright.sync_api import sync_playwright
STATE = "/opt/market-research-agent/cookies/storeleads_state.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
JS = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  const f=(j&&j.facets&&j.facets.cat)||{};
  return {total:j&&j.totalHits, terms:f.terms||[], other:f.other};
}"""
BASE = {"f:p":"1","f:ds":"1","all_facets":True}
L1S = ["Home & Garden","Sports","Toys & Hobbies","Pets & Animals","Consumer Electronics",
       "Health","Autos & Vehicles","Gifts & Special Events","Computers","Beauty & Fitness"]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    for L1 in L1S:
        r=pg.evaluate(JS,json.dumps({**BASE,"f:cat1":L1})); time.sleep(1.0)
        pref="/"+L1
        subs=[]
        for t in r.get("terms") or []:
            term=str(t.get("term","")); cnt=t.get("count",0) or 0
            if term.startswith(pref+"/"):
                depth=term.count("/")
                if depth==2:  # direct L2 child
                    subs.append((term[len(pref)+1:], cnt))
        subs.sort(key=lambda x:-x[1])
        print(f"\n===== {L1}  (L1 total={r.get('total')}, other={r.get('other')}) =====")
        for name,cnt in subs:
            print(f"  {cnt:>8}  {name}")
    b.close()
print("\n=== SUBCENSUS DONE ===")
