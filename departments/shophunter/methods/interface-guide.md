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
