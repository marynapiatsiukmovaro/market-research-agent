# Tightened Stage-1 cut: catch leaked ingestibles + cut clearly-below-floor (<$36). Keep $36-170 physical + ambiguous.
import json, re
from collections import Counter
OUT = "/opt/market-research-agent/logs/shophunter"
ls = json.load(open(f"{OUT}/hg_sh4b_ls2.json"))

INGEST_EXT = ["soft gel", "softgel", "iodine", "black seed", "sea moss", "seamoss", "ormus", "moringa", "oregano",
              "patches", "sango", "koralle", "b-complex", "glutathione", "ashwagand", "monatomic", "tincture",
              "drops", "capsule", "gummies", "gummy", "powder", " tea ", "supplement", "vitamin", "probiotic",
              "electrolyte", "omega", "creatine", "peptide", "nmn", "nad+", "shilajit", "manna gold", "booster pack",
              "nasal spray", "oil bundle", "sea-moss", "softgels", "lecithin", "berberine", "mushroom complex"]
def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, lst):
    s = low(t); return any(k in s for k in lst)

def reason_cut(r):
    fl = r.get("flags", [])
    if r.get("tier") == "DROP": return "dead/unreachable"
    if "пустышка" in fl: return "пустышка (Marina #1)"
    if not r.get("physical", False): return "non-gadget (%s)" % r.get("kind", "")
    if has(r.get("product", ""), INGEST_EXT): return "ingestible (leaked, caught now)"
    if r.get("price", 0) > 170: return "price > $170"
    if r.get("price", 0) < 36: return "below $36 (under floor)"
    return None

cut, surv = [], []
for r in ls:
    rc = reason_cut(r)
    (cut if rc else surv).append((r, rc))
print("=== TIGHTENED STAGE-1 CUT (301-450) ===")
print("TOTAL:", len(ls), "| CUT:", len(cut), "| SURVIVORS:", len(surv))
print("\n-- cut reasons --")
for k, v in Counter(rc for _, rc in cut).most_common(): print("  %-34s %d" % (k, v))
print("\n-- survivors price flags --", dict(Counter(r["pflag"] for r, _ in surv)))
print("-- survivors by niche --")
for k, v in Counter(r["niche"] for r, _ in surv).most_common(): print("  %-16s %d" % (k, v))
json.dump([r for r, _ in surv], open(f"{OUT}/hg_sh4b_survivors.json", "w"), ensure_ascii=False, indent=1)
print("\nsurvivors -> hg_sh4b_survivors.json (", len(surv), ")")
