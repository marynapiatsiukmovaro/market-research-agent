# Store Leads — Discovery Funnel (PILOT method — in development)

> **Status: SYSTEM-BUILD — chain validated twice** (2026-05-30 US Kitchen & Dining 200; 2026-05-31 Home
> Improvement band 200). Numbers here are ILLUSTRATIVE, never quotas. Permanent discipline now lives in
> `operational-memory/op-rules.md`; this doc holds the *method* (the how) and stays a living doc. Funnel
> mechanics still being calibrated across sessions before any further promotion.

## Core idea
Store Leads returns rich STORE-LEVEL data inside the search result, so heavy filtering is cheap
and **only finalists need a live site visit**. The source-agnostic tail (enrich → deep-score) is
the same discipline as ShopHunter; only Stage-0 (the source) is new.

## Founder principle (non-negotiable — Marina)
**Every store gets analysed; nothing is lost.** Volume is not the point — coverage + correctness
are. **A live site visit is REQUIRED** for finalists because service data (Store Leads, like
ShopHunter) is not always accurate (esp. price, and "which product is the hero"). Verify on the
site before asserting. The browse-pool ensures the founder can catch what the agent's bar missed.

## The chain (numbers illustrative)

**Stage 0 — Dump (VPS, API, ~0 tokens).** `sl_dump_full.py "<cat path>" <slug>`: POST `/json/auth/domains`
with the advanced **`bq` (Bleve)** query — Platform=Shopify, Status=Active, Category(`match`),
**Created≥2020** server-side (`cratyyyymm` TermRange). Big subcategories (>25k) are split into
**created windows** (each <25k) and merged → no ceiling loss (HI 27,052 collected exact). `cursor`
pagination (50/page, `ps` capped at 50; ~21 min for 27k → run in background). **Country: currently NO `cc`
filter** — we dump ALL markets (results are US-dominant + UK/DE/EU/CA/AU/NZ mixed in, all acceptable per our
target markets). Per-country query+merge is only needed IF we later restrict markets (multi-cc comma = AND bug →
one country per query then merge — TO BUILD). Persist raw JSON; reuse, don't re-pull. (`sl_dump3.py` = quick sample.)

**Stage 1 — Client-side filter + table (VPS, ~0 tokens).** Created≥2020 is now server-side (Stage 0).
Client-side on the dump fields: `erf` (monthly revenue) `≤ $1M`, `apf` (avg price) `≤ $350`, weight,
and **sort by `mvis` (Est Visits) desc** (primary ranking signal — start >1000 visits, don't exclude lower).
Add a `cat_flag` from `pc` (product count): hero ≤300 / mid / catalog-giant >2000 (high pc =
product is one of many = weaker hero, like ShopHunter SKU insight). Output = the Stage-1 candidate
table (domain, merchant, est $/mo, avg price, created, reviews, #products, FB-pixel, …).

> **Stage-1 conservative cut — what counts as DEFINITE-NO (drop only these; when unsure, KEEP):**
> - avg price **> $350** (hard ceiling) — out of any plausible band.
> - est revenue **> $1M/mo** — established brand, not an emerging white-label window.
> - **catalog-giant** `pc > 2000` — a retailer/marketplace, not a single-hero store (deprioritize for THIS batch;
>   stays in the dump for later, not "lost").
> - **apparel / clothing** category (we don't sell it) + obvious **high-ticket / bulky** types (furniture, large
>   appliances, composting toilets — RULE 10).
> - Everything else is a SURVIVOR → goes to Stage 2. No subjective name-based pre-pick (RULE 5). Band selection
>   (e.g. visits 1k–50k) is a transparent batch choice, reported with counts (RULE 1) — not a silent cull.

**Stage 2 — Enrich finalists from the LIVE catalog (VPS, Playwright + proxy).** `sl_enrich2.py`
(4 workers). For each store: fetch the **best-selling / frontpage / featured collection**
(sales order = real hero) → fallback `/products.json`. Surface top-8 catalog products + pick a
hero candidate; record REAL price, description, kind (physical / ingestible / skincare / apparel),
пустышка flag, image, within-batch convergence. **Health-check the proxy first** (`sh_proxy_check.py` — the
shared iProyal proxy-check; Store Leads uses the same `cookies/proxy.creds` + dedicated IP as ShopHunter).

**Stage 3 — Deep-score (chat) — the real filter. NEVER skip / never eyeball the proxy tier.**
- Read **ALL** candidate sheets (A+B+C), no gut top-N (FB RULE 8). The enricher's A/B/C/`score`
  is a **revenue/price sort-aid, NOT quality** — lead with WOW + founder-taste, never the tier.
- **Hero-confirmation gate:** for every genuine-looking white-label candidate, **WebFetch the
  live homepage/best-seller to confirm the real hero + price + wow** before scoring (the enricher
  mis-picks heroes — e.g. a bundle, or a $33 grater where the list implied a grill). Never score on
  a thin/mismatched description.
- Run **`core/scoring-system.md` 100-pt + the Marina Veto Checklist** on the confirmed hero.
- Output buckets: **65+ (report-worthy) · 55–64 (borderline, founder review) · browse-pool
  (curated UNIQUE genuine-product store links)**. Patterns + niche-yield note.

**Checkpoint → Notion only after Marina's explicit OK** (work autonomously through dump→deep-score,
then WAIT). Every link in the checkpoint = a clickable markdown hyperlink. Browse-pool = unique
links only. Convergence/revenue earns at most Watchlist, never auto-Consider.

## Data-trust map — what to trust vs verify (Store Leads fields)
Service data is directional. Per field:
- **Price (`apf`/min/max) — NEVER trust; ALWAYS confirm on the live site** before scoring (the #1 unreliable field;
  ShopHunter caught $45 vs real $159.95 repeatedly; en-route currencies/locale formatting also distort it).
- **Est revenue (`erf`) — directional only.** Cross-validated OK for Stoov ($314k≈SH $332k) but off for CompoCloset
  ($344k vs SH $1M). Use for rough banding, corroborate (ShopHunter, ad activity) before relying.
- **Est Visits/PageViews (`mvis`/`mpv`) — good as a RANKING signal**, not an absolute. Start >1000, don't exclude lower.
- **Hero / "which product" — NEVER trust the enricher's auto-pick;** confirm on the live best-seller page (it grabs
  bundles/accessories/replacement parts, esp. when it falls back to the `all` collection).
