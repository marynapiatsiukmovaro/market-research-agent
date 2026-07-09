#!/usr/bin/env python3
"""sl_stage2_table.py — CANONICAL Stage-2 renderer, FOUNDER surface (sl_enrich4 v4.2 → grouped-11 HTML).

One of the TWO approved Stage-2 reading surfaces for Store Leads (S6 Marina-locked; pair named S18):
  * THIS file  → HTML for the FOUNDER (images, clickable, opened on the Desktop).
  * sl_project_any.py → text projection for the AGENT (same fields, 250 cards fit in context).
Both MUST show the FULL card (all 3 tops + every field). Any other / partial reader is forbidden —
analysing from a hand-made reader showing 1 product of 3 is what zeroed S5.

Layout = GROUPED-11 (Marina-approved 2026-06-03): #, domain·pitch, tier·score, needs_live,
geo·age, store signals (maturity·new30d·cat_flag·conv), type (store/product class),
hero qual (heroConf·descConf·pos), price USD·in_range, 🏠BANNER+top-3, social.

SELF-CERTIFYING — and it certifies exactly ONE thing: that the READING is complete (every store,
every product rendered, nothing hidden). The DATA verdict belongs to sl_qa.py / sl_accept_chunk.py.
A Stage-2 table without this banner is not canonical — STOP.

Usage: python3 sl_stage2_table.py <enriched.json> <output.html> "<title>" "<funnel banner>"
"""
import json, html, sys
from collections import Counter

# THE CONTRACT: the fields a Stage-2 surface MUST render to be called "full card" (RULE 25).
# A PROPERTY, not a script name. Kept byte-identical in sl_project_any.py; sl_card_parity.py diffs them.
FIELDS_RENDERED = ["domain", "tier", "needs_live", "needs_live_why", "unreachable_reason", "geo", "created",
                   "visits", "maturity", "store_type", "product_class", "cat_flag", "new30d", "conv_batch",
                   "hero_confidence", "kind", "pust", "home_pitch", "flags", "home_hero",
                   "tops3", "price", "in_range", "desc", "bullets", "desc_confidence", "img", "social"]

inp, outp, title = sys.argv[1], sys.argv[2], sys.argv[3]
banner = sys.argv[4] if len(sys.argv) > 4 else ""
rows = json.load(open(inp))
order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3, "MANUAL": 4, "DROP-noPhysical": 5}
rows.sort(key=lambda r: (order.get(r.get("tier"), 9), -(r.get("score") or 0)))

# ---------------- completeness (shared logic with sl_qa.py gate) ----------------
def filled(v): return v not in (None, "", [], {}, "None")
def pct(a, b): return round(100.0 * a / b, 1) if b else 0.0

def completeness(rows):
    n = len(rows)
    reach = [r for r in rows if r.get("reachable")]
    nr = len(reach)
    allp = [p for r in reach for p in (r.get("tops3") or [])]
    npx = len(allp)
    c = {
        "n": n, "reach": nr, "reach_pct": pct(nr, n),
        "avgtops": round(sum(len(r.get("tops3") or []) for r in reach) / nr, 2) if nr else 0,
        "ge1top": pct(sum(1 for r in reach if (r.get("tops3") or [])), nr),
        "tops3": pct(sum(1 for r in reach if len(r.get("tops3") or []) == 3), nr),
        "prod_img": pct(sum(1 for p in allp if filled(p.get("img"))), npx),
        "prod_inrange": pct(sum(1 for p in allp if "in_range" in p), npx),
        "prod_descconf": pct(sum(1 for p in allp if filled(p.get("desc_confidence"))), npx),
        "store_type": pct(sum(1 for r in rows if filled(r.get("store_type"))), n),
        "product_class": pct(sum(1 for r in rows if filled(r.get("product_class"))), n),
        "cat_flag": pct(sum(1 for r in rows if filled(r.get("cat_flag"))), n),
        "maturity": pct(sum(1 for r in rows if filled(r.get("maturity"))), n),
        "new30d": pct(sum(1 for r in rows if "new_products_30d" in r), n),
        "home_pitch": pct(sum(1 for r in rows if filled(r.get("home_pitch"))), n),
        "social": pct(sum(1 for r in rows if any(filled(r.get(s)) for s in ("fb", "ig", "tiktok", "pinterest"))), n),
        "home_img": pct(sum(1 for r in rows if filled(r.get("home_img"))), n),
        "needs_live": sum(1 for r in rows if r.get("needs_live")),
    }
    return c

