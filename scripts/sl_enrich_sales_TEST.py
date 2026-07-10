#!/usr/bin/env python3
"""ЗАХОД 2 (S21, Marina) — по принятому каркасу добираем блок ПРОДАЖИ.

Почему отдельным заходом. Один тяжёлый проход (обе полки + пагинация + валюта + самопроверки) слал ~15
запросов на магазин, и под воркерами эти магазины упирались в Cloudflare → reach 48%. Заход 1 (лёгкий
каркас, витрина) вернул reach 99.2%. Здесь мы НЕ трогаем каркас — читаем готовый `_P1_enriched.json` и
одним-двумя запросами на магазин добираем то, что реально ПОКУПАЮТ (Shopify `?sort_by=best-selling`), и
вписываем эти товары в начало карточки, помечая пересечение с витриной. Каркас уже принят и цел.

Формула score/тира — НЕ своя: импортируем `finalize()` из энричера, чтобы два захода не разошлись.

Usage: sl_enrich_sales_TEST.py <pass1_enriched> <out> <sentinel> [workers=6]
       (пути CWD-relative от logs/storeleads, как у энричера)
"""
import json, sys, time
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
sys.path.insert(0, "/opt/market-research-agent/scripts")
import sl_enrich4_TEST as E   # prod_row, usd, has, JUNK, PROXY, UA, sales_shelf, existing_collections, finalize

OUT = "/opt/market-research-agent/logs/storeleads"
INF, OUTF, SENT = sys.argv[1], sys.argv[2], sys.argv[3]
NW = int(sys.argv[4]) if len(sys.argv) > 4 else 6


def sales_rows(pg, dom):
    """The ПРОДАЖИ block — light: the sales-named collection (1 req) else ?sort_by=best-selling html."""
    colls = E.existing_collections(pg, dom, pages=1)
    rows, src = E.sales_shelf(pg, dom, colls)
    return rows, src


def to_top(r, store_cur):
    """A catalog row → a tops3 entry, in the exact shape the card renderers expect (same as pass 1)."""
    if r["price_raw"] <= 0:
        price, cur, rate, punk, runk = None, store_cur, None, True, False
    else:
        price, cur, rate = E.usd(r["price_raw"], store_cur)
        punk = price is None
        runk = rate is None
    t_inrange = (not punk) and price is not None and 39 <= price <= 170
    return {"src": r.get("src"), "dup": False, "t": r["t"][:60], "price": price, "price_raw": r["price_raw"],
            "cur": cur, "rate_unknown": runk, "k": r["k"], "pclass": r["pclass"], "pos": r["pos"],
            "desc": r["desc"][:550], "bullets": r.get("bullets", []), "img": r["img"],
            "handle": r.get("handle", ""), "price_unknown": punk, "in_range": t_inrange, "anchor": 0,
            "pust": E.has(r["t"] + " " + r["desc"], E.PUST), "desc_confidence": E.desc_conf(r["t"], r["desc"]),
            "invest": r["invest"]}


def work(args):
    wid, chunk = args
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, args=["--no-sandbox"], proxy=E.PROXY)
        pg = b.new_context(user_agent=E.UA, viewport={"width": 1400, "height": 1600}).new_page()
        for o in chunk:
            try:
                if not o.get("reachable"):
                    out.append(o); continue
                dom = o["domain"]
                store_cur = o.get("store_currency") or "USD"
                time.sleep(1.0)
                rows, src = sales_rows(pg, dom)
                sales = [to_top(r, store_cur) for r in rows if not E.has(r["t"], E.JUNK)]
                if sales:
                    # витрина-товары этого магазина уже в tops3 → помечаем пересечение
                    sales_handles = {t["handle"] for t in sales if t.get("handle")}
                    for t in o.get("tops3", []):
                        if t.get("handle") in sales_handles:
                            t["dup"] = True
                    o["tops3"] = sales + (o.get("tops3") or [])
                    o["hero_src"] = (src or "продажи") + " + " + (o.get("hero_src") or "-")
                    o["hero_confidence"] = "high"
                    # пере-выбор кандидата по объединённому набору — как в заходе 1
                    inr = [t for t in o["tops3"] if t["in_range"]]
                    known = [t for t in o["tops3"] if not t["price_unknown"]]
                    cand = inr[0] if inr else (known[0] if known else o["tops3"][0])
                    o["candidate"] = cand["t"]; o["price"] = cand["price"]; o["currency"] = cand["cur"]
                    o["in_range"] = cand["in_range"]; o["desc"] = cand["desc"]; o["image"] = cand["img"]
                    o["pust"] = cand["pust"]; o["kind"] = cand["k"]; o["product_class"] = cand["pclass"]
                    o["desc_confidence"] = cand["desc_confidence"]; o["storefront_pos"] = cand["pos"]
                out.append(o)
            except Exception as ex:
                o["sales_error"] = type(ex).__name__
                out.append(o)
        b.close()
    return out


if __name__ == "__main__":
    res = json.load(open(OUT + "/" + INF))
    t0 = time.time()
    chunks = [(w, res[w::NW]) for w in range(NW)]
    with Pool(NW) as pool:
        parts = pool.map(work, chunks)
    merged = [x for part in parts for x in part]
    merged = E.finalize(merged)          # ОДНА формула score/тира — общая с заходом 1
    order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3, "MANUAL": 4, "DROP-noPhysical": 5, "DROP": 6}
    merged.sort(key=lambda r: (order.get(r.get("tier"), 9), -r.get("score", -999)))
    json.dump(merged, open(OUT + "/" + OUTF, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    reach = sum(1 for r in merged if r.get("reachable"))
    with_sales = sum(1 for r in merged if any(t.get("src") and ("sell" in str(t["src"]) or "продаж" in str(t["src"]))
                                              for t in (r.get("tops3") or [])))
    errs = sum(1 for r in merged if r.get("sales_error"))
    open(OUT + "/" + SENT, "w").write("done %d secs=%d reach=%d with_sales=%d errs=%d tiers=%s" % (
        len(merged), round(time.time()-t0), reach, with_sales, errs, dict(Counter(r.get("tier") for r in merged))))
    print("=== ЗАХОД 2 (ПРОДАЖИ) DONE ===", len(merged), "secs", round(time.time()-t0),
          "reach", reach, "with_sales", with_sales, "errs", errs)
