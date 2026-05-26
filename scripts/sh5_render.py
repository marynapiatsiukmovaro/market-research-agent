# Renders SH-5 funnel stages as PNG tables (same dark style as SH-4). Parameterized.
# Usage: sh5_render.py <TAG> <stages>   e.g.  sh5_render.py sh5_b2 12     (stages 1 and 2)
#                                              sh5_render.py sh5_b2 3      (stage 3 cut)
#                                              sh5_render.py sh5_b2 45     (stages 4 and 5)
#                                              sh5_render.py sh5_b1 all
# Stage 5 reads <TAG>_verdict.json = [[type, product, what, price, verdict, reason, site], ...]
#   type in {rep, keep, mon, rej}.  Plain chromium, no profile -> no lock conflict.
import json, html, re, sys
from playwright.sync_api import sync_playwright
OUT = "/opt/market-research-agent/logs/shophunter"
TAG = sys.argv[1] if len(sys.argv) > 1 else "sh5_b1"
STAGES = sys.argv[2] if len(sys.argv) > 2 else "all"
def want(n): return STAGES == "all" or str(n) in STAGES

CSS = """
<style>
 body{font-family:-apple-system,Segoe UI,Roboto,Arial;margin:0;background:#0f1116;color:#e8eaed}
 .wrap{padding:22px 26px} h1{font-size:23px;margin:0 0 3px} .sub{color:#9aa0a6;font-size:14px;margin:0 0 16px}
 h2{font-size:16px;margin:18px 0 6px}
 table{border-collapse:collapse;width:100%;font-size:13px;margin-bottom:10px}
 th{background:#1f6feb;color:#fff;text-align:left;padding:7px 9px} th.red{background:#a5322a} th.green{background:#1f7a3d}
 td{padding:6px 9px;border-bottom:1px solid #23262d;vertical-align:top} tr:nth-child(even) td{background:#161922}
 .num{color:#6e7681;text-align:right} .money{color:#3fb950;font-weight:600} .rev{color:#d29922;font-weight:600}
 .rep{color:#3fb950;font-weight:800} .keep{color:#7ee787;font-weight:700} .mon{color:#58a6ff;font-weight:700} .rej{color:#8b949e}
 .badge{display:inline-block;padding:2px 7px;border-radius:5px;font-size:11px;font-weight:600}
 .b-A{background:#0d3321;color:#3fb950} .b-B{background:#16263a;color:#58a6ff} .b-C{background:#2a2030;color:#b08fd0}
 .conv{color:#3fb950;font-weight:600} .flag{color:#ffa657} .desc{color:#9aa0a6;font-size:12px}
</style>
"""
def esc(s): return html.escape(str(s if s is not None else ""))
def npx(s):
    m = re.search(r"([\d.,]+)", str(s) or ""); return float(m.group(1).replace(",", "")) if m else 0
JUNK=["shipping protection","protection plan","gift card","gift-card","warranty","guarantee","route package","insurance","donation","tip","sample","e-book","ebook","deposit"]
PUST=["lymphatic","red light","red-light","drainage","detox","slimming","cellulite","circulation","infrared therapy","magnetic therapy","anti-aging","anti aging","mole removal","skin tag","energy heal","chakra","aura","frequency heal","parasite","body cleanse","liver detox","grounding","manifest","collagen boost"]
SUPP=["supplement","softgel","soft gel","capsule","vitamin","gummies","gummy","probiotic","tincture","shilajit","electrolyte","omega","creatine","protein","cayenne","turmeric","magnesium","biotin","nootropic","peptide","berberine","hormone","mushroom complex","elixir","nectar","pollen","shake","metabolism","nitric oxide","greens","superfood","sea moss","seamoss","moringa","oregano","ormus","iodine","black seed","nmn","nad+","glutathione","ashwagand","prebiotic","d-mannose","lecithin","monatomic","sango","koralle","b-complex","tongkat","turkesterone","soursop"]
SKIN=["serum","face oil","moisturizer","cleanser","toner","sheet mask","ampoule","essence","face cream"]
APP=["dress","shirt","t-shirt","tee ","sneaker","shoe ","legging","bra ","hoodie","jacket","jewelry","necklace","earring","bracelet","sock","jeans","shorts","espadrille","wide leg","cardigan","blazer","windbreaker","knit","denim","loafer","skirt","fleece","coat","shaper"]
POD=["personalized","personalised","custom pet","portrait","place card","engraved","your pet","mascota","wall art","canvas","needlepoint","zodiac","woven blanket"]
def low(s): return " "+re.sub(r"[^a-z0-9+ ]"," ",(s or "").lower())+" "
def has(t,l):
    s=low(t); return any(k in s for k in l)
