# ShopHunter — Capabilities

Two parts: what we can ALREADY do (inherited, ready now) and what ShopHunter the tool
offers (to be mapped in the first exploration session).

## Part 1 — What we already do (inherited from core/ + shared/)
These exist today. ShopHunter references them — it does not recreate them.

| Capability | Where it lives |
|------------|----------------|
| Score a product 0–100 + Marina Veto Checklist | `core/scoring-system.md` |
| Hard-reject weak products (branded, пустышка, price, logistics, saturation) | `core/mandatory-filters.md` |
| Founder quality bar / winner definition | `core/founder.md` + `shared/founder-taste.md` (company-wide quality bar) |
| Assess a store / company signal (revenue trajectory, longevity, multi-store demand) | `shared/skills/shophunter.md` |
| Deep validation of a candidate (score 85+) | `shared/product-validation.md` |
| Report a product (Notion + shared logs) | `shared/notion-workflow.md`, `shared/reported-products.md`, `shared/rejected-products.md` |
| Analysis skills (wow-factor, UGC, sourcing, trend, paid-traffic) | `shared/skills/` |

Net: the moment we can SEE a product in ShopHunter, we can already filter it, score it,
validate it, and report it. What we do not yet know is what ShopHunter lets us see.

## Part 2 — What ShopHunter offers (mapped Session SH-1, 2026-05-24)

Access: `app.shophunter.io`, login persisted in a saved browser profile on the VPS.
Operated headless (Playwright) → screenshots + page text. No bot-block on login.

### Discovery surfaces (left nav)
- **Explore Products** (`/explore/products`) — product grid with revenue + ads per item
- **Explore Shops** (`/explore/shops`) — store-level view *(SH-3+: our PRIMARY discovery surface — category-checkbox filter → scroll-to-exhaustion dump; see `methods/discovery-funnel.md`)*
- **Explore Ads** (`/explore/ads`) — ad-level view *(not yet opened — natural FB cross-ref)*
- **Staff Picks** (`/staff-picks`) *(not yet opened)*
- **Tracked Shops** / **Shop & Product Collections** / **Add Shop** (`/shops/track`) — watchlists

### Filters (Explore Products)
- **Categories** — full Google product taxonomy (Health & Beauty, Home & Garden, Electronics, Sporting Goods, Furniture, Office Supplies, Toys & Games, Baby & Toddler, etc.)
- **Country** — US, Canada, UK, Germany, France, Australia, New Zealand… (= matches our target markets) + **Exclude Country** (India, Pakistan)
- **Locale** (English/French/German/Spanish/Dutch)
- **Product Features, Ads, Product Revenue, Shop Revenue, Shop Features, Shop Ads % Change**
- **Save / Load Presets** — reusable filter sets (good for repeatable scans)

### Data per product — grid card
Name · store/brand · price · **Product Ads** (count) · **Product Revenue Day/Week** + 30d trend + % change · mini chart.

### Data per product — detail page
- **Product Performance:** revenue Day / Week / Month + change
- **Store Performance:** revenue Day / Week / Month + % change
- **Revenue Trends** chart · **Advertising Activity** (often "No data")
- **Product Created date** + **Store Created date** → powers longevity + mature-vs-fresh
- Store domain · price · description (copyable) · tags · vendor · country/currency · category
- Links: **View on Shopify Store** · **View Other Products From This Shop**
- **Related Products** — same product type from OTHER shops, each with its own revenue → instant convergence / saturation / competitor read

### What this means for us
- Revenue at **product AND store** level = the traction signal we wanted (treat as **ESTIMATE** — see guardrails when written).
- **Store/Product Created dates** directly enable the mature-brand-vs-fresh-store guardrail.
- **Country filter** scopes straight to target markets.
- **Ads** field — ⚠️ **SH-4 correction (Marina):** ShopHunter's own ad-COUNT/linkage is UNRELIABLE (often the wrong FB
  account) — treat as ESTIMATE that REQUIRES VERIFICATION, do NOT decide on it. The valid join is cross-checking the
  REAL Facebook Ads Library (our other department) directly: advertised AND selling = strongest signal — but verify there, not via ShopHunter's number.
- **Related Products** gives a per-candidate competitor map for free.

### Still to map (next sessions)
- Explore Shops / Staff Picks views; how to sort by growth / find NEW stores
- Export vs read-on-screen only
- How reliable revenue numbers look vs reality
