#!/usr/bin/env python3
# Resolve curated A&P domains -> shop_ids from the dump. Read-only.
# Usage: ap_resolve_ids.py <domains_file>  -> prints "id  domain" + a space-joined ID line + misses.
import json, sys, re
D = "/opt/market-research-agent/logs/shophunter"
dump = json.load(open(D + "/animals_pet_supplies_shops.json"))
def core(d):
    return re.sub(r"^www\.", "", (d or "").strip().lower())
by = {}
for r in dump:
    by.setdefault(core(r.get("domain", "")), r)
wanted = [l.strip() for l in open(sys.argv[1]) if l.strip()]
ids, misses = [], []
for w in wanted:
    cw = core(w)
    rec = by.get(cw)
    if not rec:  # substring fallback
        for k, r in by.items():
            if cw in k or k in cw:
                rec = r; break
    if rec:
        ids.append(rec["shop_id"]); print("%-14s %s" % (rec["shop_id"], w))
    else:
        misses.append(w); print("MISS           %s" % w)
print("\nIDS:", " ".join(ids))
print("COUNT:", len(ids), "| MISSES:", len(misses), misses)
open(D + "/ap_seed_ids.txt", "w").write(" ".join(ids))
