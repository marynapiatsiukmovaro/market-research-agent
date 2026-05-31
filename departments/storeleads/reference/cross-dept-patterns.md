# Cross-Department Patterns — observed, NOT adopted (reference / archivable)

> **Status: REFERENCE only.** Patterns seen in ShopHunter / Facebook Ads Library that Store Leads does **not** run
> today, but are worth keeping on the radar. Not active rules — do not apply them as if they were. When clearly
> irrelevant or superseded, this file can be archived. (Marina's idea, 2026-05-31: "сохранить, пометить, потом заархивировать.")

## From ShopHunter (closest sibling — same "store-first" super-department)
- **Shop Collections + "Newest First" monitoring.** Add proven shops to a Collection → watch what they LAUNCH next
  (Products tab → Newest First). A watchlist/monitoring layer. *Store Leads analog (future):* saved-filter weekly-email
  monitoring of newly-created stores in a kept subcategory. Not built yet.
- **Per-niche sub-collections** (one general "Shops" + per-niche, toggle-safe membership). Useful when scoped views
  (Similar / Ads / Newest) beat a mixed pool. *SL analog:* per-subcategory saved filters.
- **Competitor Analysis as a convergence finder** — already folded into our optional SH-enrichment (see
  `shophunter-enrichment.md`); this is the one we DO use on demand.

## From Facebook Ads Library (different super-department — ad-first, not store-first)
- **Keyword-map scorecard** (per-keyword yield history → plan which keywords to run). Store Leads is category-first,
  not keyword-first → not directly applicable; the analog is a **subcategory-yield log** (which subcats yield gems).
- **Autonomous Mode** (run all keywords sequentially with a checkpoint each, HARD-STOP conditions kept). FB earned it
  at S30; Store Leads has NOT earned it — human-in-loop for now. Keep as the eventual target shape.
- **seen-advertisers rolling 20-session window** (anti-duplicate memory with rotation). *SL analog:* a seen-domains
  set across batches so we don't re-surface the same stores. Worth building when we scale to many batches.

## Super-department concept (Marina, 2026-05-31 — do NOT write to project yet)
Departments that share an ALGORITHM cluster into a "super-department":
- **Store-first super-dept:** ShopHunter + Store Leads + (future) similar services (e.g. another store-index). Very
  similar funnel — mostly differ in HOW stores are extracted; share discipline + enrichment.
- **Social/ad super-dept (future):** Instagram / TikTok — analysed very differently → its own super-department.
This is why Store Leads inherits ShopHunter's maturity so directly. Reference only; not a structural commitment yet.
