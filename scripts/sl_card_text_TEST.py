#!/usr/bin/env python3
"""Stage-2 card — AGENT surface (text). S20 rebuild, Marina-directed.

WHAT CHANGED AND WHY (the card is now built around ONE decision: go and look, or not).

  DELETED — the field lied, or never moved a decision:
    needs_live + needs_live_why   the robot told the agent what to open; the agent obeyed. The agent is
                                  the owner (Marina, S20). Three measurements (b1: 32 flags opened -> 0
                                  finds; b2: 10 dismissed reopened -> 0 losses; S3: 20 -> 0) say the flag
                                  finds nothing. What DOES matter is "the robot never saw this store" —
                                  that is not a flag, it is the bottom list.
    maturity                      established/emerging. Computed from revenue, which the slice parser had
                                  been eating -> the input was dead. Repaired the input: now 250/250 are
                                  "established". A field identical for every store carries zero bits.
    hero_confidence               `low` is a property of the SOURCE (store has no best-selling collection),
                                  not of the robot's certainty. 95 flags in b2, none actionable.
    desc_confidence, storefront_pos, invest (desc_len/imgs/variants/badges), anchor, price_raw
                                  Never once used to decide. The description itself is on the card.
    duplicate flags               `established`/`hero`/`mid`/`catalog-giant` restated columns already shown.
    currency_idx_mismatch         The index just copies the storefront's own claim, so it repeats the lie
                                  (magnetichoop: index USD, cart HKD) AND invents new ones (27/250 say USD
                                  for UK/CA/AU stores). Not a source of truth, not a signal.

  HIDDEN — collected and kept, but not in the way while deciding (Marina S20: hidden != deleted):
    visits (orders the batch), social (needed for Notion), merchant, theme, variants, reviews,
    new_products_30d, conv_batch, sl_rev, product URLs, bullets, images.
    Printed by `--all`, and by the layer-2 detail pass over the stores the agent actually picked.

  SHOWN — everything a "go and look?" decision rests on:
    domain + the store's own pitch · tier/score (a SORT-AID, printed small) · country · created ·
    catalog size + the index's price envelope · product_class · kind · пустышка ·
    banner hero + all 3 products (title, price, in_range, description).

  THE PRICE ENVELOPE is the one signal ShopHunter structurally cannot have: min/avg/max across the store's
  WHOLE catalog, straight from the index — not from the handful of items products.json exposes. It is how
  the robot admits "the products I am showing you are not what this store sells" (bumpeeztoys: shows a
  $9.99 remote; the index says the catalog runs to $379.99). No threshold, no flag, no machine verdict:
  the fact is printed, the agent decides.

  THE BOTTOM LIST: stores the robot never saw get NO tier and NO score. Calling an unopened store "Tier A"
  is a lie (ShopHunter has always listed its dead stores separately, and we never copied that).

CERT: the field list is DERIVED from what was actually printed, never declared. The old contract compared
two hand-written constants — two cooks showing each other identical copies of a recipe nobody had tasted.

Usage: sl_card_text_TEST.py <enriched.json> [--all]
"""
import json, re, sys

DESC = 150
PITCH = 110

# Fields a VERDICT rests on. Parity compares these — not decoration (images in HTML, URLs in text).
VERDICT_FIELDS = ["domain", "tier", "score", "country", "created", "catalog_pc", "price_envelope",
                  "product_class", "kind", "pust", "home_pitch", "currency_suspect", "homepage_blocked",
                  "home_hero", "tops3", "price", "in_range", "desc", "unreachable_reason",
                  "block", "shelf", "overlap"]

# S20 — two blocks, never one. `src` says which shelf a product came from; the label tells the agent
# what those three products are WORTH. A product read off /products.json proves nothing: that endpoint
# returns the catalog in publish order (measured: 28 of the 30 stores whose "hero" silently changed
# overnight sat on that rung). A product read off the sales shelf is what people actually buy here.
# S21: the shelf is now found by the MEANING of its name, so its handle can be anything the merchant
# invented (`best-selling-products`, `top-sellers`…). A label that enumerates spellings would then call a
# real sales shelf "случайная выборка" — the exact class of lie we are removing. Match the same way.
SALES_NAME = re.compile(r"best[-_ ]?sell|bestseller|top[-_ ]?seller|most[-_ ]?popular")
FRONT_SRC = ("frontpage", "featured", "homepage")


