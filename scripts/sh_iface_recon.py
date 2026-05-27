# ShopHunter interface recon: capture Explore Shops + Explore Products UI
# (category taxonomy, sort/filter controls) for strategy review. Login via storage_state, no proxy.
import sys
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/shophunter"
STATE = "/opt/market-research-agent/cookies/sh_state.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

def grab(pg, url, tag):
    pg.goto(url, wait_until="domcontentloaded", timeout=45000)
    pg.wait_for_timeout(4000)
    for y in (300, 900):
        pg.evaluate("window.scrollTo(0,%d)" % y); pg.wait_for_timeout(600)
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(500)
    pg.screenshot(path="%s/iface_%s.png" % (OUT, tag), full_page=True)
    txt = pg.eval_on_selector("body", "e=>e.innerText")
    print("\n========== %s (%s) ==========" % (tag, url))
    print(txt[:4000])

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={"width": 1500, "height": 2200})
    pg = ctx.new_page()
    grab(pg, "https://app.shophunter.io/explore/shops", "explore_shops")
    # try to open the category filter panel if collapsed (click any 'Categories' text)
    try:
        loc = pg.locator("text=Categories").first
        if loc.count():
            loc.click(); pg.wait_for_timeout(1500)
            pg.screenshot(path="%s/iface_shops_categories.png" % OUT, full_page=True)
            print("\n---- after click Categories ----")
            print(pg.eval_on_selector("body", "e=>e.innerText")[:3500])
    except Exception as e:
        print("cat-click:", type(e).__name__)
    grab(pg, "https://app.shophunter.io/explore/products", "explore_products")
    b.close()
print("\n=== RECON DONE ===")
