#!/usr/bin/env python3
"""Store Leads — BUILD-select: next N stores, excluding processed ∪ enriched_index (S11, decoupled).

Replaces SKIP-paging for reservoir-build. The page is defined by EXCLUSION, not by position, so a parallel
analysis session marking stores `processed` never shifts it (those stores are already in enriched_index →
already excluded; processed⊆enriched for built stores). This removes the SKIP coverage-gap risk and lets
analysis run on the SAME niche being built. Order = visits desc, missing-visits last but KEPT (RULE 24).
Only-exclusions = processed (RULE 19) ∪ enriched (RULE 30). NO field filters (RULE 24).

Usage:  sl_select_build.py <dedup_full_slug> <out_slug> [N=250]
  (slug relative to logs/storeleads, e.g. niches/pets-and-animals/dogs/dogs_dedup — reads <slug>_full.json)
"""
import json, sys, os
OUT = "/opt/market-research-agent/logs/storeleads"
SLUG = sys.argv[1]; OUTSLUG = sys.argv[2]
N = int(sys.argv[3]) if len(sys.argv) > 3 else 250


def norm(d):
    d = str(d).strip().lower()
    for p in ("http://", "https://"):
        if d.startswith(p):
            d = d[len(p):]
    d = d.split("/")[0].split("?")[0]
    if d.startswith("www."):
        d = d[4:]
    return d.rstrip(".")


rows = json.load(open(f"{OUT}/{SLUG}_full.json"))
PROC = f"{OUT}/processed_domains.json"
IDX = f"{OUT}/enriched_index.json"
processed = set(norm(k) for k in json.load(open(PROC)).keys()) if os.path.exists(PROC) else set()
enriched = set(norm(k) for k in json.load(open(IDX)).keys()) if os.path.exists(IDX) else set()
excl = processed | enriched
pool = [r for r in rows if norm(r.get("domain")) not in excl]          # exclude processed ∪ enriched only
pool.sort(key=lambda r: (r.get("visits") if r.get("visits") is not None else -1), reverse=True)
sel = pool[:N]


def conv(r):
    return {"name": r["domain"], "merch": r.get("merchant"), "erf": r.get("sales"), "apf": r.get("avg_price"),
            "pc": r.get("products"), "created": r.get("created"), "fbpx": None,
            "visits": r.get("visits"), "country": r.get("country"), "min_price": r.get("min_price"),
            "max_price": r.get("max_price"), "avg_weight": r.get("avg_weight"), "variants": r.get("variants"),
            "comb_reviews": r.get("comb_reviews"), "tp_reviews": r.get("tp_reviews"),
            "fb": r.get("fb"), "ig": r.get("ig"), "tiktok": r.get("tiktok"), "pinterest": r.get("pinterest"),
            "theme": r.get("theme")}


json.dump([conv(r) for r in sel], open(f"{OUT}/{OUTSLUG}.json", "w"), ensure_ascii=False)
total = len(rows)
print(f"total={total} | processed={len(processed)} | enriched={len(enriched)} | "
      f"remaining(unbuilt)={len(pool)} | selected={len(sel)}")
miss = sum(1 for r in sel if r.get("visits") is None)
print(f"  selected incl. {miss} with MISSING visits (kept, not dropped)")
if sel:
    vs = [r.get("visits") for r in sel if r.get("visits") is not None]
    if vs:
        print(f"  selected visits range (non-missing): {min(vs):,}..{max(vs):,}")
print("=== SELECT-BUILD DONE ===")
