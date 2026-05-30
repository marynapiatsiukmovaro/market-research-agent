# Store Leads Stage-2 enricher. Input = sl_dump survivors (domain + Store-Leads store data,
# NO per-product revenue). Reads LIVE /products.json via proxy, surfaces top catalog products
# (hero chosen by main agent at deep-score), real prices + desc + classification + convergence.
import json, re, sys, time
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/storeleads"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 4
LIMIT = int(sys.argv[5]) if len(sys.argv) > 5 else 0
creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1); creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
INGEST = ["supplement", "softgel", "soft gel", "capsule", "vitamin", "gummies", "gummy", "probiotic", "tincture",
          "shilajit", "electrolyte", "omega", "creatine", "protein powder", "turmeric", "magnesium", "biotin",
          "berberine", "nmn", "moringa", "sea moss", "mushroom", "elixir", "tonic", "collagen powder", "tea bag"]
SKIN = ["serum", "face oil", "balm", "lotion", "moisturizer", "cleanser", "toner", "sheet mask", "ampoule", "essence"]
APP = ["dress", "shirt", "t-shirt", "tee ", "sneaker", "legging", "hoodie", "jacket", "necklace", "earring",
       "bracelet", "jeans", "cardigan", "blazer", "loafer", "skirt", "shorts", "apron"]
JUNK = ["shipping protection", "protection plan", "gift card", "warranty", "route package", "insurance", "donation",
        "sample", "e-gift", "subscription", "digital download", "ebook", "recipe book"]
PUST = ["lymphatic", "red light therapy", "infrared therapy", "magnetic therapy", "detox", "slimming", "cellulite",
        "circulation", "anti-aging", "chakra", "aura", "parasite", "body cleanse", "alkaline water", "grounding"]
NICHE = [("Kitchen-prep", ["cutting board", "knife", "peeler", "grater", "chopper", "mandoline", "press"]),
         ("Kitchen-cook", ["pan", "pot", "cookware", "skillet", "dutch oven", "grill", "griddle", "bakeware"]),
         ("Kitchen-appliance", ["juicer", "blender", "frother", "espresso", "kettle", "toaster", "air fryer", "mixer", "maker"]),
         ("Drinkware", ["bottle", "tumbler", "flask", "mug", "cup", "glass", "carafe", "pitcher"]),
         ("Storage/Organize", ["jar", "container", "canister", "organizer", "storage", "lid", "wrap", "bag"]),
         ("Tableware", ["plate", "bowl", "cutlery", "flatware", "utensil", "dinnerware", "serving"]),
         ("Cleaning", ["scrubber", "scrub", "cleaner", "sponge", "brush", "dish"]),
         ("Gadget", ["dispenser", "thermometer", "scale", "timer", "sharpener", "opener", "tool"])]
def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, l):
    s = low(t); return any(k in s for k in l)
def npx(s):
    m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
def kind(t):
    if has(t, INGEST): return "ingestible"
    if has(t, SKIN): return "skincare"
    if has(t, APP): return "apparel"
    return "physical"
def niche_of(t):
    for n, kws in NICHE:
        if has(t, kws): return n
    return "Other"
def clean_desc(html):
    t = re.sub(r"<[^>]+>", " ", html or "")
    t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:200]
def get_json(pg, url, tries=4):
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=30000)
            body = pg.inner_text("body")
            if body.strip().startswith("{"):
                return json.loads(body)
        except Exception:
            pass
        time.sleep(2.5 + a * 2.5)
    return None
def pick(products):
    out = []
    for p in products[:40]:
        title = p.get("title", "")
        if has(title, JUNK):
            continue
        v = (p.get("variants") or [{}])[0]
        price = npx(v.get("price"))
        cmp_at = npx(v.get("compare_at_price"))
        img = ""
        if p.get("images"):
            img = (p["images"][0].get("src") or "")
        desc = clean_desc(p.get("body_html"))
        out.append({"t": title, "price": price, "cmp": cmp_at, "k": kind(title + " " + desc), "desc": desc, "img": img})
        if len(out) >= 12:
            break
    return out