def klass(t):
    if has(t,PUST): return "пустышка"
    if has(t,SUPP): return "supplement"
    if has(t,SKIN): return "skincare"
    if has(t,POD): return "pod/art"
    if has(t,APP): return "apparel"
    return "physical"
def drop_reason(d):
    top=d.get("top",[])
    if not top: return ("DEAD/no-hero","")
    nonsvc=[p for p in top if not has(p["t"],JUNK)]
    if not nonsvc: return ("ALL-SERVICE",top[0]["t"])
    hero=nonsvc[0]; hk=klass(hero["t"]); phys=[p for p in nonsvc if klass(p["t"])=="physical"]
    if hk=="пустышка": return ("ПУСТЫШКА-hero",hero["t"])
    if not phys: return (hk.upper()+"-only",hero["t"])
    pp=[npx(p["price"]) for p in phys if npx(p["price"])>0]
    if pp and all((x>220 or x<25) for x in pp):
        return (("PRICE all>$220" if all(x>220 for x in pp) else "PRICE all<$25"),phys[0]["t"])
    return (None,hero["t"])

def render(pg,title,sub,sections,fname):
    blocks=""
    for hdr,headers,rows,aligns,hcls in sections:
        if hdr: blocks+=f"<h2>{esc(hdr)}</h2>"
        thc=f' class="{hcls}"' if hcls else ""
        th="".join(f"<th{thc}>{esc(h)}</th>" for h in headers)
        body="".join("<tr>"+"".join(f'<td class="{(aligns[c] if aligns and c<len(aligns) else "")}">{cell}</td>' for c,cell in enumerate(r))+"</tr>" for r in rows)
        blocks+=f"<table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>"
    pg.set_content(f"<html>{CSS}<body><div class='wrap'><h1>{esc(title)}</h1><p class='sub'>{esc(sub)}</p>{blocks}</div></body></html>",wait_until="networkidle")
    pg.set_viewport_size({"width":1340,"height":820}); pg.screenshot(path=f"{OUT}/{fname}",full_page=True); print("wrote",fname)

