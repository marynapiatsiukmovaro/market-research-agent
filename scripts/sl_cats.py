#!/usr/bin/env python3
"""Print the Store Leads category tree (cat / cat1 facet terms + counts) from the saved
unfiltered domains dump. Run on VPS: python3 scripts/sl_cats.py"""
import json
d = json.load(open('/opt/market-research-agent/logs/storeleads/full_domains.json'))
fac = d.get('facets', {})
for key in ('cat1', 'cat'):
    f = fac.get(key, {})
    terms = f.get('terms', [])
    print(f'\n===== {key}  (total tagged: {f.get("total")}, {len(terms)} buckets shown) =====')
    for t in terms[:80]:
        lbl = t.get('term', t.get('name', t.get('value')))
        cnt = t.get('count', t.get('c'))
        print(f'  {cnt:>9}  {lbl}')
