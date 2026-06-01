# Store Leads Stage-2 enricher v4 / v4.1 / v4.2 — STORE/PRODUCT ESSENCE + SELF-CHECK (Marina-agreed S3, 2026-06-01).
# v4.2 (2026-06-01): "ни один магазин не тонет на первом проходе" (Marina). Goal = bring ENOUGH per store that a
#   "skip without opening" is trustworthy → fewer forced live re-opens, 0 quality loss. ALL 0-token, VPS-side. Adds:
#   (a) home_pitch — the store's OWN homepage pitch (og:title + H1 + og:description = the banner/value-prop text).
#       👉 izimini case: storefront says "going outdoors with a crawling baby isn't a picnic" → instantly readable.
#   (b) home_hero — the product the homepage BANNER features, captured ALWAYS & shown ALONGSIDE the best-seller
#       candidate (not instead). 👉 swaddlean case: best-seller pick = "knit blanket" but banner hero = sleep sacks.
#   (c) longer desc (~600, was 220) + feature bullets — conveys the real benefit/mechanism (dingle-dangle case).
#   (d) home_img — the homepage banner image (for the Stage-2 visual sheet).
#   (e) needs_live flag + why — the store's OWN "open me by hand" worklist (low hero/desc conf, price-unknown,
#       unreachable, or best-seller≠banner-hero). The main agent MUST live-open every needs_live store (op-rule RULE 23).
#   DROPPED per Marina: review-count/rating & brand-strength markers — both fakeable at launch, not real signals.
# v4.1 (2026-06-01): 8 workers · moderate fast-fail (15s×2) · home-hero only when hero_confidence=low ·
#   new class `diy-home` (paint/sealant/coating/fastener/roofing/work-gear → sunk like trade) · product handle exported.
# Builds on v3 (open-ladder, top-3, currency→USD, hero/desc-confidence, maturity, conv-dedupe, no-revenue proxy).
# NEW in v4 (all 0-token, VPS-side; goal = show store/product essence + cut MY re-opens + better ABC):
#   (1) product_class per candidate (consumer-gadget / appliance / fixture / kitchen / decor / part / material / pro-tool / apparel)
#   (2) store_type (single-product-DTC / niche-brand / trade-store / parts-supply / services / catalog-giant)
#   (3) SELF-CHECK pass (Marina's "double-check before you come to me"): ALWAYS also pull the homepage featured
#       hero (catches heatka/hanboost: scraper's collection-hero ≠ the store's real front hero); and when the
#       chosen candidate's desc is empty/mismatched, RE-FETCH that product's own page to correct it.
#   (4) new_products_30d (store actively launching = live/test candidate + feeds the monitor keep-list)
#   (5) brand_core now collapses subdomains to the registrable root (fixes false conv, e.g. parts.cleanburn /
#       parts.gingerich.cleanburn = ONE brand) + handles 2-part TLDs (co.uk/com.au/...).
#   (6) ABC reformula: trade classes (part/material/pro-tool/fixture) deprioritized, consumer-gadget lifted —
#       STILL ONLY A SORT-AID; the main agent reads ALL (op-rule RULE 6). No coverage is cut.
# Usage: sl_enrich4.py <infile> <outfile> <sentinel> [nworkers] [limit]
import json, re, sys, time, datetime
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/storeleads"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 8   # v4.1: 8 workers (Playwright, credit-safe) — ~2x faster, 0 quality loss
LIMIT = int(sys.argv[5]) if len(sys.argv) > 5 else 0
creds = {}
for line in open("/opt/market-research-agent/cookies/proxy.creds"):
    if "=" in line:
        k, v = line.strip().split("=", 1); creds[k] = v
PROXY = {"server": "http://%s:%s" % (creds["PROXY_HOST"], creds["PROXY_PORT"]),
         "username": creds["PROXY_USER"], "password": creds["PROXY_PASS"]}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

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

