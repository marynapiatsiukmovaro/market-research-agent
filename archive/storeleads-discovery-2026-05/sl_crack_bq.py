#!/usr/bin/env python3
"""Crack the `bq` advanced-query format by INTERCEPTING the real request the SPA fires.
Strategy: install a request listener on /json/auth/domains capturing postData, then
navigate to dashboard URLs carrying a `bq` query param (as the UI does). Whatever the
SPA actually POSTs is canonical truth. Validate totalHits against known numbers:
  K&D no-date = 33,944 ; K&D created>=2020-01-01 = 29,150.
Run on VPS: python3 scripts/sl_crack_bq.py
"""
import json, time, urllib.parse
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
KD="/Home & Garden/Kitchen & Dining"

# candidate bq objects to drop in the URL (UI reads bq from query string)
CANDIDATES = {
 "A_min_platform_only": {"must":{"conjuncts":[{"field":"p","operator":"is","value":"1"}]}},
 "B_p_ds_cat": {"must":{"conjuncts":[
     {"field":"p","operator":"is","value":"1"},
     {"field":"ds","operator":"is","value":"1"},
     {"field":"cat","operator":"is","value":KD}]}},
 "C_with_created_range": {"must":{"conjuncts":[
     {"field":"p","operator":"is","value":"1"},
     {"field":"ds","operator":"is","value":"1"},
     {"field":"cat","operator":"is","value":KD},
     {"field":"cratyyyymmdd","operator":"range","start":"2020-01-01"}]}},
}

captured=[]  # (url_label, postData, total)

with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page()
    last_post={"data":None}
    def on_req(req):
        if "/json/auth/domains" in req.url and req.method=="POST":
            last_post["data"]=req.post_data
    pg.on("request", on_req)

    # ---- (0) DEFAULT load: what does the SPA send with NO filters? (zero-guess canonical body) ----
    last_post["data"]=None
    resp_total={"t":None}
    def on_resp(resp):
        if "/json/auth/domains" in resp.url and resp.request.method=="POST":
            try: resp_total["t"]=resp.json().get("totalHits")
            except: pass
    pg.on("response", on_resp)
    pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000)
    pg.wait_for_timeout(3000)
    print("######## (0) DEFAULT dashboard request body ########")
    print("  POST body:", last_post["data"])
    print("  total:", resp_total["t"])

    # ---- (1..) navigate with each candidate bq in URL, capture what SPA re-emits + total ----
    for label,obj in CANDIDATES.items():
        bq=urllib.parse.quote(json.dumps(obj))
        url=f"https://storeleads.app/dashboard/domains?bq={bq}"
        last_post["data"]=None; resp_total["t"]=None
        pg.goto(url,wait_until="networkidle",timeout=60000)
        pg.wait_for_timeout(3500)
        print(f"\n######## {label} ########")
        print("  sent in URL:", json.dumps(obj,ensure_ascii=False))
        print("  SPA POSTed :", last_post["data"])
        print("  total      :", resp_total["t"], "(KD nofilter=33944, KD>=2020=29150)")
    b.close()
print("\n=== CRACK BQ DONE ===")
