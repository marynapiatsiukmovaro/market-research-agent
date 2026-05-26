# HYPOTHESIS — Tracked-Shop Collection + "Newest First" monitoring layer

**Status: PARKED (Marina, SH-5, 2026-05-26).** Idea agreed + seed built (47 shops); the CHECK-UP JOB is **not built yet** —
revisit once the collection is larger (Marina: "сначала собрать больше магазинов, потом посмотреть"). Recorded here as a
hypothesis to validate later, not active work.

## The idea
Maintain a ShopHunter **Collection** of proven/competent shops (operators with traction). Every 2–3 days, check the
collection's **Products → Newest First** feed to catch the NEW products those operators LAUNCH — early-winner detection
BEFORE saturation (= the Entry-Window we score for). A monitoring layer ON TOP OF the one-off category dumps, not a replacement.

## Why it could be strong
- A category dump = "who exists now." A tracked-shop Newest-First feed = "what proven operators are launching." Catching a
  winner while it's NEW is the highest-value signal in store-first discovery.
- Operators with existing traction + a fresh product = pre-validated seller + fresh entry window.

## Mechanics (mapped SH-5 — see `methods/interface-guide.md`)
- **Collection:** `/collections/shops`. Seeded via `scripts/sh_collection_add.py <shop_id…>` (shop-detail →
  "Add/Remove from Collection" → "Add"). **Add/Remove is a TOGGLE → check membership before bulk-adding** so a shop we already
  track is not accidentally removed.
- **Feed:** collection → **Products** tab → sort **"Newest First"** = aggregated products of all collection shops (price +
  Product Ads + Product Revenue each). Other tabs: Shops / **Similar** (watchlist multiplier) / Ads / News.

## The CHECK-UP JOB (to build when un-parked)
1. Scrape `/collections/shops` → Products → Newest First.
2. **Dedup vs a `seen-product-id` list** (like FB's seen-advertisers) → keep only products NEW since the last run. *(Without
   this, a 1000+-shop collection's feed is huge to re-scan every time — this is the key mechanic.)*
3. Apply the conservative cut + live-description filter (same funnel) → surface NEW candidates.
4. Cadence ~every 2–3 days, **human-in-loop** (ShopHunter has not earned autonomous mode).

## Open questions to test later
- Collection size limit? Feed pagination / performance at 1000–2000 shops?
- "Similar" tab as an auto-multiplier (harvest similar shops of the best operators).
- "News" tab — what is it (shop-level change alerts?).

## Un-park trigger
When the collection is large enough to make a 2–3-day check-up worthwhile (Marina decides). Grow it each batch via the
Collection seeding rule (`methods/discovery-funnel.md`).
