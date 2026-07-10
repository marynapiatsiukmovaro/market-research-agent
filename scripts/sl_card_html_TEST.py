#!/usr/bin/env python3
"""Stage-2 card — FOUNDER surface (HTML). S20 rebuild, Marina-directed. Twin of sl_card_text_TEST.py.

Same card, two pairs of eyes. Deleted / hidden / shown — the reasoning lives in the text twin's header.
Short version:
  DELETED  needs_live · maturity · hero_confidence · desc_confidence · storefront_pos · invest · anchor ·
           duplicate flags · currency_idx_mismatch      (they lied, or never moved a decision)
  HIDDEN   visits · social · merchant · theme · variants · reviews · new30d · conv · yearly revenue
           -> one button, "показать скрытые поля". Hidden is not deleted (Marina S20).
  SHOWN    domain + the store's own pitch · tier/score (small, a sort-aid) · country · created ·
           catalog size + the index's price envelope · product_class · kind · пустышка ·
           banner hero + all 3 products (photo, price, in_range, description)
  BOTTOM   stores the robot never saw: no tier, no score. Naming an unopened store "Tier A" is a lie.

CERT: the verdict-field list is DERIVED from what was actually rendered, never declared, so parity can
fail for a real reason. (The old check compared two hand-copied constants.)

Usage: sl_card_html_TEST.py <enriched.json> <out.html> "<title>" "<banner>"
"""
import json, html, re, sys

VERDICT_FIELDS = ["domain", "tier", "score", "country", "created", "catalog_pc", "price_envelope",
                  "product_class", "kind", "pust", "home_pitch", "currency_suspect", "homepage_blocked",
                  "home_hero", "tops3", "price", "in_range", "desc", "unreachable_reason",
                  "block", "shelf", "overlap"]

# S21: shelf found by MEANING of the name → the label must match the same way, or a real sales shelf
# gets printed as "случайная выборка" — the very class of lie we are removing.
SALES_NAME = re.compile(r"best[-_ ]?sell|bestseller|top[-_ ]?seller|most[-_ ]?popular")
FRONT_SRC = ("frontpage", "featured", "homepage")
SHELF_RU = {"best-selling": "продажи", "bestsellers": "продажи", "best-sellers": "продажи",
            "shelf-best-selling": "продажи", "frontpage": "витрина", "featured": "витрина",
            "homepage": "главная", "all": "⚠ случайная выборка каталога", "-": "—"}


def block_of(src):
    if src and SALES_NAME.search(src):
        return "ПРОДАЖИ"
    return "ВИТРИНА" if src in FRONT_SRC else "СЛУЧАЙНАЯ ВЫБОРКА"


def shelf_label(hero_src):
    def one(x):
        x = x.strip()
        return "продажи" if SALES_NAME.search(x) else SHELF_RU.get(x, x)
    return " + ".join(one(x) for x in (hero_src or "?").split("+"))

inp, outp, title = sys.argv[1], sys.argv[2], sys.argv[3]
banner = sys.argv[4] if len(sys.argv) > 4 else ""
rows = json.load(open(inp))
rendered = set()


def mark(*n):
    rendered.update(n)


def esc(x, n=400):
    return html.escape(str(x if x is not None else ""))[:n]


def link(u, txt):
    if not u:
        return ""
    u = str(u)
    if not u.startswith("http"):
        u = "https://" + u
    return f"<a href='{html.escape(u)}'>{txt}</a>"


seen = [r for r in rows if r.get("reachable") and (r.get("tops3") or [])]
unseen = [r for r in rows if not (r.get("reachable") and (r.get("tops3") or []))]
order = {"A": 0, "B": 1, "C": 2, "PRICE-CHECK": 3}
seen.sort(key=lambda r: (order.get(r.get("tier"), 9), -(r.get("score") or 0)))

