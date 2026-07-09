#!/usr/bin/env python3
"""sl_project_any.py — CANONICAL Stage-2 renderer, AGENT surface (text projection of the full card).

One of the TWO approved Stage-2 reading surfaces for Store Leads (pair named S18):
  * sl_stage2_table.py → HTML for the FOUNDER (images, clickable, opened on the Desktop).
  * THIS file          → text for the AGENT (same fields; 250 cards fit in a context window).
Both MUST show the FULL card. Any other / partial reader is forbidden — analysing from a hand-made
reader that showed 1 product of 3 is what zeroed S5.

S18 fix — this projector used to be a PARTIAL reader itself (and lived only on the VPS, outside git):
it dropped `home_hero` (the homepage-banner product, added in v4.2 precisely because the best-seller
auto-pick misfires — swaddlean / dingle-dangle), truncated `desc` to 58 chars, and never printed
bullets / desc_confidence / hero_confidence / the unreachable reason. So the agent judged on less
than the founder saw. It now prints the whole contract and SELF-CERTIFIES the product count.

SELF-CERTIFYING — it certifies exactly ONE thing: that the READING is complete (every store, every
product printed, nothing hidden). The DATA verdict belongs to sl_qa.py / sl_accept_chunk.py.

tier/score = revenue SORT-AID, never quality (RULE 6). Read every row.

Usage: python3 sl_project_any.py <enriched.json>
"""
import json, sys

# ⚠ S18b — DENSITY MATTERS AS MUCH AS COMPLETENESS.
# The S18 rewrite restored every contract field but blew the card up 4.3x on the same 250-store file
# (968 -> 5,696 lines; 121k -> 528k chars), because each product got 4 lines + up to 4 bullets.
# A reader that no longer fits a context window is broken in the OTHER direction. Same 28 fields,
# packed layout: 2 lines per product; bullets ONLY when the description can't be trusted.
DESC = 150          # description budget per product
PITCH = 90

# THE CONTRACT: the fields a Stage-2 surface MUST render to be called "full card" (RULE 25).
# Named here as a PROPERTY, not tied to any script. `img` is rendered as a product URL in text and
# as a thumbnail in HTML — both count as "the product is visually reachable".
FIELDS_RENDERED = ["domain", "tier", "needs_live", "needs_live_why", "unreachable_reason", "geo", "created",
                   "visits", "maturity", "store_type", "product_class", "cat_flag", "new30d", "conv_batch",
                   "hero_confidence", "kind", "pust", "home_pitch", "flags", "home_hero",
                   "tops3", "price", "in_range", "desc", "bullets", "desc_confidence", "img", "social"]

rows = json.load(open(sys.argv[1]))
order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3, "MANUAL": 4, "DROP-noPhysical": 5}
rows.sort(key=lambda r: (order.get(r.get("tier"), 9), -(r.get("score") or 0)))


def s(x, n=70):
    if x is None:
        return ""
    return str(x).replace("\n", " ").strip()[:n]


def money(p):
    pv = p.get("price")
    cur = p.get("cur") or ""
    if p.get("price_unknown") or pv in (None, 0):
        return "$?"
    return f"${pv}{('/' + cur) if cur and cur != 'USD' else ''}"


def product_line(p, dom, tag):
    ir = "IN" if p.get("in_range") else ("$?" if p.get("price_unknown") else "out")
    url = f"https://{dom}/products/{p['handle']}" if p.get("handle") else f"https://{dom}"
    veto = " ⚠ПУСТЫШКА" if p.get("pust") else ""
    dc = s(p.get("desc_confidence"), 10) or "?"
    inv = p.get("invest") or {}
    out = [f"   {tag} {money(p):>9} [{ir}] {s(p.get('k'), 9) or 'kind?'}/{s(p.get('pclass'), 15)}"
           f" pos{p.get('pos')} d{inv.get('desc_len')} i{inv.get('imgs')} v{inv.get('variants')}"
           f" {'b:' + ','.join(inv.get('badges') or []) if inv.get('badges') else ''}"
           f" desc:{dc}{veto}  {s(p.get('t'), 62)}  {url}"]
    d = s(p.get("desc"), DESC)
    if d:
        out.append(f"      {d}")
    if dc != "ok":                       # desc untrustworthy → bullets are the only real signal left
        bl = " • ".join(s(b, 60) for b in (p.get("bullets") or [])[:3])
        if bl:
            out.append(f"      • {bl}")
    return out


