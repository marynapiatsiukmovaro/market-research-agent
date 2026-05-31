#!/usr/bin/env python3
# Diagnose WHY the 12 unreachable stores failed: is the SITE up, and is /products.json disabled/blocked?
# Distinguishes "site down" from "catalog API disabled but site openable (WebFetch fallback would work)".
import json, sys
from playwright.sync_api import sync_playwright
creds={}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line: k,v=line.strip().split("=",1); creds[k]=v
PROXY={"server":"http://%s:%s"%(creds["PROXY_HOST"],creds["PROXY_PORT"]),"username":creds["PROXY_USER"],"password":creds["PROXY_PASS"]}
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
d=json.load(open("/opt/market-research-agent/logs/storeleads/hi_band_200_enriched.json"))
doms=[r["domain"] for r in d if not r.get("reachable")]
def probe(pg,url):
    try:
        r=pg.goto(url,wait_until="domcontentloaded",timeout=20000)
        st=r.status if r else None
        body=""
        try: body=pg.inner_text("body")[:200]
        except: pass
        return st, body.strip().replace("\n"," ")[:80]
    except Exception as e:
        return None, type(e).__name__
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"],proxy=PROXY)
    pg=b.new_context(user_agent=UA).new_page()
    print(f"{'domain':32} {'home':>6} {'pjson':>6}  verdict")
    for dom in doms:
        hs,hb=probe(pg,"https://%s/"%dom)
        js,jb=probe(pg,"https://%s/products.json?limit=1"%dom)
        if js==200 and jb.startswith("{"): verdict="products.json OK NOW (transient earlier)"
        elif hs and hs<400 and (js in (404,401,403) or not jb.startswith("{")): verdict="SITE UP, products.json disabled/blocked -> WebFetch homepage would work"
        elif hs is None: verdict="site unreachable via proxy (down/geo/block): %s"%hb
        else: verdict="home=%s pjson=%s"%(hs,js)
        print(f"{str(dom)[:32]:32} {str(hs):>6} {str(js):>6}  {verdict}")
    b.close()
print("=== RETRY DIAG DONE ===")