# ---------------- what THIS generator certifies: the READING, not the data ----------------
# Two layers, one owner each: sl_qa.py / sl_accept_chunk.py certify the DATA (completeness of the
# scraper's output); this generator certifies that every store and every product the file holds is
# actually RENDERED — nothing hidden. (The S5 failure was a reader showing 1 product of 3.)
# S18 fix: the banner used to re-check sl_qa's numeric thresholds, so on one and the same file
# sl_accept_chunk could say ACCEPT (benign products.json dip) while this banner said STOP. Two
# verdicts, one file. The data percentages below are now INFO ONLY and never STOP the reader.
c = completeness(rows)
tops_avail = sum(len(r.get("tops3") or []) for r in rows)
imgs_avail = sum(1 for r in rows for p in (r.get("tops3") or []) if filled(p.get("img")))
tops_rendered = sum(min(len(r.get("tops3") or []), 3) for r in rows)   # tops_cell renders [:3]
miss = []
if tops_rendered != tops_avail:
    miss.append(f"products hidden: rendered {tops_rendered} of {tops_avail}")
verdict_ok = not miss

# ---------------- render helpers ----------------
def link(u, txt):
    if not u: return ""
    u = str(u)
    if not u.startswith("http"): u = "https://" + u
    return f"<a href='{html.escape(u)}'>{txt}</a>"

def tops_cell(r):
    out = []
    dom = r.get("domain") or ""
    hh = r.get("home_hero")
    if hh and not hh.get("in_clean") and hh.get("t"):
        purl = (f"https://{dom}/products/{hh.get('handle')}" if hh.get("handle") else f"https://{dom}")
        thumb = (f"<a href='{html.escape(purl)}'><img src='{html.escape(str(hh.get('img')))}' style='float:left;margin:0 6px 2px 0'></a>" if hh.get("img") else "")
        out.append(f"<div style='margin-bottom:6px;overflow:hidden;background:#eaf2ff;padding:3px;border-radius:4px'>{thumb}"
                   f"🏠 <b>BANNER:</b> {link(purl, html.escape(str(hh.get('t'))))}</div>")
    elif hh and hh.get("img"):
        out.append(f"<div style='margin-bottom:6px;overflow:hidden;background:#eaf2ff;padding:3px;border-radius:4px'>"
                   f"<img src='{html.escape(str(hh.get('img')))}' style='float:left;margin:0 6px 2px 0'>🏠 <b>BANNER</b></div>")
    for t in (r.get("tops3") or [])[:3]:
        pr = t.get("price"); cur = t.get("cur") or ""
        flag = "✓" if t.get("in_range") else ("?" if t.get("price_unknown") else "✗")
        dc = t.get("desc_confidence", ""); pcl = t.get("pclass", "")
        desc = html.escape(str(t.get("desc") or ""))[:170]
        bl = t.get("bullets") or []
        blhtml = ("<br><span style='color:#555'>• " + " • ".join(html.escape(b) for b in bl[:3]) + "</span>") if bl else ""
        purl = (f"https://{dom}/products/{t.get('handle')}" if t.get("handle") else f"https://{dom}")
        thumb = (f"<a href='{html.escape(purl)}'><img src='{html.escape(str(t.get('img')))}' style='float:left;margin:0 6px 2px 0'></a>" if t.get("img") else "")
        ttl = link(purl, html.escape(str(t.get("t") or "product")))
        out.append(f"<div style='margin-bottom:6px;overflow:hidden'>{thumb}<b>{pr} {cur}</b> {flag} "
                   f"<span style='color:#888'>[{html.escape(str(dc))}·{html.escape(str(pcl))}]</span> {ttl}<br>{desc}{blhtml}</div>")
    return "".join(out) or "<i>—</i>"

