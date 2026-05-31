#!/usr/bin/env python3
"""Render a funnel-stage JSON as an HTML table → screenshot PNG (so Marina can SEE the fields/interface).
Usage: sl_table_shot.py <mode> <in_json> <out_png> ["Title"] [rows]
  mode = select | enrich
No proxy needed (renders a local file:// page). Keeps the scraper proxy untouched.
"""
import json, sys, html, re
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/storeleads"
MODE, INF, PNG = sys.argv[1], sys.argv[2], sys.argv[3]
TITLE = sys.argv[4] if len(sys.argv) > 4 else MODE
MAXROWS = int(sys.argv[5]) if len(sys.argv) > 5 else 60

rows = json.load(open(INF if INF.startswith("/") else f"{OUT}/{INF}"))

if MODE == "select":   # Stage 1 — candidate table (from sl_select output)
    cols = [("name","Domain"),("country","Cy"),("visits","Visits/mo"),("erf","Est$/mo"),
            ("apf","AvgPx"),("min_price","Min"),("max_price","Max"),("pc","#Prod"),
            ("variants","Var"),("created","Created"),("comb_reviews","Rev#")]
elif MODE == "enrich":  # Stage 2 — enriched candidate sheet (from sl_enrich3 output)
    cols = [("domain","Domain"),("maturity","Maturity"),("hero_src","Src"),("hero_confidence","HConf"),
            ("tier","Tier"),("candidate","Candidate (hero of top-3)"),("price","$USD"),("currency","Cur"),
            ("in_range","InRng"),("desc_confidence","DescConf"),("conv_batch","Conv"),("storefront_pos","Pos"),
            ("flags","Flags")]
else:
    print("mode must be select|enrich"); sys.exit(1)

def fmt(r, k):
    v = r.get(k)
    if v is None: return ""
    if isinstance(v, list): v = ", ".join(str(x) for x in v)
    s = html.escape(str(v))
    if k in ("name", "domain"):
        return f'<a href="https://{s}" target="_blank">{s}</a>'
    if k == "candidate": return s[:46]
    return s

def rowclass(r):
    t = r.get("tier", "")
    if t == "A": return "ta"
    if t == "B": return "tb"
    if t == "MANUAL": return "tm"
    if str(t).startswith("DROP"): return "td"
    return ""

shown = rows[:MAXROWS]
css = """body{font:12px -apple-system,system-ui,sans-serif;margin:18px;color:#222}
h3{margin:0 0 10px}table{border-collapse:collapse;width:100%}
th,td{border:1px solid #ddd;padding:4px 8px;text-align:left;vertical-align:top}
th{background:#2b3a4a;color:#fff;position:sticky;top:0}
tr:nth-child(even){background:#fafafa}a{color:#0a6;text-decoration:none}
.ta{background:#e7f7e7!important}.tb{background:#f2faf2!important}.tm{background:#fff4e0!important}.td{background:#f6f6f6!important;color:#999}
.note{color:#666;margin:4px 0 12px}"""
h = [f"<meta charset=utf-8><style>{css}</style>",
     f"<h3>{html.escape(TITLE)}</h3>",
     f'<div class=note>Показано {len(shown)} из {len(rows)} строк · поля = то, с чем работает агент на этом этапе</div>',
     "<table><tr>"] + [f"<th>{c[1]}</th>" for c in cols] + ["</tr>"]
for r in shown:
    h.append(f'<tr class="{rowclass(r)}">' + "".join(f"<td>{fmt(r,k)}</td>" for k,_ in cols) + "</tr>")
h.append("</table>")
htmlpath = PNG.replace(".png", ".html")
open(htmlpath, "w").write("".join(h))

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=["--no-sandbox"])
    pg = b.new_context(viewport={"width": 1500, "height": 1000}, device_scale_factor=2).new_page()
    pg.goto("file://" + htmlpath)
    pg.wait_for_timeout(400)
    pg.screenshot(path=PNG, full_page=True)
    b.close()
print(f"wrote {PNG} ({len(shown)} rows)")
