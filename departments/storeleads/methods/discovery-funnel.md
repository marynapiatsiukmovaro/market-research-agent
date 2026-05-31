# Store Leads — Discovery Funnel (PILOT method — in development)

> **Status: PILOT (1 full run, 2026-05-30 — US Kitchen & Dining 200 stores).** Validated that
> the chain runs end-to-end. NOT yet stable; numbers are ILLUSTRATIVE, never quotas. Living doc —
> do NOT carve into a permanent op-rules file until validated across several sessions.

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
pagination (50/page, `ps` capped at 50; ~21 min for 27k → run in background). ONE country per query
(multi-cc AND bug) → merge. Persist raw JSON; reuse, don't re-pull. (`sl_dump3.py` = quick sample.)

**Stage 1 — Client-side filter + table (VPS, ~0 tokens).** Created≥2020 is now server-side (Stage 0).
Client-side on the dump fields: `erf` (monthly revenue) `≤ $1M`, `apf` (avg price) `≤ $350`, weight,
and **sort by `mvis` (Est Visits) desc** (primary ranking signal — start >1000 visits, don't exclude lower).
Add a `cat_flag` from `pc` (product count): hero ≤300 / mid / catalog-giant >2000 (high pc =
product is one of many = weaker hero, like ShopHunter SKU insight). Output = the Stage-1 candidate
table (domain, merchant, est $/mo, avg price, created, reviews, #products, FB-pixel, …).

**Stage 2 — Enrich finalists from the LIVE catalog (VPS, Playwright + proxy).** `sl_enrich2.py`
(4 workers). For each store: fetch the **best-selling / frontpage / featured collection**
(sales order = real hero) → fallback `/products.json`. Surface top-8 catalog products + pick a
hero candidate; record REAL price, description, kind (physical / ingestible / skincare / apparel),
пустышка flag, image, within-batch convergence. **Health-check the proxy first** (`sh_proxy_check.py`).

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
