# Stage-2 enricher (FINAL, per subagent-spec.md, agreed SH-4).
# Sub-agents read LIVE catalog (products.json via proxy) and write a Candidate Sheet:
# best in-range physical from top-3 + REAL prices of all top-3 + niche + DESC + convergence + flags + image.
# NO reviews/rating, NO multi-niche, NO FB-ads, NO branded-flag. Proxy = price-in-range + convergence + Stage-1 revenue.
import json, re, sys, time
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/shophunter"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 4
creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1); creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
INGEST = ["supplement", "softgel", "soft gel", "capsule", "vitamin", "gummies", "gummy", "probiotic", "tincture",
          "shilajit", "electrolyte", "omega", "creatine", "protein", "turmeric", "magnesium", "biotin", "peptide",
          "berberine", "nmn", "nad", "moringa", "sea moss", "seamoss", "powder", "drops", "mushroom", "elixir",
          "iodine", "black seed", "oregano", "ormus", "patches", "tonic", "glutathione", "collagen powder"]
SKIN = ["serum", "face oil", "cream ", "balm", "lotion", "moisturizer", "cleanser", "toner", "sheet mask", "ampoule", "essence"]
APP = ["dress", "shirt", "t-shirt", "tee ", "sneaker", "legging", "bra ", "hoodie", "jacket", "necklace", "earring",
       "bracelet", "jeans", "cardigan", "blazer", "windbreaker", "loafer", "skirt", "fleece", "shorts", "coat"]
JUNK = ["shipping protection", "protection plan", "gift card", "warranty", "route package", "insurance", "donation", "sample"]
PUST = ["lymphatic", "red light therapy", "infrared therapy", "magnetic therapy", "detox", "slimming", "cellulite",
        "circulation", "anti-aging", "mole removal", "skin tag", "chakra", "aura", "parasite", "body cleanse",
        "liver detox", "flat tummy", "manifest", "frequency", "grounding"]
NICHE = [("Kitchen", ["cutting board", "knife", "pan", "cookware", "juicer", "oil dispenser", "espresso", "frother", "blender", "toaster", "grill"]),
         ("Cleaning", ["scrubber", "scrub", "cleaner", "mop", "vacuum", "pressure", "jet", "duster", "stain"]),
         ("Sleep/Bedding", ["pillow", "mattress", "blanket", "quilt", "sheet", "duvet", "topper"]),
         ("Garden/Outdoor", ["garden", "plant", "seed", "kneeler", "hose", "grow", "harvest", "sand-free", "camping", "beach"]),
         ("Pet", ["pet", "dog", "cat", "flea", "groom", "litter", "odor"]),
         ("Beauty-device", ["microcurrent", "led mask", "ipl", "callus", "scalp massager", "facial steamer"]),
         ("Personal-care", ["shoe dryer", "shaver", "trimmer", "foot file", "nail"]),
         ("Home-decor", ["lamp", "light", "mirror", "vase", "frame", "music box"]),
         ("Tech-gadget", ["detector", "tracker", "charger", "power bank", "fan", "humidifier", "purifier"]),
         ("Tools", ["wrench", "multitool", "sharpener", "drill"])]
KNOWN = {"titanium cutting board": "titavos", "jar opener": "stamny", "companion planter": "ivy",
         "smart planter": "ivy", "shoe dryer": "sneakertizer"}
def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, l):
    s = low(t); return any(k in s for k in l)
def npx(s):
    m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
def nrev(s):
    if not s: return 0
    s = str(s).replace("$", "").replace(",", "").strip(); m = re.match(r"([\d.]+)\s*([KMkm]?)", s)
    if not m: return 0
    v = float(m.group(1)); u = m.group(2).upper(); return v*1000 if u == "K" else v*1_000_000 if u == "M" else v
def kind(t):
    if has(t, INGEST): return "ingestible"
    if has(t, SKIN): return "skincare"
    if has(t, APP): return "apparel"
    return "physical"
def niche_of(t):
    for n, kws in NICHE:
        if has(t, kws): return n
    return "Other"
def conv_known(t):
    s = low(t)
    for k, w in KNOWN.items():
        if k in s: return w
    return None
def match_product(cat, title):
    tt = set(low(title).split()); best, ov = None, 0
    for p in cat:
        o = len(tt & set(low(p.get("title", "")).split()))
        if o > ov: ov, best = o, p
    return best if ov >= 2 else None
def clean_desc(html):
    t = re.sub(r"<[^>]+>", " ", html or "")
    t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:200]
def get_json(pg, url, tries=4):
    # retry with backoff — recovers transient proxy throttle (SH-3 paced-fallback safeguard)
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=30000)
            body = pg.inner_text("body")
            if body.strip().startswith("{"):
                return json.loads(body)
        except Exception:
            pass
        time.sleep(2.5 + a * 2.5)  # 2.5s, 5s, 7.5s backoff between attempts
    return None