tops_avail = sum(len(r.get("tops3") or []) for r in rows)
# S20: the card now carries TWO blocks (up to 6 products). The old counter still said min(...,3):
# the table would render six rows while certifying three. Parity caught it — that is its job.
tops_rendered = sum(len(r.get("tops3") or []) for r in seen)
banners = 0


def envelope(r):
    pc, lo, hi = r.get("sl_pc"), r.get("sl_min"), r.get("sl_max")
    if pc is None and lo is None:
        return "<i>—</i>"
    mark("catalog_pc")
    out = f"<b>{esc(pc)}</b> товаров" if pc is not None else "? товаров"
    if r.get("envelope_broken"):
        mark("price_envelope")
        out += "<br><span class=warn>конверт не разобран</span>"   # S21: max < min → parse failure, not data
    elif lo is not None and hi is not None:
        mark("price_envelope")
        out += f"<br><span class=k>индекс знает цены<br>${esc(lo)} – ${esc(hi)}</span>"
    return out


def price_cell(t):
    """S21, Marina: показывать обе стороны — валюта магазина → доллары.
    А если курса нет, доллары НЕ выдумывать и вердикт «out» НЕ ставить: судить о цене нечем."""
    cur = t.get("cur") or "?"
    raw = t.get("price_raw")
    if t.get("rate_unknown"):
        amt = f"{raw:,.2f}".replace(",", " ") if isinstance(raw, (int, float)) else "?"
        return (f"<b>{amt} {esc(cur)}</b> <span class=warn>курс неизвестен</span>", "")
    if t.get("price_unknown") or t.get("price") in (None, 0):
        return ("<b>$?</b>", "<span class='out'>$?</span>")
    usd = f"<b>${esc(t.get('price'))}</b>"
    if cur and cur != "USD" and isinstance(raw, (int, float)):
        amt = f"{raw:,.2f}".replace(",", " ")
        usd = f"<span class=k>{amt} {esc(cur)} →</span> {usd}"
    flag = ("<span class='in'>✓ IN</span>" if t.get("in_range") else "<span class='out'>✗ out</span>")
    return (usd, flag)


def products_cell(r):
    global banners
    dom = r.get("domain") or ""
    out = []
    hh = r.get("home_hero")
    if hh and hh.get("t"):
        banners += 1
        mark("home_hero")
        same = hh.get("in_clean")
        purl = f"https://{dom}/products/{hh.get('handle')}" if hh.get("handle") else f"https://{dom}"
        note = "= один из товаров ниже" if same else "≠ подбор робота — смотри ОБА"
        bg = "#eef4ff" if same else "#fff2e0"
        thumb = (f"<img src='{esc(hh.get('img'), 900)}'>" if hh.get("img") else "")
        out.append(f"<div class=ban style='background:{bg}'>{thumb}🏠 <b>БАННЕР</b> "
                   f"<span class=k>{note}</span><br>{link(purl, esc(hh.get('t'), 90))}</div>")
    for t in (r.get("tops3") or [])[:6]:
        mark("tops3", "price", "in_range", "desc", "block")
        price_html, flag = price_cell(t)
        purl = f"https://{dom}/products/{t.get('handle')}" if t.get("handle") else f"https://{dom}"
        thumb = (f"<a href='{html.escape(purl)}'><img src='{esc(t.get('img'), 900)}'></a>" if t.get("img") else "")
        blk = block_of(t.get("src"))
        bcls = "bsale" if blk == "ПРОДАЖИ" else ("bfront" if blk == "ВИТРИНА" else "brand")
        dup = ""
        if t.get("dup"):
            mark("overlap"); dup = " <span class=dup>= то же, что в продажах</span>"
        out.append(f"<div class=prod>{thumb}<span class='blk {bcls}'>{blk}</span>{dup} "
                   f"{price_html} {flag} {link(purl, esc(t.get('t'), 90))}"
                   f"<br><span class=d>{esc(t.get('desc'), 190)}</span></div>")
    return "".join(out) or "<i>—</i>"


