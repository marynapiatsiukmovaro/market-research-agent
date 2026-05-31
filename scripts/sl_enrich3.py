# Store Leads Stage-2 enricher v3 — PRODUCT-CENTRIC (Marina-agreed S2, 2026-05-31).
# Changes vs sl_enrich2: (1) OPEN-LADDER (best-selling→frontpage→featured→/products.json→homepage HTML),
# never a silent DROP — unreachable gets a reason. (2) TOP-3 candidates/store (not 1 hero), each full.
# (3) Early signals per product: storefront position + investment (desc/imgs/variants/badges). (4) Currency→USD.
# (5) hero_confidence (high=sales-ordered collection, low=all/homepage). (6) desc_confidence (ok/empty/mismatched).
# (7) maturity (emerging/established — established is NOT a reject). proxy_score has NO revenue term.
# Usage: sl_enrich3.py <infile> <outfile> <sentinel> [nworkers]
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

# --- currency → USD (approximate; goal = kill gross errors like ₹4000 / AUD read as $; main agent confirms live) ---
# keyed by Store Leads countryCode (the dump's `country`). Unknown → assume USD (rate 1, currency '?').
CC_CUR = {"US":("USD",1.0),"GB":("GBP",1.27),"CA":("CAD",0.73),"AU":("AUD",0.66),"NZ":("NZD",0.61),
          "DE":("EUR",1.08),"FR":("EUR",1.08),"IT":("EUR",1.08),"ES":("EUR",1.08),"NL":("EUR",1.08),
          "IE":("EUR",1.08),"AT":("EUR",1.08),"BE":("EUR",1.08),"FI":("EUR",1.08),"PT":("EUR",1.08),
          "IN":("INR",0.012),"ZA":("ZAR",0.055),"SE":("SEK",0.095),"NO":("NOK",0.093),"DK":("DKK",0.145),
          "CH":("CHF",1.12),"JP":("JPY",0.0066),"BR":("BRL",0.18),"MX":("MXN",0.058),"PL":("PLN",0.25),
          "AE":("AED",0.27),"SG":("SGD",0.74),"HK":("HKD",0.128)}

INGEST = ["supplement","softgel","soft gel","capsule","vitamin","gummies","gummy","probiotic","tincture","shilajit",
          "electrolyte","omega","creatine","protein powder","turmeric","magnesium","biotin","berberine","nmn","nad",
          "moringa","sea moss","seamoss","mushroom","elixir","tonic","collagen powder","tea bag","coffee bean","ground coffee"]
SKIN = ["serum","face oil","balm","lotion","moisturizer","cleanser","toner","sheet mask","ampoule","essence"]
APP = ["dress","shirt","t-shirt","tee ","sneaker","legging","hoodie","jacket","necklace","earring","bracelet",
       "jeans","cardigan","blazer","loafer","skirt","shorts","apron","hat ","sock","coat","fleece"]
JUNK = ["shipping protection","protection plan","gift card","warranty","route package","insurance","donation",
        "sample","e-gift","subscription","digital download","ebook","class ","ticket","deposit","membership"]
PUST = ["lymphatic","red light therapy","infrared therapy","magnetic therapy","detox","slimming","cellulite",
        "circulation","anti-aging","mole removal","skin tag","chakra","aura","parasite","alkaline water","grounding","frequency"]
BADGE = ["bestseller","best seller","best-seller","as seen","#1 ","number one","viral","tiktok made","trending","award","patented","sold out"]

def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, l):
    s = low(t); return any(k in s for k in l)
def npx(s):
    m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0.0
def kind(t):
    if has(t, INGEST): return "ingestible"
    if has(t, SKIN): return "skincare"
    if has(t, APP): return "apparel"
    return "physical"
def clean_desc(html):
    t = re.sub(r"<[^>]+>", " ", html or ""); t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:220]
def toks(s): return set(w for w in low(s).split() if len(w) > 3)

def brand_core(dom):
    # strip geo prefixes (mx-, de-, nl-, www.) + glopal/shopify mirror suffixes → a brand-core for conv dedupe
    d = re.sub(r"^https?://", "", dom).strip("/").split("/")[0]
    d = re.sub(r"^www\.", "", d)
    d = re.sub(r"^[a-z]{2}-", "", d)                       # mx-foo / de-foo → foo
    d = re.sub(r"\.(glopalstore|myshopify|globale?)\..*$", "", d)  # mirror platforms
    return re.sub(r"\.[a-z.]+$", "", d)                    # drop TLD

