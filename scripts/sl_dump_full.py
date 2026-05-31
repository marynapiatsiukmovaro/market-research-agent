#!/usr/bin/env python3
"""FULL windowed dump of a subcategory >=2020 via cracked Bleve bq. Bypasses 25k ceiling by
splitting created into date windows (each <25k), paginates each fully, merges/dedupes,
sorts by Est Visits, saves JSON + a styled HTML table. VPS.
Usage: python3 scripts/sl_dump_full.py "<cat path>" <slug>"""
import json, sys, time, html
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
CAT=sys.argv[1] if len(sys.argv)>1 else "/Home & Garden/Home Improvement"
SLUG=sys.argv[2] if len(sys.argv)>2 else "home_improvement"
# date windows (each proven <25k for HI; generic-safe). Last window open-ended (min only).
WINDOWS=[("2020-01","2022-12"),("2023-01",None)]
PS=200  # try larger page size to cut request count
FETCH="""async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {total:j&&j.totalHits, next:j&&j.next_cursor, n:(j&&j.domains||[]).length, domains:(j&&j.domains)||[]};
}"""
def crat(lo,hi):
    o={"field":"cratyyyymm","min":lo,"inclusive_min":True}
    if hi: o["max"]=hi; o["inclusive_max"]=True
    return o
def bq_for(lo,hi):
    return {"must":{"conjuncts":[{"field":"p","term":"1"},{"field":"ds","term":"1"},
            {"field":"cat","match":CAT},crat(lo,hi)]}}
def soc(ids,kind):
    for it in ids or []:
        u=str(it.get('full_value') or it.get('value') or '')
        if kind in u.lower(): return u
    return ''
def row(d):
    ids=d.get('identifiers')
    return {"domain":d.get('name') or d.get('tld1'),"merchant":d.get('merchantName'),
      "country":d.get('countryCode'),"loc":d.get('loc'),"lang":d.get('langn'),
      "created":str(d.get('createdAt') or '')[:10],
      "visits":d.get('mvis'),"pageviews":d.get('mpv'),"sales":d.get('erf'),
      "avg_price":d.get('apf'),"min_price":d.get('minpf'),"max_price":d.get('maxpf'),
      "avg_weight":d.get('apw'),"products":d.get('pc'),"variants":d.get('varc'),
      "app_spend":d.get('masf'),"rank":d.get('rank'),"prank":d.get('prank'),
      "theme":d.get('themeName'),"last_theme":d.get('ltheme'),
      "meta_desc":(d.get('md') or ''),
      "comb_reviews":d.get('combrs'),"tp_reviews":d.get('tprs'),
      "fb":soc(ids,'facebook'),"ig":soc(ids,'instagram'),
      "tiktok":soc(ids,'tiktok'),"pinterest":soc(ids,'pinterest')}
seen={}; rows=[]; server_totals=[]
t0=time.time()
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    for lo,hi in WINDOWS:
        base={"bq":json.dumps(bq_for(lo,hi)),"ps":PS}
        r=pg.evaluate(FETCH,json.dumps(base)); tot=r.get("total"); server_totals.append((lo,hi,tot))
        pgsize=r.get("n") or 0
        print(f"[window {lo}..{hi or 'now'}] server_total={tot} pagesize={pgsize}",flush=True)
        if tot and tot>=25000: print(f"  !! WARNING window >=25000 ({tot}) — would hit ceiling, needs finer split",flush=True)
        def ingest(ds):
            for d in ds:
                i=d.get("id")
                if i not in seen: seen[i]=1; rows.append(row(d))
        ingest(r.get("domains") or []); nxt=r.get("next"); page=1
        while nxt:
            r=pg.evaluate(FETCH,json.dumps({**base,"cursor":nxt})); time.sleep(0.5)
            ds=r.get("domains") or []
            if not ds: break
            ingest(ds); nxt=r.get("next"); page+=1
            if page%20==0: print(f"    ...{lo}: page {page}, collected so far {len(rows)}",flush=True)
    b.close()
