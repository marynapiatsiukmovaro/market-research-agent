#!/usr/bin/env python3
"""Store Leads — build a niche SLICE (`<slug>_full.json`) from the universe CSV (S14, 2026-06-08).

S20 FIX — the money parser was silently eating every price field.
  The CSV stores money as a STRING with a currency code and a symbol: "USD $150.27", "CHF 21.21 CHF",
  "USD $1,109.00". The old `to_float()` called `float(s)` on that, raised ValueError, and returned None.
  Result: `avg_price` / `min_price` / `max_price` / `sales` were **None for 7,639 of 7,639 stores** in the
  Toys & Hobbies slice (measured S20) — and for every slice built since S14. The card printed
  "SL revNone/avgNone" on all 250 rows of every batch, and `maturity` (which divides by revenue) has been
  deciding on a dead input this whole time. Absence of a field has no symptom.

What the slice now carries (all verified against the live CSV header):
  * `currency`        — the store's DECLARED currency (Store Leads copies the storefront's own claim, so it
                        can lie exactly like /meta.json does — magnetichoop.com declares USD, charges HK$).
  * `avg_price_usd`   — Store Leads' own USD conversion of the store's average product price.
  * `avg_price_native`, `min_price_native`, `max_price_native` — as the store shows them.
  * `min_price_usd`, `max_price_usd` — converted with the store's OWN implied rate
                        (avg_usd / avg_native), so we never depend on our hard-coded rate table here.
  * `sales_usd`       — estimated yearly sales.

The PRICE ENVELOPE (min/avg/max) is the one signal ShopHunter cannot have: it comes from the index, not
from the store's `products.json`. It is what catches "the robot is showing me spare parts" (bumpeeztoys:
products.json exposes a $14.99 battery and two $9.99 remotes; the index says max $379.99, avg $150.27).

Usage:
  python3 scripts/sl_slice_from_csv.py <universe.csv> <out_slug> "<TopCategory>" [visit_lo=1000] [visit_hi=10000]
  Writes  logs/storeleads/<out_slug>_full.json  (relative slug, like sl_select_build).
"""
import csv, sys, json, os, re
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


BAD_PARSE = []


def money(s):
    """'USD $1,109.00' -> 1109.0 · 'CHF 21.21 CHF' -> 21.21 · '' -> None.

    Reads the FIRST number in the string. Thousands separators are commas in this export (verified on
    200k rows: 'USD $1,109.00', 'USD $3,600.00'); no European 1.109,00 form seen. Naive "strip everything
    that isn't a digit/dot/comma" breaks on 'AED 420.34 .د.إ' — the Arabic dirham symbol contributes a
    second dot (93 such values in the Toys & Hobbies slice). Anything unparsed is recorded in BAD_PARSE
    and reported at the end — a parse failure must be LOUD, never a silent None (that is the exact bug
    this function replaces).
    """
    if s in ("", None):
        return None
    m = re.search(r"[0-9][0-9,]*(?:\.[0-9]+)?", str(s))
    if not m:
        BAD_PARSE.append(s)
        return None
    try:
        return float(m.group(0).replace(",", ""))
    except ValueError:
        BAD_PARSE.append(s)
        return None


with open(csv_path, newline="", encoding="utf-8", errors="replace") as f:
    r = csv.reader(f)
    h = next(r)
    ix = {name: h.index(name) for name in (
        "domain", "estimated_monthly_visits", "merchant_name", "estimated_yearly_sales",
        "average_product_price", "average_product_price_usd", "minimum_product_price",
        "maximum_product_price", "currency",
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

        avg_usd = money(row[ix["average_product_price_usd"]])
        avg_nat = money(row[ix["average_product_price"]])
        mn_nat = money(row[ix["minimum_product_price"]])
        mx_nat = money(row[ix["maximum_product_price"]])
        # the store's OWN implied rate — no hard-coded table needed, and it stays right even if our
        # rate table drifts. min/max come in the NATIVE currency; avg comes in both.
        rate = (avg_usd / avg_nat) if (avg_usd and avg_nat) else 1.0
        cur = g("currency")
        if cur in ("XXX",):        # Store Leads' "unknown currency" marker — treat as absent
            cur = None

        out.append({
            "domain": g("domain"), "visits": v, "merchant": g("merchant_name"),
            "sales": money(row[ix["estimated_yearly_sales"]]),
            "currency": cur,
            "avg_price": avg_usd,                                   # USD (was silently None before S20)
            "avg_price_native": avg_nat,
            "min_price": round(mn_nat * rate, 2) if mn_nat is not None else None,   # USD
            "max_price": round(mx_nat * rate, 2) if mx_nat is not None else None,   # USD
            "min_price_native": mn_nat, "max_price_native": mx_nat,
            "products": to_int(row[ix["products_sold"]]),
            "created": g("created"), "country": g("country_code"),
            "avg_weight": money(row[ix["average_product_weight"]]),
            "variants": to_int(row[ix["product_variants"]]),
            "comb_reviews": to_int(row[ix["combined_reviews"]]),
            "tp_reviews": to_int(row[ix["trustpilot_reviews"]]),
            "fb": g("facebook"), "ig": g("instagram"), "tiktok": g("tiktok"),
            "pinterest": g("pinterest"), "theme": g("theme")})
        if n % 500000 == 0:
            print(f"  ...scanned {n:,}, matched {matched:,}", flush=True)

json.dump(out, open(out_path, "w"), ensure_ascii=False)
print(f"SLICE: category='{category}' visits[{lo},{hi}) -> matched {matched:,} stores")

# --- LOUD self-report: which fields actually arrived (the S20 lesson: a dead field has no symptom) ---
def filled(k):
    c = sum(1 for r in out if r.get(k) is not None)
    return f"{k}={c}/{len(out)} ({round(100*c/max(len(out),1))}%)"
print("  FIELDS: " + " · ".join(filled(k) for k in
      ("currency", "avg_price", "min_price", "max_price", "sales", "products", "visits")))
if BAD_PARSE:
    print(f"  ⚠ money() could not parse {len(BAD_PARSE)} values, e.g. {BAD_PARSE[:5]}")
else:
    print("  money(): 0 unparsed values")
print(f"written: {out_path}")
print("DONE")
