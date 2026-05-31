#!/usr/bin/env python3
"""Base cracked: p/ds=term, cat=match -> 33944. Now find created>=2020 range form. want 29150. VPS."""
import json, time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
KD="/Home & Garden/Kitchen & Dining"
JS="""async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {status:r.status, total:j&&j.totalHits, err:j&&(j.error||j.message)};
}"""
def bq(conj): return {"all_facets":True,"bq":json.dumps({"must":{"conjuncts":conj}})}
BASE=[{"field":"p","term":"1"},{"field":"ds","term":"1"},{"field":"cat","match":KD}]
DATE=[
 ("createdAt RFC3339 start",  {"field":"createdAt","start":"2020-01-01T00:00:00Z","inclusive_start":True}),
 ("crat RFC3339 start",       {"field":"crat","start":"2020-01-01T00:00:00Z","inclusive_start":True}),
 ("created RFC3339 start",    {"field":"created","start":"2020-01-01T00:00:00Z","inclusive_start":True}),
 ("cratyyyymm TermRange min", {"field":"cratyyyymm","min":"2020-01","inclusive_min":True}),
 ("cratyyyymm TermRange min+max", {"field":"cratyyyymm","min":"2020-01","max":"2030-12","inclusive_min":True,"inclusive_max":True}),
 ("cratyyyymmdd TermRange str min", {"field":"cratyyyymmdd","min":"2020-01-01","inclusive_min":True}),
 ("cratyyyy TermRange min",   {"field":"cratyyyy","min":"2020","inclusive_min":True}),
 ("cratyyyy match 2020",      {"field":"cratyyyy","match":"2020"}),
 ("cratts numeric min",       {"field":"cratts","min":1577836800,"inclusive_min":True}),
 ("createdAt numeric min ms", {"field":"createdAt","min":1577836800000,"inclusive_min":True}),
]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    print("base check:", pg.evaluate(JS,json.dumps(bq(BASE))).get("total"), "(want 33944)")
    for label,dq in DATE:
        r=pg.evaluate(JS,json.dumps(bq(BASE+[dq]))); time.sleep(0.9)
        mark=" <== MATCH 29150!" if r.get("total")==29150 else (" (filtered)" if r.get("total") not in (33944,None,0) else "")
        print(f"  {label:30} status={r.get('status')} total={r.get('total')} {r.get('err') or ''}{mark}")
    b.close()
print("\n=== CRACK BQ4 DONE ===")
