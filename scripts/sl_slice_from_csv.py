#!/usr/bin/env python3
"""Store Leads — build a niche SLICE (`<slug>_full.json`) from the universe CSV (S14, 2026-06-08).

New data-acquisition path: instead of a paginated dump, we filter the captured universe CSV
(see methods/csv-export.md) by TOP-LEVEL category + visit band, and emit the same `_full.json`
schema that `sl_select_build.py` consumes. The rest of the pipeline (select_build → enrich4 →
accept_chunk → mark_enriched, waves of 7) is UNCHANGED. Dedup vs processed∪enriched is automatic
inside sl_select_build, so this just defines the strategic slice.

Usage:
  python3 scripts/sl_slice_from_csv.py <universe.csv> <out_slug> "<TopCategory>" [visit_lo=1000] [visit_hi=10000]
    e.g. ... storeleads_shopify_active_2026-06-08.csv niches/home-and-garden/hg_band1k "Home & Garden" 1000 10000
  Writes  logs/storeleads/<out_slug>_full.json  (relative slug, like sl_select_build).
"""
import csv, sys, json, os
csv.field_size_limit(sys.maxsize)
OUT = "/opt/market-research-agent/logs/storeleads"

csv_path = sys.argv[1] if not sys.argv[1].startswith("/") else sys.argv[1]
out_slug = sys.argv[2]
category = sys.argv[3]
lo = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
hi = int(sys.argv[5]) if len(sys.argv) > 5 else 10000
if not os.path.isabs(csv_path):
    csv_path = os.path.join(OUT, "exports", csv_path)
out_path = os.path.join(OUT, out_slug + "_full.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)


def top_levels(catfield):
    tops = set()
    for pth in (catfield or "").split(":"):
        seg = pth.strip().strip("/").split("/")
        if seg and seg[0]:
            tops.add(seg[0])
    return tops


def to_int(s):
    try:
        return int(float(s)) if s not in ("", None) else None
    except ValueError:
        return None


def to_float(s):
    try:
        return float(s) if s not in ("", None) else None
    except ValueError:
        return None


with open(csv_path, newline="", encoding="utf-8", errors="replace") as f:
    r = csv.reader(f)
    h = next(r)
    ix = {name: h.index(name) for name in (
        "domain", "estimated_monthly_visits", "merchant_name", "estimated_yearly_sales",
        "average_product_price_usd", "minimum_product_price", "maximum_product_price",
        "products_sold", "created", "country_code", "average_product_weight", "product_variants",
        "combined_reviews", "trustpilot_reviews", "facebook", "instagram", "tiktok", "pinterest",
        "theme", "categories")}
    out = []
    n = 0
    matched = 0
    for row in r:
        n += 1
        if len(row) <= ix["categories"]:
            continue
        v = to_int(row[ix["estimated_monthly_visits"]])
        if v is None or not (lo <= v < hi):
            continue
        if category not in top_levels(row[ix["categories"]]):
            continue
        matched += 1
        g = lambda k: row[ix[k]] if row[ix[k]] != "" else None
        out.append({
            "domain": g("domain"), "visits": v, "merchant": g("merchant_name"),
            "sales": to_float(row[ix["estimated_yearly_sales"]]),
            "avg_price": to_float(row[ix["average_product_price_usd"]]),
            "min_price": to_float(row[ix["minimum_product_price"]]),
            "max_price": to_float(row[ix["maximum_product_price"]]),
            "products": to_int(row[ix["products_sold"]]),
            "created": g("created"), "country": g("country_code"),
            "avg_weight": to_float(row[ix["average_product_weight"]]),
            "variants": to_int(row[ix["product_variants"]]),
            "comb_reviews": to_int(row[ix["combined_reviews"]]),
            "tp_reviews": to_int(row[ix["trustpilot_reviews"]]),
            "fb": g("facebook"), "ig": g("instagram"), "tiktok": g("tiktok"),
            "pinterest": g("pinterest"), "theme": g("theme")})
        if n % 500000 == 0:
            print(f"  ...scanned {n:,}, matched {matched:,}", flush=True)

json.dump(out, open(out_path, "w"), ensure_ascii=False)
print(f"SLICE: category='{category}' visits[{lo},{hi}) -> matched {matched:,} stores")
print(f"written: {out_path}")
print("DONE")
