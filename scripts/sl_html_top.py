#!/usr/bin/env python3
"""Write a light top-N HTML from a saved *_full.json. Usage: sl_html_top.py <slug> <N> "<title>" """
import json, sys, html
OUT="/opt/market-research-agent/logs/storeleads"
SLUG=sys.argv[1]; N=int(sys.argv[2]); TITLE=sys.argv[3] if len(sys.argv)>3 else SLUG
rows=json.load(open(f"{OUT}/{SLUG}_full.json"))
import os
_pp=f"{OUT}/processed_domains.json"
PROC=set(json.load(open(_pp)).keys()) if os.path.exists(_pp) else set()
rows=rows[:N]
def fnum(v):
    try: return f"{int(v):,}"
    except: return "" if v in (None,"") else html.escape(str(v))
def lk(u,l): return f'<a href="{html.escape(u)}" target="_blank">{l}</a>' if u else ""
def socx(r):
    return " ".join(lk(u,l) for u,l in [(r["fb"],"FB"),(r["ig"],"IG"),(r["tiktok"],"TT"),(r["pinterest"],"Pin")] if u)
hdr=["#","✓","Domain","Merchant","Cn","Created","Est Visits","Est PViews","Est Sales/mo","Avg $","Min $","Max $",
     "Avg Wt","Prods","Vars","AppSpend","Rank","Theme","Last Theme","Reviews","TP","Social","Meta"]
trs=[]
for i,r in enumerate(rows,1):
    dom=r["domain"] or ""; durl="https://"+dom if dom and not str(dom).startswith("http") else dom
    cells=[str(i),("✓" if dom in PROC else ""),lk(durl,html.escape(str(dom))),html.escape(str(r["merchant"] or "")),html.escape(str(r["country"] or "")),
      r["created"] or "",fnum(r["visits"]),fnum(r["pageviews"]),html.escape(str(r["sales"] or "")),
      html.escape(str(r["avg_price"] or "")),html.escape(str(r["min_price"] or "")),html.escape(str(r["max_price"] or "")),
      html.escape(str(r["avg_weight"] or "")),fnum(r["products"]),fnum(r["variants"]),html.escape(str(r["app_spend"] or "")),
      fnum(r["rank"]),html.escape(str(r["theme"] or "")),html.escape(str(r["last_theme"] or "")),
      fnum(r["comb_reviews"]),fnum(r["tp_reviews"]),socx(r),html.escape(str(r["meta_desc"] or "")[:140])]
    trs.append("<tr>"+"".join(f"<td>{c}</td>" for c in cells)+"</tr>")
doc=f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(TITLE)} top {N}</title>
<style>body{{font-family:-apple-system,Segoe UI,Arial,sans-serif;margin:18px}}
h1{{font-size:18px;margin:0 0 4px}}.sub{{color:#666;font-size:13px;margin-bottom:14px}}
table{{border-collapse:collapse;font-size:12px;width:100%}}
th,td{{border:1px solid #e3e3e3;padding:4px 7px;text-align:left;white-space:nowrap;max-width:340px;overflow:hidden;text-overflow:ellipsis}}
th{{background:#1f6feb;color:#fff;position:sticky;top:0}}tr:nth-child(even){{background:#f7f9fc}}
td:nth-child(6),td:nth-child(7){{text-align:right}}a{{color:#1f6feb;text-decoration:none}}a:hover{{text-decoration:underline}}</style></head><body>
<h1>{html.escape(TITLE)} — top {N} by Est Visits</h1>
<div class="sub">Shopify · Active · Created ≥ 2020 · полная выгрузка = 27,052 (это лёгкое превью топ-{N})</div>
<table><thead><tr>{"".join(f"<th>{h}</th>" for h in hdr)}</tr></thead><tbody>{"".join(trs)}</tbody></table></body></html>"""
open(f"{OUT}/{SLUG}_top{N}.html","w").write(doc)
print(f"saved {SLUG}_top{N}.html ({len(rows)} rows)")
