#!/usr/bin/env python3
"""sl_stage2_table.py — render a Stage-2 enriched JSON (sl_enrich3 v3) to an HTML table.
Stage artifact for Marina's Desktop. One row per store, ordered by tier then proxy score.
Shows the v3 early signals (hero/desc confidence, maturity, storefront_pos, conv) + the
top-3 product candidates each with USD price + in_range. Proxy tier/score = a SORT-AID, not
quality (op-rule RULE 6) — the banner says so.
Usage: python3 sl_stage2_table.py <enriched.json> <output.html> "<title>" "<funnel banner>"
"""
import json, html, sys
from collections import Counter

inp, outp, title = sys.argv[1], sys.argv[2], sys.argv[3]
banner = sys.argv[4] if len(sys.argv) > 4 else ""
rows = json.load(open(inp))
order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3, "MANUAL": 4, "DROP-noPhysical": 5}
rows.sort(key=lambda r: (order.get(r.get("tier"), 9), -(r.get("score") or 0)))

def link(u, txt):
    if not u: return ""
    u = str(u)
    if not u.startswith("http"): u = "https://" + u
    return f"<a href='{html.escape(u)}'>{txt}</a>"

def tops_cell(r):
    out = []
    dom = r.get("domain") or ""
    for t in (r.get("tops3") or [])[:3]:
        pr = t.get("price"); cur = t.get("cur") or ""
        flag = "✓" if t.get("in_range") else ("?" if t.get("price_unknown") else "✗")
        dc = t.get("desc_confidence", "")
        desc = html.escape(str(t.get("desc") or ""))[:120]
        purl = (f"https://{dom}/products/{t.get('handle')}" if t.get("handle") else f"https://{dom}")
        thumb = (f"<a href='{html.escape(purl)}'><img src='{html.escape(str(t.get('img')))}' style='float:left;margin:0 6px 2px 0'></a>"
                 if t.get("img") else "")
        link = f"<a href='{html.escape(purl)}'>↗ product</a>"
        out.append(f"<div style='margin-bottom:6px;overflow:hidden'>{thumb}<b>${pr} {cur}</b> {flag} "
                   f"<span style='color:#888'>[{dc}]</span> {link}<br>{desc}</div>")
    return "".join(out) or "<i>—</i>"

tiers = Counter(r.get("tier") for r in rows)
h = ['<html><head><meta charset="utf-8"><style>'
     'body{font:12px/1.45 -apple-system,Arial;margin:20px;color:#1a1a1a}h1{font-size:18px}'
     '.banner{background:#fff4e6;border:1px solid #f0c890;padding:8px 12px;border-radius:6px;margin:8px 0;font-size:13px}'
     'table{border-collapse:collapse;font-size:11px}td,th{border:1px solid #ccc;padding:4px 6px;vertical-align:top}'
     'th{background:#f4f4f4}tr.A{background:#f3fff3}tr.B{background:#fbfff8}tr.PRICE-CHECK{background:#fff8e6}'
     'tr.MANUAL,tr.DROP-noPhysical{background:#fff0f0}a{color:#1763d6;text-decoration:none}'
     '.lo{color:#c00}.hi{color:#080}.est{background:#eef;padding:1px 3px}img{max-width:60px;max-height:60px}</style></head><body>']
h.append(f"<h1>{html.escape(title)}</h1>")
h.append(f"<div class=banner><b>⚠ Proxy tier/score = SORT-AID, NOT quality (RULE 6).</b> "
         f"Stage 3 = читаю ВСЕ, подтверждаю hero+цену на живом сайте, 100-pt+Veto. Tiers: {html.escape(str(dict(tiers)))}</div>")
if banner:
    h.append(f"<div class=banner style='background:#eef4ff;border-color:#b9d0f5'><b>Funnel (RULE 1):</b> {html.escape(banner)}</div>")
cols = ["#","domain","tier","score","country","created","visits","maturity","conv","heroConf","descConf","pos","price USD","in_range","top-3 candidates (photo · price · desc)","social"]
h.append("<table><tr>" + "".join(f"<th>{html.escape(c)}</th>" for c in cols) + "</tr>")
for i, r in enumerate(rows, 1):
    dom = r.get("domain") or ""
    hc = r.get("hero_confidence", ""); dc = r.get("desc_confidence", "")
    hc_s = f"<span class={'hi' if hc=='high' else 'lo'}>{hc}</span>"
    social = " ".join(filter(None, [link(r.get("fb"), "FB"), link(r.get("ig"), "IG"),
                                     link(r.get("tiktok"), "TT"), link(r.get("pinterest"), "Pin")]))
    vis = f"{r.get('visits'):,}" if isinstance(r.get("visits"), int) else html.escape(str(r.get("visits") or ""))
    cells = [str(i), link(dom, html.escape(dom)), r.get("tier",""), str(r.get("score","")),
             html.escape(str(r.get("country") or "")), html.escape(str(r.get("created") or "")[:10]), vis,
             html.escape(str(r.get("maturity") or "")), str(r.get("conv_batch") or ""),
             hc_s, html.escape(str(dc)), html.escape(str(r.get("storefront_pos") or "")),
             html.escape(str(r.get("price") or "")) + (f" <span class=est>{html.escape(str(r.get('store_currency') or ''))}</span>" if r.get("store_currency") else ""),
             ("✓" if r.get("in_range") else "✗"), tops_cell(r), social]
    h.append(f"<tr class='{r.get('tier','')}'>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
h.append("</table></body></html>")
open(outp, "w").write("\n".join(h))
print("HTML written:", outp, "rows:", len(rows), "tiers:", dict(tiers))