# currency rates keyed by ISO currency code (the TRUE store currency from /meta.json)
CUR_RATE = {"USD":1.0,"GBP":1.27,"EUR":1.08,"CAD":0.73,"AUD":0.66,"NZD":0.61,"INR":0.012,"ZAR":0.055,
            "SEK":0.095,"NOK":0.093,"DKK":0.145,"CHF":1.12,"JPY":0.0066,"BRL":0.18,"MXN":0.058,
            "PLN":0.25,"AED":0.27,"SGD":0.74,"HKD":0.128,"CZK":0.043,"RON":0.22,"HUF":0.0028}

def store_currency(pg, dom):
    # TRUE store currency from Shopify /meta.json (country code from the dump is NOT reliable — renpho.uk=HK but sells GBP).
    for ep in ("/meta.json", "/cart.json"):
        try:
            pg.goto("https://%s%s" % (dom, ep), wait_until="domcontentloaded", timeout=15000)
            body = pg.inner_text("body")
            if body.strip().startswith("{"):
                d = json.loads(body)
                c = d.get("currency") or (d.get("shop") or {}).get("currency")
                if c: return c.upper()
        except Exception:
            pass
    return None

def usd(price, cur):
    rate = CUR_RATE.get((cur or "").upper(), 1.0)
    return round(price * rate, 2), (cur or "?"), rate

def desc_conf(title, desc):
    if not desc or len(desc) < 10: return "empty"
    if len(toks(title) & toks(desc)) == 0: return "mismatched"
    return "ok"

def maturity(created, pc, erf):
    yr = 0
    m = re.match(r"(\d{4})", str(created) or "")
    if m: yr = int(m.group(1))
    rev = npx(erf)
    if (pc or 0) >= 80 or rev >= 200000 or (yr and yr <= 2021 and (pc or 0) >= 30):
        return "established"
    return "emerging"

def as_list(x):
    # Shopify endpoints vary: /products.json gives variants/images as LISTS;
    # /products/<handle>.json sometimes gives them as DICTS ({"0": {...}}) → normalize to a list.
    if isinstance(x, dict): return list(x.values())
    if isinstance(x, list): return x
    return []

def prod_row(p, pos, src):
    variants = as_list(p.get("variants"))
    v = variants[0] if variants else {}
    imgs = as_list(p.get("images"))
    img = ""
    if imgs:
        first = imgs[0]
        img = (first.get("src") or "") if isinstance(first, dict) else (first if isinstance(first, str) else "")
    title = p.get("title", "")
    desc = clean_desc(p.get("body_html"))
    invest = {"desc_len": len(desc), "imgs": len(imgs), "variants": len(variants),
              "badges": [b for b in BADGE if b in low(title + " " + desc)]}
    return {"t": title, "price_raw": npx(v.get("price")), "cmp": npx(v.get("compare_at_price")),
            "k": kind(title + " " + desc), "desc": desc, "img": img, "pos": pos, "src": src, "invest": invest}

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

def get_html(pg, url, tries=2):
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=25000)
            return pg.content()
        except Exception:
            time.sleep(2.0 + a * 2.0)
    return ""

def collect_products(pg, dom):
    """OPEN-LADDER: sales-ordered collections → bulk products.json → homepage HTML single-product fetch.
    Returns (rows, src, hero_confidence)."""
    # 1-3: sales-ordered / curated collections (high confidence — merchant's own order)
    for coll in ["best-selling", "bestsellers", "best-sellers", "frontpage", "featured"]:
        j = get_json(pg, "https://%s/collections/%s/products.json?limit=20" % (dom, coll))
        if j and j.get("products"):
            return [prod_row(p, i, coll) for i, p in enumerate(j["products"])], coll, "high"
    # 4: bulk catalog (order = not sales → lower confidence)
    j = get_json(pg, "https://%s/products.json?limit=50" % dom)
    if j and j.get("products"):
        return [prod_row(p, i, "all") for i, p in enumerate(j["products"])], "all", "low"
    # 5: homepage HTML — products.json disabled but site alive. Extract /products/<handle>, fetch single .json.
    html = get_html(pg, "https://%s/" % dom)
    if html:
        handles = []
        for h in re.findall(r"/products/([a-z0-9][a-z0-9\-]{1,80})", html):
            if h not in handles: handles.append(h)
            if len(handles) >= 8: break
        rows = []
        for i, h in enumerate(handles):
            jp = get_json(pg, "https://%s/products/%s.json" % (dom, h), tries=2)
            if jp and jp.get("product"):
                rows.append(prod_row(jp["product"], i, "homepage"))
        if rows:
            return rows, "homepage", "low"
        # site loaded but no parseable products → still NOT a silent drop; reason carries the truth
        return [], "homepage-noprod", "low"
    return [], "unreachable", "low"