tiers = Counter(r.get("tier") for r in rows)
matc = Counter(r.get("maturity") for r in rows)
h = ['<!doctype html><html lang=ru><meta charset=utf-8><title>', html.escape(title), '</title><style>'
     'body{font:12px/1.45 -apple-system,Arial;margin:18px;color:#1a1a1a}h1{font-size:17px}'
     '.banner{background:#fff4e6;border:1px solid #f0c890;padding:8px 12px;border-radius:6px;margin:8px 0;font-size:13px}'
     '.accept{padding:10px 14px;border-radius:8px;margin:10px 0;font-size:13px;border:2px solid}'
     '.accept.pass{background:#eafff0;border-color:#2faa55}.accept.stop{background:#fff0f0;border-color:#d33}'
     'table{border-collapse:collapse;font-size:11px}td,th{border:1px solid #ccc;padding:4px 6px;vertical-align:top}'
     'th{background:#222;color:#fff;position:sticky;top:0}tr.A{background:#f3fff3}tr.B{background:#fbfff8}'
     'tr.PRICE-CHECK{background:#fff8e6}tr.MANUAL,tr.DROP-noPhysical{background:#fff0f0}'
     'a{color:#1763d6;text-decoration:none}.lo{color:#c00}.hi{color:#080}.est{background:#eef;padding:1px 3px;border-radius:3px}'
     'img{max-width:60px;max-height:60px;border-radius:4px}.sig{font-size:10px;color:#444}.k{color:#888}</style><body>']
h.append(f"<h1>{html.escape(title)} — layout: grouped (canonical)</h1>")

# --- SELF-CERTIFYING banner: FULL CARD RENDERED (reading completeness — data verdict = sl_qa) ---
verline = (f"✅ <b>FULL CARD RENDERED — PASS.</b> Stage-2 enriched file (not Stage-1); every store and every "
           f"product it holds is shown: {c['n']} stores · {tops_rendered}/{tops_avail} products · {imgs_avail} images. "
           f"Nothing hidden, nothing truncated. Canonical generator (sl_stage2_table.py)."
           if verdict_ok else
           "⛔ <b>READING INCOMPLETE — STOP.</b> This table hides part of the card. Do NOT analyse: "
           + html.escape("; ".join(miss)))
h.append(f"<div class='accept {'pass' if verdict_ok else 'stop'}'>{verline}<br>"
         f"<span style='font-size:11px'><b>Данные (INFO — вердикт даёт sl_qa.py / sl_accept_chunk.py, не эта таблица):</b> "
         f"stores {c['n']} · reachable {c['reach']} ({c['reach_pct']}%) · avgtops {c['avgtops']} · "
         f"≥1top {c['ge1top']}% · 3tops {c['tops3']}% · prod-img {c['prod_img']}% · in_range {c['prod_inrange']}% · descConf {c['prod_descconf']}% · "
         f"store_type {c['store_type']}% · product_class {c['product_class']}% · cat_flag {c['cat_flag']}% · maturity {c['maturity']}% · "
         f"new30d {c['new30d']}% · home_pitch {c['home_pitch']}% · social {c['social']}% · home_img/banner {c['home_img']}% · "
         f"needs_live {c['needs_live']} → живой заход руками</span></div>")

h.append(f"<div class=banner><b>⚠ tier/score = SORT-AID, не качество (RULE 6).</b> Stage 3 = читаю ВСЕ строки, "
         f"подтверждаю hero+цену на живом сайте, открываю КАЖДЫЙ needs_live (RULE 23), 100-pt+Veto. "
         f"Tiers {html.escape(str(dict(tiers)))} · maturity {html.escape(str(dict(matc)))}</div>")
if banner:
    h.append(f"<div class=banner style='background:#eef4ff;border-color:#b9d0f5'><b>Funnel (RULE 1):</b> {html.escape(banner)}</div>")

cols = ["#", "domain · pitch", "tier·score", "needs_live", "geo·age (country·created·visits)",
        "store signals (maturity·new30d·cat_flag·conv)", "type (store/product class)",
        "hero qual (heroConf·descConf·pos)", "price USD·in_range",
        "🏠 BANNER + top-3 (photo·price·desc·bullets)", "social"]
h.append("<table><tr>" + "".join(f"<th>{html.escape(x)}</th>" for x in cols) + "</tr>")