# --- v4 product-class keyword sets ---
# STRONG_CONSUMER is checked FIRST (a clear consumer DEVICE wins even if its desc mentions an "adapter"/"kit").
# Bias = err toward "consumer" (so it RISES and I read it); a part mislabeled consumer is read+dropped (safe),
# a consumer mislabeled trade SINKS (unsafe). ABC is only a sort — main agent reads ALL (RULE 6).
STRONG_CONS = ["bidet","humidifier","dehumidifier","air purifier"," purifier","massager","body scale","smart scale",
               "door lock","keypad lock","smart lock","fingerprint lock","projector","earbud","headphone","blender",
               "electric kettle","robot vacuum","mug warmer","heated cushion","heated blanket","desk mat","night light",
               "pet camera","bird feeder","water fountain","multi-tool","multitool","ultrasonic cutter","posture",
               "neck massager","foot spa","ice maker","portable bidet"]
APPLIANCE = ["humidifier","dehumidifier","air purifier","purifier","space heater","ceramic heater","bladeless",
             "air cooler","thermostat","mug warmer","heated","desk mat","fan ","ceiling fan","box fan"]
PART = ["replacement","oem"," part #"," part#","cartridge","spare part","adapter","fitting","bracket","valve",
        "gasket","seal kit","compatible with","fits ","filter for","filter replacement","sprocket","muffler",
        "header pipe","drum","spring","impeller","switch","battery adapter","cut wheel","replacement set"]
MATERIAL = ["tile","porcelain","ceramic tile","flooring","floor plank","vinyl plank","laminate","lumber","plywood",
            "timber","grout","membrane","drywall","concrete","brick","paver","decking","insulation","trellis",
            "downpipe","gutter","baseboard","plenum","corrimano","tabletop panel","composite panel","tappeti","matto"]
PROTOOL = ["brazing","abrasive","sanding belt","sanding disc","router bit","chainsaw","welding","grinding","buffing",
           "carbide","edger disc","sandblast","wide belt","hammertacker","saw chain","work light","drill holster",
           "chisel roll","angle gauge","gong machine","lock pick","picking"]
FIXTURE = ["faucet","sink","basin","drain","shower drain","vent ","grille","diffuser","robinet","caniveau",
           "handrail","mixer tap","downrod ceiling fan"]
DECOR = ["rug","carpet"," mat ","cushion","pillow","vase","wall art","tapestry","beanie","cutting board","chopping board"]
GADGET = ["portable","cordless","rechargeable","wireless","bidet","multi-tool","multitool","ultrasonic","mini "]
# v4.1: diy-home = DIY/building consumables + work gear that leaked into "consumer-other" and stayed in tier A
# (paint/sealant/coating/fastener/roofing/work-wear). Sunk like trade. Checked AFTER material/part/fixture.
DIY_HOME = ["paint","primer","sealant","sealer"," coating","varnish","wood stain","lacquer","adhesive","caulk",
            "epoxy","urethane","roofing"," roof ","cladding","flashing","chimney","safety vest","hi viz","hi-vis",
            "spanner"," wrench","ratchet","socket set","fastener"," screw"," bolt ","nut bolt","insulation","batt",
            "pvc floor","click pvc","floor covering","linoleum","marmoleum","underlay","threadlocker","work light"]

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

def product_class(t, desc, k):
    """Essence of the PRODUCT. STRONG consumer DEVICE words win FIRST (bidet/lock/scale/massager…) so a clear
    consumer product isn't sunk to 'part' just because its desc mentions an adapter/kit. Then unambiguous trade
    (material), then part/pro-tool, then fixture/decor. Bias toward consumer = the zero-loss-safe direction."""
    if k != "physical": return k          # ingestible / skincare / apparel
    s = t + " " + desc
    if has(s, STRONG_CONS): return "appliance" if has(s, APPLIANCE) else "consumer-gadget"
    if has(s, MATERIAL): return "material"
    if has(s, PROTOOL): return "pro-tool"
    if has(s, PART): return "part"
    if has(s, FIXTURE): return "fixture"
    if has(s, DIY_HOME): return "diy-home"
    if has(s, DECOR): return "decor"
    if has(s, APPLIANCE): return "appliance"
    if has(s, GADGET): return "consumer-gadget"
    return "consumer-other"               # physical, no trade match, no clear gadget cue

TRADE_CLASSES = {"part", "material", "pro-tool", "fixture", "diy-home"}

