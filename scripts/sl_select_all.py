#!/usr/bin/env python3
"""Select the next N UNPROCESSED stores from a *_full.json — NO field filters.

Marina S3 (2026-06-01): analyze EVERY store in the niche. visits / products / price / revenue are UNRELIABLE
fields — a missing/low value does NOT mean the store is dead or disqualified (missing != absent). So we NEVER
filter or drop by them (that repeats the weight-filter trap: a field-filter silently drops stores lacking the
field). The ONLY exclusion is already-processed (so a store is never analysed twice). This is why we dumped the
whole niche with just the 3 server-side filters (Shopify / Active / Created>=2020).

Order by visits desc is for BATCHING ORDER ONLY (process higher-confidence-traffic first); stores with missing
visits sort LAST but are fully KEPT and analysed. Output in sl_enrich4 input format.

Usage: sl_select_all.py <full_json_slug> <out_slug> [N=250] [SKIP=0]
  (with per-batch sl_mark_processed, SKIP can stay 0 — processed-exclusion pages you forward automatically.)
"""
import json, sys, os
OUT = "/opt/market-research-agent/logs/storeleads"
SLUG = sys.argv[1]; OUTSLUG = sys.argv[2]
N = int(sys.argv[3]) if len(sys.argv) > 3 else 250
SKIP = int(sys.argv[4]) if len(sys.argv) > 4 else 0
rows = json.load(open(f"{OUT}/{SLUG}_full.json"))
PROC = f"{OUT}/processed_domains.json"
processed = set(json.load(open(PROC)).keys()) if os.path.exists(PROC) else set()
pool = [r for r in rows if r.get("domain") not in processed]   # ONLY exclusion = already-processed
pool.sort(key=lambda r: (r.get("visits") if r.get("visits") is not None else -1), reverse=True)  # missing → last, KEPT
sel = pool[SKIP:SKIP + N]
def conv(r):
    return {"name": r["domain"], "merch": r.get("merchant"), "erf": r.get("sales"), "apf": r.get("avg_price"),
            "pc": r.get("products"), "created": r.get("created"), "fbpx": None,
            "visits": r.get("visits"), "country": r.get("country"), "min_price": r.get("min_price"),
            "max_price": r.get("max_price"), "avg_weight": r.get("avg_weight"), "variants": r.get("variants"),
            "comb_reviews": r.get("comb_reviews"), "tp_reviews": r.get("tp_reviews"),
            "fb": r.get("fb"), "ig": r.get("ig"), "tiktok": r.get("tiktok"), "pinterest": r.get("pinterest"),
            "theme": r.get("theme")}
json.dump([conv(r) for r in sel], open(f"{OUT}/{OUTSLUG}.json", "w"), ensure_ascii=False)
total = len(rows); done = len(rows) - len(pool)
print(f"total={total} | already-processed={done} | remaining(unprocessed)={len(pool)} | selected={len(sel)}")
miss = sum(1 for r in sel if r.get("visits") is None)
print(f"  selected incl. {miss} with MISSING visits (kept, not dropped)")
if sel:
    vs = [r.get("visits") for r in sel if r.get("visits") is not None]
    if vs: print(f"  selected visits range (non-missing): {min(vs):,}..{max(vs):,}")
print("=== SELECT-ALL DONE ===")
