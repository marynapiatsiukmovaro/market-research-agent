#!/usr/bin/env python3
"""Select a band/batch from a *_full.json for Stage-2 enrichment.
Filter: visits in [VLO,VHI], revenue<=REVMAX, avg_price<=PMAX, exclude catalog-giants (pc>PCMAX).
Sort by visits desc, take N. Output in sl_enrich2 input format (name/merch/erf/apf/pc/created).
Usage: sl_select.py <full_json_slug> <out_slug> [VLO VHI N]"""
import json, re, sys
OUT="/opt/market-research-agent/logs/storeleads"
SLUG=sys.argv[1]; OUTSLUG=sys.argv[2]
VLO=int(sys.argv[3]) if len(sys.argv)>3 else 1000
VHI=int(sys.argv[4]) if len(sys.argv)>4 else 50000
N=int(sys.argv[5]) if len(sys.argv)>5 else 200
REVMAX=1_000_000; PMAX=350.0; PCMAX=2000
def money(s):
    if s in (None,""): return None
    t=re.sub(r"[^0-9.,]","",str(s)).replace(",","")  # drop currency/letters + thousands commas
    if not t: return None
    parts=t.split(".")
    if len(parts)>2: t="".join(parts[:-1])+"."+parts[-1]  # multi-dot: keep last as decimal
    try: return float(t)
    except: return None
rows=json.load(open(f"{OUT}/{SLUG}_full.json"))
import os
PROC_PATH=f"{OUT}/processed_domains.json"
processed=set(json.load(open(PROC_PATH)).keys()) if os.path.exists(PROC_PATH) else set()
band=[]; drop_vis=drop_rev=drop_price=drop_pc=drop_proc=0
for r in rows:
    if r.get("domain") in processed: drop_proc+=1; continue   # already analysed in a prior session — never re-surface
    v=r.get("visits")
    if v is None or not (VLO<=v<=VHI): drop_vis+=1; continue
    rev=money(r.get("sales"))
    if rev is not None and rev>REVMAX: drop_rev+=1; continue
    pr=money(r.get("avg_price"))
    if pr is not None and pr>PMAX: drop_price+=1; continue
    pc=r.get("products")
    if pc and pc>PCMAX: drop_pc+=1; continue
    band.append(r)
band.sort(key=lambda x:(x["visits"] or 0),reverse=True)
sel=band[:N]
def conv(r):
    return {"name":r["domain"],"merch":r.get("merchant"),"erf":r.get("sales"),"apf":r.get("avg_price"),
            "pc":r.get("products"),"created":r.get("created"),"fbpx":None,
            "visits":r.get("visits"),"country":r.get("country"),"min_price":r.get("min_price"),
            "max_price":r.get("max_price"),"avg_weight":r.get("avg_weight"),"variants":r.get("variants"),
            "comb_reviews":r.get("comb_reviews"),"tp_reviews":r.get("tp_reviews"),
            "fb":r.get("fb"),"ig":r.get("ig"),"tiktok":r.get("tiktok"),"pinterest":r.get("pinterest"),
            "theme":r.get("theme")}
json.dump([conv(r) for r in sel],open(f"{OUT}/{OUTSLUG}.json","w"),ensure_ascii=False)
print(f"total rows={len(rows)} | qualified in band={len(band)} | selected={len(sel)}")
print(f"dropped: already-processed={drop_proc} out-of-visit-band={drop_vis} rev>{REVMAX}={drop_rev} price>{PMAX}={drop_price} pc>{PCMAX}={drop_pc}")
if sel:
    vs=[r["visits"] for r in sel]
    print(f"selected visits range: {min(vs):,}..{max(vs):,}")
    pcs=[r.get("products") or 0 for r in sel]
    hero=sum(1 for p in pcs if p<=300); mid=sum(1 for p in pcs if 300<p<=2000)
    print(f"product-count mix in selection: hero(<=300)={hero} mid(301-2000)={mid}")
    print("\nsample (top 12 by visits):")
    for r in sel[:12]:
        print(f"  {str(r['domain'])[:30]:30} vis={r['visits']:>6} pc={str(r.get('products')):>5} price={r.get('avg_price')} created={r.get('created')}")
print("=== SELECT DONE ===")
