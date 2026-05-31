#!/usr/bin/env python3
"""Census under Shopify+Active, with Created>=2020 computed from the cratyyyymm month-facet.
Per category (L1 via f:cat1, L2 via f:cat): total + created>=2020 count. Run on VPS."""
import json, re, time
from playwright.sync_api import sync_playwright
STATE = "/opt/market-research-agent/cookies/storeleads_state.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
JS = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  const f=(j&&j.facets&&j.facets.cratyyyymm)||{};
  const d=(j&&j.domains&&j.domains[0])||{};
  return {total:j&&j.totalHits, terms:f.terms||[], other:f.other, missing:f.missing,
          sample:{mvis:d.mvis,mpv:d.mpv,er:d.erf,ap:d.apf}};
}"""
BASE = {"f:p":"1","f:ds":"1","all_facets":True}
# keep-list: (label, filter-key, value)
CATS = [
 ("Home & Garden","f:cat1","Home & Garden"),
 ("  HG/Kitchen & Dining","f:cat","/Home & Garden/Kitchen & Dining"),
 ("  HG/Home Improvement","f:cat","/Home & Garden/Home Improvement"),
 ("  HG/Home Appliances","f:cat","/Home & Garden/Home Appliances"),
 ("  HG/Bed & Bath","f:cat","/Home & Garden/Bed & Bath"),
 ("  HG/Gardening & Landscaping","f:cat","/Home & Garden/Gardening & Landscaping"),
 ("  HG/Yard & Patio","f:cat","/Home & Garden/Yard & Patio"),
 ("Pets & Animals","f:cat1","Pets & Animals"),
 ("Consumer Electronics","f:cat1","Consumer Electronics"),
 ("Sports","f:cat1","Sports"),
 ("  Sports/Sporting Goods","f:cat","/Sports/Sporting Goods"),
 ("Toys & Hobbies","f:cat1","Toys & Hobbies"),
 ("  Toys/Arts & Crafts","f:cat","/Toys & Hobbies/Arts & Crafts"),
 ("Health","f:cat1","Health"),
 ("Beauty & Fitness/Fitness","f:cat","/Beauty & Fitness/Fitness"),
 ("Autos & Vehicles","f:cat1","Autos & Vehicles"),
 ("Gifts & Special Events","f:cat1","Gifts & Special Events"),
 ("Computers","f:cat1","Computers"),
]
def c2020(terms):
    s=0
    for t in terms:
        term=str(t.get("term",""));
        if re.match(r"^20\d\d-\d\d$",term) and term>="2020-01":
            s+=t.get("count",0) or 0
    return s
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    diag=None
    print(f"{'category':38} {'total':>9} {'>=2020':>9}")
    for label,k,v in CATS:
        r=pg.evaluate(JS,json.dumps({**BASE,k:v})); time.sleep(1.0)
        terms=r.get("terms") or []
        if diag is None:
            diag={"n_terms":len(terms),"other":r.get("other"),"missing":r.get("missing"),
                  "min_term":min((t.get("term") for t in terms),default=None),
                  "max_term":max((t.get("term") for t in terms),default=None),"sample":r.get("sample")}
        print(f"{label:38} {str(r.get('total')):>9} {str(c2020(terms)):>9}")
    print("\nFACET DIAGNOSTIC (1st category):",json.dumps(diag,ensure_ascii=False))
    b.close()
print("=== CENSUS DONE ===")