def block_of(src):
    if src and SALES_NAME.search(src):
        return "ПРОДАЖИ"
    if src in FRONT_SRC:
        return "ВИТРИНА"
    return "СЛУЧАЙНАЯ ВЫБОРКА"


SHELF_RU = {"best-selling": "продажи", "bestsellers": "продажи", "best-sellers": "продажи",
            "shelf-best-selling": "продажи", "frontpage": "витрина", "featured": "витрина",
            "homepage": "главная", "all": "⚠ случайная выборка каталога", "-": "—"}


def shelf_label(hero_src):
    def one(x):
        x = x.strip()
        if SALES_NAME.search(x):
            return "продажи"
        return SHELF_RU.get(x, x)
    return " + ".join(one(x) for x in (hero_src or "?").split("+"))
HIDDEN_FIELDS = ["visits", "social", "merchant", "theme", "variants", "reviews", "new_products_30d",
                 "conv_batch", "sl_rev", "product_url", "bullets", "img"]

rows = json.load(open(sys.argv[1]))
SHOW_ALL = "--all" in sys.argv
rendered = set()          # what this run ACTUALLY printed


def mark(*names):
    rendered.update(names)


def s(x, n=70):
    return "" if x is None else str(x).replace("\n", " ").strip()[:n]


def money(p):
    """S21, Marina: обе стороны — валюта магазина → доллары. Курса нет → доллары не выдумываем.
    Старая запись `$87.04/HKD` читалась двусмысленно: то ли 87 долларов, то ли 87 гонконгских."""
    cur = p.get("cur") or "?"
    raw = p.get("price_raw")
    if p.get("rate_unknown"):
        amt = f"{raw:,.2f}".replace(",", " ") if isinstance(raw, (int, float)) else "?"
        return f"{amt} {cur} (курс неизв.)"
    if p.get("price_unknown") or p.get("price") in (None, 0):
        return "$?"
    if cur and cur != "USD" and isinstance(raw, (int, float)):
        amt = f"{raw:,.2f}".replace(",", " ")
        return f"{amt} {cur} → ${p['price']}"
    return f"${p['price']}"


def envelope(r):
    """catalog size + what the INDEX knows about this store's prices."""
    pc = r.get("sl_pc")
    lo, hi = r.get("sl_min"), r.get("sl_max")
    if pc is None and lo is None:
        return ""
    mark("catalog_pc")
    out = f"каталог {pc} тов" if pc is not None else "каталог ?"
    if r.get("envelope_broken"):
        mark("price_envelope")
        out += " · ⚠ конверт не разобран"      # S21: max < min → ошибка разбора, а не факт
    elif lo is not None and hi is not None:
        mark("price_envelope")
        out += f" · индекс знает цены ${lo}–${hi}"
    return out


# ---- split: the robot saw the store, or it did not -------------------------------------------------
seen = [r for r in rows if r.get("reachable") and (r.get("tops3") or [])]
unseen = [r for r in rows if not (r.get("reachable") and (r.get("tops3") or []))]
order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3}
seen.sort(key=lambda r: (order.get(r.get("tier"), 9), -(r.get("score") or 0)))

tops_avail = sum(len(r.get("tops3") or []) for r in rows)
tops_printed = 0
banners = 0

print(f"# STAGE-2 КАРТОЧКА (поверхность агента) — {len(rows)} магазинов "
      f"· {len(seen)} робот увидел · {len(unseen)} не увидел")
print("# tier/score = сортировка, НЕ качество. Читаю все. Решение «идти смотреть» принимаю я, не робот.")
print("#" + "=" * 106)

