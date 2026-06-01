#!/usr/bin/env python3
"""sl_stage3_pull.py — compact Stage-3 digest from an sl_enrich4 (v4.2) enriched JSON.
Prints (token-lean, for the main agent's deep-score): the candidate POOL (stores with >=1
in_range physical non-пустышка candidate, full desc), plus PRICE-CHECK / MANUAL domains, plus
a tally of the rest (loss-measurement transparency, RULE 1). Read-only.
Usage: python3 sl_stage3_pull.py <enriched.json>
"""
import json, sys
from collections import Counter
rows = json.load(open(sys.argv[1]))
def tops(r): return r.get("tops3") or []

pool, other_phys, nonphys, pricechk, manual = [], [], 0, [], []
for r in rows:
    t = r.get("tier")
    if t == "MANUAL": manual.append(r.get("domain"))
    if t == "PRICE-CHECK":
        pricechk.append((r.get("domain"), [(c.get("price"), c.get("cur"), (c.get("desc") or "")[:60]) for c in tops(r)]))
    inr = [c for c in tops(r) if c.get("in_range") and not c.get("pust")]
    if inr: pool.append(r)
    elif any(c.get("price_unknown") for c in tops(r)): pass
    elif tops(r): other_phys.append(r)
    else: nonphys += 1

print("POOL (>=1 in_range physical candidate):", len(pool))
print("other (physical, all out-of-range):", len(other_phys), "| no-candidates:", nonphys)
print("PRICE-CHECK:", len(pricechk), "| MANUAL:", len(manual))
print("conv distribution (pool):", dict(Counter(r.get("conv_batch") for r in pool)))
print("=" * 80)
for r in sorted(pool, key=lambda x: (-(x.get("conv_batch") or 0), {"A": 0, "B": 1, "C": 2}.get(x.get("tier"), 3))):
    h = [c for c in tops(r) if c.get("in_range") and not c.get("pust")]
    print("\n### %s | tier=%s score=%s | mat=%s conv=%s heroConf=%s descConf=%s | created=%s visits=%s rev=%s" % (
        r.get("domain"), r.get("tier"), r.get("score"), r.get("maturity"), r.get("conv_batch"),
        r.get("hero_confidence"), r.get("desc_confidence"), r.get("created"), r.get("visits"), r.get("sl_rev")))
    for c in h:
        print("   $%s %s [%s] pos=%s inv=%s: %s" % (
            c.get("price"), c.get("cur"), c.get("desc_confidence"), c.get("pos"), c.get("invest"), (c.get("desc") or "")[:170]))
print("\n" + "=" * 80)
print("PRICE-CHECK (confirm price live):")
for d, cs in pricechk: print("  ", d, cs)
print("MANUAL (open manually):", manual)
print("\nOTHER physical out-of-range (loss-measurement sample — first 15 domains):",
      [r.get("domain") for r in other_phys[:15]])
