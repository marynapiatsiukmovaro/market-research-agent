# SH-5 conservative Stage-1 cut (faithful to subagent-spec.md + SH-4 funnel).
# Input: parallel-hero output (list of {shop_id,name,domain,...,top:[{t,price,wk},...]}).
# Drops ONLY definite-no: dead / no physical product at all / hero is пустышка /
#   ALL physical products in an EXTREME price band (SH price unreliable -> generous pad [25,220]).
# Service-SKU as #1 (shipping protection / gift card / warranty) = ShopHunter mislabel -> DIG top-3, never drop on it.
# Everything ambiguous is KEPT -> the live DESCRIPTION at Stage-2 is the real filter.
# Survivors written in FULL hero-record format (top preserved) -> enricher input.
# Usage: sh5_cut.py <hero_infile> <enrich_outfile>
import json, re, sys
from collections import Counter
OUT = "/opt/market-research-agent/logs/shophunter"
INF, OUTF = sys.argv[1], sys.argv[2]
data = json.load(open(OUT + "/" + INF))

JUNK = ["shipping protection", "protection plan", "gift card", "gift-card", "warranty", "guarantee",
        "route package", "insurance", "donation", "tip", "sample", "e-book", "ebook", "deposit"]
PUST = ["lymphatic", "red light", "red-light", "drainage", "detox", "slimming", "cellulite", "circulation",
        "infrared therapy", "magnetic therapy", "anti-aging", "anti aging", "mole removal", "skin tag",
        "energy heal", "chakra", "aura", "frequency heal", "parasite", "body cleanse", "liver detox",
        "grounding", "manifest", "collagen boost"]
SUPP = ["supplement", "softgel", "soft gel", "capsule", "vitamin", "gummies", "gummy", "probiotic", "tincture",
        "shilajit", "electrolyte", "omega", "creatine", "protein", "cayenne", "turmeric", "magnesium", "biotin",
        "nootropic", "peptide", "berberine", "hormone", "mushroom complex", "elixir", "nectar", "pollen", "shake",
        "metabolism", "nitric oxide", "greens", "superfood", "sea moss", "seamoss", "moringa", "oregano", "ormus",
        "iodine", "black seed", "nmn", "nad+", "glutathione", "ashwagand", "prebiotic", "d-mannose", "lecithin",
        "monatomic", "sango", "koralle", "b-complex"]
SKIN = ["serum", "face oil", "moisturizer", "cleanser", "toner", "sheet mask", "ampoule", "essence", "face cream"]
APP = ["dress", "shirt", "t-shirt", "tee ", "sneaker", "shoe ", "legging", "bra ", "hoodie", "jacket", "jewelry",
       "necklace", "earring", "bracelet", "sock", "jeans", "shorts", "espadrille", "wide leg", "cardigan",
       "blazer", "windbreaker", "knit", "denim", "loafer", "skirt", "fleece", "coat"]
POD = ["personalized", "personalised", "custom pet", "portrait", "place card", "engraved", "your pet",
       "mascota", "wall art", "canvas", "needlepoint"]

def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, l):
    s = low(t); return any(k in s for k in l)
def npx(s):
    m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
def klass(t):
    if has(t, PUST): return "пустышка"
    if has(t, SUPP): return "supplement"
    if has(t, SKIN): return "skincare"
    if has(t, POD): return "pod/art"
    if has(t, APP): return "apparel"
    return "physical"

PAD_LO, PAD_HI = 25, 220  # generous band: SH price unreliable both ways (real filter = Stage-2)
surv, drops = [], []
reasons = Counter()
for d in data:
    top = d.get("top", [])
    name = d.get("name", "")[:30]
    if not top:
        drops.append(("DEAD/no-hero", name, "", 0, d.get("domain", ""))); reasons["dead"] += 1; continue
    # real hero = first non-service product (service #1 = ShopHunter mislabel)
    svc1 = has(top[0]["t"], JUNK)
    nonsvc = [p for p in top if not has(p["t"], JUNK)]
    if not nonsvc:
        drops.append(("ALL-SERVICE", name, top[0]["t"][:44], npx(top[0]["price"]), d.get("domain", ""))); reasons["all-service"] += 1; continue
    hero = nonsvc[0]
    hk = klass(hero["t"])
    phys = [p for p in nonsvc if klass(p["t"]) == "physical"]
    # DROP 1: hero is пустышка (Marina #1)
    if hk == "пустышка":
        drops.append(("ПУСТЫШКА-hero", name, hero["t"][:44], npx(hero["price"]), d.get("domain", ""))); reasons["пустышка"] += 1; continue
    # DROP 2: no physical product anywhere in top -> store is supp/skin/apparel/pod
    if not phys:
        drops.append((hk.upper() + "-only", name, hero["t"][:44], npx(hero["price"]), d.get("domain", ""))); reasons[hk] += 1; continue
    # DROP 3: ALL physical products in an EXTREME band (padded for SH unreliability)
    pp = [npx(p["price"]) for p in phys if npx(p["price"]) > 0]
    if pp and all((x > PAD_HI or x < PAD_LO) for x in pp):
        band = "all>$220" if all(x > PAD_HI for x in pp) else ("all<$25" if all(x < PAD_LO for x in pp) else "all-out-band")
        drops.append(("PRICE-" + band, name, phys[0]["t"][:44], pp[0], d.get("domain", ""))); reasons["price-extreme"] += 1; continue
    # KEEP — preserve full hero record for the enricher; tag service-dig for visibility
    rec = dict(d)
    rec["_svc1"] = svc1
    surv.append(rec)

json.dump(surv, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)

print("=== SH-5 CONSERVATIVE CUT —", INF, "===")
print("input:", len(data), "| SURVIVORS(->enrich):", len(surv), "| dropped:", len(drops))
print("drop reasons:", dict(reasons))
print("service-SKU-as-#1 dug (kept):", sum(1 for r in surv if r.get("_svc1")))
print("\n--- DROPPED (verify none is a real gadget — RULE 8 spirit) ---")
for tag, nm, hero, pr, dom in drops:
    print("  [%-16s] %-30s | %-44s | $%-7.0f | %s" % (tag, nm, hero, pr, dom))
print("\n--- SURVIVOR price-flag distribution (SH price, for context only) ---")
fl = Counter()
for r in surv:
    phys = [p for p in r["top"] if klass(p["t"]) == "physical" and not has(p["t"], JUNK)]
    pp = [npx(p["price"]) for p in phys if npx(p["price"]) > 0]
    inr = any(39 <= x <= 170 for x in pp)
    fl["has-in-range" if inr else "needs-real-price-check"] += 1
print(dict(fl))
