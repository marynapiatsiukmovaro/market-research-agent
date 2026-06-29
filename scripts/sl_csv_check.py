#!/usr/bin/env python3
"""Inspect / count the universe CSV. Verify export faithfulness vs live StoreLeads counts.
Usage:
  python3 sl_csv_check.py sample
  python3 sl_csv_check.py count "<category substring>"
"""
import csv, sys
F = "/opt/market-research-agent/logs/storeleads/exports/storeleads_shopify_active_2026-06-08.csv"
csv.field_size_limit(10**9)
mode = sys.argv[1] if len(sys.argv) > 1 else "sample"
r = csv.reader(open(F, newline=''))
h = next(r)
ci = h.index("categories"); vi = h.index("estimated_monthly_visits"); di = h.index("domain")
if mode == "sample":
    n = 0
    for row in r:
        if n >= 8:
            break
        print("domain=", repr(row[di]), "| categories=", repr(row[ci]), "| visits=", repr(row[vi]))
        n += 1
else:
    needle = sys.argv[2]
    tot = 0; band = 0; n = 0
    for row in r:
        n += 1
        if len(row) <= max(ci, vi, di):
            continue
        if needle in row[ci]:
            tot += 1
            try:
                v = float(row[vi])
                if 1000 <= v <= 10000:
                    band += 1
            except Exception:
                pass
    print(f"rows scanned: {n}")
    print(f"category contains {needle!r}: total = {tot} | of which visits 1k-10k = {band}")
