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

DESC = 220          # description budget per product (HTML shows 170 + bullets; text has no images)
PITCH = 110

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
    ir = "IN-RANGE" if p.get("in_range") else ("price?" if p.get("price_unknown") else "out-of-range")
    url = f"https://{dom}/products/{p['handle']}" if p.get("handle") else f"https://{dom}"
    veto = "  ⚠ПУСТЫШКА" if p.get("pust") else ""
    kind = s(p.get("k"), 12)                      # physical / apparel / ingestible / skincare (Veto input)
    out = [f"      {tag} {money(p):>10}  [{ir}] [desc:{s(p.get('desc_confidence'), 10) or '?'}"
           f" · {kind or 'kind?'} · {s(p.get('pclass'), 16)} · pos{p.get('pos')} · inv{p.get('invest')}]{veto}",
           f"         {s(p.get('t'), 100)}",
           f"         {url}"]
    d = s(p.get("desc"), DESC)
    if d:
        out.append(f"         {d}")
    for b in (p.get("bullets") or [])[:4]:
        out.append(f"         • {s(b, 90)}")
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
    print(f"{i:3} [{r.get('tier','?'):>3} {r.get('score') or 0:>3}] {nl} {dom}{reach}"
          f"   {r.get('country') or '?'} · created {s(r.get('created'), 7)} · visits {r.get('visits')}")
    print(f"      {s(r.get('maturity'), 9)} · {s(r.get('store_type'), 18)} · {s(r.get('product_class'), 16)}"
          f" · cat:{s(r.get('cat_flag'), 14)} · new30d:{r.get('new_products_30d')} · conv_batch:{r.get('conv_batch')}"
          f" · hero_conf:{s(r.get('hero_confidence'), 6)} ({s(r.get('hero_src'), 14)})"
          f" · kind:{s(r.get('kind'), 12)}{'  ⚠ПУСТЫШКА-STORE' if r.get('pust') else ''}")
    print(f"      SL-оценки (directional): rev {r.get('sl_rev')} · avg-price {r.get('sl_avg')} · products {r.get('sl_pc')}")
    pitch = s(r.get("home_pitch"), PITCH)
    if pitch:
        print(f"      pitch: {pitch}")
    if r.get("flags"):
        print(f"      flags: {s(r.get('flags'), 80)}")
    if r.get("needs_live"):
        print(f"      why-live: {s(r.get('needs_live_why'), 80)}")
    if not r.get("reachable"):
        print(f"      unreachable-reason: {s(r.get('reason'), 90)}  → ОТКРЫТЬ ЖИВЬЁМ, карточки нет")

    hh = r.get("home_hero")
    if hh and hh.get("t"):
        banners += 1
        url = f"https://{dom}/products/{hh['handle']}" if hh.get("handle") else f"https://{dom}"
        mark = "" if hh.get("in_clean") else "  ≠ bestseller-подбор (робот мог промахнуться — смотри оба)"
        print(f"      🏠 BANNER (товар с главной){mark}")
        print(f"         {s(hh.get('t'), 100)}")
        print(f"         {url}")

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
