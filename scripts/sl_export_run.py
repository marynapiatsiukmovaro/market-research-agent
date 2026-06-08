#!/usr/bin/env python3
"""Store Leads — REAL universe CSV export, ALL fields (S-pivot, 2026-06-08).

Applies a Platform(+optional Status) filter, selects ALL fields (standard + Social + Page URL +
Product groups), then exports the full filtered set to ONE CSV on the VPS. Designed to run
DETACHED (nohup) because a multi-million-row all-fields export takes several minutes to begin
and produces a multi-GB file. Writes a .sentinel when finished so a background waiter can detect it.

Usage (on VPS, detached):
  python3 scripts/sl_export_run.py <platform> <status|none> <out_basename>
  e.g. python3 scripts/sl_export_run.py Shopify Active shopify_active_all
       python3 scripts/sl_export_run.py WooCommerce none woocommerce_all

Outputs to logs/storeleads/exports/:
  <out_basename>.csv         the export
  <out_basename>.pre.png     screenshot of the export dialog right before clicking Export (proof of selection)
  <out_basename>.sentinel    written last: "done rows=<N> bytes=<B> secs=<S> exporturl=<url>"
"""
import os, sys, time, re
from playwright.sync_api import sync_playwright

STATE = '/opt/market-research-agent/cookies/storeleads_state.json'
EXP = '/opt/market-research-agent/logs/storeleads/exports'
URL = 'https://storeleads.app/dashboard/domains'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')

PLATFORM = sys.argv[1] if len(sys.argv) > 1 else 'Shopify'
STATUS = sys.argv[2] if len(sys.argv) > 2 else 'Active'
BASE = sys.argv[3] if len(sys.argv) > 3 else 'export_all'
os.makedirs(EXP, exist_ok=True)
csv_path = os.path.join(EXP, BASE + '.csv')
sent_path = os.path.join(EXP, BASE + '.sentinel')
t0 = time.time()


def click_any(pg, sels, label, timeout=8000, required=False):
    for sel in sels:
        try:
            el = pg.locator(sel).first
            if el.count() > 0 and el.is_visible():
                el.click(timeout=timeout)
                print(f'  clicked {label} via {sel}', flush=True)
                return True
        except Exception as ex:
            print(f'  {label} sel {sel} failed: {str(ex)[:70]}', flush=True)
    msg = f'  !! {label} NOT clicked'
    print(msg, flush=True)
    if required:
        raise RuntimeError(f'required click failed: {label}')
    return False


export_url_seen = {'url': None}