for i, r in enumerate(seen, 1):
    dom = r.get("domain") or "?"
    # mark() records only what is ACTUALLY printed — `kind` is marked below, where it prints.
    # (Its first run caught exactly this: `kind` was declared here but printed only for non-physical
    # stores, so the two surfaces' field lists diverged. The check earns its keep on day one.)
    mark("domain", "tier", "score", "country", "created", "product_class")
    head = (f"{i:3} [{r.get('tier','?'):>2}{r.get('score') or 0:>4}] {dom}"
            f"  {r.get('country') or '?'} {s(r.get('created'), 7)}"
            f" · {s(r.get('product_class'), 16)}")
    env = envelope(r)
    mark("shelf")
    print()
    print(head + (" · " + env if env else ""))
    print(f"      полка: {shelf_label(r.get('hero_src'))}")

    if r.get("pust"):
        mark("pust"); print("      ⚠ ПУСТЫШКА")
    if r.get("homepage_blocked"):
        mark("homepage_blocked")
        print("      ⚠ витрина не открылась — питча нет, робот видел только каталог")
    else:
        pitch = s(r.get("home_pitch"), PITCH)
        if pitch:
            mark("home_pitch"); print(f"      «{pitch}»")
    if r.get("currency_suspect"):
        mark("currency_suspect")
        print(f"      ⚠ валюта: витрина торгует в {r.get('store_currency')}, объявлено другое — цену подтвердить живьём")
    if r.get("kind") and r["kind"] != "physical":
        mark("kind"); print(f"      kind: {r['kind']}")

    hh = r.get("home_hero")
    if hh and hh.get("t"):
        banners += 1; mark("home_hero")
        if hh.get("in_clean"):
            print(f"   🏠 БАННЕР = один из товаров ниже: {s(hh.get('t'), 60)}")
        else:
            print(f"   🏠 БАННЕР ≠ подбор робота (смотри оба): {s(hh.get('t'), 60)}")

    for j, p in enumerate(r.get("tops3") or [], 1):
        tops_printed += 1
        mark("tops3", "price", "in_range", "desc", "block")
        ir = "IN" if p.get("in_range") else ("$?" if p.get("price_unknown") else "out")
        blk = block_of(p.get("src"))
        dup = ""
        if p.get("dup"):
            mark("overlap"); dup = " =дубль"
        print(f"   [{blk:>17}]{dup:8} {money(p):>10} [{ir}]  {s(p.get('t'), 60)}")
        d = s(p.get("desc"), DESC)
        if d:
            print(f"      {d}")
        if SHOW_ALL:
            mark("product_url", "bullets")
            if p.get("handle"):
                print(f"      https://{dom}/products/{p['handle']}")
            bl = " • ".join(s(b, 55) for b in (p.get("bullets") or [])[:3])
            if bl:
                print(f"      • {bl}")

    if SHOW_ALL:
        mark("visits", "social", "merchant", "new_products_30d", "conv_batch", "sl_rev")
        soc = " · ".join(f"{k}:{r.get(k)}" for k in ("fb", "ig", "tiktok", "pinterest") if r.get(k))
        print(f"      [скрытое] визиты {r.get('visits')} · мерчант {s(r.get('store'), 24)}"
              f" · новинок30д {r.get('new_products_30d')} · конв {r.get('conv_batch')}"
              f" · выручка/год {r.get('sl_rev')}" + (f" · {soc}" if soc else ""))

# ---- the bottom list: no tier, no score, no pretending ----------------------------------------------
print()
print("#" + "=" * 106)
print(f"# РОБОТ НЕ УВИДЕЛ ЭТИ МАГАЗИНЫ ({len(unseen)}) — тира нет, оценки нет. Открываю руками, все.")
for r in unseen:
    mark("unreachable_reason")
    env = envelope(r)
    print(f"   {r.get('domain'):<38} {s(r.get('reason') or 'товары не извлечены', 56)}"
          + (f"   [{env}]" if env else ""))

print()
print(f"# КАРТОЧКА НАПЕЧАТАНА ПОЛНОСТЬЮ — {'PASS' if tops_printed == tops_avail else 'STOP — ТОВАРЫ СКРЫТЫ'}: "
      f"{tops_printed}/{tops_avail} товаров · {banners} баннеров · {len(seen)} видимых · {len(unseen)} не увиденных.")
print("# Данные (охват/полнота) сертифицирует sl_qa.py / sl_accept_chunk.py, не этот файл.")
vf = sorted(f for f in rendered if f in VERDICT_FIELDS)
print(f"CERT surface=agent-text stores={len(rows)} products={tops_printed} banners={banners} "
      f"unseen={len(unseen)} verdict_fields={','.join(vf)}")
sys.exit(0 if tops_printed == tops_avail else 1)
