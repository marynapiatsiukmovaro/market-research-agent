#!/usr/bin/env python3
# Manage ShopHunter shop sub-collections via the per-shop "Manage Shop Collections" dialog.
# TOGGLE-SAFE: this script ONLY ever clicks an "Add" button — it NEVER clicks "Remove",
# so it can never accidentally drop a shop from the general "Shops" collection (Marina's concern).
# Reads each collection row's button label (Add = not a member / Remove = already a member)
# = the RELIABLE membership source (vs the virtualized /collections/shops scroll which undercounts).
#
# Usage:
#   sh_collection_manage.py create "<Collection Name>" <seed_shop_id>    -> create collection (Save New), seeded by one shop
#   sh_collection_manage.py add    "<Collection Name>" <shop_id> [...]   -> add each shop IF its row shows "Add" (else skip)
#   sh_collection_manage.py verify "<Collection Name>" <shop_id> [...]   -> report membership of each shop in the collection
#   sh_collection_manage.py list   <shop_id>                             -> list ALL collections + Add/Remove state for one shop
import sys, time
from playwright.sync_api import sync_playwright

PROFILE = '/opt/market-research-agent/cookies/shophunter_profile'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
MODE = sys.argv[1]
NAME = sys.argv[2] if MODE != 'list' else None
IDS = sys.argv[3:] if MODE != 'list' else sys.argv[2:]

# Scoped to the open modal; returns [{name,label}] for each collection row (label in {Add,Remove}).
ROWS_JS = r"""
() => {
  const hdr=[...document.querySelectorAll('h2')].find(h=>(h.innerText||'').includes('Manage Shop Collections'));
  if(!hdr) return [];
  let modal=hdr;
  for(let i=0;i<6;i++){ if(modal.classList && modal.classList.contains('max-w-md')) break; if(!modal.parentElement) break; modal=modal.parentElement; }
  const rows=[];
  modal.querySelectorAll('span.font-medium').forEach(s=>{
    const p=s.parentElement; const btn=p && p.querySelector('button');
    if(btn && /^(Add|Remove)$/.test((btn.innerText||'').trim()))
      rows.push({name:(s.innerText||'').trim(), label:(btn.innerText||'').trim()});
  });
  return rows;
}"""

CLICK_JS = r"""
(name) => {
  const hdr=[...document.querySelectorAll('h2')].find(h=>(h.innerText||'').includes('Manage Shop Collections'));
  if(!hdr) return 'NO_MODAL';
  let modal=hdr;
  for(let i=0;i<6;i++){ if(modal.classList && modal.classList.contains('max-w-md')) break; if(!modal.parentElement) break; modal=modal.parentElement; }
  const spans=[...modal.querySelectorAll('span.font-medium')];
  for(const s of spans){
    if((s.innerText||'').trim()===name){
      const b=s.parentElement.querySelector('button');
      if(b){ const l=(b.innerText||'').trim(); if(l==='Add'){ b.click(); return 'CLICKED_ADD'; } return l; }
    }
  }
  return 'NO_ROW';
}"""


def open_dialog(pg, sid):
    pg.goto(f'https://app.shophunter.io/shops/{sid}', wait_until='domcontentloaded', timeout=60000)
    pg.wait_for_timeout(3500)
    if '/login' in pg.url:
        return False
    pg.get_by_text('Add/Remove from Collection').first.click()
    pg.wait_for_selector('text=Manage Shop Collections', timeout=12000)
    pg.wait_for_timeout(1200)
    return True


with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(user_data_dir=PROFILE, headless=True, user_agent=UA,
                                               viewport={'width': 1500, 'height': 1400})
    pg = ctx.new_page()
    try:
        if MODE == 'create':
            sid = IDS[0]
            if not open_dialog(pg, sid):
                print('SESSION_DROPPED'); raise SystemExit
            existing = [r['name'] for r in pg.evaluate(ROWS_JS)]
            if NAME in existing:
                print('EXISTS_ALREADY', repr(NAME), '| collections:', existing)
            else:
                pg.fill('input[placeholder="New Collection Name"]', NAME)
                pg.wait_for_timeout(800)
                pg.get_by_text('Save New', exact=True).first.click()
                pg.wait_for_timeout(2800)
                rows = [r['name'] for r in pg.evaluate(ROWS_JS)]
                print('CREATED', repr(NAME), '| seed', sid, '| collections now:', rows)
        elif MODE == 'add':
            ok = fail = already = nocoll = 0
            for sid in IDS:
                try:
                    if not open_dialog(pg, sid):
                        print('SESSION_DROPPED', sid); break
                    rows = {r['name']: r['label'] for r in pg.evaluate(ROWS_JS)}
                    if NAME not in rows:
                        print('NO_COLLECTION', sid, '| has:', list(rows)); nocoll += 1; continue
                    if rows[NAME] == 'Add':
                        res = pg.evaluate(CLICK_JS, NAME); pg.wait_for_timeout(1300)
                        print('ADDED', sid, res); ok += 1
                    else:
                        print('ALREADY', sid); already += 1
                except Exception as e:
                    print('FAIL', sid, type(e).__name__, str(e)[:50]); fail += 1
            print(f'=== ADD SUMMARY: added={ok} already={already} no_collection={nocoll} fail={fail} ===')
        elif MODE == 'verify':
            member = notmem = 0
            for sid in IDS:
                try:
                    if not open_dialog(pg, sid):
                        print('SESSION_DROPPED', sid); break
                    m = {r['name']: r['label'] for r in pg.evaluate(ROWS_JS)}
                    st = 'MEMBER' if m.get(NAME) == 'Remove' else ('NOT' if m.get(NAME) == 'Add' else 'NO_COLLECTION')
                    if st == 'MEMBER': member += 1
                    else: notmem += 1
                    print('VERIFY', sid, '=', st, '| all:', m)
                except Exception as e:
                    print('FAIL', sid, type(e).__name__, str(e)[:50])
            print(f'=== VERIFY SUMMARY ({NAME!r}): member={member} not/other={notmem} ===')
        elif MODE == 'list':
            sid = IDS[0]
            if not open_dialog(pg, sid):
                print('SESSION_DROPPED'); raise SystemExit
            print('SHOP', sid, 'collections:')
            for r in pg.evaluate(ROWS_JS):
                print('  ', r['name'], '->', r['label'])
    finally:
        ctx.close()
print('MANAGE_DONE')