def store_type(classes, pc, merch, dom):
    """Essence of the STORE — what kind of operation it is."""
    blob = low((merch or "") + " " + (dom or ""))
    if pc and pc > 2000: return "catalog-giant"
    if any(w in blob for w in ["supply","warehouse","wholesale","distributor","hardware","megastore","outlet"]): return "parts-supply"
    if any(w in blob for w in ["service","remodel","install","hvac","plumb","contractor","builders","lumber","block"]): return "services/trade"
    if classes:
        trade = sum(1 for c in classes if c in TRADE_CLASSES)
        if trade >= max(1, len(classes) * 0.6): return "trade-store"
    if pc is not None and pc <= 12: return "single-product/DTC"
    return "niche-brand"

def clean_desc(html, cap=600):                 # v4.2: 220 → 600 (richer benefit/mechanism so a no-open skip is safe)
    t = re.sub(r"<[^>]+>", " ", html or ""); t = re.sub(r"&[a-z#0-9]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()[:cap]
def bullets(html):                             # v4.2: pull feature bullets (<li>) — the spec/benefit list
    out = []
    for m in re.findall(r"<li[^>]*>(.*?)</li>", html or "", re.S | re.I):
        b = re.sub(r"<[^>]+>", " ", m); b = re.sub(r"&[a-z#0-9]+;", " ", b)
        b = re.sub(r"\s+", " ", b).strip()
        if 8 <= len(b) <= 140 and b not in out:
            out.append(b)
        if len(out) >= 6: break
    return out
def toks(s): return set(w for w in low(s).split() if len(w) > 3)

# 2-part TLDs to drop fully so the registrable label is correct
TLD2 = {"co.uk","com.au","co.nz","com.mx","co.za","com.br","co.jp","com.sg","co.in","com.tr","com.ua"}
def brand_core(dom):
    d = re.sub(r"^https?://", "", dom or "").strip("/").split("/")[0]
    d = re.sub(r"^www\.", "", d)
    d = re.sub(r"\.(glopalstore|myshopify|globale?)\..*$", "", d)
    parts = d.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in TLD2:
        return parts[-3]                  # foo.co.uk → foo ; parts.foo.co.uk → foo
    if len(parts) >= 2:
        return parts[-2]                  # parts.cleanburn.com → cleanburn ; uk.deervalleybath.com → deervalleybath
    return parts[0]

CUR_RATE = {"USD":1.0,"GBP":1.27,"EUR":1.08,"CAD":0.73,"AUD":0.66,"NZD":0.61,"INR":0.012,"ZAR":0.055,
            "SEK":0.095,"NOK":0.093,"DKK":0.145,"CHF":1.12,"JPY":0.0066,"BRL":0.18,"MXN":0.058,
            "PLN":0.25,"AED":0.27,"SGD":0.74,"HKD":0.128,"CZK":0.043,"RON":0.22,"HUF":0.0028}

def store_currency(pg, dom):
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
    if isinstance(x, dict): return list(x.values())
    if isinstance(x, list): return x
    return []

NOW = datetime.datetime.now(datetime.timezone.utc)
def days_since(s):
    try:
        dt = datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        if dt.tzinfo is None: dt = dt.replace(tzinfo=datetime.timezone.utc)
        return (NOW - dt).days
    except Exception:
        return None

def prod_row(p, pos, src):
    variants = as_list(p.get("variants"))
    v = variants[0] if variants else {}
    imgs = as_list(p.get("images"))
    img = ""
    if imgs:
        first = imgs[0]
        img = (first.get("src") or "") if isinstance(first, dict) else (first if isinstance(first, str) else "")
    title = p.get("title", "")
    body = p.get("body_html")
    desc = clean_desc(body)
    blts = bullets(body)
    k = kind(title + " " + desc)
    invest = {"desc_len": len(desc), "imgs": len(imgs), "variants": len(variants),
              "badges": [b for b in BADGE if b in low(title + " " + desc)]}
    return {"t": title, "handle": p.get("handle", ""), "price_raw": npx(v.get("price")), "cmp": npx(v.get("compare_at_price")),
            "k": k, "pclass": product_class(title, desc, k), "desc": desc, "bullets": blts, "img": img, "pos": pos, "src": src,
            "invest": invest, "created_days": days_since(p.get("created_at") or p.get("published_at"))}

def get_json(pg, url, tries=2):                 # v4.1: moderate fast-fail (15s×2, was 25s×3) — dead endpoint
    for a in range(tries):                      # fails fast → open-ladder moves on; a real-but-slow site → MANUAL (hand-checked)
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=15000)
            body = pg.inner_text("body")
            if body.strip().startswith("{"):
                return json.loads(body)
        except Exception:
            pass
        time.sleep(1.5 + a * 1.5)
    return None