h = ["<!doctype html><html lang=ru><meta charset=utf-8><title>", html.escape(title), "</title><style>",
     "body{font:12.5px/1.5 -apple-system,Arial;margin:18px;color:#1a1a1a}h1{font-size:17px}",
     ".banner{background:#fff4e6;border:1px solid #f0c890;padding:8px 12px;border-radius:6px;margin:8px 0}",
     ".cert{background:#eafff0;border:2px solid #2faa55;padding:10px 14px;border-radius:8px;margin:10px 0}",
     ".cert.stop{background:#fff0f0;border-color:#d33}",
     "table{border-collapse:collapse;font-size:11.5px;width:100%}td,th{border:1px solid #ccc;padding:5px 7px;vertical-align:top}",
     "th{background:#222;color:#fff;position:sticky;top:0;text-align:left}",
     "tr.A{background:#f5fff5}tr.B{background:#fcfffa}",
     ".blk{font-size:9px;font-weight:700;padding:1px 5px;border-radius:3px;letter-spacing:.3px}",
     ".bsale{background:#e6f4ea;color:#1a6b32}.bfront{background:#fff1e0;color:#8a4b00}",
     ".brand{background:#fde8e8;color:#a11}.dup{font-size:9px;color:#888}",
     ".shelf{font-size:10px;color:#666;margin-top:3px}",
     "a{color:#1763d6;text-decoration:none}.k{color:#888;font-size:10px}.d{color:#444}",
     "img{max-width:58px;max-height:58px;border-radius:4px;float:left;margin:0 6px 3px 0}",
     ".prod{overflow:hidden;margin-bottom:7px;clear:both}.ban{overflow:hidden;margin-bottom:7px;padding:4px;border-radius:4px;clear:both}",
     ".in{color:#080;font-weight:600}.out{color:#c00}.pust{color:#d33;font-weight:700}",
     ".warn{color:#b45309}.hid{display:none}.hid.on{display:table-cell}",
     "button{font:12px -apple-system;padding:6px 12px;border-radius:6px;border:1px solid #999;background:#fff;cursor:pointer}",
     "h2{font-size:14px;margin-top:26px}", "</style><body>"]
h.append(f"<h1>{html.escape(title)}</h1>")
h.append(f"<div class=banner><b>tier/score = сортировка, не качество.</b> Решение «идти смотреть» принимает агент, "
         f"не робот. Цена — ориентир, а не приговор: вниз по цене магазин не роняем, подтверждаем живьём.<br>"
         f"{html.escape(banner)}</div>")
h.append("<button onclick=\"document.querySelectorAll('.hid').forEach(e=>e.classList.toggle('on'));"
         "this.textContent=this.textContent[0]=='П'?'Скрыть служебные поля':'Показать скрытые поля'\">"
         "Показать скрытые поля</button>")

cols = ["#", "домен · о чём магазин · полка", "тир·score", "страна<br>основан", "каталог · цены индекса",
        "класс товара", "🏠 баннер · ПРОДАЖИ (что покупают) + ВИТРИНА (что показывают)"]
hidcols = ["визиты", "соцсети", "мерчант · новинки30д · конв · выручка/год"]
h.append("<table><tr>" + "".join(f"<th>{c}</th>" for c in cols)
         + "".join(f"<th class=hid>{c}</th>" for c in hidcols) + "</tr>")