- **Reviews (`combrs`/`tprs`) — weak/fakeable;** never a selector.
- **Social follower counts / 30-day growth — ABSENT in the API** (only account links exist).
- **Category — `None` blind spot:** ~400k/2.85M active Shopify have no category → any category filter silently drops
  them. We accept this (we work category-by-category) but never claim "full universe" coverage.
- **ShopHunter cross-check — ~25% hit-rate** on emerging Store Leads stores; absence in SH ≠ a negative signal.

## Adopted from ShopHunter (keep)
VPS-side heavy lifting, chat gets only finalists (FB RULE 7) · verify ALL above bar, no gut top-N
(FB RULE 8) · parallel workers (NOT parallel claude — credit safety) · revenue/metrics = ESTIMATE,
corroborate · Tier-1 vs Tier-2 (propose system changes, don't self-write) · end-of-session memory +
HANDOFF · human-in-loop · checkpoint-before-Notion · lead with WOW/taste not the proxy tier.

## Lessons from the pilot (2026-05-30, US Kitchen & Dining 200)
1. **Real Stage-3 is mandatory** — the first attempt eyeballed the enricher's A/B/C tiers and
   editorialised scores instead of running 100-pt + Veto with confirmed heroes → unreliable
   "no winner". Fixed: read all + confirm heroes + score properly. Never cut this corner.
2. **Hero from best-selling collection** (`sl_enrich2`) > highest-priced-in-range; but ~half the
   stores have no best-selling/frontpage collection → fall back to catalog order (weaker) → confirm
   on site for finalists.
3. **Rank/visits-top surfaces the BIGGEST stores = established brands** (Hunter Fan, Honeywell,
   Grohe) → emerging white-label sits MID-list (getcanopy, dreo, horow, forgenflame). Confirmed
   again on the full HI≥2020 dump. So Est-Visits sort = the entry order; white-label selection is
   by eye/score across the whole created≥2020 set (which `bq` now gives us complete).
4. **Kitchen & Dining yield (this band) = brand/catalog/artisan-glass/knife-collector/decor/food
   heavy; few impulse white-label gadgets, and those skew branded/premium/saturated.** Tier-1 yield
   fact — do NOT close the niche or add a filter; keep scoring as-is. (Compare to ShopHunter H&G.)

## Open / to build (next sessions)
✅ DONE: `bq` advanced query (created≥2020 server-side + multi-cat OR + 25k-window bypass) · table/field
calibration with Marina · first full clean dump (HI≥2020 = 27,052). · TO BUILD: multi-country merge in
the dumper · saved-filter weekly-email monitoring (Lists) · optional ShopHunter enrichment for
top finalists · then compact + promote stable rules.
