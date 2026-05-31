#!/usr/bin/env python3
"""
Store Leads interface recon (logged-in session). For each URL: screenshot (full page),
dump title, all dashboard links (nav map), table column headers, pagination, result count,
and the left filter sidebar text. Heavy capture stays on the VPS; we scp a few key shots.

Usage (on VPS):
    python3 /opt/market-research-agent/scripts/sl_recon.py [url1 url2 ...]
Default = the main domains search page.
"""
import os, sys, json, re
from playwright.sync_api import sync_playwright

BASE = '/opt/market-research-agent'
STATE = f'{BASE}/cookies/storeleads_state.json'
OUT = f'{BASE}/logs/storeleads'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')
os.makedirs(OUT, exist_ok=True)

URLS = sys.argv[1:] or ['https://storeleads.app/dashboard/domains']

def tag_of(url):
    t = re.sub(r'^https?://storeleads\.app/?', '', url)
    t = re.sub(r'[^a-zA-Z0-9]+', '_', t).strip('_') or 'home'
    return t[:40]

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA,
                        viewport={'width': 1600, 'height': 1600}, device_scale_factor=1)
    pg = ctx.new_page()
    for url in URLS:
        tag = tag_of(url)
        try:
            pg.goto(url, wait_until='networkidle', timeout=60000)
        except Exception as e:
            print(f'\n##### {url}\nERR goto {type(e).__name__}')
            continue
        pg.wait_for_timeout(4500)
        pg.screenshot(path=f'{OUT}/recon_{tag}.png', full_page=True)

        title = pg.title()
        # nav map: all dashboard links
        links = pg.evaluate("""() => {
            const seen = {};
            document.querySelectorAll('a[href]').forEach(a => {
                const h = a.getAttribute('href');
                if (!h) return;
                if (h.startsWith('/dashboard') || h.includes('storeleads.app/dashboard') || h.startsWith('/help') ) {
                    const t = (a.innerText||'').trim().slice(0,40);
                    if (!(h in seen)) seen[h] = t;
                }
            });
            return seen;
        }""")
        # table headers + first 3 row cells
        headers = pg.evaluate("""() => Array.from(document.querySelectorAll('th, [role=columnheader]'))
            .map(h => (h.innerText||'').trim()).filter(Boolean).slice(0,30)""")
        # filter sidebar group headers (collapsible sections)
        groups = pg.evaluate("""() => {
            const out = [];
            document.querySelectorAll('*').forEach(el => {});
            // heuristic: sidebar is the left column; grab bold/section-ish short texts
            return out;
        }""")
        # pagination + counts: just grab body text and slice key parts
        body = (pg.evaluate('document.body.innerText') or '')
        # extract a 'Total ...' line and page numbers
        total = ''
        for line in body.split('\n'):
            ls = line.strip()
            if re.search(r'(Total|Domains|results|Showing)', ls, re.I) and len(ls) < 60:
                total += ls + ' | '

        print(f'\n##### {url}  ->  {pg.url}')
        print('title    :', title)
        print('headers  :', headers)
        print('totals?  :', total[:300])
        print('nav links:')
        for h, t in links.items():
            print(f'   {h}   "{t}"')
        # dump full body text to a file for offline read (cheap)
        with open(f'{OUT}/recon_{tag}.txt', 'w') as f:
            f.write(body)
        print(f'(full text -> recon_{tag}.txt, {len(body)} chars)')
    b.close()
print('\n=== SL RECON DONE ===')