def work(args):
    wid, chunk = args
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=PROXY)
        ctx = b.new_context(user_agent=UA, viewport={"width": 1400, "height": 1600})
        pg = ctx.new_page()
        for d in chunk:
            time.sleep(1.0)  # pace requests to avoid proxy burst-throttle
            dom = d["domain"].replace("https://", "").replace("http://", "").rstrip("/")
            top = d.get("top", [])
            cat = get_json(pg, "https://" + dom + "/products.json?limit=250")
            cat = cat.get("products", []) if cat else None
            picks = []
            for sp in top[:4]:
                if has(sp["t"], JUNK): continue
                m = match_product(cat, sp["t"]) if cat else None
                v = (m.get("variants") or [{}])[0] if m else {}
                price = npx(v.get("price")) if v.get("price") else npx(sp.get("price"))
                cmp_at = npx(v.get("compare_at_price")) if v.get("compare_at_price") else 0
                desc = clean_desc(m.get("body_html")) if m else ""
                img = ""
                if m and m.get("images"):
                    img = (m["images"][0].get("src") or "")
                picks.append({"t": sp["t"], "price": price, "wk": nrev(sp.get("wk")), "k": kind(sp["t"]),
                              "desc": desc, "cmp_at": cmp_at, "img": img,
                              "src": "real" if v.get("price") else "SH-est"})
            phys = [x for x in picks if x["k"] == "physical"]
            inr = [x for x in phys if 39 <= x["price"] <= 170]
            cand = max(inr, key=lambda x: x["wk"]) if inr else (max(phys, key=lambda x: x["wk"]) if phys else (picks[0] if picks else None))
            o = {"store": d["name"][:26], "domain": dom, "reachable": cat is not None,
                 "rev_week": d.get("rev_week", ""), "sku": d.get("sku", ""),
                 "all_tops": [{"t": x["t"][:30], "$": x["price"], "k": x["k"], "src": x["src"]} for x in picks]}
            if cand is None:
                o["tier"] = "DROP"; o["candidate"] = None; res.append(o); continue
            o["candidate"] = cand["t"][:50]; o["price"] = cand["price"]; o["price_src"] = cand["src"]
            o["in_range"] = 39 <= cand["price"] <= 170; o["niche"] = niche_of(cand["t"])
            o["desc"] = cand["desc"]; o["image"] = cand["img"]
            o["anchor"] = round(100 * (1 - cand["price"] / cand["cmp_at"])) if cand["cmp_at"] > cand["price"] > 0 else 0
            o["pust"] = has(cand["t"] + " " + cand["desc"], PUST)
            o["kind"] = cand["k"]; o["conv_known"] = conv_known(cand["t"])
            res.append(o)
        b.close()
    return res

if __name__ == "__main__":
    rows = json.load(open(OUT + "/" + INF))
    chunks = [(w, rows[w::NW]) for w in range(NW)]
    t0 = time.time()
    with Pool(NW) as pool:
        parts = pool.map(work, chunks)
    res = [x for part in parts for x in part]
    # within-batch convergence: candidates sharing >=2 significant tokens
    cands = [r for r in res if r.get("candidate")]
    def toks(s): return set(w for w in low(s).split() if len(w) > 3)
    for r in cands:
        rt = toks(r["candidate"]); n = 0
        for o in cands:
            if o is r: continue
            if len(rt & toks(o["candidate"])) >= 2: n += 1
        r["conv_batch"] = n
    # final proxy-score + tier (RELIABLE only: price-in-range + convergence + Stage-1 revenue)
    for r in res:
        if not r.get("candidate"):
            r["score"] = 0; r["flags"] = []; r["line"] = "[DROP] no candidate | " + r["domain"]; continue
        inr = r["in_range"]; pust = r["pust"]; phys = r["kind"] == "physical"
        conv = r.get("conv_known") or (r.get("conv_batch", 0) >= 1)
        wk = nrev(r["rev_week"])
        sc = 0
        sc += 35 if inr else 5
        sc += 25 if conv else 0
        sc += 20 if wk >= 50000 else 15 if wk >= 20000 else 10 if wk >= 5000 else 5
        if pust: sc -= 30
        if not phys: sc -= 30
        if r["anchor"] >= 55: sc -= 8
        r["score"] = sc
        flags = []
        if r.get("conv_known"): flags.append("CONV:" + r["conv_known"])
        elif r.get("conv_batch", 0) >= 1: flags.append("CONV-batch:%d" % r["conv_batch"])
        if pust: flags.append("пустышка")
        if not phys: flags.append(r["kind"])
        if not inr: flags.append("price-out")
        if r["anchor"] >= 55: flags.append("anchor%d%%" % r["anchor"])
        r["flags"] = flags
        r["tier"] = "A" if sc >= 60 and inr and phys and not pust else ("B" if sc >= 42 and inr and phys and not pust else "C")
        r["line"] = "[%s|%d] %s | %s $%.0f%s | rev:%s%s | %s" % (
            r["tier"], sc, r["niche"], r["candidate"][:30], r["price"], "" if inr else "(OUT)",
            r["rev_week"] or "-", (" " + ",".join(flags)) if flags else "", (r["desc"][:95] or "no-desc"))
    order = {"A": 0, "B": 1, "C": 2, "DROP": 3}
    res.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d tiers=%s" % (
        len(res), round(time.time() - t0), sum(1 for r in res if r.get("reachable")), dict(Counter(r.get("tier") for r in res))))
    print("=== ENRICH-FINAL DONE ===", len(res), "secs", round(time.time() - t0),
          "| reachable", sum(1 for r in res if r.get("reachable")), "| tiers", dict(Counter(r.get("tier") for r in res)))
