# Store Leads Stage-2 enricher v2 — REAL hero detection.
# Hero = first physical product of the store's best-selling/frontpage collection (sales order),
# fallback to /products.json. Keeps top-8 catalog for the main agent. Real price + desc + class.
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
INGEST = ["supplement", "softgel", "capsule", "vitamin", "gummies", "gummy", "probiotic", "tincture", "shilajit",
          "electrolyte", "omega", "creatine", "protein powder", "turmeric", "magnesium", "biotin", "berberine",
          "nmn", "moringa", "sea moss", "mushroom", "elixir", "tonic", "collagen powder", "tea bag", "coffee bean", "ground coffee"]
SKIN = ["serum", "face oil", "balm", "lotion", "moisturizer", "cleanser", "toner", "sheet mask", "ampoule"]
APP = ["dress", "shirt", "t-shirt", "tee ", "sneaker", "legging", "hoodie", "jacket", "necklace", "earring",
       "bracelet", "jeans", "cardigan", "blazer", "loafer", "skirt", "shorts", "apron", "hat ", "sock"]
JUNK = ["shipping protection", "protection plan", "gift card", "warranty", "route package", "insurance", "donation",
        "sample", "e-gift", "subscription", "digital download", "ebook", "class ", "ticket", "deposit", "membership"]
PUST = ["lymphatic", "red light therapy", "infrared therapy", "magnetic therapy", "detox", "slimming", "cellulite",
        "circulation", "anti-aging", "chakra", "aura", "parasite", "alkaline water", "grounding", "frequency"]
NICHE = [("Kitchen-prep", ["cutting board", "knife", "peeler", "grater", "chopper", "mandoline", "press", "sharpener"]),
         ("Kitchen-cook", ["pan", "pot", "cookware", "skillet", "dutch oven", "grill", "griddle", "bakeware", "roaster"]),
         ("Kitchen-appliance", ["juicer", "blender", "frother", "espresso", "kettle", "toaster", "air fryer", "mixer", "maker", "grinder", "ice cream"]),
         ("Drinkware", ["bottle", "tumbler", "flask", "mug", "cup", "glass", "carafe", "pitcher", "decanter"]),
         ("Storage/Organize", ["jar", "container", "canister", "organizer", "storage", "lid", "wrap", "fermentation", "canner"]),
         ("Tableware", ["plate", "bowl", "cutlery", "flatware", "utensil", "dinnerware", "serving", "tong"]),
         ("Cleaning", ["scrubber", "scrub", "cleaner", "sponge", "dish soap"]),
         ("Gadget", ["dispenser", "thermometer", "scale", "timer", "opener", "warmer", "self-heating", "rechargeable"])]
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
    t = re.sub(r"<[^>]+>", " ", html or ""); t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:220]
def get_json(pg, url, tries=3):
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=25000)
            body = pg.inner_text("body")
            if body.strip().startswith("{"):
                return json.loads(body)
        except Exception:
            pass
        time.sleep(2.0 + a * 2.0)
    return None
def prod_row(p):
    v = (p.get("variants") or [{}])[0]
    img = (p["images"][0].get("src") or "") if p.get("images") else ""
    return {"t": p.get("title", ""), "price": npx(v.get("price")), "cmp": npx(v.get("compare_at_price")),
            "k": kind(p.get("title", "") + " " + clean_desc(p.get("body_html"))),
            "desc": clean_desc(p.get("body_html")), "img": img}
def hero_list(pg, dom):
    # sales-ordered collections first (real hero), then generic catalog
    for coll in ["best-selling", "bestsellers", "best-sellers", "frontpage", "featured", "all"]:
        j = get_json(pg, "https://%s/collections/%s/products.json?limit=20" % (dom, coll))
        if j and j.get("products"):
            return [prod_row(p) for p in j["products"]], coll
    j = get_json(pg, "https://%s/products.json?limit=250" % dom)
    return ([prod_row(p) for p in j.get("products", [])] if j else []), "products"
