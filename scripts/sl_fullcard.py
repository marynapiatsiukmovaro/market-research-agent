#!/usr/bin/env python3
"""sl_fullcard.py — COMPLETE text card reader for in-context analysis (RULE 6/25 — full card, NEVER 1-of-3).
Shows every store with ALL 3 top products (name + price + in_range + image-present + descConf + desc),
the store essence (store_type / product_class), home_pitch, and the needs_live flag + reason. Companion to
the canonical HTML (sl_stage2_table.py); this is the text view the agent reads so nothing is silently dropped.
Usage: python3 sl_fullcard.py <enriched.json>
"""
import json, sys

def t(s, n): return (str(s if s is not None else "")).replace("\n", " ").strip()[:n]

d = json.load(open(sys.argv[1]))
ds = sorted(d, key=lambda r: -(r.get("score") or 0))  # score = SORT-AID only; read ALL
print(f"=== {sys.argv[1].split('/')[-1]} — {len(d)} stores (FULL CARD, score-desc sort-aid; READ ALL RULE 6) ===")
for i, r in enumerate(ds):
    nl = " NEEDS_LIVE[" + ",".join(r.get("needs_live_why") or []) + "]" if r.get("needs_live") else ""
    unr = "" if r.get("reachable") else " !UNREACHABLE"
    print(f"\n{i} | {r.get('domain')} | v{r.get('visits')} | {r.get('tier')}/{r.get('score')} | {t(r.get('store_type'),12)}/{t(r.get('product_class'),14)}{nl}{unr}")
    pit = t(r.get("home_pitch"), 95)
    if pit: print(f"   pitch: {pit}")
    for j, p in enumerate(r.get("tops3") or []):
        pr = p.get("price")
        prs = f"${pr:.0f}" if isinstance(pr, (int, float)) else str(pr)
        ir = "IR" if p.get("in_range") else "oor"
        img = "img" if p.get("img") else "NOIMG"
        print(f"   {j+1}. {t(p.get('t'),50)} {prs}{p.get('cur','')} [{ir}|{img}|{p.get('desc_confidence','?')}] {t(p.get('desc'),75)}")
