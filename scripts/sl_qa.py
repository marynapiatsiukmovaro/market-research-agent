#!/usr/bin/env python3
"""sl_qa.py — Stage-2 ACCEPTANCE GATE (the gate of record, Store Leads).

Audits an enriched JSON (sl_enrich4 v4.2) for CARD COMPLETENESS before any analysis.
Extended S6 (2026-06-03) to close the S5 hole: the old gate only checked reach/price/cur and
would PASS a card missing essence fields / images / 2-of-3 products. Now it verifies the FULL
contract: 3-tops coverage, per-product image+in_range+descConf, and the 5 essence fields
(store_type, product_class, cat_flag, maturity, new_products_30d) the S3 table silently dropped.

PASS thresholds (Marina-approved S6). Run BEFORE analysis; STOP if any FLAG.
Usage: python3 sl_qa.py <enriched.json> [<enriched2.json> ...]
"""
import json, sys

def pct(a, b): return round(100 * a / b, 1) if b else 0.0
def filled(v): return v not in (None, "", [], {}, "None")

# ---- PASS thresholds (Marina-approved S6 2026-06-03) ----
TH = dict(reach=90, cand=95, price=95, ge1top=97, prod_img=90, prod_inrange=99,
          prod_descconf=99, store_type=95, product_class=95, cat_flag=95, maturity=95,
          new30d=95, home_pitch=90, avgtops=2.0, empty_tops_reach_max=5)

def audit(path):
    d = json.load(open(path))
    n = len(d)
    reach = [r for r in d if r.get("reachable")]
    nr = len(reach)
    cand = sum(1 for r in d if r.get("candidate"))
    withprice = sum(1 for r in d if isinstance(r.get("price"), (int, float)) and r.get("price") > 0)
    curnull = sum(1 for r in d if (isinstance(r.get("price"), (int, float)) and r.get("price") > 0) and not r.get("currency"))
    avgtops = round(sum(len(r.get("tops3") or []) for r in reach) / nr, 2) if nr else 0
    ge1 = sum(1 for r in reach if (r.get("tops3") or []))
    tops3 = sum(1 for r in reach if len(r.get("tops3") or []) == 3)
    empty_tops_reach = nr - ge1
    allp = [p for r in reach for p in (r.get("tops3") or [])]
    npx = len(allp)
    prod_img = sum(1 for p in allp if filled(p.get("img")))
    prod_inrange = sum(1 for p in allp if "in_range" in p)
    prod_descconf = sum(1 for p in allp if filled(p.get("desc_confidence")))
    ess = {k: sum(1 for r in d if (("new_products_30d" in r) if k == "new30d" else filled(r.get(k))))
           for k in ("store_type", "product_class", "cat_flag", "maturity", "new30d")}
    home_pitch = sum(1 for r in d if filled(r.get("home_pitch")))
    social = sum(1 for r in d if any(filled(r.get(s)) for s in ("fb", "ig", "tiktok", "pinterest")))
    home_img = sum(1 for r in d if filled(r.get("home_img")))

    M = dict(reach=pct(nr, n), cand=pct(cand, n), price=pct(withprice, max(cand, 1)),
             ge1top=pct(ge1, nr), prod_img=pct(prod_img, npx), prod_inrange=pct(prod_inrange, npx),
             prod_descconf=pct(prod_descconf, npx), store_type=pct(ess["store_type"], n),
             product_class=pct(ess["product_class"], n), cat_flag=pct(ess["cat_flag"], n),
             maturity=pct(ess["maturity"], n), new30d=pct(ess["new30d"], n),
             home_pitch=pct(home_pitch, n), avgtops=avgtops,
             empty_tops_reach=pct(empty_tops_reach, nr))
    name = path.split("/")[-1]
    print("=" * 78)
    print(f"{name}  (n={n}, reachable={nr})")
    print(f"  reach {M['reach']}% · cand {M['cand']}% · price {M['price']}% · cur_null {curnull} · avgtops {avgtops}")
    print(f"  PRODUCTS (n={npx}): >=1top {M['ge1top']}% · 3tops {pct(tops3,nr)}%(info) · img {M['prod_img']}% · in_range {M['prod_inrange']}% · descConf {M['prod_descconf']}%")
    print(f"  ESSENCE: store_type {M['store_type']}% · product_class {M['product_class']}% · cat_flag {M['cat_flag']}% · maturity {M['maturity']}% · new30d {M['new30d']}%")
    print(f"  CONTEXT: home_pitch {M['home_pitch']}% · social {pct(social,n)}%(info) · home_img/banner {pct(home_img,n)}%(info) · empty_tops_reach {M['empty_tops_reach']}%")

    flags = []
    if M["reach"] < TH["reach"]: flags.append(f"reach<{TH['reach']}")
    if M["cand"] < TH["cand"]: flags.append(f"cand<{TH['cand']}")
    if M["price"] < TH["price"]: flags.append(f"price<{TH['price']}")
    if curnull > 0: flags.append(f"cur_null={curnull}")
    if M["avgtops"] < TH["avgtops"]: flags.append(f"avgtops<{TH['avgtops']}")
    if M["ge1top"] < TH["ge1top"]: flags.append(f"ge1top<{TH['ge1top']}")
    if M["prod_img"] < TH["prod_img"]: flags.append(f"prod_img<{TH['prod_img']}")
    if M["prod_inrange"] < TH["prod_inrange"]: flags.append(f"prod_inrange<{TH['prod_inrange']}")
    if M["prod_descconf"] < TH["prod_descconf"]: flags.append(f"prod_descconf<{TH['prod_descconf']}")
    for k in ("store_type", "product_class", "cat_flag", "maturity", "new30d"):
        if M[k] < TH[k]: flags.append(f"{k}<{TH[k]}")
    if M["home_pitch"] < TH["home_pitch"]: flags.append(f"home_pitch<{TH['home_pitch']}")
    if M["empty_tops_reach"] > TH["empty_tops_reach_max"]: flags.append(f"empty_tops>{TH['empty_tops_reach_max']}")
    print("  GATE:", "✅ PASS — full card, safe to analyse" if not flags else "⛔ STOP -> " + ", ".join(flags))
    return not flags

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: sl_qa.py <enriched.json> [...]"); sys.exit(2)
    allok = all(audit(p) for p in sys.argv[1:])
    sys.exit(0 if allok else 1)
