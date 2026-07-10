#!/usr/bin/env python3
"""S20 probe 2 — can Shopify give us the human's shelf when there is no best-selling collection?
Compares, per domain: homepage order · /collections/all?sort_by=best-selling · plain /products.json."""
import re, sys, time, json
from playwright.sync_api import sync_playwright
creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1); creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
def get(pg, url):
    for _ in range(2):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=20000); return pg.content(), pg.inner_text("body")
        except Exception: time.sleep(1.5)
    return "", ""
def handles(html, n=5):
    out = []
    for h in re.findall(r"/products/([a-z0-9][a-z0-9\-]{1,80})", html or ""):
        if h not in out: out.append(h)
        if len(out) >= n: break
    return out
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
    pg = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600}).new_page()
    for dom in sys.argv[1:]:
        print("="*94); print(dom)
        h, _ = get(pg, f"https://{dom}/")
        print("  ГЛАВНАЯ                                :", handles(h))
        h, _ = get(pg, f"https://{dom}/collections/all?sort_by=best-selling")
        print("  ВИТРИНА sort_by=best-selling           :", handles(h))
        _, body = get(pg, f"https://{dom}/products.json?limit=5")
        try: js = json.loads(body) if body.strip().startswith("{") else {"products": []}
        except Exception: js = {"products": []}
        print("  /products.json (что робот читает сейчас):", [x.get("handle") for x in js.get("products", [])[:5]])
    b.close()
