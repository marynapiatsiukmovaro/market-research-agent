# Capture PUBLIC Store Leads pages (no login) for interface review. Full-page PNGs.
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/shophunter"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
PAGES = [
    ("https://storeleads.app/", "01_home"),
    ("https://storeleads.app/#pricing", "02_pricing"),
    ("https://storeleads.app/help/features/advanced-search", "03_advanced_search"),
    ("https://storeleads.app/help/features/product_search", "04_product_search"),
    ("https://storeleads.app/help/features/historical-data", "05_historical_data"),
    ("https://storeleads.app/help/features/calculated-values", "06_calculated_values"),
    ("https://storeleads.app/help/faq/list-of-domain-filters", "07_filters_list"),
    ("https://storeleads.app/api", "08_api"),
    ("https://storeleads.app/help", "09_help_index"),
]
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"])
    ctx = b.new_context(user_agent=UA, viewport={"width": 1440, "height": 1600}, device_scale_factor=2)
    pg = ctx.new_page()
    for url, tag in PAGES:
        try:
            pg.goto(url, wait_until="networkidle", timeout=45000)
            pg.wait_for_timeout(2500)
            for y in (600, 1400, 2400, 3400):
                pg.evaluate("window.scrollTo(0,%d)" % y); pg.wait_for_timeout(500)
            pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(800)
            pg.screenshot(path="%s/sl_%s.png" % (OUT, tag), full_page=True)
            print("OK", tag, "|", url)
        except Exception as e:
            print("ERR", tag, type(e).__name__, "|", url)
    b.close()
print("=== SL SHOTS DONE ===")
