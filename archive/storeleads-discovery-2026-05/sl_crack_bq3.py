#!/usr/bin/env python3
"""bq = JSON STRING of a Bleve query {"must":{"conjuncts":[...]}}. Find the right conjunct
query types. Validate: p+ds+cat = 33944 ; + created>=2020 = 29150. VPS."""
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

# platform/status as term (ids); vary category query type
def trip(cat_q): return [{"field":"p","term":"1"},{"field":"ds","term":"1"},cat_q]
CAT_TYPES = [
 ("cat term",        {"field":"cat","term":KD}),
 ("cat match",       {"field":"cat","match":KD}),
 ("cat match_phrase",{"field":"cat","match_phrase":KD}),
 ("cat prefix",      {"field":"cat","prefix":KD}),
 ("cat wildcard",    {"field":"cat","wildcard":KD}),
]
# also try p/ds as match in case term fails
ALT = [
 ("p/ds match + cat term", [{"field":"p","match":"1"},{"field":"ds","match":"1"},{"field":"cat","term":KD}]),
 ("p/ds numeric + cat term", [{"field":"p","min":1,"max":1,"inclusive_min":True,"inclusive_max":True},{"field":"ds","min":1,"max":1,"inclusive_min":True,"inclusive_max":True},{"field":"cat","term":KD}]),
]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    def post(body): return pg.evaluate(JS,json.dumps(body));
    print("---- base (want 33944) ----")
    winner=None
    for label,catq in CAT_TYPES:
        r=pg.evaluate(JS,json.dumps(bq(trip(catq)))); time.sleep(0.9)
        mark=" <== MATCH" if r.get("total")==33944 else ""
        print(f"  {label:18} status={r.get('status')} total={r.get('total')} {r.get('err') or ''}{mark}")
        if r.get("total")==33944 and not winner: winner=catq
    for label,conj in ALT:
        r=pg.evaluate(JS,json.dumps(bq(conj))); time.sleep(0.9)
        mark=" <== MATCH" if r.get("total")==33944 else ""
        print(f"  {label:24} status={r.get('status')} total={r.get('total')} {r.get('err') or ''}{mark}")
        if r.get("total")==33944 and not winner: winner=conj[-1]

    if winner:
        print(f"\n---- created>=2020 range on winning base {winner} (want 29150) ----")
        DATE = [
         ("crat start incl",        {"field":"crat","start":"2020-01-01","inclusive_start":True}),
         ("createdAt start incl",   {"field":"createdAt","start":"2020-01-01","inclusive_start":True}),
         ("cratyyyymmdd start",     {"field":"cratyyyymmdd","start":"2020-01-01","inclusive_start":True}),
         ("crat start+end",         {"field":"crat","start":"2020-01-01","end":"2030-01-01","inclusive_start":True}),
         ("crat numeric min",       {"field":"crat","min":20200101,"inclusive_min":True}),
         ("cratyyyymmdd numeric",   {"field":"cratyyyymmdd","min":20200101,"inclusive_min":True}),
         ("cratts start",           {"field":"cratts","start":"2020-01-01","inclusive_start":True}),
        ]
        for label,dq in DATE:
            r=pg.evaluate(JS,json.dumps(bq(trip(winner)+[dq]))); time.sleep(0.9)
            mark=" <== MATCH" if r.get("total")==29150 else ""
            print(f"  {label:22} status={r.get('status')} total={r.get('total')} {r.get('err') or ''}{mark}")
    else:
        print("\nNo base matched 33944 — query type still wrong.")
    b.close()
print("\n=== CRACK BQ3 DONE ===")
