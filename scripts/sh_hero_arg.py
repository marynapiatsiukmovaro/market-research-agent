import json, time, sys
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/shophunter"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
rows = json.load(open(OUT + "/" + INF))

def parse_top(txt):
    tp = txt.find("Top Products")
    if tp < 0:
        return []
    seg = txt[tp:]
    lines = [l.strip() for l in seg.split("\n") if l.strip()]
    ps = []
    for i, l in enumerate(lines):
        if l == "Competitor Analysis":
            break
        if l == "Product Ads" and i >= 2:
            title, price = lines[i - 2], lines[i - 1]
            if not price.startswith("$"):
                continue
            wk = ""
            for j in range(i, min(i + 14, len(lines))):
                if lines[j] == "Product Revenue - Day/Week" and j + 3 < len(lines):
                    wk = lines[j + 3]
                    break
            ps.append({"t": title[:60], "price": price, "wk": wk})
    return ps

res = []
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir="/opt/market-research-agent/cookies/shophunter_profile",
        headless=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        viewport={"width": 1500, "height": 1700})
    pg = ctx.new_page()
    for idx, r in enumerate(rows):
        sid = r["shop_id"]
        o = {"shop_id": sid, "name": r.get("name", ""), "domain": r.get("domain", ""),
             "country": r.get("country", ""), "sku": r.get("sku", ""), "shop_ads": r.get("shop_ads", ""),
             "rev_week": r.get("rev_week", ""), "fb": r.get("fb", ""), "top": []}
        try:
            pg.goto("https://app.shophunter.io/shops/" + sid, wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(4500)
            for y in (400, 1200, 2200):
                pg.evaluate("window.scrollTo(0,%d)" % y)
                pg.wait_for_timeout(400)
            o["top"] = parse_top(pg.eval_on_selector("body", "e=>e.innerText"))
        except Exception as e:
            o["err"] = type(e).__name__
        res.append(o)
        if (idx + 1) % 10 == 0:
            json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False)
            print("...", idx + 1, "/", len(rows), "hero=", sum(1 for x in res if x["top"]), flush=True)
        time.sleep(0.8)
    ctx.close()
json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
open(OUT + "/" + SENT, "w").write("done %d hero=%d" % (len(res), sum(1 for x in res if x["top"])))
print("=== DONE ===", sum(1 for x in res if x["top"]), "/", len(res))