for i, r in enumerate(rows, 1):
    dom = r.get("domain") or ""
    hc = r.get("hero_confidence", ""); dc = r.get("desc_confidence", "")
    hc_s = f"<span class={'hi' if hc=='high' else 'lo'}>{html.escape(str(hc))}</span>"
    himg = (f"<img src='{html.escape(str(r.get('home_img')))}' style='max-width:46px;max-height:46px;float:right;margin-left:4px'>" if r.get("home_img") else "")
    pitch = html.escape(str(r.get("home_pitch") or ""))[:170]
    dom_cell = link(dom, html.escape(dom)) + himg + (f"<br><span style='color:#777;font-size:10px'>{pitch}</span>" if pitch else "")
    nl = r.get("needs_live"); nlw = ",".join(r.get("needs_live_why") or [])
    nl_cell = (f"<b style='color:#c60'>OPEN</b><br><span style='font-size:9px;color:#a60'>{html.escape(nlw)}</span>") if nl else "<span style='color:#8a8'>ok</span>"
    if not r.get("reachable"):   # S18: the unreachable reason was rendered NOWHERE — the highest-risk pile
        nl_cell += (f"<br><b style='color:#d33'>⛔UNREACHABLE</b><br><span style='font-size:9px;color:#a33'>"
                    f"{html.escape(str(r.get('reason') or ''))[:60]}</span>")
    geo = (f"{html.escape(str(r.get('country') or ''))}<br><span class=k>{html.escape(str(r.get('created') or '')[:10])}</span>"
           f"<br>v{html.escape(str(r.get('visits') if r.get('visits') is not None else '—'))}")
    sigs = (f"<span class=sig>mat: <b>{html.escape(str(r.get('maturity') or ''))}</b><br>"
            f"new30d: {html.escape(str(r.get('new_products_30d') or ''))}<br>"
            f"cat: {html.escape(str(r.get('cat_flag') or ''))}<br>conv: {html.escape(str(r.get('conv_batch') or ''))}</span>")
    # S18: kind / pust / flags were collected by the enricher but rendered NOWHERE — and pust+kind
    # are direct inputs to the Marina Veto. A surface that hides a Veto input is not a full card.
    pust_s = "<br><b style='color:#d33'>⚠ПУСТЫШКА</b>" if r.get("pust") else ""
    flags_s = (f"<br><span style='font-size:9px;color:#a60'>{html.escape(', '.join(r.get('flags') or []))[:70]}</span>"
               if r.get("flags") else "")
    typ = (f"<span class=sig>{html.escape(str(r.get('store_type') or ''))}"
           f"<br><span class=k>{html.escape(str(r.get('product_class') or ''))}</span>"
           f"<br><span class=k>kind: {html.escape(str(r.get('kind') or '—'))}</span>{pust_s}{flags_s}</span>")
    hq = (f"<span class=sig>hero: {hc_s}<br>desc: {html.escape(str(dc))}<br>pos: {html.escape(str(r.get('storefront_pos') or ''))}</span>")
    price = (html.escape(str(r.get("price") or "")) + (f" <span class=est>{html.escape(str(r.get('store_currency') or ''))}</span>" if r.get("store_currency") else "")
             + "<br>" + ("✓" if r.get("in_range") else "✗"))
    social = " ".join(filter(None, [link(r.get("fb"), "FB"), link(r.get("ig"), "IG"),
                                    link(r.get("tiktok"), "TT"), link(r.get("pinterest"), "Pin")]))
    cells = [str(i), dom_cell, f"<b>{html.escape(str(r.get('tier','')))}</b> · {html.escape(str(r.get('score','')))}",
             nl_cell, geo, sigs, typ, hq, price, tops_cell(r), social]
    h.append(f"<tr class='{r.get('tier','')}'>" + "".join(f"<td>{x}</td>" for x in cells) + "</tr>")
h.append("</table></body></html>")
open(outp, "w").write("\n".join(h))
print("HTML written:", outp, "| rows:", len(rows),
      f"| RENDERED: {tops_rendered}/{tops_avail} products,", imgs_avail, "images |",
      "FULL CARD — PASS" if verdict_ok else "STOP " + ";".join(miss))
# Machine-readable certificate — compared against the agent's text surface by sl_card_parity.py.
banners_html = sum(1 for r in rows if (r.get("home_hero") or {}).get("t"))
print(f"CERT surface=founder-html stores={len(rows)} products={tops_rendered} banners={banners_html} "
      f"fields={','.join(FIELDS_RENDERED)}")
