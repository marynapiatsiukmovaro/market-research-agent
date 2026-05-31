#!/usr/bin/env python3
"""Capture how the logged-in StoreLeads dashboard looks on our VPS session, for Marina to compare. VPS."""
import time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1600,"height":1100},device_scale_factor=2)
    pg=ctx.new_page()
    shots=[
      ("https://storeleads.app/dashboard/domains","sl_view_1_domains"),
      ("https://storeleads.app/dashboard/account","sl_view_2_account"),
      ("https://storeleads.app/dashboard/domains?f:cat=/Home%20%26%20Garden/Home%20Improvement","sl_view_3_homeimprov"),
    ]
    for url,name in shots:
        try:
            pg.goto(url,wait_until="networkidle",timeout=60000)
        except Exception as e:
            print("nav warn",name,e)
        pg.wait_for_timeout(4500)
        pg.screenshot(path=f"{OUT}/{name}.png",full_page=True)
        print("saved",name, "| title:", pg.title(), "| url:", pg.url)
    b.close()
print("=== SHOTS DONE ===")
