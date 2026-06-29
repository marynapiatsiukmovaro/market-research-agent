#!/usr/bin/env python3
"""Build the full niche (L1) -> sub-niche (L2) tree with store counts from the captured Shopify universe CSV.
A store is counted once per distinct L1 and once per distinct L1/L2 it lists (categories are ':'-separated paths).
Writes: text summary to stdout + a full HTML tree to <out.html>.
Usage: python3 sl_niche_tree.py <out.html>
"""
import csv, sys, html
from collections import Counter, defaultdict
F = "/opt/market-research-agent/logs/storeleads/exports/storeleads_shopify_active_2026-06-08.csv"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/opt/market-research-agent/logs/storeleads/niche_tree.html"
csv.field_size_limit(10**9)
r = csv.reader(open(F, newline=''))
h = next(r); ci = h.index("categories")
L1 = Counter(); tree = defaultdict(Counter)
n = 0; nocat = 0
for row in r:
    n += 1
    if len(row) <= ci:
        continue
    c = row[ci]
    if not c:
        nocat += 1; continue
    seen1 = set(); seen2 = set()
    for p in c.split(":"):
        parts = [x for x in p.split("/") if x]
        if not parts:
            continue
        l1 = parts[0]
        if l1 not in seen1:
            L1[l1] += 1; seen1.add(l1)
        if len(parts) >= 2:
            key = (l1, parts[1])
            if key not in seen2:
                tree[l1][parts[1]] += 1; seen2.add(key)
# ---- text summary (L2 >= 200 for chat brevity) ----
print(f"ROWS={n:,}  no-category={nocat:,}  L1-count={len(L1)}")
print("\n===== NICHE (L1) -> SUB-NICHE (L2) =====")
for l1, t1 in L1.most_common():
    subs = tree[l1].most_common()
    big = [(s, v) for s, v in subs if v >= 200]
    omitted = len(subs) - len(big)
    print(f"\n■ {l1}  —  {t1:,} stores  ({len(subs)} sub-niches)")
    for s, v in big:
        print(f"    {v:>8,}  {l1} / {s}")
    if omitted:
        small = sum(v for s, v in subs if v < 200)
        print(f"    (+ {omitted} smaller sub-niches, {small:,} stores total, <200 each — in HTML)")
# ---- full HTML ----
rows = []
for l1, t1 in L1.most_common():
    rows.append(f'<tr style="background:#eef"><td><b>{html.escape(l1)}</b></td><td align=right><b>{t1:,}</b></td></tr>')
    for s, v in tree[l1].most_common():
        rows.append(f'<tr><td style="padding-left:24px">{html.escape(l1)} / {html.escape(s)}</td><td align=right>{v:,}</td></tr>')
open(OUT, "w").write(
    "<html><meta charset=utf-8><body style='font-family:system-ui;font-size:13px'>"
    f"<h2>Store Leads — full niche tree (Shopify-Active, snapshot 2026-06-08)</h2>"
    f"<p>{n:,} stores · {nocat:,} no-category · {len(L1)} L1 niches</p>"
    "<table border=1 cellspacing=0 cellpadding=3>" + "".join(rows) + "</table></body></html>")
print(f"\nHTML written -> {OUT}")
