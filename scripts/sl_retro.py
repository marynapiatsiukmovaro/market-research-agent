#!/usr/bin/env python3
"""sl_retro.py — Store Leads retro-calibration of already-processed batches.
Read-only. Answers S3 calibration questions WITHOUT new scraping:
  Q1  Did the proxy tier/score SURFACE the winners, or bury them? (tests op-rule RULE 6)
  Q2  Effort map: how many stores were 'cheap-killable' (could be cut by a CHEAP early
      signal before the expensive live-read) vs needed the full read to reject?
  Q3  v3 early-signal behaviour (batch4): does desc_confidence / hero_confidence /
      maturity actually flag the stores that needed manual/price-check?
Outputs: compact stdout summary + a self-contained HTML report.
Usage:  python3 sl_retro.py
"""
import json, html, os
BASE = "/opt/market-research-agent/logs/storeleads/"
WINNERS = {"stoov.com": 73, "maskingmaster.com": 72}  # reported 65+ (Step Handrail re-run domain found dynamically)

BATCHES = [
    ("BATCH1", "hi_band_200_enriched.json", "enrich2"),
    ("BATCH2", "hi_batch2_enriched.json",   "enrich2"),
    ("BATCH3", "hi_batch3_enriched.json",   "enrich2"),
    ("BATCH4", "hi_batch4_enriched.json",   "enrich3"),
]

def load(fn):
    d = json.load(open(BASE + fn))
    if isinstance(d, dict):
        d = d.get("results") or list(d.values())
    return d

def cheap_kill_reason(r):
    """Would a CHEAP early signal (no live deep-read) have rejected this store?
    Cheap = derivable from dump fields + enricher flags, no human judgement."""
    if r.get("kind") == "apparel":            return "apparel"
    if r.get("pust"):                          return "пустышка-claim"
    if r.get("cat_flag") == "catalog-giant":   return "catalog-giant pc>2000"
    if r.get("in_range") is False:             return "price out-of-band"
    return None

def summarize(rows, kind):
    n = len(rows)
    reach = sum(1 for r in rows if r.get("reachable", True))
    tiers = {}
    for r in rows:
        tiers[r.get("tier", "?")] = tiers.get(r.get("tier", "?"), 0) + 1
    cheap = {}
    for r in rows:
        why = cheap_kill_reason(r)
        if why:
            cheap[why] = cheap.get(why, 0) + 1
    cheap_total = sum(cheap.values())
    out = {"n": n, "reach": reach, "tiers": tiers, "cheap": cheap, "cheap_total": cheap_total}
    if kind == "enrich3":
        dc = {}; hc = {}; mat = {}
        for r in rows:
            dc[r.get("desc_confidence", "?")] = dc.get(r.get("desc_confidence", "?"), 0) + 1
            hc[r.get("hero_confidence", "?")] = hc.get(r.get("hero_confidence", "?"), 0) + 1
            mat[r.get("maturity", "?")] = mat.get(r.get("maturity", "?"), 0) + 1
        out.update({"desc_conf": dc, "hero_conf": hc, "maturity": mat})
    return out

def top_by_score(rows, k=12):
    return sorted(rows, key=lambda r: (r.get("score") or 0), reverse=True)[:k]

report = []
html_parts = ['<html><head><meta charset="utf-8"><style>'
    'body{font:13px/1.5 -apple-system,Arial;margin:24px;color:#1a1a1a}'
    'h1{font-size:20px}h2{font-size:15px;margin-top:26px;border-bottom:2px solid #ddd;padding-bottom:4px}'
    'table{border-collapse:collapse;margin:8px 0;font-size:12px}'
    'td,th{border:1px solid #ccc;padding:4px 8px;text-align:left}'
    'th{background:#f4f4f4}.win{background:#fff6d5}.kill{color:#a00}'
    'code{background:#f0f0f0;padding:1px 4px}.note{color:#666;font-size:12px}</style></head><body>']
html_parts.append("<h1>Store Leads — Retro-калибровка обработанных батчей (S3)</h1>")
html_parts.append('<p class=note>Read-only анализ уже собранных enriched-JSON. Без нового скрапинга. '
                  'Цель: какие ранние сигналы предсказывают качество · что можно убить дёшево до live-read · работает ли v3 confidence.</p>')

# locate winner / handrail domains across batches
winner_rows = []
for label, fn, kind in BATCHES:
    rows = load(fn)
    for r in rows:
        dom = (r.get("domain") or "").lower()
        if dom in WINNERS:
            winner_rows.append((label, r))

print("="*70)
print("WINNERS — early-signal fingerprint (the 2 reported 65+)")
print("="*70)
html_parts.append("<h2>1. Отпечаток winner'ов — вытащил ли их proxy наверх? (тест RULE 6)</h2>")
wcols = ["domain","score","tier","in_range","conv_batch","cat_flag","sl_rev","sl_pc","created","hero_src","kind"]
html_parts.append("<table><tr><th>batch</th>" + "".join(f"<th>{c}</th>" for c in wcols) + "</tr>")
for label, r in winner_rows:
    vals = [r.get(c) for c in wcols]
    print(f"{label} {WINNERS.get((r.get('domain') or '').lower(),'')}/100 →", {c: r.get(c) for c in wcols})
    html_parts.append(f"<tr class=win><td>{label}</td>" + "".join(f"<td>{html.escape(str(v))}</td>" for v in vals) + "</tr>")
html_parts.append("</table>")