def get_html(pg, url, tries=2):
    for a in range(tries):
        try:
            pg.goto(url, wait_until="domcontentloaded", timeout=15000)
            return pg.content()
        except Exception:
            time.sleep(1.5 + a * 1.5)
    return ""

def homepage_hero(pg, dom):
    """SELF-CHECK: the product the merchant features on the HOMEPAGE (front hero). Catches the case where the
    best-selling/all collection hero ≠ the store's real front hero (heatka/hanboost). Returns a prod_row or None."""
    html = get_html(pg, "https://%s/" % dom, tries=1)
    if not html: return None
    m = re.search(r"/products/([a-z0-9][a-z0-9\-]{1,80})", html)
    if not m: return None
    jp = get_json(pg, "https://%s/products/%s.json" % (dom, m.group(1)), tries=2)
    if jp and jp.get("product"):
        return prod_row(jp["product"], -1, "home-hero")   # pos=-1 → sorts to the front
    return None

def recheck_desc(pg, dom, row):
    """SELF-CHECK: if the candidate's desc is empty/mismatched, re-fetch its OWN product page to correct it."""
    if not row.get("handle"): return row
    jp = get_json(pg, "https://%s/products/%s.json" % (dom, row["handle"]), tries=2)
    if jp and jp.get("product"):
        fixed = prod_row(jp["product"], row["pos"], row["src"] + "+recheck")
        if fixed["desc"] and desc_conf(fixed["t"], fixed["desc"]) == "ok":
            return fixed
    return row

def homepage_meta(pg, dom):
    """v4.2: ONE homepage fetch → the store's OWN pitch (og:title + H1 + og:description = the banner/value-prop),
    the banner image, and the handle of the product the banner features. Lets me judge 'is this our kind of store'
    from the merchant's own words — without opening the site. (No review/brand-claim fields — Marina: fakeable.)"""
    html = get_html(pg, "https://%s/" % dom, tries=2)
    if not html:
        return {"pitch": "", "img": "", "hero_handle": "", "ok": False}
    def meta(prop):
        m = re.search(r'<meta[^>]+(?:property|name)=["\']%s["\'][^>]*content=["\']([^"\']+)' % re.escape(prop), html, re.I)
        if not m:
            m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*(?:property|name)=["\']%s["\']' % re.escape(prop), html, re.I)
        return m.group(1).strip() if m else ""
    og_title = meta("og:title")
    og_desc = meta("og:description") or meta("description")
    h1 = ""
    mh = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    if mh:
        h1 = re.sub(r"<[^>]+>", " ", mh.group(1)); h1 = re.sub(r"\s+", " ", h1).strip()
    og_img = meta("og:image")
    # v4.2: pick the first REAL product handle on the homepage as the banner hero — skip gift-card/shipping/
    # personalization junk handles (else a header gift-card link masquerades as the banner hero → false divergence).
    HJUNK = ["gift-card", "gift_card", "giftcard", "personaliz", "reship", "shipping", "warranty",
             "deposit", "insurance", "protection", "sample", "subscription", "e-gift", "egift"]
    hero_handle = ""
    for h in re.findall(r"/products/([a-z0-9][a-z0-9\-]{1,80})", html):
        if any(j in h for j in HJUNK):
            continue
        hero_handle = h; break
    seen = []
    for x in (og_title, h1, og_desc):
        x = (x or "").strip()
        if x and x not in seen:
            seen.append(x)
    return {"pitch": " | ".join(seen)[:400], "img": og_img, "hero_handle": hero_handle, "ok": True}

