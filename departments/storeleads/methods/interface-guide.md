# Store Leads — Interface & API Guide

How to drive Store Leads on the VPS. The dashboard is a Vaadin **Shadow-DOM** SPA (so
`body.innerText` is empty — judge screenshots, not text), but it is powered by a clean
**authenticated JSON API** that we call directly with the logged-in session. Mapped 2026-05-30.

## Access / login (passwordless email code)
- storeleads.app/login is passwordless: enter email → a 6-char **code** is emailed → enter code.
  (NOT Google/password, despite the Google button.)
- `scripts/sl_email_login.py` (run `ssh -i ~/.ssh/market_research_vps -t root@5.78.217.133
  'python3 /opt/market-research-agent/scripts/sl_email_login.py'`) — Marina types email, then the
  emailed code. Saves `cookies/storeleads_state.json` (Playwright storage_state) + persistent
  profile `cookies/storeleads_profile` (gitignored, chmod 600).
- `scripts/sl_check_login.py <url>` — verify session (loads state, screenshots a page).
- Session persists for days/weeks; re-run sl_email_login with a fresh code when it expires.
- Account = babbystorecom@gmail.com. invisible reCAPTCHA Enterprise present → stay gentle.

## How we read the data: the internal JSON API
All calls are `POST` to `https://storeleads.app/json/auth/<endpoint>`, replayed via the page's
own `fetch()` (so cookies + the `X-CSRF-TOKEN` header — read from the cookie — match the app).
Pattern in `scripts/sl_dump_full.py` (production) / `sl_dump3.py` (quick sample).

Key endpoints:
- **`/json/auth/domains`** — the store search. Returns `domains` (50/page), `next_cursor`,
  `totalHits`, `facets`, `maxRank`, `request` (echo of the parsed query — use as ground truth).
- `/json/auth/dashboard-load` — account, availablePlans (incl. `max_searches`), features, facets.
- `/json/auth/apps` — search by installed Shopify app. `/json/auth/country` — 249 countries.
- `/json/auth/list` — saved Lists (watchlist layer; weekly email on saved filters — to wire later).

### Two filter layers — simple `f:` and advanced `bq` (both cracked)

**(1) Simple term filters** — body keys `"f:<field>": "<value>"`. Fast for single-category counts/dumps:
- `f:p` = platform (1 = Shopify, 7 = BigCommerce) · `f:ds` = status (1 = Active, 3 = Password-protected)
- `f:cc` = country code (e.g. `US`) · `f:cat` = full category path; `f:cat1` = L1 category
- `f:cratyyyymm="YYYY-MM"` = **exact month** (not a range). The `cratyyyymm` FACET returns all 114
  months (`other=0`) → sum months ≥2020 for an exact created≥2020 count without dumping (see `sl_count.py`).
- Response `request` echoes parsed filters (`qp/qs/qcc/qcat/...`) — ground truth.
- ⚠️ **Multi-value `f:cc` via comma = 0 hits** (ANDs, not ORs) → query ONE country, merge.
- ⚠️ Range filters (price/weight/created-range/revenue) do NOT work as `f:` — use `bq` (below).

**(2) Advanced `bq` — the real query engine (Bleve DSL). ⭐ cracked 2026-05-31.** This is how we do
created≥2020, multi-category OR, and beat the 25k ceiling. `bq` is a **JSON *string*** in the POST
body (server: `bq` is type string). Container = `{"must":{"conjuncts":[ <query objects> ]}}`:
- Platform / Status: `{"field":"p","term":"1"}` · `{"field":"ds","term":"1"}` (term, ids as strings)
- Category EXACT: `{"field":"cat","match":"/Home & Garden/Home Improvement"}` — **`match`, not `term`** (term→0)
- Category **OR** (the UI "Show more" checklist / Operation:Or): wrap one conjunct as a disjunction →
  `{"disjuncts":[{"field":"cat","match":A},{"field":"cat","match":B}]}`
- **Created ≥ 2020** = Bleve TermRange on `cratyyyymm`: `{"field":"cratyyyymm","min":"2020-01","inclusive_min":true}`
  (createdAt/crat as RFC3339 = ignored or 0; only `cratyyyymm` string-range works). Validated K&D=29,150.
- **Beat the 25k ceiling** = add `"max":"YYYY-MM","inclusive_max":true` → split a big subcategory into
  created windows each <25k, paginate each, merge/dedupe. Verified exact (HI 6,969+20,083=27,052). See `sl_dump_full.py`.
