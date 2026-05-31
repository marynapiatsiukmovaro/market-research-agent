#!/usr/bin/env python3
"""Exact >=2020 count per approved subcategory (cratyyyymm facet sum) + total. VPS."""
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
  return {total:j&&j.totalHits, terms:f.terms||[]};
}"""
BASE = {"f:p":"1","f:ds":"1","all_facets":True}
GREEN = [
 "/Home & Garden/Kitchen & Dining","/Home & Garden/Home Improvement","/Home & Garden/Bed & Bath",
 "/Home & Garden/Gardening & Landscaping","/Home & Garden/Home Appliances","/Home & Garden/Nursery & Playroom",
 "/Home & Garden/Cleaning","/Home & Garden/Home Safety & Security",
 "/Pets & Animals/Pet Food & Supplies","/Pets & Animals/Dogs","/Pets & Animals/Cats",
 "/Health/Oral & Dental Care",
]
def c2020(terms):
    return sum((t.get("count",0) or 0) for t in terms if re.match(r"^20\d\d-\d\d$",str(t.get("term",""))) and str(t.get("term"))>="2020-01")
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    tot=0; s2020=0
    print(f"{'subcategory':42} {'total':>8} {'>=2020':>8}")
    for path in GREEN:
        r=pg.evaluate(JS,json.dumps({**BASE,"f:cat":path})); time.sleep(1.0)
        c=c2020(r.get("terms") or []); t=r.get("total") or 0
        tot+=t; s2020+=c
        print(f"{path[:42]:42} {t:>8} {c:>8}")
    print(f"\n{'SUM (naive, with overlap)':42} {tot:>8} {s2020:>8}")
    b.close()
print("=== COUNT DONE ===")
