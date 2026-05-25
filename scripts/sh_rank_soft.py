# SOFT Stage-3 (SH-4 revision): top-3 hero w/ service-SKU dig, soft price (tag not drop),
# name-class only for sorting, hard-drop ONLY dead stores. Outputs review buckets for manual validation.
import json, re, sys
from collections import Counter
OUT = "/opt/market-research-agent/logs/shophunter"
INF = sys.argv[1] if len(sys.argv) > 1 else "hg_sh4b_par.json"
data = json.load(open(OUT + "/" + INF))

# service / add-on SKUs that are NOT a real hero (ShopHunter mislabel signal) -> dig for real product
JUNK = ["shipping protection", "protection plan", "gift card", "gift-card", "warranty", "guarantee",
        "route package", "insurance", "donation", "tip", "sample", "e-book", "ebook", "deposit"]
PUST = ["lymphatic", "red light", "red-light", "drainage", "detox", "slimming", "cellulite", "circulation",
        "infrared therapy", "magnetic therapy", "collagen", "anti-aging", "anti aging", "mole", "skin tag",
        "energy heal", "chakra", "aura", "frequency", "parasite", "cleanse"]
# 2nd-pass broader supplement/ingestible signal (the leaky-name fix)
SUPP2 = ["supplement", "softgel", "capsule", "vitamin", "gummies", "gummy", "probiotic", "tincture", "shilajit",
         "electrolyte", "omega", "sea moss", "ashwagand", "creatine", "protein", "cayenne", "turmeric",
         "magnesium", "biotin", "nootropic", "peptide", "berberine", "hormone", "mushroom", "elixir", "nectar",
         "pollen", "shake", "metabolism", "nitric oxide", "greens", "superfood", "drops", "mcg", " mg", "blend",
         "mind", "longevity", "immune", "gut health", "prebiotic", "fiber", "d-mannose", "menopause", "fuel"]
APP = ["top", "dress", "shirt", "tee", "sneaker", "shoe", "legging", "bra", "hoodie", "jacket", "jewelry",
       "necklace", "earring", "bracelet", "sock", "jeans", "shorts", "espadrille", "wide leg", "cardigan",
       "blazer", "windbreaker", "knit", "denim"]
POD = ["personalized", "personalised", "custom pet", "portrait", "place card", "engraved", "your pet",
       "mascota", "wall art", "canvas", "needlepoint"]

def hasw(t, lst):
    s = " " + t.lower() + " "
    return any(k in s for k in lst)
def npx(s):
    m = re.search(r"([\d.,]+)", s or "")
    return float(m.group(1).replace(",", "")) if m else 0
def nrev(s):
    if not s: return 0
    s = s.replace("$", "").replace(",", "").strip()
    m = re.match(r"([\d.]+)\s*([KMkm]?)", s)
    if not m: return 0
    v = float(m.group(1)); u = m.group(2).upper()
    return v * 1000 if u == "K" else v * 1_000_000 if u == "M" else v
def klass(t):
    if hasw(t, PUST): return "пустышка"
    if hasw(t, SUPP2): return "supplement"
    if hasw(t, POD): return "pod/art"
    if hasw(t, APP): return "apparel"
    return "physical"

rows = []
for d in data:
    top = d.get("top", [])
    if not top:
        rows.append({"name": d["name"][:26], "domain": d["domain"], "klass": "DEAD/no-hero",
                     "hero": "(none)", "price": 0, "wk": 0, "wk_raw": "", "sku": d.get("sku", ""),
                     "ads": d.get("shop_ads", ""), "svc": False, "pflag": "-"})
        continue
    # service-SKU dig: real hero = first product whose name is NOT a service SKU
    svc = hasw(top[0]["t"], JUNK)
    real = next((p for p in top if not hasw(p["t"], JUNK)), top[0])
    p = npx(real["price"])
    pflag = "in" if 39 <= p <= 170 else ("below$39" if p < 39 else "above$170")
    rows.append({"name": d["name"][:26], "domain": d["domain"], "klass": klass(real["t"]),
                 "hero": real["t"][:46], "price": p, "wk": nrev(real.get("wk", "")), "wk_raw": real.get("wk", ""),
                 "sku": d.get("sku", ""), "ads": d.get("shop_ads", ""), "svc": svc, "pflag": pflag,
                 "top3": [(x["t"][:38], x["price"]) for x in top[:3]]})

# buckets
dead = [r for r in rows if r["klass"] == "DEAD/no-hero"]
phys = [r for r in rows if r["klass"] == "physical"]
drop_supp = [r for r in rows if r["klass"] == "supplement"]
drop_pust = [r for r in rows if r["klass"] == "пустышка"]
drop_app = [r for r in rows if r["klass"] == "apparel"]
drop_pod = [r for r in rows if r["klass"] == "pod/art"]
phys.sort(key=lambda r: -r["wk"])

print("=== STAGE-3 SOFT — batch", INF, "===")
print("total:", len(rows), "| DEAD:", len(dead), "| physical(KEEP):", len(phys),
      "| auto-drop supp:", len(drop_supp), "пуст:", len(drop_pust), "app:", len(drop_app), "pod/art:", len(drop_pod))
print("physical price flags:", dict(Counter(r["pflag"] for r in phys)))
print("service-SKU-as-#1 (dug for real hero):", sum(1 for r in rows if r["svc"]))
for r in rows:
    if r["svc"]: print("   SVC-DIG:", r["name"], "-> real hero:", r["hero"], r["price"])

print("\n=== PHYSICAL CANDIDATES (kept, ranked by revenue; price soft-flagged) ===")
for r in phys:
    print("  %-26s | %-46s | $%-7.0f %-9s | wk:%-8s sku:%-4s ads:%-3s | %s" % (
        r["name"], r["hero"], r["price"], r["pflag"], r["wk_raw"], r["sku"], r["ads"] or "0", r["domain"]))

print("\n=== AUTO-DROPPED (non-physical by name — VERIFY none is a real gadget) ===")
for tag, b in [("SUPPLEMENT", drop_supp), ("ПУСТЫШКА", drop_pust), ("APPAREL", drop_app), ("POD/ART", drop_pod), ("DEAD", dead)]:
    for r in b:
        print("  [%s] %-44s | $%-6.0f | %s" % (tag, r["hero"], r["price"], r["domain"]))

json.dump({"physical": phys, "drop_supp": drop_supp, "drop_pust": drop_pust, "drop_app": drop_app,
           "drop_pod": drop_pod, "dead": dead}, open(OUT + "/hg_sh4b_soft.json", "w"), ensure_ascii=False, indent=1)
