# ShopHunter — Interface & Operation Guide

Operational manual: how to drive the tool. Grows as we learn. Mapped Session SH-1.

## Access (on the VPS)
- Runs on the shared VPS (`5.78.217.133`), headless Chromium via Playwright.
- Credentials: `cookies/shophunter.creds` (gitignored, chmod 600). Set/refresh via
  `scripts/set_shophunter_creds.py` — run on the VPS with a TTY:
  `ssh -i ~/.ssh/market_research_vps -t root@5.78.217.133 'python3 /opt/market-research-agent/scripts/set_shophunter_creds.py'`
- **Login is persisted** in a browser profile at `cookies/shophunter_profile` →
  most runs skip re-login. If the session drops, just re-run the login script.
- Login mechanics: `launch_persistent_context(user_data_dir=cookies/shophunter_profile,
  headless=True, desktop-Chrome UA)`; fill `input[type=email]` + `input[type=password]`,
  check `#remember`, click button **"Sign In"**. App URL: `app.shophunter.io`.
- To "see" a page: navigate → `screenshot()` (viewport = readable) or
  `full_page=True` (whole page) AND/OR dump `body.innerText` for cheap text extraction.
  scp screenshots to local to view. No bot-block observed on login or browsing.

## Navigation map
Explore **Products** (`/explore/products`) · Explore **Shops** (`/explore/shops`) ·
Explore **Ads** (`/explore/ads`) · **Staff Picks** · **Tracked Shops** ·
**Shop/Product Collections** · **Add Shop** (`/shops/track`).

## Looking up a KNOWN store (Explore → Shops)
- Search box placeholder **"Search Shops"**; submit with **Enter** (no separate button).
- **RULE: search the BARE DOMAIN only** (e.g. `renpho.com`), NOT a full product URL —
  `renpho.com/collections/eye-massager` does NOT surface the store. Strip everything
  after the first slash. (Confirmed S-SH1; see learnings.md.)
- **⚠ SH-2 CORRECTION:** bare domain ALONE is NOT enough — it fails for stores whose canonical domain
  has `www.` (e.g. `seattosleep.co.uk` → 0 results, but `https://www.seattosleep.co.uk` → found). Strip
  only the PATH, then try in order: **full Store Link URL → `https://www.`+domain → bare domain → brand
  name as words**; ALWAYS open the result and confirm the shop's shown domain matches. See learnings.md SH-2.
- Result cards link to `/shops/{shop_id}`. Skip the `/shops/track` nav link.

## Shop page data (`/shops/{shop_id}`)
- **Revenue Performance:** Day / Week / Month + % change
- **Store Overview:** Country · **Store Creation Date** · **SKU count** · **Tracked by N users**
- Revenue Trends chart · Advertising Activity
- Links: View Products · **View on Facebook Ads Archive** (→ FB department cross-ref) · Add to Collection
- Shopify Theme · Business Categories · Shopify Apps · Tech Stack
- **Competitor Analysis:** rival stores (incl. regional UK/EU variants) with revenue +
  Top Revenue Producers / Top Advertised Products — a free competitive landscape per store.

## Product page data (`/shops/{shop_id}/{product_id}`)
- **Product Performance** (Day/Week/Month revenue + change) · **Store Performance**
- **Product Created** + **Store Created** dates · price · description · tags · vendor · category
- View on Shopify Store · View Other Products From This Shop
- **Related Products** — same product type from other shops, each with its own revenue.

## Always treat revenue as an ESTIMATE
ShopHunter numbers are estimates — directional only. Corroborate (ad activity, reviews,
multiple sellers, longevity) before trusting. Use **Store Creation Date + SKU count +
trajectory** to separate a mature brand (not a white-label opening) from a fresh/growing store.

## VPS helper scripts (ad-hoc, S-SH1 — `/opt/market-research-agent/scripts/`)
`set_shophunter_creds.py` (also in repo) · `sh_login.py` · `sh_explore.py` ·
`sh_shop_search.py` · `sh_open_shop.py` · `sh_renpho_shots.py`. Reusable patterns —
rewrite/extend as needed; they are not canonical yet.