# per-batch: where did the winners RANK by proxy score within their batch?
print("\n" + "="*70)
print("PROXY-RANK of winners within their batch (does score/tier surface them?)")
print("="*70)
html_parts.append("<h2>2. Ранг winner'а по proxy-score внутри своего батча</h2>")
html_parts.append("<table><tr><th>winner</th><th>batch</th><th>proxy score</th><th>rank by score</th><th>of N</th><th>tier</th></tr>")
for label, fn, kind in BATCHES:
    rows = load(fn)
    ordered = sorted(rows, key=lambda r: (r.get("score") or 0), reverse=True)
    for i, r in enumerate(ordered, 1):
        dom = (r.get("domain") or "").lower()
        if dom in WINNERS:
            print(f"{dom}: proxy_score={r.get('score')} rank={i}/{len(rows)} tier={r.get('tier')}")
            html_parts.append(f"<tr class=win><td>{dom}</td><td>{label}</td><td>{r.get('score')}</td>"
                              f"<td>#{i}</td><td>{len(rows)}</td><td>{r.get('tier')}</td></tr>")
html_parts.append("</table>")
html_parts.append('<p class=note>Если winner стоит НИЗКО по proxy-score → подтверждает RULE 6 (proxy = sort-aid, не качество; читать ВСЁ). '
                  'Если высоко → ранний сигнал предиктивен, можно триажить.</p>')

# per-batch summaries + effort map
print("\n" + "="*70)
print("PER-BATCH effort map")
print("="*70)
html_parts.append("<h2>3. Карта усилий: что можно убить ДЁШЕВО до live-read (экономия токенов)</h2>")
html_parts.append("<table><tr><th>batch</th><th>N</th><th>reachable</th><th>tiers</th>"
                  "<th>cheap-killable</th><th>by what</th></tr>")
for label, fn, kind in BATCHES:
    rows = load(fn)
    s = summarize(rows, kind)
    report.append((label, kind, s))
    print(f"{label} [{kind}] n={s['n']} reach={s['reach']} tiers={s['tiers']} "
          f"cheap-killable={s['cheap_total']} ({s['cheap']})")
    html_parts.append(f"<tr><td>{label}</td><td>{s['n']}</td><td>{s['reach']}</td>"
                      f"<td>{html.escape(str(s['tiers']))}</td>"
                      f"<td class=kill>{s['cheap_total']}</td>"
                      f"<td>{html.escape(str(s['cheap']))}</td></tr>")
html_parts.append("</table>")
html_parts.append('<p class=note>cheap-killable = магазины, отсекаемые по сигналу из dump+флагов enricher (apparel / пустышка / '
                  'catalog-giant / цена вне диапазона) БЕЗ дорогого чтения живого сайта. Это верхняя граница экономии шагов.</p>')

# v3 confidence behaviour (batch4)
print("\n" + "="*70)
print("V3 confidence behaviour (BATCH4)")
print("="*70)
html_parts.append("<h2>4. v3 confidence-флаги (BATCH4) — флагают ли они то, что требует ручной проверки?</h2>")
for label, fn, kind in BATCHES:
    if kind != "enrich3":
        continue
    rows = load(fn)
    s = summarize(rows, kind)
    print("desc_confidence:", s["desc_conf"])
    print("hero_confidence:", s["hero_conf"])
    print("maturity:", s["maturity"])
    # cross-tab desc_confidence x tier
    ct = {}
    for r in rows:
        key = (r.get("desc_confidence", "?"), r.get("tier", "?"))
        ct[key] = ct.get(key, 0) + 1
    html_parts.append(f"<p><b>desc_confidence</b>: {html.escape(str(s['desc_conf']))}<br>"
                      f"<b>hero_confidence</b>: {html.escape(str(s['hero_conf']))}<br>"
                      f"<b>maturity</b>: {html.escape(str(s['maturity']))}</p>")
    html_parts.append("<table><tr><th>desc_confidence × tier</th><th>count</th></tr>")
    for (dcf, t), c in sorted(ct.items()):
        html_parts.append(f"<tr><td>{html.escape(str(dcf))} × {html.escape(str(t))}</td><td>{c}</td></tr>")
    html_parts.append("</table>")

# top-12 by proxy score per batch (so Marina sees what proxy thinks is best)
html_parts.append("<h2>5. Top-12 по proxy-score в каждом батче (что proxy считает лучшим)</h2>")
for label, fn, kind in BATCHES:
    rows = load(fn)
    html_parts.append(f"<h3 style='font-size:13px'>{label} [{kind}]</h3>")
    html_parts.append("<table><tr><th>#</th><th>domain</th><th>score</th><th>tier</th>"
                      "<th>in_range</th><th>price</th><th>conv</th><th>candidate / desc</th></tr>")
    for i, r in enumerate(top_by_score(rows, 12), 1):
        dom = (r.get("domain") or "")
        cls = " class=win" if dom.lower() in WINNERS else ""
        cand = r.get("candidate") or ((r.get("tops3") or [{}])[0].get("desc") if r.get("tops3") else "") or r.get("desc") or ""
        url = f"https://{dom}"
        html_parts.append(f"<tr{cls}><td>{i}</td><td><a href='{html.escape(url)}'>{html.escape(dom)}</a></td>"
                          f"<td>{r.get('score')}</td><td>{r.get('tier')}</td><td>{r.get('in_range')}</td>"
                          f"<td>{html.escape(str(r.get('price')))}</td><td>{r.get('conv_batch')}</td>"
                          f"<td>{html.escape(str(cand))[:90]}</td></tr>")
    html_parts.append("</table>")

html_parts.append("</body></html>")
outpath = BASE + "sl_retro_report.html"
open(outpath, "w").write("\n".join(html_parts))
print("\nHTML written:", outpath)
