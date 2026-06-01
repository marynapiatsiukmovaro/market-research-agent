#!/usr/bin/env python3
"""sl_stage1_table.py — render a Stage-1 selection JSON (sl_select output) to an HTML table.
Reusable stage artifact for Marina's Desktop. Shows the dump-level fields per selected store,
sorted by Est Visits, with clickable domain + social links + a funnel-transparency banner (RULE 1).
Usage: python3 sl_stage1_table.py <input.json> <output.html> "<title>" "<funnel banner line>"
"""
import json, html, sys

inp, outp, title = sys.argv[1], sys.argv[2], sys.argv[3]
banner = sys.argv[4] if len(sys.argv) > 4 else ""
rows = json.load(open(inp))
rows.sort(key=lambda r: (r.get("visits") or 0), reverse=True)

def link(u, txt):
    if not u: return ""
    u = str(u)
    if not u.startswith("http"): u = "https://" + u
    return f"<a href='{html.escape(u)}'>{txt}</a>"

cols = [("#",""),("domain","name"),("merchant","merch"),("country","country"),("created","created"),
        ("visits","visits"),("est $/mo","erf"),("avg $","apf"),("min $","min_price"),("max $","max_price"),
        ("weight","avg_weight"),("pc","pc"),("var","variants"),("reviews","comb_reviews"),
        ("theme","theme"),("social","")]

h = ['<html><head><meta charset="utf-8"><style>'
     'body{font:12px/1.45 -apple-system,Arial;margin:20px;color:#1a1a1a}'
     'h1{font-size:18px}.banner{background:#eef4ff;border:1px solid #b9d0f5;padding:8px 12px;border-radius:6px;margin:8px 0;font-size:13px}'
     'table{border-collapse:collapse;font-size:11px}td,th{border:1px solid #ccc;padding:3px 6px}th{background:#f4f4f4;position:sticky;top:0}'
     'tr:nth-child(even){background:#fafafa}a{color:#1763d6;text-decoration:none}.hero{background:#f3fff3}</style></head><body>']
h.append(f"<h1>{html.escape(title)}</h1>")
if banner:
    h.append(f"<div class=banner><b>Funnel (RULE 1):</b> {html.escape(banner)}</div>")
h.append(f"<p style='color:#666'>{len(rows)} stores · sorted by Est Visits desc</p>")
h.append("<table><tr>" + "".join(f"<th>{html.escape(c[0])}</th>" for c in cols) + "</tr>")
for i, r in enumerate(rows, 1):
    pc = r.get("pc") or 0
    cls = " class=hero" if pc and pc <= 300 else ""
    social = " ".join(filter(None, [link(r.get("fb"), "FB"), link(r.get("ig"), "IG"),
                                     link(r.get("tiktok"), "TT"), link(r.get("pinterest"), "Pin")]))
    cells = [str(i), link(r.get("name"), html.escape(str(r.get("name")))), html.escape(str(r.get("merch") or "")),
             html.escape(str(r.get("country") or "")), html.escape(str(r.get("created") or "")[:10]),
             f"{r.get('visits'):,}" if r.get("visits") else "",
             html.escape(str(r.get("erf") or "")), html.escape(str(r.get("apf") or "")),
             html.escape(str(r.get("min_price") or "")), html.escape(str(r.get("max_price") or "")),
             html.escape(str(r.get("avg_weight") or "")), str(pc), html.escape(str(r.get("variants") or "")),
             html.escape(str(r.get("comb_reviews") or "")), html.escape(str(r.get("theme") or "")[:24]), social]
    h.append(f"<tr{cls}>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
h.append("</table></body></html>")
open(outp, "w").write("\n".join(h))
print("HTML written:", outp, "rows:", len(rows))
