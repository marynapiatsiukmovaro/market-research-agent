#!/usr/bin/env python3
# Re-run audit: (1) scraper data-quality check, (2) SH-style conservative cut (drop only definite-noise),
# (3) print the FULL survivor candidate sheet so the main agent reads ALL of them (no gut top-N).
import json,sys
from collections import Counter
OUT="/opt/market-research-agent/logs/storeleads"
d=json.load(open(f"{OUT}/hi_band_200_enriched.json"))
reach=[r for r in d if r.get("reachable")]
def money(s):
    import re
    if s in (None,""): return None
    t=re.sub(r"[^0-9.]","",str(s).replace(",",""))
    try: return float(t)
    except: return None
print(f"=== DATA QUALITY (of {len(d)} stores, {len(reach)} reachable) ===")
print("hero_src:", dict(Counter(r.get("hero_src") for r in reach)))
print("no candidate (DROP):", sum(1 for r in reach if not r.get("candidate")))
print("empty/short desc (<25 chars):", sum(1 for r in reach if len((r.get("desc") or ""))<25))
print("no price:", sum(1 for r in reach if not r.get("price")))
print("kind dist:", dict(Counter(r.get("kind") for r in reach if r.get("candidate"))))

# conservative cut
NOISE_KINDS={"ingestible","skincare","apparel"}
keep=[]; cut=Counter()
for r in reach:
    if not r.get("candidate"): cut["no-hero/DROP"]+=1; continue
    if r.get("pust"): cut["пустышка"]+=1; continue
    if r.get("kind") in NOISE_KINDS: cut[r["kind"]]+=1; continue
    if len((r.get("desc") or ""))<15: cut["no-desc(verify)"]+=1; continue
    keep.append(r)
print(f"\n=== CONSERVATIVE CUT: {len(reach)} reachable -> drop {dict(cut)} -> KEEP {len(keep)} survivors ===")
inr=sum(1 for r in keep if r.get("in_range")); print(f"survivors in $39-170: {inr} | price-out (kept, other top may fit): {len(keep)-inr}")

keep.sort(key=lambda r:(money(r.get("sl_rev")) or 0),reverse=True)
print(f"\n=== ALL {len(keep)} SURVIVORS (read every one) — domain | hero $price | rev | pc | src | desc ===")
for i,r in enumerate(keep,1):
    p=r.get("price"); pr=f"${p:.0f}" if p else "$?"
    oo="" if r.get("in_range") else "!"
    print(f"{i:>3} {str(r['domain'])[:30]:30} {str(r.get('candidate'))[:30]:30} {pr:>6}{oo} {str(r.get('sl_rev'))[:9]:>9} pc{str(r.get('sl_pc')):>4} {str(r.get('hero_src'))[:11]:11} | {(r.get('desc') or '')[:66]}")
print("=== AUDIT/CUT DONE ===")
