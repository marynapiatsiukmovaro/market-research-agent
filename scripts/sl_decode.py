#!/usr/bin/env python3
"""Digest the captured Store Leads API JSON: plans/limits/features + facet taxonomy +
one fully-decoded domain sample. Run on VPS: python3 scripts/sl_decode.py"""
import json, os
OUT = '/opt/market-research-agent/logs/storeleads'

def load(name):
    p = f'{OUT}/{name}'
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)

dl = load('full_dashboard_load.json')
dom = load('full_domains.json')

print('############ DASHBOARD-LOAD ############')
if dl:
    acct = dl.get('account', {})
    print('ACCOUNT keys:', list(acct.keys())[:40])
    for k in ('plan','plan_name','name','billing_status','max_searches','searches_used','searches_remaining',
              'searches','trial','role','email','can_export','export'):
        if k in acct:
            print(f'  account.{k} =', acct[k])
    print('\nbilling_status:', dl.get('billing_status'))
    print('\nAVAILABLE PLANS:')
    for pl in dl.get('availablePlans', []):
        print('  -', {k: pl.get(k) for k in ('name','monthly_fee','yearly_fee','max_searches','text_summary')})
    feats = dl.get('features')
    if isinstance(feats, dict):
        print('\nFEATURES (account gating):')
        for k, v in feats.items():
            print(f'   {k} = {v}')
    elif isinstance(feats, list):
        print('\nFEATURES list:', feats)

print('\n############ DOMAINS RESPONSE ############')
if dom:
    print('top keys:', list(dom.keys()))
    print('totalHits:', dom.get('totalHits'), '| maxRank:', dom.get('maxRank'),
          '| next_cursor:', str(dom.get('next_cursor'))[:60], '| #domains:', len(dom.get('domains', [])))
    facets = dom.get('facets', {})
    print('\nFACET FIELDS (= the left-sidebar filters):')
    if isinstance(facets, dict):
        for fname, fval in facets.items():
            if isinstance(fval, list):
                sample = []
                for b in fval[:6]:
                    if isinstance(b, dict):
                        label = b.get('name') or b.get('value') or b.get('key') or b.get('label')
                        cnt = b.get('count') or b.get('fcount') or b.get('c')
                        sample.append(f'{label}:{cnt}')
                print(f'  [{fname}] ({len(fval)} buckets) e.g. {sample}')
            elif isinstance(fval, dict):
                print(f'  [{fname}] dict keys={list(fval.keys())[:10]}')
    # one fully decoded domain
    ds = dom.get('domains', [])
    if ds:
        print('\nSAMPLE DOMAIN (all fields):')
        for k, v in ds[0].items():
            sv = str(v)
            print(f'   {k} = {sv[:90]}')
print('\n=== DECODE DONE ===')
