#!/usr/bin/env python3
"""Count stores matching a filter LIVE on StoreLeads (totalHits) — verify export completeness.
Usage: python3 sl_filter_count.py "<cat path or ''>" [vlo] [vhi]
Prints HTTP status (200 = logged in), totalHits, and the server's echoed parsed request (ground truth).
"""
import json, sys
from playwright.sync_api import sync_playwright
STATE = "/opt/market-research-agent/cookies/storeleads_state.json"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
cat = sys.argv[1] if len(sys.argv) > 1 else ""
vlo = sys.argv[2] if len(sys.argv) > 2 else None
vhi = sys.argv[3] if len(sys.argv) > 3 else None
conj = [{"field": "p", "term": "1"}, {"field": "ds", "term": "1"}]
if cat:
    conj.append({"field": "cat", "match": cat})
if vlo or vhi:
    rng = {"field": "mvis"}
    if vlo:
        rng["min"] = float(vlo); rng["inclusive_min"] = True
    if vhi:
        rng["max"] = float(vhi); rng["inclusive_max"] = True
    conj.append(rng)
bq = {"must": {"conjuncts": conj}}
FETCH = """async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {status:r.status, total:j&&j.totalHits, n:(j&&j.domains||[]).length, req:j&&j.request};
}"""
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = b.new_context(storage_state=STATE, user_agent=UA)
    pg = ctx.new_page()
    pg.goto("https://storeleads.app/dashboard/domains", wait_until="networkidle", timeout=60000)
    pg.wait_for_timeout(2000)
    r = pg.evaluate(FETCH, json.dumps({"bq": json.dumps(bq), "ps": 1}))
    print("bq:", json.dumps(bq))
    print("result:", json.dumps(r))
    b.close()
