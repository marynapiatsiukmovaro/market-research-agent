#!/usr/bin/env python3
"""
Foundation probes via the logged-in session fetch (gentle):
(A) crack SORT param, (B) demonstrate the 'filter drops stores with no data' effect +
crack the CREATED filter, (C) category census (cat1 + cat facet counts) under base filter.
Run on VPS: python3 scripts/sl_probe.py
"""
import json, time
from playwright.sync_api import sync_playwright
STATE = "/opt/market-research-agent/cookies/storeleads_state.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
JS = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  const ds=(j&&j.domains)||[];
  return {status:r.status, total:j&&j.totalHits, sort:j&&j.request&&j.request.s,
    req:j&&j.request, first:ds.slice(0,3).map(d=>({n:d.name,cr:(d.createdAt||'')&&String(d.createdAt).slice(0,7),er:d.erf})),
    facets:j&&j.facets};
}"""
BASE = {"f:p": "1", "f:ds": "1"}
def post(pg, body):
    return pg.evaluate(JS, json.dumps(body))
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={"width":1400,"height":1000})
    pg = ctx.new_page()
    pg.goto("https://storeleads.app/dashboard/domains", wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(2500)

    print("######## (A) SORT PROBES (US K&D) ########")
    kd = {**BASE, "f:cc":"US", "f:cat":"/Home & Garden/Kitchen & Dining"}
    for s in [["rank","_id"], ["createdAt","_id"], ["-createdAt","_id"], ["er","_id"], ["-er","_id"], ["ery","_id"]]:
        r = post(pg, {**kd, "s": s}); time.sleep(1.2)
        print(f"  s={s} -> echo_s={r.get('sort')} total={r.get('total')} first={r.get('first')}")

    print("\n######## (B) CREATED FILTER PROBES (US K&D, total w/o created = ~13335) ########")
    for k,v in [("f:cratyyyymmdd","2020-01-01"),("f:cratyyyymmdd","2020-01-01,"),
                ("f:cratyyyymm","2020-01"),("f:crat",">=2020-01-01"),("f:cratyyyymmdd","[2020-01-01 TO *]")]:
        r = post(pg, {**kd, k:v}); time.sleep(1.2)
        echo = {kk:vv for kk,vv in (r.get('req') or {}).items() if 'crat' in kk.lower() or 'qcr' in kk.lower()}
        print(f"  {k}={v!r} -> total={r.get('total')} echo_crat={echo}")

    print("\n######## (B2) FILTER-DROP EVIDENCE ########")
    for label, body in [("Shopify+Active (no cat)", BASE),
                        ("+ any category (f:cat1 set to each? use None test)", {**BASE}),
                        ("+ US", {**BASE,"f:cc":"US"})]:
        r = post(pg, body); time.sleep(1.0)
        print(f"  {label}: total={r.get('total')}")
    # show how many have NO category (None bucket) under Shopify+Active
    r = post(pg, {**BASE, "all_facets": True}); time.sleep(1.0)
    fac = r.get("facets") or {}
    def terms(key,n=18):
        f=fac.get(key,{}); out=[]
        for t in (f.get("terms") or [])[:n]:
            out.append((t.get("term"), t.get("count")))
        return f.get("total"), out
    c1tot, c1 = terms("cat1")
    print(f"\n######## (C) CENSUS — cat1 under Shopify+Active (facet total tagged={c1tot}) ########")
    for term,cnt in c1:
        print(f"  {cnt:>9}  {term}")
    print("\n  --- cat (L2 subcategories), top 40 ---")
    _, c2 = terms("cat", 45)
    for term,cnt in c2:
        print(f"  {cnt:>9}  {term}")
    b.close()
print("\n=== SL PROBE DONE ===")