def collect_products(pg, dom):
    for coll in ["best-selling", "bestsellers", "best-sellers", "frontpage", "featured"]:
        j = get_json(pg, "https://%s/collections/%s/products.json?limit=20" % (dom, coll))
        if j and j.get("products"):
            return [prod_row(p, i, coll) for i, p in enumerate(j["products"])], coll, "high"
    j = get_json(pg, "https://%s/products.json?limit=50" % dom)
    if j and j.get("products"):
        return [prod_row(p, i, "all") for i, p in enumerate(j["products"])], "all", "low"
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
            if not rows:
                o["reachable"] = False
                o["reason"] = {"homepage-noprod": "site loads, no parseable products (manual look)",
                               "unreachable": "site did not load (manual look)"}.get(src, "no products (manual look)")
                o["tops3"] = []; o["candidate"] = None; o["tier"] = "MANUAL"
                o["store_type"] = store_type([], pc, d.get("merch"), dom); o["product_class"] = None
                res.append(o); continue
            o["reachable"] = True
            # v4.2: ONE homepage grab → store's OWN pitch + banner image + the banner-featured product handle.
            hm = homepage_meta(pg, dom)
            o["home_pitch"] = hm["pitch"]; o["home_img"] = hm["img"]
            home_handle = hm["hero_handle"]
            # SELF-CHECK (1): when the source was weak (hconf=low: we fell to `all`/homepage, hero unreliable), promote
            # the homepage banner-featured product to the front (heatka/hanboost case). High-conf sales collection → skip.
            if hconf == "low" and home_handle:
                jp = get_json(pg, "https://%s/products/%s.json" % (dom, home_handle), tries=2)
                if jp and jp.get("product"):
                    hh = prod_row(jp["product"], -1, "home-hero")
                    if hh["handle"] and hh["handle"] not in [r.get("handle") for r in rows]:
                        rows = [hh] + rows
                        hconf = "high"; o["hero_confidence"] = "high"; o["hero_src"] = src + "+home-hero"
            store_cur = store_currency(pg, dom) or CC_CUR.get((cc or "").upper(), ("?", 1.0))[0]
            o["store_currency"] = store_cur
            clean = []
            for r in rows:
                if has(r["t"], JUNK): continue
                if r["price_raw"] <= 0:
                    r["price"] = None; r["currency"] = store_cur; r["rate"] = 1.0; r["price_unknown"] = True
                else:
                    pu, cur, rate = usd(r["price_raw"], store_cur)
                    r["price"] = pu; r["currency"] = cur; r["rate"] = rate; r["price_unknown"] = False
                clean.append(r)
            # v4.2: capture the homepage BANNER-featured product as a SEPARATE field, shown ALONGSIDE the best-seller
            # candidate (Marina: show BOTH heroes). If it differs from the pick → contributes to needs_live (I decide).
            o["home_hero"] = None
            if home_handle:
                in_clean = next((r for r in clean if r.get("handle") == home_handle), None)
                if in_clean is not None:
                    o["home_hero"] = {"t": in_clean["t"][:60], "handle": home_handle, "in_clean": True}
                else:
                    jph = get_json(pg, "https://%s/products/%s.json" % (dom, home_handle), tries=2)
                    if jph and jph.get("product"):
                        hr = prod_row(jph["product"], -1, "home-featured")
                        if hr["price_raw"] > 0:
                            hp, hcur, _ = usd(hr["price_raw"], store_cur)
                        else:
                            hp, hcur = None, store_cur
                        o["home_hero"] = {"t": hr["t"][:60], "handle": home_handle, "price": hp, "cur": hcur,
                                          "desc": hr["desc"][:300], "bullets": hr["bullets"], "img": hr["img"],
                                          "pclass": hr["pclass"], "k": hr["k"], "in_clean": False}
            # store essence: derive from the catalog's product classes + pc + name
            o["store_type"] = store_type([r["pclass"] for r in clean], pc, d.get("merch"), dom)
            recent = [r["created_days"] for r in clean if r["created_days"] is not None and r["created_days"] <= 30]
            o["new_products_30d"] = len(recent)
            phys = [r for r in clean if r["k"] == "physical"]
            def invest_score(r):
                iv = r["invest"]; return iv["desc_len"] + iv["imgs"]*20 + iv["variants"]*5 + len(iv["badges"])*40
            phys.sort(key=lambda r: (r["pos"], -invest_score(r)))
            tops3 = phys[:3] if phys else clean[:3]
            def t_inrange(r): return (not r["price_unknown"]) and 39 <= r["price"] <= 170
            o["tops3"] = [{"t": r["t"][:60], "price": r["price"], "price_raw": r["price_raw"], "cur": r["currency"],
                           "k": r["k"], "pclass": r["pclass"], "pos": r["pos"], "desc": r["desc"][:550], "bullets": r.get("bullets", []), "img": r["img"],
                           "handle": r.get("handle", ""), "price_unknown": r["price_unknown"], "in_range": t_inrange(r),
                           "anchor": (round(100*(1-r["price"]/(r["cmp"]*r["rate"]))) if (not r["price_unknown"] and r["cmp"]>r["price_raw"]>0) else 0),
                           "pust": has(r["t"]+" "+r["desc"], PUST), "desc_confidence": desc_conf(r["t"], r["desc"]),
                           "invest": r["invest"]} for r in tops3]
            if not tops3:
                o["candidate"] = None; o["tier"] = "DROP-noPhysical"; o["product_class"] = None; res.append(o); continue
            if all(t["price_unknown"] for t in o["tops3"]):
                t0c = o["tops3"][0]
                o["candidate"] = t0c["t"]; o["price"] = None; o["in_range"] = None
                o["desc"] = t0c["desc"]; o["bullets"] = t0c.get("bullets", []); o["image"] = t0c["img"]; o["kind"] = t0c["k"]
                o["product_class"] = t0c["pclass"]; o["desc_confidence"] = t0c["desc_confidence"]
                o["pust"] = t0c["pust"]; o["storefront_pos"] = t0c["pos"]; o["anchor"] = 0
                o["tier"] = "PRICE-CHECK"; o["reason"] = "products.json prices all 0 (region-gated) → confirm price live"
                res.append(o); continue
            inr = [t for t in o["tops3"] if t["in_range"]]
            known = [t for t in o["tops3"] if not t["price_unknown"]]
            cand = inr[0] if inr else (known[0] if known else o["tops3"][0])
            # SELF-CHECK (2): if the chosen candidate's desc is empty/mismatched → re-fetch its own page to correct
            if cand.get("desc_confidence") != "ok" and cand.get("handle"):
                fixed = recheck_desc(pg, dom, {"handle": cand["handle"], "pos": cand["pos"], "src": "cand"})
                if fixed.get("desc") and desc_conf(fixed["t"], fixed["desc"]) == "ok":
                    cand["desc"] = fixed["desc"][:550]; cand["desc_confidence"] = "ok"; cand["pclass"] = fixed["pclass"]
                    cand["bullets"] = fixed.get("bullets", cand.get("bullets", [])); cand["rechecked"] = True
            o["candidate"] = cand["t"]; o["price"] = cand["price"]; o["currency"] = cand["cur"]
            o["in_range"] = cand["in_range"]; o["desc"] = cand["desc"]; o["bullets"] = cand.get("bullets", []); o["image"] = cand["img"]
            o["pust"] = cand["pust"]; o["kind"] = cand["k"]; o["product_class"] = cand["pclass"]
            o["desc_confidence"] = cand["desc_confidence"]; o["anchor"] = cand["anchor"]; o["storefront_pos"] = cand["pos"]
            res.append(o)
          except Exception as e:
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
    cands = [r for r in res if r.get("candidate")]
    for r in cands:
        rt = toks(r["candidate"]); cores = set()
        for o in cands:
            if o is r: continue
            if len(rt & toks(o["candidate"])) >= 2:
                cores.add(brand_core(o["domain"]))
        cores.discard(brand_core(r["domain"]))
        r["conv_batch"] = len(cores)
    for r in res:
        if not r.get("candidate"):
            r["score"] = 0; r["tier"] = r.get("tier", "DROP"); continue
        if r.get("tier") == "PRICE-CHECK":
            r["score"] = 0
            r["flags"] = ["price-unknown→live", ("established" if r.get("maturity") == "established" else r.get("cat_flag", ""))]
            if r.get("conv_batch", 0) >= 1: r["flags"].insert(0, "CONV:%d" % r["conv_batch"])
            continue
        inr = r["in_range"]; pust = r["pust"]; phys = r["kind"] == "physical"; conv = r.get("conv_batch", 0) >= 1
        sf = r.get("storefront_pos", 9); dc = r.get("desc_confidence"); pcl = r.get("product_class")
        sc = 0
        sc += 35 if inr else 5
        sc += 22 if conv else 0
        sc += 12 if sf <= 0 else 8 if sf <= 2 else 3
        sc += 7 if r["cat_flag"] == "hero" else (-8 if r["cat_flag"] == "catalog-giant" else 0)
        # v4: product-class modifier — deprioritize trade, lift genuine consumer (SORT-AID only; main agent reads ALL)
        if pcl in TRADE_CLASSES: sc -= 25
        elif pcl in ("consumer-gadget", "consumer-other"): sc += 8
        if pust: sc -= 30
        if not phys: sc -= 30
        r["score"] = sc
        flags = []
        if conv: flags.append("CONV:%d" % r["conv_batch"])
        if pust: flags.append("пустышка")
        if not inr: flags.append("price-out")
        if pcl in TRADE_CLASSES: flags.append("TRADE:%s" % pcl)
        if dc != "ok": flags.append("desc:%s→WebFetch" % dc)
        if r["hero_confidence"].startswith("low"): flags.append("hero:low→confirm")
        if r.get("new_products_30d", 0) >= 1: flags.append("new30d:%d" % r["new_products_30d"])
        if r["maturity"] == "established": flags.append("established")
        flags.append(r["cat_flag"])
        r["flags"] = flags
        r["tier"] = "A" if sc >= 54 and inr and phys and not pust else ("B" if sc >= 40 and inr and phys and not pust else "C")
    # v4.2.1 (2026-06-01): needs_live = CARD-INSUFFICIENT only (the store's "open me by hand" worklist; RULE 23).
    # The agent MUST live-open every needs_live + unreachable store. Calibration lesson (batch2): `hero_confidence=low`
    # is a SOURCE artifact (store has no best-selling collection → products.json fallback), NOT real uncertainty —
    # the rich card (pitch + both heroes + long desc + bullets) is usually fully readable, so low-conf alone does NOT
    # force an open (it inflated needs_live to 62%). Force-open ONLY when the card can't actually be judged:
    #   unreachable · price-unknown · candidate desc not-ok · nothing-readable (no pitch AND no readable candidate desc)
    #   · banner-hero diverges AND that hero is itself unreadable in the card.
    for r in res:
        nl = False; why = []
        if not r.get("reachable"):
            nl = True; why.append("unreachable")
        else:
            dc = r.get("desc_confidence")
            if dc and dc != "ok": nl = True; why.append("desc-" + dc)
            if r.get("tier") == "PRICE-CHECK": nl = True; why.append("price-unknown")
            pitch_ok = bool((r.get("home_pitch") or "").strip())
            cand_readable = (dc == "ok") and bool((r.get("desc") or "").strip())
            if not pitch_ok and not cand_readable: nl = True; why.append("card-thin")
            hh = r.get("home_hero")
            if hh and not hh.get("in_clean") and hh.get("handle") and hh.get("k") == "physical" and not hh.get("desc"):
                nl = True; why.append("banner-hero-unreadable")
        r["needs_live"] = nl; r["needs_live_why"] = why
    order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3, "MANUAL": 4, "DROP-noPhysical": 5, "DROP": 6}
    res.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(res, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    reach = sum(1 for r in res if r.get("reachable"))
    manual = sum(1 for r in res if r.get("tier") == "MANUAL")
    needs_live = sum(1 for r in res if r.get("needs_live"))
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d manual=%d needs_live=%d tiers=%s classes=%s stores=%s" % (
        len(res), round(time.time()-t0), reach, manual, needs_live,
        dict(Counter(r.get("tier") for r in res)), dict(Counter(r.get("product_class") for r in res)),
        dict(Counter(r.get("store_type") for r in res))))
    print("=== SL ENRICH4 v4.2 DONE ===", len(res), "secs", round(time.time()-t0), "reach", reach, "needs_live", needs_live,
          "tiers", dict(Counter(r.get("tier") for r in res)),
          "classes", dict(Counter(r.get("product_class") for r in res)),
          "store_types", dict(Counter(r.get("store_type") for r in res)))
