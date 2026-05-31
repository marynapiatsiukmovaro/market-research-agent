#!/usr/bin/env python3
"""Crack created-range: POST `bq` directly in body + test f: range encodings.
Validate by totalHits: K&D no-date=33944 ; K&D created>=2020-01-01=29150. VPS."""
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

# bq base = category exact (expect 33944) — find which operator/value key works
BQ_BASE = lambda conj: {"all_facets":True,"bq":{"must":{"conjuncts":conj}}}
BQ_BASE_STR = lambda conj: {"all_facets":True,"bq":json.dumps({"must":{"conjuncts":conj}})}
cat_is   = [{"field":"cat","operator":"is","value":KD}]
cat_Is   = [{"field":"cat","operator":"Is","value":KD}]
cat_eq   = [{"field":"cat","operator":"eq","value":KD}]
cat_vals = [{"field":"cat","operator":"is","values":[KD]}]
cat_oneof= [{"field":"cat","operator":"one_of","values":[KD]}]

# created range conjuncts (appended to whichever base works) — many key styles
def crat(op,**kw): return {"field":"cratyyyymmdd","operator":op, **kw}

CANDS = [
 ("bq obj cat is value",            BQ_BASE(cat_is)),
 ("bq obj cat Is value",            BQ_BASE(cat_Is)),
 ("bq obj cat eq value",            BQ_BASE(cat_eq)),
 ("bq obj cat is values[]",         BQ_BASE(cat_vals)),
 ("bq obj cat one_of values[]",     BQ_BASE(cat_oneof)),
 ("bq STRING cat is value",         BQ_BASE_STR(cat_is)),
 # f: range encodings (no bq)
 ("f:cratyyyymmdd from/to keys",    {"all_facets":True,"f:p":"1","f:ds":"1","f:cat":KD,"f:cratyyyymmdd_from":"2020-01-01"}),
 ("f:cratyyyymmdd range comma",     {"all_facets":True,"f:p":"1","f:ds":"1","f:cat":KD,"f:cratyyyymmdd":"2020-01-01,2030-01-01"}),
 ("f:crat gte string",              {"all_facets":True,"f:p":"1","f:ds":"1","f:cat":KD,"f:crat":"2020-01-01,"}),
 ("f:cratyyyymm range comma",       {"all_facets":True,"f:p":"1","f:ds":"1","f:cat":KD,"f:cratyyyymm":"2020-01,2026-12"}),
]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    def post(body): return pg.evaluate(JS,json.dumps(body))
    print(f"{'candidate':34} {'status':>6} {'total':>9}  note")
    for label,body in CANDS:
        r=post(body); time.sleep(1.0)
        print(f"{label:34} {str(r.get('status')):>6} {str(r.get('total')):>9}  {r.get('err') or ''}")

    # If a bq base hit 33944, immediately try created range on it
    print("\n---- created-range trials on bq base (cat is value) ----")
    base_conj=cat_is
    for label,extra in [
        ("range start",      crat("range",start="2020-01-01")),
        ("range start/end",  crat("range",start="2020-01-01",end="2030-01-01")),
        ("range from/to",    crat("range",**{"from":"2020-01-01","to":"2030-01-01"})),
        ("range gte/lte",    crat("range",gte="2020-01-01",lte="2030-01-01")),
        ("gte op value",     crat("gte",value="2020-01-01")),
        ("range value[]",    crat("range",value=["2020-01-01","2030-01-01"])),
        ("between value[]",  crat("between",value=["2020-01-01","2030-01-01"])),
    ]:
        body=BQ_BASE(base_conj+[extra])
        r=post(body); time.sleep(1.0)
        print(f"  {label:22} status={r.get('status')} total={r.get('total')}  {r.get('err') or ''} (want 29150)")
    b.close()
print("\n=== CRACK BQ2 DONE ===")