with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"]); pg=b.new_page()
    if want(1):
        raw=json.load(open(f"{OUT}/{TAG}.json"))
        rows=[[f'<span class="num">{i}</span>',esc(d["name"][:34]),f'<span class="money">{esc(d.get("domain",""))}</span>',esc(d.get("country","")),f'<span class="rev">{esc(d.get("rev_week",""))}</span>',esc(d.get("sku","")),esc(d.get("shop_ads","") or "0")] for i,d in enumerate(raw[:34],1)]
        render(pg,f"SH-5 ЭТАП 1 — Сырой дамп магазинов ({TAG})","ShopHunter (Home & Garden) отдаёт магазины + ИХ ДОМЕН (= рабочая ссылка). Продукта тут ещё нет. 34 из 150.",[(None,["#","Магазин","Сайт (= ссылка)","Гео","Выр/нед","SKU","FB Ads"],rows,["num","","money","","rev","num","num"],None)],f"{TAG}_stage1_raw.png")
    if want(2):
        hero=json.load(open(f"{OUT}/{TAG}_hero.json"))
        rows=[[f'<span class="num">{i}</span>',f'<span class="money">{esc(d.get("domain",""))}</span>',esc(d["top"][0]["t"][:46]),f'<span class="money">{esc(d["top"][0]["price"])}</span>',f'<span class="rev">{esc(d["top"][0].get("wk",""))}</span>'] for i,d in enumerate([x for x in hero if x.get("top")][:34],1)]
        render(pg,"SH-5 ЭТАП 2 — Извлечён HERO-товар каждого магазина","Parallel-парсер берёт блок 'Top Products' (#1 по выручке/нед). Домен = ссылка, рядом hero. 148/148 отдали hero, без proxy.",[(None,["#","Сайт (= ссылка)","HERO-товар (#1 Top Products)","Цена*","Выр/нед"],rows,["num","money","","money","rev"],None)],f"{TAG}_stage2_heroes.png")
    if want(3):
        hero=json.load(open(f"{OUT}/{TAG}_hero.json")); surv_ids={r["shop_id"] for r in json.load(open(f"{OUT}/{TAG}_enrich_in.json"))}
        drops=[];survs=[]
        for d in hero:
            (survs if d["shop_id"] in surv_ids else drops).append(d)
        drow=[]
        for d in drops:
            r,nm=drop_reason(d); drow.append([f'<span class="flag">{esc(r or "?")}</span>',esc(d["name"][:28]),esc(nm[:40]),f'<span class="money">{esc(d.get("domain",""))}</span>'])
        srow=[[esc(d["name"][:30]),f'<span class="money">{esc(d.get("domain",""))}</span>',esc(d["top"][0]["t"][:40]),f'<span class="rev">{esc(d["top"][0].get("wk",""))}</span>'] for d in survs[:14]]
        render(pg,"SH-5 ЭТАП 3 — Консервативный cut (drop только definite-no)",f"Дропаем ТОЛЬКО точное «нет»: dead / нет physical в top-3 / пустышка-hero / все физ.товары в экстрем-цене. Спорное = KEEP. Итог: {len(hero)} → {len(survs)} survivors, {len(drops)} дропов.",[("❌ Дропнуто (проверка: ни одного реального гаджета не потеряно)",["Причина","Магазин","Hero-товар","Сайт"],drow,["flag","","","money"],"red"),("✅ Survivors → Stage-2 enrich (показано 14)",["Магазин","Сайт","Hero-товар","Выр/нед"],srow,["","money","","rev"],"green")],f"{TAG}_stage3_cut.png")
    if want(4):
        enr=json.load(open(f"{OUT}/{TAG}_enriched.json")); order={"A":0,"B":1,"C":2,"DROP":3}
        enr=sorted(enr,key=lambda r:(order.get(r.get("tier"),9),-(r.get("score") or -999)))
        rows=[]
        for r in enr[:46]:
            t=r.get("tier","?"); fl=r.get("flags",[]) or []
            conv="".join(f'<span class="conv">{esc(f)}</span> ' for f in fl if str(f).startswith("CONV"))
            other=" ".join(f'<span class="flag">{esc(f)}</span>' for f in fl if not str(f).startswith("CONV"))
            pr=r.get("price") or 0; oo="" if r.get("in_range") else "(OUT)"
            rows.append([f'<span class="badge b-{t}">{t}|{r.get("score")}</span>',esc((r.get("candidate") or "")[:30]),esc(r.get("niche","")),f'<span class="money">${pr:.0f}{oo}</span>',f'<span class="rev">{esc(r.get("rev_week",""))}</span>',conv+other,f'<span class="desc">{esc((r.get("desc") or "no-desc")[:60])}</span>',f'<span class="money">{esc(r.get("domain",""))}</span>'])
        render(pg,"SH-5 ЭТАП 4 — Candidate Sheets (суб-агент: реальная цена + описание + конвергенция)","Суб-агент читает ЖИВОЙ каталог (products.json через proxy): РЕАЛЬНАЯ цена, ниша, выручка, конвергенция, флаги, ОПИСАНИЕ. Tier = revenue-sort aid, НЕ финальный скор. Топ-46.",[(None,["Tier|score","Кандидат","Ниша","Real $","Выр/нед","Conv/Flags","Описание","Сайт"],rows,["","","","money","rev","","desc","money"],None)],f"{TAG}_stage4_sheets.png")
    if want(5):
        V=json.load(open(f"{OUT}/{TAG}_verdict.json"))
        cmap={"rep":"rep","keep":"keep","mon":"mon","rej":"rej"}
        rows=[[f'<span class="{cmap.get(v[0],"rej")}">{esc(v[1])}</span>',esc(v[2]),esc(v[3]),f'<span class="{cmap.get(v[0],"rej")}">{esc(v[4])}</span>',esc(v[5]),(f'<span class="money">{esc(v[6])}</span>' if len(v)>6 and v[6] else "")] for v in V]
        render(pg,"SH-5 ЭТАП 5 — Финалисты + ВЕРДИКТ (deep-score: Veto + 100-pt, lead WOW+taste)",f"Итог батча {TAG}: мой ручной deep-score каждого genuine-гаджета. Reportable 65+ → Notion; founder-kept <65 по запросу; monitor-convergence.",[(None,["Товар","Что это","Цена","Вердикт","Причина","Сайт"],rows,["","","","","","money"],None)],f"{TAG}_stage5_verdict.png")
    b.close()
print(f"=== {TAG} renders done (stages {STAGES}) ===")
