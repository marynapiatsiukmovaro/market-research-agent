#!/usr/bin/env python3
"""Put the CRACKED Bleve bq in the URL path -> SPA forwards to server -> table renders with filter+count.
Target Home Improvement >=2020 = 27,052. VPS."""
import json, urllib.parse
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
HI="/Home & Garden/Home Improvement"
bleve={"must":{"conjuncts":[
  {"field":"p","term":"1"},
  {"field":"ds","term":"1"},
  {"field":"cat","match":HI},
  {"field":"cratyyyymm","min":"2020-01","inclusive_min":True}]}}
enc=urllib.parse.quote(json.dumps(bleve),safe="")
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1700,"height":1100},device_scale_factor=2)
    pg=ctx.new_page()
    pg.goto(f"https://storeleads.app/dashboard/domains/bq={enc}",wait_until="networkidle",timeout=60000)
    pg.wait_for_timeout(6000)
    pg.screenshot(path=f"{OUT}/sl_adv_HI_2020.png",full_page=True)
    print("saved sl_adv_HI_2020 | url:", pg.url[:80])
    b.close()
print("=== SHOTS3 DONE ===")
