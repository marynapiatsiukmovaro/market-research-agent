import json, re
OUT = "/opt/market-research-agent/logs/shophunter"
ls = json.load(open(f"{OUT}/hg_sh4b_ls2.json"))
par = {s["domain"]: s for s in json.load(open(f"{OUT}/hg_sh4b_par.json"))}
INGEST_EXT = ["soft gel", "softgel", "iodine", "black seed", "sea moss", "seamoss", "ormus", "moringa", "oregano",
              "patches", "sango", "koralle", "glutathione", "ashwagand", "monatomic", "tincture", "drops", "capsule",
              "gummies", "powder", " tea ", "supplement", "vitamin", "probiotic", "electrolyte", "omega", "creatine",
              "peptide", "nmn", "nad+", "shilajit", "manna gold", "booster pack", "nasal spray", "oil bundle", "berberine"]
def low(s): return " " + re.sub(r"[^a-z0-9+ ]", " ", (s or "").lower()) + " "
def has(t, l):
    s = low(t); return any(k in s for k in l)
# include = survivors(tightened) + price>170 cuts (to rescue in-range top-3). Exclude пустышка/ingestible/non-phys.
keep_ids = []
for r in ls:
    fl = r.get("flags", [])
    if r.get("tier") == "DROP": continue
    if "пустышка" in fl: continue
    if not r.get("physical"): continue
    if has(r.get("product", ""), INGEST_EXT): continue
    # keep if in-range survivor OR a premium (>170) store worth rechecking top-3
    if r.get("price", 0) >= 36:  # drop clearly-below-floor; keep in-range AND >170 (recheck)
        keep_ids.append(r["domain"])
recs = [par[i] for i in keep_ids if i in par]
json.dump(recs, open(f"{OUT}/hg_sh4b_enrich_in.json", "w"), ensure_ascii=False, indent=1)
json.dump(recs[:5], open(f"{OUT}/enrich_test5.json", "w"), ensure_ascii=False, indent=1)
print("enrich input:", len(recs), "| test5 built")
print("price>170 included for recheck:", sum(1 for r in ls if r["shop_id"] in keep_ids and r.get("price", 0) > 170))