with sync_playwright() as p:
    b = p.chromium.launch(headless=True, args=['--no-sandbox'])
    ctx = b.new_context(storage_state=STATE, user_agent=UA, accept_downloads=True,
                        viewport={'width': 1600, 'height': 1500}, device_scale_factor=2)
    pg = ctx.new_page()

    # capture any export/csv backend request as a curl fallback
    def on_req(req):
        u = req.url
        if any(k in u.lower() for k in ['export', 'csv', 'download']):
            export_url_seen['url'] = u
            print('  [net] export-ish request:', u[:160], flush=True)
    pg.on('request', on_req)

    pg.goto(URL, wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(6000)

    # --- apply filters ---
    print(f'applying Platform={PLATFORM}, Status={STATUS}', flush=True)
    click_any(pg, [f'[class*="filter"] >> text="{PLATFORM}"', f'aside >> text="{PLATFORM}"',
                   f'text="{PLATFORM}"'], f'filter {PLATFORM}', required=True)
    pg.wait_for_timeout(3500)
    if STATUS and STATUS.lower() != 'none':
        click_any(pg, [f'[class*="filter"] >> text="{STATUS}"', f'aside >> text="{STATUS}"',
                       f'text="{STATUS}"'], f'filter {STATUS}', required=True)
        pg.wait_for_timeout(4000)
    print('filtered URL :', pg.url, flush=True)

    # --- open export + select all fields ---
    click_any(pg, ['button:has-text("EXPORT")', 'button:has-text("Export")', 'text=EXPORT'],
              'EXPORT-open', required=True)
    pg.wait_for_timeout(3000)
    # top-level Select All (standard fields)
    click_any(pg, ['text=Select All', 'button:has-text("Select All")'], 'Select-All-standard')
    pg.wait_for_timeout(800)
    # expand groups and select-all within each
    for grp in ['Social Media Fields', 'Page URL Fields', 'Product Fields']:
        click_any(pg, [f'text={grp}'], f'expand {grp}')
        pg.wait_for_timeout(700)
    # click EVERY "Select All" link via JS (standard + all 3 groups), regardless of visibility — a group's
    # Select All can sit below the fold (that lost the 21 Product Fields in the first VPS run). Idempotent.
    n_sa = pg.evaluate('''() => {
        const els = [...document.querySelectorAll('*')].filter(e =>
            e.children.length === 0 && (e.textContent||'').trim() === 'Select All');
        els.forEach(e => e.click());
        return els.length;
    }''')
    print('  JS-clicked Select-All links:', n_sa, flush=True)
    pg.wait_for_timeout(1200)

    checked = pg.locator('input[type=checkbox]:checked').count()
    print('checkboxes CHECKED in dialog:', checked, flush=True)
    pg.screenshot(path=os.path.join(EXP, BASE + '.pre.png'), full_page=True)

    # --- click Export, capture the download ---
    print('clicking Export, awaiting download (long timeout)...', flush=True)
    # The REAL data-export button is a <vaadin-menu-bar-button theme="icon primary">Export</vaadin-menu-bar-button>
    # INSIDE the export dialog overlay (a Vaadin menu-bar split-button) — NOT a <vaadin-button>, and NOT the
    # page's facet-export button (which produced the 16-byte "Shopify,2890820" facet file). Scope to the overlay.
    mb = pg.locator('vaadin-dialog-overlay vaadin-menu-bar-button')
    target = None
    for i in range(mb.count()):
        try:
            if (mb.nth(i).inner_text() or '').strip() == 'Export':
                target = mb.nth(i)
                print(f'  menu-bar Export button at idx {i}', flush=True)
                break
        except Exception:
            pass
    if target is None:
        cand = pg.locator('vaadin-menu-bar-button', has_text='Export')
        if cand.count() > 0:
            target = cand.first
            print('  fallback: vaadin-menu-bar-button has_text Export', flush=True)
    if target is None:
        print('DOWNLOAD FAILED: no menu-bar Export button found', flush=True)
        open(sent_path, 'w').write(f'FAILED-nobtn secs={int(time.time()-t0)} exporturl={export_url_seen["url"]}')
        b.close(); raise SystemExit(1)
    try:
        with pg.expect_download(timeout=900000) as di:   # up to 15 min; CSV streams progressively (Marina confirmed)
            try:
                target.click(timeout=12000)
            except Exception:
                target.dispatch_event('click')
            print('  clicked menu-bar Export', flush=True)
        dl = di.value
        dl.save_as(csv_path)        # blocks until the full file is written
        print('download saved:', csv_path, flush=True)
    except Exception as ex:
        print('DOWNLOAD FAILED:', str(ex)[:300], flush=True)
        print('export_url fallback:', export_url_seen['url'], flush=True)
        open(sent_path, 'w').write(f'FAILED secs={int(time.time()-t0)} exporturl={export_url_seen["url"]}')
        b.close()
        raise SystemExit(1)
    b.close()

# --- count rows + write sentinel ---
rows = 0
try:
    with open(csv_path, 'rb') as f:
        for _ in f:
            rows += 1
except Exception as ex:
    print('row-count failed:', ex, flush=True)
data_rows = max(0, rows - 1)   # minus header
size = os.path.getsize(csv_path) if os.path.exists(csv_path) else 0
open(sent_path, 'w').write(
    f'done rows={data_rows} bytes={size} secs={int(time.time()-t0)} exporturl={export_url_seen["url"]}')
print(f'=== EXPORT DONE rows(data)={data_rows} bytes={size} secs={int(time.time()-t0)} ===', flush=True)
