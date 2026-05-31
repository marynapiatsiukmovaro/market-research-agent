#!/usr/bin/env python3
"""Test path-form bq URL (UI form: operator/values) renders Advanced filters + count in headless.
Try platform-only first (target 3,593,276), then full filter. VPS."""
import json, urllib.parse, time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
HI="/Home & Garden/Home Improvement"
def uiform(conj): return urllib.parse.quote(json.dumps({"must":{"conjuncts":conj}}),safe="")
TESTS=[
 ("plat_v1",  [{"field":"p","operator":"Or","values":["1"]}]),
 ("plat_shop",[{"field":"p","operator":"Or","values":["Shopify"]}]),
 ("full_hi",  [{"field":"p","operator":"Or","values":["1"]},
               {"field":"ds","operator":"Or","values":["1"]},
               {"field":"cat","operator":"Or","values":[HI]}]),
]
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1600,"height":1100},device_scale_factor=2)
    pg=ctx.new_page()
    for name,conj in TESTS:
        url=f"https://storeleads.app/dashboard/domains/bq={uiform(conj)}"
        try: pg.goto(url,wait_until="networkidle",timeout=60000)
        except Exception as e: print("warn",name,e)
        pg.wait_for_timeout(5000)
        pg.screenshot(path=f"{OUT}/sl_adv_{name}.png",full_page=False)
        print("saved sl_adv_"+name, "| url:", pg.url[:90])
    b.close()
print("=== SHOTS2 DONE ===")
