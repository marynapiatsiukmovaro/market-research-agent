#!/usr/bin/env python3
"""Cheap field-selection check: apply filter, open Export, JS-click every Select All, then Download Sample
and report the sample's column count — confirms the all-162-fields fix WITHOUT a full 4-min export."""
import os
from playwright.sync_api import sync_playwright
STATE = '/opt/market-research-agent/cookies/storeleads_state.json'
OUT = '/opt/market-research-agent/logs/storeleads'
URL = 'https://storeleads.app/dashboard/domains'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/123.0.0.0 Safari/537.36')
with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, accept_downloads=True,
                        viewport={'width': 1600, 'height': 3000})
    pg = ctx.new_page()
    pg.goto(URL, wait_until='networkidle', timeout=60000); pg.wait_for_timeout(6000)
    pg.locator('text=Shopify').first.click(); pg.wait_for_timeout(3000)
    pg.locator('text=Active').first.click(); pg.wait_for_timeout(3500)
    pg.locator('text=EXPORT').first.click(); pg.wait_for_timeout(2500)
    pg.locator('text=Select All').first.click(); pg.wait_for_timeout(600)
    for grp in ['Social Media Fields', 'Page URL Fields', 'Product Fields']:
        try:
            pg.locator(f'text={grp}').first.click(); pg.wait_for_timeout(500)
        except Exception:
            pass
    n = pg.evaluate('''() => {
        const els = [...document.querySelectorAll('*')].filter(e =>
            e.children.length === 0 && (e.textContent||'').trim() === 'Select All');
        els.forEach(e => e.click()); return els.length; }''')
    print('JS Select-All links clicked:', n)
    pg.wait_for_timeout(1000)
    print('checkboxes checked:', pg.locator('input[type=checkbox]:checked').count())
    with pg.expect_download(timeout=40000) as di:
        pg.locator('text=Download Sample').first.click()
    s = os.path.join(OUT, 'sl_fields_sample.csv')
    di.value.save_as(s)
    with open(s, errors='replace') as f:
        header = f.readline().strip()
    cols = header.count(',') + 1
    print('SAMPLE COLUMNS:', cols)
    has_prod = any(k in header for k in ['average_product_price', 'products_sold', 'product_variants'])
    print('has Product Fields:', has_prod)
    b.close()
print('=== VERIFY DONE ===')
