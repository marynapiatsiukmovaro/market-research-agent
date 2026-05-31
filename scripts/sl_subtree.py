#!/usr/bin/env python3
"""Full L2 subcategory tree (Shopify+Active) from the global cat facet, grouped by L1. VPS."""
import json
from collections import defaultdict
from playwright.sync_api import sync_playwright
STATE = "/opt/market-research-agent/cookies/storeleads_state.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
JS = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  const f=(j&&j.facets&&j.facets.cat)||{};
  return {terms:f.terms||[], other:f.other, n:(f.terms||[]).length};
}"""
KEEP_L1 = ["Home & Garden","Sports","Toys & Hobbies","Pets & Animals","Consumer Electronics",
           "Health","Autos & Vehicles","Gifts & Special Events","Computers","Office Supplies",
           "Furniture","Hardware"]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    r=pg.evaluate(JS,json.dumps({"f:p":"1","f:ds":"1","all_facets":True}))
    print("cat facet terms:",r.get("n"),"other:",r.get("other"))
    import re
    def norm(s): return re.sub(r"[^A-Za-z0-9&()'-]+"," ",str(s)).strip()
    def key(s): return re.sub(r"[^a-z0-9]","",str(s).lower())
    tree=defaultdict(list)
    for t in r.get("terms") or []:
        term=str(t.get("term","")); cnt=t.get("count",0) or 0
        segs=term.split("/")  # '', L1, L2, ...
        if len(segs)==3 and segs[1]:
            tree[key(segs[1])].append((norm(segs[2]),cnt))
    for L1 in KEEP_L1:
        subs=sorted(tree.get(key(L1),[]),key=lambda x:-x[1])
        if not subs: continue
        print(f"\n===== {L1}  (total subs shown: {len(subs)}) =====")
        for name,cnt in subs:
            print(f"  {cnt:>8}  {name}")
    b.close()
print("\n=== SUBTREE DONE ===")
