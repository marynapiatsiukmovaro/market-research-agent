#!/usr/bin/env python3
"""Second digest: sort options, parsed-filter echo, revenue/created/category/plan facet
buckets, and any search-quota field. Run on VPS: python3 scripts/sl_decode2.py"""
import json, os
OUT = '/opt/market-research-agent/logs/storeleads'

def load(name):
    p = f'{OUT}/{name}'
    return json.load(open(p)) if os.path.exists(p) else None

dom = load('full_domains.json')
dl = load('full_dashboard_load.json')

def terms(facets, key, n=12):
    f = (facets or {}).get(key)
    if not isinstance(f, dict):
        return f'(no {key})'
    out = []
    for t in (f.get('terms') or [])[:n]:
        lbl = t.get('term', t.get('name', t.get('value')))
        cnt = t.get('count', t.get('c'))
        out.append(f'{lbl}:{cnt}')
    return f"total={f.get('total')} | " + ', '.join(out)

if dom:
    print('SORT current:', json.dumps(dom.get('sort'), ensure_ascii=False))
    print('\nSORT OPTIONS:')
    for s in dom.get('sortOptions', []):
        if isinstance(s, dict):
            print('  ', {k: s.get(k) for k in ('name', 'field', 'id', 'label', 'dir', 'desc')})
        else:
            print('  ', s)
    print('\nREQUEST echo (parsed filters/state):', json.dumps(dom.get('request'), ensure_ascii=False)[:800])
    fac = dom.get('facets', {})
    print('\n--- facet buckets ---')
    print('erb  (est. revenue ranges):', terms(fac, 'erb'))
    print('cat  (category)          :', terms(fac, 'cat'))
    print('cat1 (category L1)       :', terms(fac, 'cat1'))
    print('cc   (country)           :', terms(fac, 'cc'))
    print('plan (shopify plan)      :', terms(fac, 'plan'))
    print('p    (platform)          :', terms(fac, 'p'))
    print('ds   (data source)       :', terms(fac, 'ds'))
    print('cratyyyymm (created mon) :', terms(fac, 'cratyyyymm'))
    print('feat (features)          :', terms(fac, 'feat'))
    print('tech (technologies)      :', terms(fac, 'tech'))
    print('empcb(employees)         :', terms(fac, 'empcb'))
    # numeric range facets
    for rk in ('mv', 'mmv', 'pv', 'dmxp'):
        f = fac.get(rk)
        if isinstance(f, dict):
            print(f'{rk} (range): ', {k: f.get(k) for k in ('field', 'total', 'missing', 'min', 'max')})

print('\n--- quota / searches ---')
for src_name, src in (('account', (dl or {}).get('account', {})), ('organization', (dl or {}).get('organization', {})),
                      ('plan', (dl or {}).get('plan', {})), ('top', dl or {})):
    if isinstance(src, dict):
        for k, v in src.items():
            if any(s in k.lower() for s in ('search', 'quota', 'limit', 'remain', 'used', 'count')) and not isinstance(v, (dict, list)):
                print(f'  {src_name}.{k} = {v}')
print('\n=== DECODE2 DONE ===')