def work(args):
    wid, chunk = args; res = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
        ctx = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600})
        pg = ctx.new_page()
        for d in chunk:
            time.sleep(1.0)
            dom = (d.get("name") or "").replace("https://", "").replace("http://", "").rstrip("/")
            cat = get_json(pg, "https://" + dom + "/products.json?limit=250")
            prods = cat.get("products", []) if cat else None
            tops = pick(prods) if prods else []
            pcount = len(prods) if prods else 0
            phys = [x for x in tops if x["k"] == "physical"]
            inr = [x for x in phys if 39 <= x["price"] <= 170]
            cand = (max(inr, key=lambda x: x["price"]) if inr else (phys[0] if phys else (tops[0] if tops else None)))
            pc = d.get("pc") or 0
            o = {"store": (d.get("merch") or dom)[:26], "domain": dom, "reachable": cat is not None,
                 "sl_rev": d.get("erf"), "sl_avg": d.get("apf"), "sl_pc": pc, "created": str(d.get("created") or "")[:10],
                 "fbpx": d.get("fbpx"), "cat_flag": ("hero" if pc <= 300 else "mid" if pc <= 2000 else "catalog-giant"),
                 "live_pc": pcount, "tops": [{"t": x["t"][:34], "$": x["price"], "k": x["k"]} for x in tops]}
            if cand is None:
                o["tier"] = "DROP"; o["candidate"] = None; res.append(o); continue
            o["candidate"] = cand["t"][:60]; o["price"] = cand["price"]; o["in_range"] = 39 <= cand["price"] <= 170
            o["niche"] = niche_of(cand["t"]); o["desc"] = cand["desc"]; o["image"] = cand["img"]
            o["anchor"] = round(100 * (1 - cand["price"] / cand["cmp"])) if cand["cmp"] > cand["price"] > 0 else 0
            o["pust"] = has(cand["t"] + " " + cand["desc"], PUST); o["kind"] = cand["k"]
            res.append(o)
        b.close()
    return res
if __name__ == "__main__":
    rows = json.load(open(OUT + "/" + INF))
    if LIMIT:
        rows = rows[:LIMIT]
    chunks = [(w, rows[w::NW]) for w in range(NW)]
    t0 = time.time()
    with Pool(NW) as pool:
        parts = pool.map(work, chunks)
    res = [x for part in parts for x in part]
    cands = [r for r in res if r.get("candidate")]
    def toks(s): return set(w for w in low(s).split() if len(w) > 3)
    for r in cands:
        rt = toks(r["candidate"]); n = 0
        for o in cands:
            if o is r: continue
            if len(rt & toks(o["candidate"])) >= 2: n += 1
        r["conv_batch"] = n
    def revnum(s):
        m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
    for r in res:
        if not r.get("candidate"):
            r["score"] = 0; r["flags"] = []; r["line"] = "[DROP] " + r["domain"]; continue
        inr = r["in_range"]; pust = r["pust"]; phys = r["kind"] == "physical"
        conv = r.get("conv_batch", 0) >= 1
        rev = revnum(r.get("sl_rev"))
        sc = 0
        sc += 35 if inr else 5
        sc += 20 if conv else 0
        sc += 18 if rev >= 300000 else 13 if rev >= 100000 else 9 if rev >= 50000 else 5
        if r["cat_flag"] == "hero": sc += 7
        elif r["cat_flag"] == "catalog-giant": sc -= 8
        if pust: sc -= 30
        if not phys: sc -= 30
        if r["anchor"] >= 55: sc -= 6
        r["score"] = sc
        flags = []
        if conv: flags.append("CONV-batch:%d" % r["conv_batch"])
        if pust: flags.append("пустышка")
        if not phys: flags.append(r["kind"])
        if not inr: flags.append("price-out")
        flags.append(r["cat_flag"])
        r["flags"] = flags
        r["tier"] = "A" if sc >= 58 and inr and phys and not pust else ("B" if sc >= 42 and inr and phys and not pust else "C")
        r["line"] = "[%s|%d] %s | %s $%.0f%s | rev:%s pc:%s | %s" % (
            r["tier"], sc, r["niche"], r["candidate"][:30], r["price"], "" if inr else "(OUT)",
            r.get("sl_rev") or "-", r.get("sl_pc"), (r["desc"][:80] or "no-desc"))
    order = {"A": 0, "B": 1, "C": 2, "DROP": 3}
    res.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d tiers=%s" % (
        len(res), round(time.time() - t0), sum(1 for r in res if r.get("reachable")), dict(Counter(r.get("tier") for r in res))))
    print("=== SL ENRICH DONE ===", len(res), "secs", round(time.time() - t0),
          "| reachable", sum(1 for r in res if r.get("reachable")), "| tiers", dict(Counter(r.get("tier") for r in res)))