tops_avail = sum(len(r.get("tops3") or []) for r in rows)
tops_printed = 0
banners = 0

print(f"# STAGE-2 FULL CARD (agent surface) — {len(rows)} stores — sl_project_any.py")
print("# tier/score = SORT-AID, NOT quality. Read ALL. NL = needs_live (живой заход обязателен).")
print("#" + "=" * 108)

for i, r in enumerate(rows, 1):
    dom = r.get("domain") or "?"
    nl = "NL" if r.get("needs_live") else "  "
    reach = "" if r.get("reachable") else "  ⛔UNREACHABLE"
    print()
    print(f"{i:3} [{r.get('tier','?'):>3}{r.get('score') or 0:>4}] {nl} {dom}{reach}  {r.get('country') or '?'}"
          f" {s(r.get('created'), 7)} v{r.get('visits')} · {s(r.get('maturity'), 9)}/{s(r.get('store_type'), 18)}"
          f"/{s(r.get('product_class'), 15)} cat:{s(r.get('cat_flag'), 13)} new30d:{r.get('new_products_30d')}"
          f" conv:{r.get('conv_batch')} hero:{s(r.get('hero_confidence'), 4)}({s(r.get('hero_src'), 12)})"
          f" kind:{s(r.get('kind'), 10)}{' ⚠ПУСТЫШКА-STORE' if r.get('pust') else ''}"
          f" · SL rev{r.get('sl_rev')}/avg{r.get('sl_avg')}/pc{r.get('sl_pc')}")
    pitch = s(r.get("home_pitch"), PITCH)
    if pitch:
        print(f"      «{pitch}»")
    tail = []
    if r.get("flags"):
        tail.append(f"flags:{s(r.get('flags'), 70)}")
    if r.get("needs_live"):
        tail.append(f"why-live:{s(r.get('needs_live_why'), 50)}")
    if tail:
        print("      " + " · ".join(tail))
    if not r.get("reachable"):
        print(f"      ⛔ {s(r.get('reason'), 80)} → ОТКРЫТЬ ЖИВЬЁМ, карточки нет")

    hh = r.get("home_hero")
    if hh and hh.get("t"):
        banners += 1
        url = f"https://{dom}/products/{hh['handle']}" if hh.get("handle") else f"https://{dom}"
        mark = "" if hh.get("in_clean") else " ≠подбор(робот мог промахнуться — смотри оба)"
        print(f"   🏠 BANNER{mark}  {s(hh.get('t'), 62)}  {url}")

    tops = r.get("tops3") or []
    for j, p in enumerate(tops, 1):
        tops_printed += 1
        for ln in product_line(p, dom, f"#{j}"):
            print(ln)
    if not tops and r.get("reachable"):
        print("      — товаров не извлечено (reachable, но пусто) → живой заход")

    soc = [f"{k}:{r.get(k)}" for k in ("fb", "ig", "tiktok", "pinterest") if r.get(k)]
    if soc:
        print(f"      social: {' · '.join(s(x, 60) for x in soc)}")

print()
print("#" + "=" * 108)
ok = tops_printed == tops_avail
print(f"# FULL CARD RENDERED — {'PASS' if ok else 'STOP — PRODUCTS HIDDEN'}: "
      f"{tops_printed}/{tops_avail} products · {banners} banner-heroes · {len(rows)} stores.")
print("# Данные (reach/полнота полей) сертифицирует sl_qa.py / sl_accept_chunk.py, не этот файл.")
# Machine-readable certificate — compared against the founder's HTML surface by sl_card_parity.py.
# `fields` = the contract fields THIS surface actually renders. The S18 bug was invisible precisely
# because nobody ever compared the two surfaces' field lists (absence of a field has no symptom).
print(f"CERT surface=agent-text stores={len(rows)} products={tops_printed} banners={banners} "
      f"fields={','.join(FIELDS_RENDERED)}")
sys.exit(0 if ok else 1)
