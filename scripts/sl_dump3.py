#!/usr/bin/env python3
"""Stage-1 sample via CRACKED bq (Bleve). Home Improvement >=2020, all agreed fields,
client-sort by Est Visits. Saves full JSON + prints top + per-field coverage. VPS.
Usage: python3 scripts/sl_dump3.py [pages]"""
import json, sys, time
from playwright.sync_api import sync_playwright
STATE="/opt/market-research-agent/cookies/storeleads_state.json"
OUT="/opt/market-research-agent/logs/storeleads"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
HI="/Home & Garden/Home Improvement"
PAGES=int(sys.argv[1]) if len(sys.argv)>1 else 6
BLEVE={"must":{"conjuncts":[
  {"field":"p","term":"1"},{"field":"ds","term":"1"},
  {"field":"cat","match":HI},
  {"field":"cratyyyymm","min":"2020-01","inclusive_min":True}]}}
FETCH="""async (bodyStr) => {
  const m=document.cookie.match(/X-CSRF-TOKEN=([^;]+)/); const h={'Content-Type':'application/json'};
  if(m)h['X-CSRF-TOKEN']=decodeURIComponent(m[1]);
  const r=await fetch('/json/auth/domains',{method:'POST',headers:h,body:bodyStr,credentials:'include'});
  let j=null; try{j=await r.json();}catch(e){}
  return {total:j&&j.totalHits, next:j&&j.next_cursor, domains:(j&&j.domains)||[]};
}"""
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
      "meta_desc":(d.get('md') or '')[:120],
      "comb_reviews":d.get('combrs'),"tp_reviews":d.get('tprs'),
      "fb":soc(ids,'facebook'),"ig":soc(ids,'instagram'),
      "tiktok":soc(ids,'tiktok'),"pinterest":soc(ids,'pinterest'),
      # cryptic candidates for followers/growth (raw, to inspect)
      "_tsss":d.get('tsss'),"_atsss":d.get('atsss'),"_stcs":d.get('stcs'),"_shcs":d.get('shcs')}
with sync_playwright() as p:
    b=p.chromium.launch(headless=True,args=["--no-sandbox"])
    ctx=b.new_context(storage_state=STATE,user_agent=UA,viewport={"width":1400,"height":1000})
    pg=ctx.new_page(); pg.goto("https://storeleads.app/dashboard/domains",wait_until="networkidle",timeout=60000); pg.wait_for_timeout(2500)
    base={"all_facets":False,"bq":json.dumps(BLEVE)}
    r=pg.evaluate(FETCH,json.dumps(base)); total=r.get("total")
    seen={}; rows=[]
    def ingest(ds):
        for d in ds:
            i=d.get("id")
            if i not in seen: seen[i]=1; rows.append((d,row(d)))
    ingest(r.get("domains") or []); nxt=r.get("next")
    for _ in range(PAGES-1):
        if not nxt: break
        r=pg.evaluate(FETCH,json.dumps({**base,"cursor":nxt})); time.sleep(0.8)
        ds=r.get("domains") or []
        if not ds: break
        ingest(ds); nxt=r.get("next")
    b.close()
recs=[rr for _,rr in rows]
recs.sort(key=lambda x:(x["visits"] or 0),reverse=True)
json.dump(recs,open(f"{OUT}/hi_sample_table.json","w"),ensure_ascii=False)
print(f"HI >=2020 total(server)={total} | collected sample={len(recs)} (saved hi_sample_table.json)")
# field coverage
flds=["merchant","loc","visits","pageviews","sales","avg_price","avg_weight","products","variants",
      "app_spend","rank","theme","last_theme","meta_desc","comb_reviews","tp_reviews","fb","ig","tiktok","pinterest"]
n=len(recs) or 1
print("\nFIELD COVERAGE (% rows non-empty):")
print("  "+" | ".join(f"{f}:{round(100*sum(1 for r in recs if r.get(f) not in (None,'',0))/n)}%" for f in flds))
print("\nTOP 20 by Est Visits:")
print(f"{'#':>2} {'domain':26} {'visits':>8} {'sales/mo':>12} {'avgP':>6} {'wt':>5} {'prod':>5} {'created':>10} {'rank':>6} soc")
for i,x in enumerate(recs[:20],1):
    s=''.join(['F' if x['fb'] else '-','I' if x['ig'] else '-','T' if x['tiktok'] else '-','P' if x['pinterest'] else '-'])
    print(f"{i:>2} {str(x['domain'])[:26]:26} {str(x['visits']):>8} {str(x['sales'])[:12]:>12} {str(x['avg_price'])[:6]:>6} {str(x['avg_weight'])[:5]:>5} {str(x['products']):>5} {x['created']:>10} {str(x['rank']):>6} {s}")
print("\nCRYPTIC (followers/growth?) sample for top-3:")
for x in recs[:3]:
    print(f"  {x['domain']}: tsss={x['_tsss']} atsss={x['_atsss']} stcs={x['_stcs']} shcs={x['_shcs']}")
print("=== DUMP3 DONE ===")