rows.sort(key=lambda x:(x["visits"] or 0),reverse=True)
json.dump(rows,open(f"{OUT}/{SLUG}_full.json","w"),ensure_ascii=False)

# ---------- HTML ----------
def fnum(v):
    try: return f"{int(v):,}"
    except: return "" if v in (None,"") else html.escape(str(v))
def lk(u,label):
    return f'<a href="{html.escape(u)}" target="_blank">{label}</a>' if u else ""
def socx(r):
    out=[]
    for u,l in [(r["fb"],"FB"),(r["ig"],"IG"),(r["tiktok"],"TT"),(r["pinterest"],"Pin")]:
        if u: out.append(lk(u,l))
    return " ".join(out)
hdr=["#","Domain","Merchant","Cn","Created","Est Visits","Est PViews","Est Sales/mo",
     "Avg $","Min $","Max $","Avg Wt","Prods","Vars","AppSpend","Rank","Theme","Last Theme",
     "Reviews","TP","Social","Meta"]
def cell(x): return f"<td>{x}</td>"
trs=[]
for i,r in enumerate(rows,1):
    dom=r["domain"] or ""
    durl="https://"+dom if dom and not str(dom).startswith("http") else dom
    cells=[str(i), lk(durl, html.escape(str(dom))), html.escape(str(r["merchant"] or "")),
      html.escape(str(r["country"] or "")), r["created"] or "",
      fnum(r["visits"]), fnum(r["pageviews"]), html.escape(str(r["sales"] or "")),
      html.escape(str(r["avg_price"] or "")), html.escape(str(r["min_price"] or "")), html.escape(str(r["max_price"] or "")),
      html.escape(str(r["avg_weight"] or "")), fnum(r["products"]), fnum(r["variants"]),
      html.escape(str(r["app_spend"] or "")), fnum(r["rank"]),
      html.escape(str(r["theme"] or "")), html.escape(str(r["last_theme"] or "")),
      fnum(r["comb_reviews"]), fnum(r["tp_reviews"]), socx(r), html.escape(str(r["meta_desc"] or "")[:140])]
    trs.append("<tr>"+"".join(cell(c) for c in cells)+"</tr>")
elapsed=round(time.time()-t0)
html_doc=f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(CAT)} — Store Leads ≥2020</title>
<style>
body{{font-family:-apple-system,Segoe UI,Arial,sans-serif;margin:18px;color:#1a1a1a}}
h1{{font-size:18px;margin:0 0 4px}} .sub{{color:#666;font-size:13px;margin-bottom:14px}}
table{{border-collapse:collapse;font-size:12px;width:100%}}
th,td{{border:1px solid #e3e3e3;padding:4px 7px;text-align:left;white-space:nowrap;max-width:340px;overflow:hidden;text-overflow:ellipsis}}
th{{background:#1f6feb;color:#fff;position:sticky;top:0}}
tr:nth-child(even){{background:#f7f9fc}}
td:nth-child(6),td:nth-child(7){{text-align:right;font-variant-numeric:tabular-nums}}
a{{color:#1f6feb;text-decoration:none}} a:hover{{text-decoration:underline}}
.meta{{color:#777}}
</style></head><body>
<h1>{html.escape(CAT)} — Shopify · Active · Created ≥ 2020</h1>
<div class="sub">Собрано {len(rows):,} магазинов (server total {sum(t for _,_,t in server_totals if t):,}) · окна {", ".join(f"{lo}..{hi or 'now'}={t}" for lo,hi,t in server_totals)} · отсортировано по Est Visits ↓ · сгенерировано за {elapsed}s</div>
<table><thead><tr>{"".join(f"<th>{h}</th>" for h in hdr)}</tr></thead>
<tbody>{"".join(trs)}</tbody></table></body></html>"""
open(f"{OUT}/{SLUG}_table.html","w").write(html_doc)
print(f"\nDONE: collected {len(rows)} unique (server windows sum {sum(t for _,_,t in server_totals if t)}) in {elapsed}s")
print(f"saved {SLUG}_full.json + {SLUG}_table.html")
print("=== DUMP FULL DONE ===")
