#!/usr/bin/env python3
"""Store Leads — record a BUILT chunk's domains in enriched_index.json (S11, Marina-approved 2026-06-07).

enriched != processed (RULE 30). The reservoir-BUILD marks a store `enriched` here (card built, ready for
analysis); ONLY the analysis session marks `processed`. Keeping them in SEPARATE indexes is what lets a
parallel analysis session consume built chunks (even of the niche being built) WITHOUT shifting the build's
selection page — `sl_select_build.py` excludes processed ∪ enriched, so a store moving from enriched→processed
is a no-op for the remaining build pool. (Fixes the SKIP-paging coverage-gap risk under parallel analysis.)

Usage:  sl_mark_enriched.py <enriched_or_selected.json> <niche> [chunk_label]
"""
import json, sys, os, datetime
OUT = "/opt/market-research-agent/logs/storeleads"
IDX = OUT + "/enriched_index.json"


def norm(d):
    d = str(d).strip().lower()
    for p in ("http://", "https://"):
        if d.startswith(p):
            d = d[len(p):]
    d = d.split("/")[0].split("?")[0]
    if d.startswith("www."):
        d = d[4:]
    return d.rstrip(".")


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: sl_mark_enriched.py <enriched_or_selected.json> <niche> [chunk_label]")
    path = sys.argv[1]
    niche = sys.argv[2]
    chunk = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(path).replace("_enriched.json", "").replace(".json", "")
    sel = path.replace("_enriched.json", ".json")            # built == selected (count-reconciled)
    if not os.path.exists(sel):
        sys.exit(f"selected file not found: {sel}")
    rows = json.load(open(sel))
    idx = json.load(open(IDX)) if os.path.exists(IDX) else {}
    today = datetime.date.today().isoformat()
    added = 0
    for r in rows:
        dom = norm(r.get("name") or r.get("domain") or "")
        if dom and dom not in idx:
            idx[dom] = {"niche": niche, "chunk": chunk, "date": today}
            added += 1
    json.dump(idx, open(IDX, "w"), ensure_ascii=False)
    print(f"enriched_index: +{added} new (chunk {chunk}, niche {niche}) | total {len(idx)}")


if __name__ == "__main__":
    main()