for i, r in enumerate(seen, 1):
    dom = r.get("domain") or ""
    mark("domain", "tier", "score", "country", "created", "product_class")
    warn = []
    if r.get("pust"):
        mark("pust"); warn.append("<div class=pust>⚠ ПУСТЫШКА</div>")
    if r.get("homepage_blocked"):
        mark("homepage_blocked")
        warn.append("<div class=warn>⚠ витрина не открылась — питча нет, робот видел только каталог</div>")
    if r.get("currency_suspect"):
        mark("currency_suspect")
        warn.append(f"<div class=warn>⚠ валюта: витрина в {esc(r.get('store_currency'))}, объявлено другое "
                    f"— цену подтвердить живьём</div>")
    pitch = ""
    if not r.get("homepage_blocked") and r.get("home_pitch"):
        mark("home_pitch")
        pitch = f"<br><span class=k>{esc(r.get('home_pitch'), 200)}</span>"
    kind = ""
    if r.get("kind") and r["kind"] != "physical":
        mark("kind"); kind = f"<br><span class=k>kind: {esc(r.get('kind'))}</span>"
    soc = " ".join(filter(None, [link(r.get("fb"), "FB"), link(r.get("ig"), "IG"),
                                 link(r.get("tiktok"), "TT"), link(r.get("pinterest"), "Pin")]))
    mark("shelf")
    cells = [str(i),
             link(dom, esc(dom)) + pitch
             + f"<div class=shelf>полка: {esc(shelf_label(r.get('hero_src')))}</div>" + "".join(warn),
             f"<b>{esc(r.get('tier'))}</b> <span class=k>{esc(r.get('score'))}</span>",
             f"{esc(r.get('country'))}<br><span class=k>{esc(r.get('created'))[:10]}</span>",
             envelope(r),
             esc(r.get("product_class")) + kind,
             products_cell(r)]
    hid = [esc(r.get("visits")), soc or "<i>—</i>",
           f"{esc(r.get('store'), 26)}<br><span class=k>новинок30д {esc(r.get('new_products_30d'))} · "
           f"конв {esc(r.get('conv_batch'))} · выручка/год {esc(r.get('sl_rev'))}</span>"]
    h.append(f"<tr class='{esc(r.get('tier'))}'>" + "".join(f"<td>{c}</td>" for c in cells)
             + "".join(f"<td class=hid>{c}</td>" for c in hid) + "</tr>")
h.append("</table>")

# ---- bottom list: the robot never saw these. No tier, no score. ------------------------------------
h.append(f"<h2>Робот не увидел эти магазины ({len(unseen)}) — тира нет, оценки нет. Открываю руками, все.</h2>")
h.append("<table><tr><th>#</th><th>домен</th><th>что случилось</th><th>каталог · цены индекса</th></tr>")
for i, r in enumerate(unseen, 1):
    mark("unreachable_reason")
    h.append(f"<tr><td>{i}</td><td>{link(r.get('domain'), esc(r.get('domain')))}</td>"
             f"<td>{esc(r.get('reason') or 'товары не извлечены')}</td><td>{envelope(r)}</td></tr>")
h.append("</table>")

ok = tops_rendered == tops_avail
h.append(f"<div class='cert {'' if ok else 'stop'}'>"
         f"{'✅ <b>КАРТОЧКА НАПЕЧАТАНА ПОЛНОСТЬЮ.</b>' if ok else '⛔ <b>ЧАСТЬ КАРТОЧКИ СКРЫТА — НЕ АНАЛИЗИРОВАТЬ.</b>'} "
         f"{len(rows)} магазинов · {len(seen)} робот увидел · {len(unseen)} не увидел · "
         f"{tops_rendered}/{tops_avail} товаров · {banners} баннеров.<br>"
         f"<span class=k>Данные (охват/полнота) сертифицирует sl_qa.py / sl_accept_chunk.py, не эта таблица.</span></div>")
h.append("</body></html>")
open(outp, "w").write("\n".join(h))

vf = sorted(f for f in rendered if f in VERDICT_FIELDS)
print("HTML:", outp, f"| {len(seen)} видимых, {len(unseen)} не увиденных, {tops_rendered}/{tops_avail} товаров")
print(f"CERT surface=founder-html stores={len(rows)} products={tops_rendered} banners={banners} "
      f"unseen={len(unseen)} verdict_fields={','.join(vf)}")
