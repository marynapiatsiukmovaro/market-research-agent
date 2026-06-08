# Store Leads — CSV Universe Export (Pro plan) — METHOD & RULES

**Status:** LIVE since 2026-06-08 (S14). This is the **upgraded data-acquisition method** — it **replaces the
old paginated dump** (`sl_dump*.py` → `/json/auth/domains`, which burned the Premium 2,000-search/mo quota →
HTTP 402; see [[project_storeleads_quota]]). Pro plan = **unlimited searches + Export-to-CSV**, so we pull a
whole filtered set into ONE CSV with no pagination, no quota, no cursor-transients.

Tool: **`scripts/sl_export_run.py`** (runs on the VPS, headless Playwright, saved session
`cookies/storeleads_state.json`). Helpers: `sl_filter_check.py` (read a filter's store count), `sl_verify_fields.py`
(cheap column-count check via Download Sample).

---

## Why this method exists (the hard-won part)
The Store Leads dashboard is a **Vaadin web-component SPA**. Naive Playwright clicks FAIL on it. It took many
attempts to find the right selectors + delivery mechanism. The rules below encode what actually works, so we
never re-derive it.

## The export mechanism — step by step
1. **Filter** via the left sidebar by clicking the option label (e.g. `Shopify`, `Active`). The filter is
   encoded in the URL: `f%3Ap=1` = Platform=Shopify, `f%3Ads=1` = Status=Active. The sidebar shows the matching
   count next to each selected filter — that count is the **export target row-count** (use it to verify completeness).
2. **Open the export dialog** — click the top-right **`EXPORT`** (it is NOT a `<button>` tag; match `text=EXPORT`).
3. **Select ALL fields = 162 columns.** The dialog has:
   - **Standard Fields (88)** — one `Select All` link.
   - **Social Media Fields (32)**, **Page URL Fields (21)**, **Product Fields (21)** — three collapsible groups,
     **each with its OWN `Select All`**. They can sit **below the fold**, so clicking only the visible ones MISSES
     a group (this once lost the 21 Product Fields → a 141-col file instead of 162).
   - ✅ **RULE:** click EVERY `Select All` link via JS regardless of visibility (idempotent):
     ```js
     [...document.querySelectorAll('*')]
       .filter(e => e.children.length===0 && e.textContent.trim()==='Select All')
       .forEach(e => e.click());
     ```
     Then confirm `input[type=checkbox]:checked` ≈ 190 (→ 162 CSV columns incl. `average_product_price`,
     `products_sold`, `most_recent_product_*`, etc.).
4. **Click the REAL Export button.** ⚠️ This is the single trickiest part:
   - The data-export button is a **`<vaadin-menu-bar-button theme="icon primary">Export</vaadin-menu-bar-button>`
     INSIDE the `vaadin-dialog-overlay`** (a Vaadin menu-bar split-button with a ▾ caret). It is **NOT** a
     `<vaadin-button>`, and it FAILS Playwright's visible/stable actionability checks (it's a web-component below
     the fold), so `.click()`/force/scroll all error with "Element is not visible".
   - There is a **decoy**: a page-level *facet-export* `vaadin-button[theme=primary]` "Export" that, if clicked,
     downloads a **16-byte facet file** (`Shopify,2890820`) — NOT the data. Always **scope to the overlay**.
   - ✅ **RULE:** locate `vaadin-dialog-overlay vaadin-menu-bar-button` whose `inner_text()=='Export'` and click it
     (normal `.click()`; fall back to `dispatch_event('click')`).
5. **Async job + progressive download.** The click triggers an **async export job**: the browser POSTs to
   `…/json/auth/domains/export`, **polls** that endpoint for status, then fetches
   `…/json/auth/domains/export/{job_id}` which streams the CSV. Generation takes **~3–4 min for ~3M rows**
   (Marina-observed; "it hangs a few minutes, then the file downloads progressively"). `expect_download` with a
   generous timeout (we use 15 min) catches the stream; `download.save_as()` writes it to disk as it streams.

## Run it
```bash
# on VPS (detached, writes <base>.sentinel when done):
python3 scripts/sl_export_run.py <Platform> <Status|none> <out_basename>
#   e.g.  Shopify  Active  storeleads_shopify_active_2026-06-08
#         WooCommerce  none  storeleads_woocommerce_all_2026-06-08
```
Output → `logs/storeleads/exports/<base>.csv` (+ `.sentinel` = `done rows=<N> bytes=<B> secs=<S> exporturl=…`).

## Verify completeness (RULE — always)
- **Columns:** must be **162** (header comma-count). If 141 → the Product Fields group was missed (re-run; usually
  a stale script not scp'd to the VPS). Quick pre-check without a full export: `sl_verify_fields.py` (Download
  Sample → counts the sample's columns).
- **Rows:** the script's `rows=` is a **raw line count — it OVERCOUNTS** because descriptions contain embedded
  newlines inside quoted fields. For the exact figure, stream with `csv.reader` (the Python counter we used).
  Then compare to the sidebar's filter count. Example 2026-06-08:
  - Shopify-Active: csv-rows **2,890,820** (line-count 2,896,909) · 162 cols · 6.14 GB
  - WooCommerce:    csv-rows **4,255,809** (line-count 4,319,100) · 162 cols · 4.98 GB
  - Σ = **7,146,629** = the dashboard "Active" total across both platforms → whole active universe captured.

## Gotchas (don't repeat these)
- **`scp` the script to the VPS before every run.** A run with the stale (pre-fix) script produced 141 cols.
- **Line-count ≠ row-count** (multiline descriptions). Never report the raw line count as the store count.
- **Don't widen the viewport hoping the button becomes "visible"** — it won't; it's a web-component. Use the
  overlay-scoped `vaadin-menu-bar-button` locator.
- **One account, one export job at a time** — when a parallel browser session is exporting, don't fire a second
  concurrent export (do them sequentially, as we did).
- Credit-guard still applies (RULE 13): `claude` runs on the Mac, never on the VPS; the VPS only runs Playwright.

## What this enables next
The two universe CSVs (Shopify-Active + WooCommerce, 162 cols) live on the **VPS**
`logs/storeleads/exports/` (backup) **and** Marina's **Desktop** `~/Desktop/StoreLeads_Exports/` (origin) —
two copies, byte-identical. They are the **permanent snapshot** (re-exportable until the Pro window ends
**2026-06-29**; after that, no re-export — the saved files are the asset).

Going forward, niche analysis can either:
- **filter the universe CSV** down to a niche (locally / on the VPS) → feed `sl_enrich4` → the standard
  100-pt + Veto analysis (RULE 24 etc. unchanged — only data ACQUISITION changed, not enrichment/scoring); or
- **self-export a filtered niche directly** via `sl_export_run.py` with the niche's sidebar filters (fast, the
  Product Fields give a price band to pre-filter before enriching).