## Shop Collections + Newest-First monitoring (mapped SH-5, 2026-05-26)
The watchlist layer Marina proposed — add proven shops to a Collection, then monitor what they LAUNCH.
- **URLs:** Shop Collections = `/collections/shops` · Product Collections = `/collections/products` ·
  Tracked Shops = `/collections/shops?tracked=true` · Add Shop = `/shops/track`.
- **Add a shop to a collection — 2 entry points (both confirmed live):** (a) Explore Shops card → **⋮** menu →
  *Add/Remove from Collection*; (b) shop detail `/shops/{id}` → button *Add/Remove from Collection*. Dialog offers
  **Add** (to existing collection) + **Save New** (create) + **View Collections**. With ONE collection, clicking **Add**
  adds the shop. **SCRIPTABLE:** goto `/shops/{id}` → click "Add/Remove from Collection" → click "Add". (VERIFIED SH-5:
  bulk-added nulooa+hago → collection 2→4. ⚠ it's a TOGGLE — check membership before clicking to avoid removing.)
  **→ SH-6 UPDATE: there are now MULTIPLE collections (Shops + niche ones) — the dialog lists a row per collection; use the
  niche-aware, toggle-safe `sh_collection_manage.py` (see "Multi-collection" section below), not the single-collection `sh_collection_add.py`.**
- **Monitoring feed:** collection → **Products** tab → sort **"Newest First"** = "Products from shops in this collection"
  (aggregates ALL products of the collection's shops, each with price + Product Ads + Product Revenue). Other tabs:
  Shops / **Similar** (suggests similar shops → watchlist multiplier) / Ads / News. Include/Exclude-All toggles pick which
  shops feed the Products view.
- **Check-up mechanic (planned, human-in-loop):** scrape Products→Newest-First → dedup vs a seen-product-id list →
  conservative cut + description filter → surface NEW candidates. Cadence ~every 2-3 days.
- Recon scripts: `sh_collections_recon.py`, `sh_collections_recon2.py`, `sh_collection_add_test.py`.

## Multi-collection / niche sub-collections (mapped SH-6, 2026-05-26 — Marina's structure)
**Structure (Marina-agreed):** keep ONE general collection **"Shops"** (every tracked shop) + one **per-niche** collection
(e.g. **"Baby & Toddler"**, **"Home & Garden"**, future "Arts & Entertainment" / "Toys & Games"). A shop can be in MANY
collections. Why: the **Similar / Ads / Products(Newest-First)** views are far more useful scoped to a niche than over a
mixed 100+ pool (cross-niche "Similar" = noise). Per-niche also makes Newest-First monitoring niche-specific.
- **The dialog** (shop detail → "Add/Remove from Collection") = a modal **"Manage Shop Collections"** (`div.max-w-md`):
  a **"New Collection Name" input + "Save New"** button (create; Save New is `disabled` until text entered, and it also
  adds the current shop to the new collection), then ONE ROW PER existing collection: `<span class="font-medium">NAME</span>`
  + a button whose text is **"Add"** (NOT a member) or **"Remove"** (already a member). Bottom: View Collections / Close.
- **RELIABLE membership read (the strengthened verification):** the per-row Add/Remove label is the truthful membership
  source — far better than the `/collections/shops` page count, which **UNDERCOUNTS due to DOM virtualization/lazy-load**
  (SH-6: page showed ~50–96 when the real count was ~100). Always verify membership via the dialog label, not the page.
- **TOGGLE-SAFETY:** the row button is a toggle (Add↔Remove). To add safely you must read the label first and click ONLY
  when it says "Add" — never click "Remove". This guarantees you can't drop a shop from "Shops" when adding it to a niche.
- **Script: `scripts/sh_collection_manage.py`** (reusable, toggle-safe) — modes:
  `create "<Name>" <seed_id>` · `add "<Name>" <id…>` (clicks Add only) · `verify "<Name>" <id…>` · `list <id>` (all collections + state for one shop). DOM selectors scoped to the modal.
- **SH-6 state:** "Shops" = all ~100; "Baby & Toddler" = 53 B&T shops; "Home & Garden" = 47 H&G shops. Verified cross-correct
  (B&T shops ∈ Baby&Toddler+Shops, ∉ Home&Garden; H&G shops ∈ Home&Garden+Shops, ∉ Baby&Toddler; Shops intact for all).
- **Going forward:** each category session seeds its shops into BOTH "Shops" (general) AND its own niche collection.