def work(args):
    wid, chunk = args; res = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
        ctx = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600})
        pg = ctx.new_page()
        for d in chunk:
          try:
            time.sleep(0.8)
            dom = (d.get("name") or "").replace("https://", "").replace("http://", "").rstrip("/")
            cc = d.get("country")
            rows, src, hconf = collect_products(pg, dom)
            pc = d.get("pc") or 0
            o = {"store": (d.get("merch") or dom)[:26], "domain": dom, "country": cc,
                 "sl_rev": d.get("erf"), "sl_avg": d.get("apf"), "sl_pc": pc,
                 "created": str(d.get("created") or "")[:10], "visits": d.get("visits"),
                 "maturity": maturity(d.get("created"), pc, d.get("erf")),
                 "cat_flag": ("hero" if pc <= 300 else "mid" if pc <= 2000 else "catalog-giant"),
                 "fb": d.get("fb"), "ig": d.get("ig"), "tiktok": d.get("tiktok"), "pinterest": d.get("pinterest"),
                 "hero_src": src, "hero_confidence": hconf}
            # not reachable → NEVER a silent DROP: carry the reason for manual look
            if not rows:
                o["reachable"] = False
                o["reason"] = {"homepage-noprod": "site loads, no parseable products (manual look)",
                               "unreachable": "site did not load (manual look)"}.get(src, "no products (manual look)")
                o["tops3"] = []; o["candidate"] = None; o["tier"] = "MANUAL"
                res.append(o); continue
            o["reachable"] = True
            # TRUE store currency from /meta.json (country code is unreliable — see store_currency); fallback to CC map
            store_cur = store_currency(pg, dom) or CC_CUR.get((cc or "").upper(), ("?", 1.0))[0]
            o["store_currency"] = store_cur
            # service-SKU skip; keep PHYSICAL only. price 0 in products.json is OFTEN a region-gating artifact
            # (proxy fetch returns 0.00 though the live site has a real price) — NOT a reason to drop the STORE.
            # So: price<=0 → keep the product with price unknown (flag), confirm live; never silently lose a real store.
            clean = []
            for r in rows:
                if has(r["t"], JUNK): continue
                if r["price_raw"] <= 0:
                    r["price"] = None; r["currency"] = store_cur; r["rate"] = 1.0; r["price_unknown"] = True
                else:
                    pu, cur, rate = usd(r["price_raw"], store_cur)
                    r["price"] = pu; r["currency"] = cur; r["rate"] = rate; r["price_unknown"] = False
                clean.append(r)
            phys = [r for r in clean if r["k"] == "physical"]
            # TOP-3: order by storefront position (the collection's own order), then investment (desc+imgs+variants)
            def invest_score(r):
                iv = r["invest"]; return iv["desc_len"] + iv["imgs"]*20 + iv["variants"]*5 + len(iv["badges"])*40
            phys.sort(key=lambda r: (r["pos"], -invest_score(r)))
            tops3 = phys[:3] if phys else clean[:3]
            def t_inrange(r): return (not r["price_unknown"]) and 39 <= r["price"] <= 170
            o["tops3"] = [{"t": r["t"][:60], "price": r["price"], "price_raw": r["price_raw"], "cur": r["currency"],
                           "k": r["k"], "pos": r["pos"], "desc": r["desc"][:200], "img": r["img"],
                           "price_unknown": r["price_unknown"], "in_range": t_inrange(r),
                           "anchor": (round(100*(1-r["price"]/(r["cmp"]*r["rate"]))) if (not r["price_unknown"] and r["cmp"]>r["price_raw"]>0) else 0),
                           "pust": has(r["t"]+" "+r["desc"], PUST), "desc_confidence": desc_conf(r["t"], r["desc"]),
                           "invest": r["invest"]} for r in tops3]
            if not tops3:
                # genuinely nothing physical at all (e.g. apparel-only like man-tle, or truly empty)
                o["candidate"] = None; o["tier"] = "DROP-noPhysical"; res.append(o); continue
            # all candidates price-unknown → don't score, route to PRICE-CHECK (manual live look), never silent drop
            if all(t["price_unknown"] for t in o["tops3"]):
                o["candidate"] = o["tops3"][0]["t"]; o["price"] = None; o["in_range"] = None
                o["desc"] = o["tops3"][0]["desc"]; o["image"] = o["tops3"][0]["img"]
                o["kind"] = o["tops3"][0]["k"]; o["desc_confidence"] = o["tops3"][0]["desc_confidence"]
                o["pust"] = o["tops3"][0]["pust"]; o["storefront_pos"] = o["tops3"][0]["pos"]; o["anchor"] = 0
                o["tier"] = "PRICE-CHECK"; o["reason"] = "products.json prices all 0 (region-gated) → confirm price live"
                res.append(o); continue
            # candidate = the in-range physical highest on storefront; else first known-price physical (price-out flagged)
            inr = [t for t in o["tops3"] if t["in_range"]]
            known = [t for t in o["tops3"] if not t["price_unknown"]]
            cand = inr[0] if inr else (known[0] if known else o["tops3"][0])
            o["candidate"] = cand["t"]; o["price"] = cand["price"]; o["currency"] = cand["cur"]
            o["in_range"] = cand["in_range"]; o["desc"] = cand["desc"]; o["image"] = cand["img"]
            o["pust"] = cand["pust"]; o["kind"] = cand["k"]; o["desc_confidence"] = cand["desc_confidence"]
            o["anchor"] = cand["anchor"]; o["storefront_pos"] = cand["pos"]
            res.append(o)
          except Exception as e:
            # one bad store must never kill the whole batch → record it as MANUAL with the error reason
            res.append({"domain": (d.get("name") or ""), "store": (d.get("merch") or d.get("name") or "")[:26],
                        "reachable": False, "tier": "MANUAL", "candidate": None, "tops3": [],
                        "reason": "error: " + type(e).__name__})
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
    # convergence within the enriched batch — count DISTINCT BRAND-CORES (geo-mirrors deduped), not domains
    cands = [r for r in res if r.get("candidate")]
    for r in cands:
        rt = toks(r["candidate"]); cores = set()
        for o in cands:
            if o is r: continue
            if len(rt & toks(o["candidate"])) >= 2:
                cores.add(brand_core(o["domain"]))
        cores.discard(brand_core(r["domain"]))
        r["conv_batch"] = len(cores)
    # proxy_score — NO revenue term (early winner has none). RELIABLE signals only.
    for r in res:
        if not r.get("candidate"):
            r["score"] = 0; r["tier"] = r.get("tier", "DROP"); continue
        if r.get("tier") == "PRICE-CHECK":   # keep this tier — price unknown, goes to manual live-check
            r["score"] = 0
            r["flags"] = ["price-unknown→live", ("established" if r.get("maturity") == "established" else r.get("cat_flag", ""))]
            if r.get("conv_batch", 0) >= 1: r["flags"].insert(0, "CONV:%d" % r["conv_batch"])
            continue
        inr = r["in_range"]; pust = r["pust"]; phys = r["kind"] == "physical"; conv = r.get("conv_batch", 0) >= 1
        sf = r.get("storefront_pos", 9); dc = r.get("desc_confidence")
        sc = 0
        sc += 35 if inr else 5
        sc += 22 if conv else 0
        sc += 12 if sf == 0 else 8 if sf <= 2 else 3            # storefront position (merchant's own ranking)
        sc += 7 if r["cat_flag"] == "hero" else (-8 if r["cat_flag"] == "catalog-giant" else 0)
        if pust: sc -= 30
        if not phys: sc -= 30
        if dc != "ok": sc -= 0                                   # don't penalise — just flags a must-WebFetch
        r["score"] = sc
        flags = []
        if conv: flags.append("CONV:%d" % r["conv_batch"])
        if pust: flags.append("пустышка")
        if not inr: flags.append("price-out")
        if dc != "ok": flags.append("desc:%s→WebFetch" % dc)
        if r["hero_confidence"] == "low": flags.append("hero:low→confirm")
        if r["maturity"] == "established": flags.append("established")
        flags.append(r["cat_flag"])
        r["flags"] = flags
        r["tier"] = "A" if sc >= 54 and inr and phys and not pust else ("B" if sc >= 40 and inr and phys and not pust else "C")
    order = {"A": 0, "B": 1, "C": 2, "MANUAL": 3, "DROP-noPhysical": 4, "DROP": 5}
    res.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    reach = sum(1 for r in res if r.get("reachable"))
    manual = sum(1 for r in res if r.get("tier") == "MANUAL")
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d manual=%d tiers=%s srcs=%s" % (
        len(res), round(time.time()-t0), reach, manual,
        dict(Counter(r.get("tier") for r in res)), dict(Counter(r.get("hero_src") for r in res))))
    print("=== SL ENRICH3 DONE ===", len(res), "secs", round(time.time()-t0),
          "reach", reach, "manual", manual, "tiers", dict(Counter(r.get("tier") for r in res)),
          "srcs", dict(Counter(r.get("hero_src") for r in res)))