def work(args):
    wid, chunk = args; res = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
        ctx = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600})
        pg = ctx.new_page()
        for d in chunk:
            time.sleep(0.8)
            dom = (d.get("name") or "").replace("https://", "").replace("http://", "").rstrip("/")
            rows, src = hero_list(pg, dom)
            reach = bool(rows)
            tops = [r for r in rows if not has(r["t"], JUNK)][:8]
            phys = [x for x in tops if x["k"] == "physical"]
            # hero = FIRST physical in sales order (not most expensive); prefer in-range if the very first is out
            hero = None
            for x in phys:
                hero = x; break
            if hero and not (39 <= hero["price"] <= 170):
                inr = [x for x in phys if 39 <= x["price"] <= 170]
                if inr: hero = inr[0]
            if hero is None and tops: hero = tops[0]
            pc = d.get("pc") or 0
            o = {"store": (d.get("merch") or dom)[:26], "domain": dom, "reachable": reach, "hero_src": src,
                 "sl_rev": d.get("erf"), "sl_avg": d.get("apf"), "sl_pc": pc, "created": str(d.get("created") or "")[:10],
                 "fbpx": d.get("fbpx"), "cat_flag": ("hero" if pc <= 300 else "mid" if pc <= 2000 else "catalog-giant"),
                 "tops": [{"t": x["t"][:36], "$": x["price"], "k": x["k"]} for x in tops]}
            if hero is None:
                o["tier"] = "DROP"; o["candidate"] = None; res.append(o); continue
            o["candidate"] = hero["t"][:60]; o["price"] = hero["price"]; o["in_range"] = 39 <= hero["price"] <= 170
            o["niche"] = niche_of(hero["t"]); o["desc"] = hero["desc"]; o["image"] = hero["img"]
            o["anchor"] = round(100 * (1 - hero["price"] / hero["cmp"])) if hero["cmp"] > hero["price"] > 0 else 0
            o["pust"] = has(hero["t"] + " " + hero["desc"], PUST); o["kind"] = hero["k"]
            res.append(o)
        b.close()
    return res
if __name__ == "__main__":
    rows = json.load(open(OUT + "/" + INF))
    if LIMIT: rows = rows[:LIMIT]
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
            if o is not r and len(rt & toks(o["candidate"])) >= 2: n += 1
        r["conv_batch"] = n
    def revnum(s):
        m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
    for r in res:
        if not r.get("candidate"):
            r["score"] = 0; r["flags"] = []; r["line"] = "[DROP] " + r["domain"]; continue
        inr = r["in_range"]; pust = r["pust"]; phys = r["kind"] == "physical"; conv = r.get("conv_batch", 0) >= 1
        rev = revnum(r.get("sl_rev")); sc = 0
        sc += 35 if inr else 5
        sc += 20 if conv else 0
        sc += 18 if rev >= 300000 else 13 if rev >= 100000 else 9 if rev >= 50000 else 5
        sc += 7 if r["cat_flag"] == "hero" else (-8 if r["cat_flag"] == "catalog-giant" else 0)
        if pust: sc -= 30
        if not phys: sc -= 30
        r["score"] = sc
        flags = []
        if conv: flags.append("CONV:%d" % r["conv_batch"])
        if pust: flags.append("пустышка")
        if not phys: flags.append(r["kind"])
        if not inr: flags.append("price-out")
        flags.append(r["cat_flag"])
        r["flags"] = flags
        r["tier"] = "A" if sc >= 58 and inr and phys and not pust else ("B" if sc >= 42 and inr and phys and not pust else "C")
        r["line"] = "[%s|%d] %s | %s $%.0f%s | rev:%s pc:%s src:%s | %s" % (
            r["tier"], sc, r["niche"], r["candidate"][:32], r["price"], "" if inr else "(OUT)",
            r.get("sl_rev") or "-", r.get("sl_pc"), r.get("hero_src"), (r["desc"][:75] or "no-desc"))
    order = {"A": 0, "B": 1, "C": 2, "DROP": 3}
    res.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d tiers=%s herosrc=%s" % (
        len(res), round(time.time() - t0), sum(1 for r in res if r.get("reachable")),
        dict(Counter(r.get("tier") for r in res)), dict(Counter(r.get("hero_src") for r in res))))
    print("=== SL ENRICH2 DONE ===", len(res), "secs", round(time.time() - t0),
          "reach", sum(1 for r in res if r.get("reachable")), "tiers", dict(Counter(r.get("tier") for r in res)),
          "herosrc", dict(Counter(r.get("hero_src") for r in res)))
