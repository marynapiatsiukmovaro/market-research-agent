# Parallel hero extractor: N workers share one login (storage_state), smart wait, top-3 capture.
# Usage: sh_hero_par.py <infile> <outfile> <sentinel> [nworkers]
import json, time, sys, os
from multiprocessing import Pool
from playwright.sync_api import sync_playwright

OUT = "/opt/market-research-agent/logs/shophunter"
STATE = "/opt/market-research-agent/cookies/sh_state.json"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 4
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"


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


def work(args):
    wid, chunk = args
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"])
        ctx = b.new_context(storage_state=STATE, user_agent=UA, viewport={"width": 1500, "height": 1700})
        pg = ctx.new_page()
        for r in chunk:
            sid = r["shop_id"]
            o = {"shop_id": sid, "name": r.get("name", ""), "domain": r.get("domain", ""),
                 "country": r.get("country", ""), "sku": r.get("sku", ""), "shop_ads": r.get("shop_ads", ""),
                 "rev_week": r.get("rev_week", ""), "fb": r.get("fb", ""), "top": []}
            try:
                pg.goto("https://app.shophunter.io/shops/" + sid, wait_until="domcontentloaded", timeout=45000)
                try:
                    pg.wait_for_selector("text=Top Products", timeout=9000)
                except Exception:
                    pass
                # original scroll cadence (lazy-load trigger) — this is what gave 100%
                for y in (400, 1200, 2200):
                    pg.evaluate("window.scrollTo(0,%d)" % y)
                    pg.wait_for_timeout(400)
                top = parse_top(pg.eval_on_selector("body", "e=>e.innerText"))
                tries = 0
                while not top and tries < 2:  # retry safety net for slow stores
                    pg.wait_for_timeout(1500)
                    pg.evaluate("window.scrollTo(0,2200)")
                    pg.wait_for_timeout(400)
                    top = parse_top(pg.eval_on_selector("body", "e=>e.innerText"))
                    tries += 1
                o["top"] = top
            except Exception as e:
                o["err"] = type(e).__name__
            res.append(o)
        b.close()
    return res


if __name__ == "__main__":
    rows = json.load(open(OUT + "/" + INF))
    chunks = [(w, rows[w::NW]) for w in range(NW)]  # round-robin split
    t0 = time.time()
    with Pool(NW) as pool:
        parts = pool.map(work, chunks)
    res = [x for part in parts for x in part]
    order = {r["shop_id"]: i for i, r in enumerate(rows)}
    res.sort(key=lambda o: order.get(o["shop_id"], 0))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    secs = round(time.time() - t0)
    hero = sum(1 for x in res if x["top"])
    open(OUT + "/" + SENT, "w").write("done %d hero=%d secs=%d workers=%d" % (len(res), hero, secs, NW))
    print("=== DONE ===", len(res), "stores | hero", hero, "| secs", secs, "| workers", NW)
