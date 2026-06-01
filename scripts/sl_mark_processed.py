#!/usr/bin/env python3
"""sl_mark_processed.py — write the MASTER store record (RULE 19 + S3 extension).
Marks every store in an enriched batch as processed AND carries the analysis data forward
(Marina S3: "переносить данные из таблиц анализа — нам это ничего не стоит"). Single source of
truth on the VPS that sl_select excludes from future batches, AND a permanent queryable re
record (hero / price / class / store_type / score / monitor-flag).

Schema per domain (extends the old {subcat,band,date,stage,outcome}):
  {subcat, band, date, stage, outcome, tier, product_class, store_type, hero, price, score,
   maturity, new_products_30d, fb, ig, tiktok, pinterest, monitor}
- outcome default = "screened"; bump to "reported" for 65+ AFTER Marina's OK.
- monitor default = False; set True for strong/borderline stores to feed the keep-list (newest-first monitor).

Usage: python3 sl_mark_processed.py <enriched.json> <subcat> <band> <date YYYY-MM-DD> [--monitor-min SCORE]
       (score here = enricher proxy score; the main agent overwrites final 100-pt score + outcome at checkpoint)
"""
import json, sys, os
ENR, SUBCAT, BAND, DATE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
MON_MIN = None
if "--monitor-min" in sys.argv:
    MON_MIN = int(sys.argv[sys.argv.index("--monitor-min") + 1])
PROC = "/opt/market-research-agent/logs/storeleads/processed_domains.json"

rows = json.load(open(ENR))
proc = json.load(open(PROC)) if os.path.exists(PROC) else {}
added = 0
for r in rows:
    dom = r.get("domain")
    if not dom:
        continue
    rec = {
        "subcat": SUBCAT, "band": BAND, "date": DATE,
        "stage": "stage2-enriched", "outcome": "screened",
        "tier": r.get("tier"), "product_class": r.get("product_class"),
        "store_type": r.get("store_type"), "hero": r.get("candidate"),
        "price": r.get("price"), "score": r.get("score"),
        "maturity": r.get("maturity"), "new_products_30d": r.get("new_products_30d"),
        "fb": r.get("fb"), "ig": r.get("ig"), "tiktok": r.get("tiktok"), "pinterest": r.get("pinterest"),
        "monitor": bool(MON_MIN is not None and (r.get("score") or 0) >= MON_MIN
                        and r.get("tier") in ("A", "B")),
    }
    # never downgrade an existing richer record silently; merge (keep prior outcome=reported / monitor=True)
    prev = proc.get(dom, {})
    if prev.get("outcome") == "reported": rec["outcome"] = "reported"
    if prev.get("monitor"): rec["monitor"] = True
    proc[dom] = rec
    added += 1
json.dump(proc, open(PROC, "w"), ensure_ascii=False, indent=0)
mon = sum(1 for v in proc.values() if v.get("monitor"))
print("marked %d stores | total processed now=%d | monitor-flagged total=%d" % (added, len(proc), mon))
