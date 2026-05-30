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
Pattern in `scripts/sl_query.py` / `sl_dump.py`.

Key endpoints:
- **`/json/auth/domains`** — the store search. Returns `domains` (50/page), `next_cursor`,
  `totalHits`, `facets`, `maxRank`, `request` (echo of the parsed query — use as ground truth).
- `/json/auth/dashboard-load` — account, availablePlans (incl. `max_searches`), features, facets.
- `/json/auth/apps` — search by installed Shopify app. `/json/auth/country` — 249 countries.
- `/json/auth/list` — saved Lists (watchlist layer; weekly email on saved filters — to wire later).

### Filter format (cracked 2026-05-30)
Body keys are `"f:<field>": "<value>"`:
- `f:p` = platform (1 = Shopify, 7 = BigCommerce)
- `f:ds` = status (1 = Active, 3 = Password-protected)
- `f:cc` = country code (e.g. `US`)
- `f:cat` = full category path (e.g. `/Home & Garden/Kitchen & Dining`); `f:cat1` = L1 category
- The response `request` echoes parsed filters as `qp/qs/qcc/qcat/...` — confirm here.
- ⚠️ **Multi-value `f:cc` via comma = 0 hits** (the endpoint ANDs the values, not ORs).
  → **Query ONE country at a time and merge/dedupe.** (Same likely for other multi-value facets.)
- Range filters (avg price, weight, created-date, revenue band `erb`) — server-side encoding
  NOT yet cracked; for now apply these **client-side** on the returned fields (see below).
- Sort: default `["rank","_id"]`. Sort param for Created / Estimated Sales NOT yet cracked
  (sortOptions exist: Estimated Sales, Avg Product Price USD, Created, Product Count, Est Visits,
  social followers + 30d %, etc.). **Cracking sort is the next API task** (needed for "go deeper").

### Pagination
`next_cursor` from the previous response, passed back as **`"cursor": <next_cursor>`** (key
confirmed = `cursor`). `ps` = 50/page. **`cs` = 25000 = hard ceiling of results per query** —
a filter returning >25k stores only exposes the first 25k → segment via sort/sub-filters.

### Per-store fields in the search result (no site visit needed for Stage-1)
`name`/`merchantName`/`tld1` (domain) · `t` (title) · `md` (meta desc) · `cat` (category) ·
`countryCode`/`cn`/`reg`/`city` · **`erf`** (est revenue $/month, formatted) · `eryf` (yearly) ·
**`apf`** (avg product price) · `minpf`/`maxpf` · `pc` (product count) · **`createdAt`** (store
created) · `plan` (Shopify tier) · `combrs`/`tprs` (reviews count+rating) · **`mrpp`** (most-recent
published product: image + date) · `tech` (stack — incl. Facebook Pixel) · `apps` · `feat` ·
`identifiers` (FB/IG/TikTok links) · social followers (+30d growth) · `emp` · `rank`/`prank`.

### Plan limits (Premium $75)
`max_searches` ≈ 2000–4000/mo · 2 platforms · export/API/workflow = Pro+ only. A "search" =
a query/lookup; paginating a filter is browsing (Marina's read — confirm via the in-app
account/usage counter at the first real run). For a 200-store pilot the quota is irrelevant.

## Helper scripts (VPS + repo, `scripts/`)
`sl_email_login.py` (login) · `sl_check_login.py` (verify) · `sl_recon.py` (screenshot pages) ·
`sl_net.py` (capture API calls) · `sl_api.py` (capture request bodies) · `sl_decode.py`/`sl_decode2.py`
(digest plans/facets/fields) · `sl_cats.py` (category tree) · `sl_query.py` (probe filter format) ·
`sl_dump.py` (Stage-0 dump + client filters) · `sl_enrich.py` / **`sl_enrich2.py`** (Stage-2
enricher; v2 = real hero from best-selling collection). Raw outputs in VPS `logs/storeleads/`.
