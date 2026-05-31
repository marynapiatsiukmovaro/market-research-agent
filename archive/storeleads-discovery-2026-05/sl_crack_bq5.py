#!/usr/bin/env python3
"""Validate multi-category OR (disjuncts) + created-window split. VPS."""
import json, time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
KD="/Home & Garden/Kitchen & Dining"; HI="/Home & Garden/Home Improvement"
JS="""async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {status:r.status, total:j&&j.totalHits, err:j&&(j.error||j.message)};
}"""
def bq(conj): return {"all_facets":True,"bq":json.dumps({"must":{"conjuncts":conj}})}
P=[{"field":"p","term":"1"},{"field":"ds","term":"1"}]
def post(pg,conj): return pg.evaluate(JS,json.dumps(bq(conj)))
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    cre=lambda lo,hi=None: ({"field":"cratyyyymm","min":lo,"inclusive_min":True} if not hi else {"field":"cratyyyymm","min":lo,"max":hi,"inclusive_min":True,"inclusive_max":True})

    print("== multi-category OR (K&D + Home Improvement, >=2020) ; expect ~56202 (29150+27052) ==")
    disj={"disjuncts":[{"field":"cat","match":KD},{"field":"cat","match":HI}]}
    r=post(pg,P+[disj,cre("2020-01")]); print("  disjuncts:",r.get("status"),r.get("total"),r.get("err") or "")
    time.sleep(0.9)

    print("\n== created-window split on K&D (expect each <25k, sum=29150) ==")
    r1=post(pg,P+[{"field":"cat","match":KD},cre("2020-01","2022-12")]); time.sleep(0.9)
    r2=post(pg,P+[{"field":"cat","match":KD},cre("2023-01")]); time.sleep(0.9)
    print(f"  2020-01..2022-12 = {r1.get('total')}")
    print(f"  2023-01..now     = {r2.get('total')}")
    a=r1.get('total') or 0; c=r2.get('total') or 0
    print(f"  SUM = {a+c} (want 29150)")

    print("\n== Home Improvement >=2020 window split (expect each <25k) ==")
    h1=post(pg,P+[{"field":"cat","match":HI},cre("2020-01","2022-12")]); time.sleep(0.9)
    h2=post(pg,P+[{"field":"cat","match":HI},cre("2023-01")]); time.sleep(0.9)
    print(f"  2020-01..2022-12 = {h1.get('total')}")
    print(f"  2023-01..now     = {h2.get('total')}")
    print(f"  SUM = {(h1.get('total') or 0)+(h2.get('total') or 0)} (HI >=2020 census = 27052)")
    b.close()
print("\n=== CRACK BQ5 DONE ===")