- Sort: **not needed** — collect the window-merged set and sort CLIENT-SIDE by `mvis` (Est Visits).
- To **screenshot the Advanced UI**, put the same Bleve `bq` in the URL **path** (`/dashboard/domains/bq=<urlencoded>`);
  the SPA forwards it to the server and renders the filtered table + Matching count (see `sl_shots3.py`).
  Note: `?bq=` query-string is ignored; reCAPTCHA `rct` is NOT required for these body queries.

### Pagination
`next_cursor` → passed back as **`"cursor": <next_cursor>`**. **`ps` page size is capped at 50**
(server ignores larger) → ~540 requests / ~21 min for a 27k subcategory at 0.5s/page (run in background).
`cs` = 25000 = hard ceiling per query → always stay under it via `bq` created windows (above).

### Per-store fields in the search result (no site visit needed for Stage-1)
Codes used in our export table (coverage% measured on HI≥2020, n=300):
`name`/`merchantName`(100)/`tld1` (domain/merchant) · `md`(99) (meta desc) · `cat`/`lcat` (category) ·
`countryCode`/`loc`(98)/`langn` · **`erf`**(100) (est revenue $/mo) · **`mvis`**(100) (Est Visits — primary
ranking signal) · **`mpv`**(100) (Est PageViews) · **`apf`**(96)/`minpf`/`maxpf` (price) · **`apw`**(86)
(avg product weight) · **`pc`**(100) (product count) · **`varc`**(97) (variants) · **`masf`**(77) (app spend) ·
**`createdAt`** · `rank`/`prank`(100) · `themeName`(100)/`ltheme`(87) (theme / last theme) · `combrs`(45)/
`tprs`(27) (reviews) · `identifiers` → FB(75)/IG(81)/TikTok(22)/Pinterest(32) links (matched by URL).
`mrpp` (most-recent product) · `tech` (stack, incl. FB Pixel) · `apps` available too.
⚠️ **No social follower / 30-day-growth counts in this response** (dropped from our table 2026-05-31).

### Plan limits (Premium $75)
`max_searches` ≈ 2000–4000/mo · 2 platforms · export/API/workflow = Pro+ only. A "search" =
a query/lookup; paginating a filter is browsing (Marina's read — confirm via the in-app
account/usage counter at the first real run). For a 200-store pilot the quota is irrelevant.

## Helper scripts (active — repo `scripts/`, run on VPS)
- `sl_email_login.py` (login) · `sl_check_login.py` (verify session)
- **`sl_dump_full.py`** `"<cat path>" <slug>` — production: windowed `bq` dump of a subcategory ≥2020,
  all export fields, client-sort by Est Visits → `<slug>_full.json` + `<slug>_table.html`.
- `sl_dump3.py [pages]` — quick `bq` sample (a few pages) for spot-checks.
- `sl_html_top.py <slug> <N> "<title>"` — light top-N HTML preview from a `_full.json`.
- **`sl_select.py`** `<full_slug> <out_slug> [VLO VHI N]` — Stage-1: band-filter a `_full.json`, exclude already-processed, top-N by Est Visits → `<out_slug>.json`.
- **`sl_enrich4.py`** `<in> <out> <sentinel> [workers=8] [limit]` — **Stage-2 live enricher (LIVE, v4.1):** open-ladder + top-3 + currency→USD + product_class (incl. `diy-home`) / store_type + homepage-hero (only when hero_confidence=low) & desc self-check + new_products_30d + product-handle + class-aware ABC. v4.1 = 8 workers + fast-fail 15s×2. (`sl_enrich3.py` = fallback; `sl_enrich2.py` = retired.)
- **`sl_mark_processed.py`** `<enriched> <subcat> <band> <date> [--monitor-min N]` — write the master store record + monitor flag (RULE 19/20).
- **Stage artifacts → Marina's Desktop:** `sl_stage1_table.py` / `sl_stage2_table.py` (HTML tables) · `sl_stage3_pull.py` (compact deep-score digest) · `sl_retro.py` (retro-calibration of past batches) · `sl_html2png.py <in.html> <out.png>` (render any stage HTML → PNG).
- `sl_count.py` — exact ≥2020 count per subcategory (cratyyyymm facet sum).
- `sl_subtree.py` — full L2 subcategory tree (census) under Shopify+Active.
- `sl_shots3.py` — render/screenshot the Advanced UI via Bleve `bq` in the URL path.

Discovery/one-off scripts archived in `archive/storeleads-discovery-2026-05/`. Raw outputs in VPS `logs/storeleads/`.
