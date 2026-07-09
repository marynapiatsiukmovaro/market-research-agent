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

**Stage 0 — Data acquisition. ⭐ CURRENT = the captured CSV universe** (`methods/csv-export.md` +
`operational-memory/data-inventory.md`): the whole active universe is already downloaded (Shopify 2.89M +
Woo 4.26M, 162 cols). Slice the CSV to a niche → Stage 1. No per-niche dump needed anymore.

> **⚠️ RETIRED below — the old paginated API dump (preserved, do NOT use).** Superseded S14 by the CSV export;
> it burned the Premium 2,000-search/mo quota → HTTP 402. Kept for reference «вдруг вернёмся».

**(RETIRED) Dump (VPS, API, ~0 tokens).** `sl_dump_full.py "<cat path>" <slug>`: POST `/json/auth/domains`
with the advanced **`bq` (Bleve)** query — Platform=Shopify, Status=Active, Category(`match`),
**Created≥2020** server-side (`cratyyyymm` TermRange). Big subcategories (>25k) are split into
**created windows** (each <25k) and merged → no ceiling loss (HI 27,052 collected exact). `cursor`
pagination (50/page, `ps` capped at 50; ~21 min for 27k → run in background). **Country: currently NO `cc`
filter** — we dump ALL markets (results are US-dominant + UK/DE/EU/CA/AU/NZ mixed in, all acceptable per our
target markets). Per-country query+merge is only needed IF we later restrict markets (multi-cc comma = AND bug →
one country per query then merge — TO BUILD). Persist raw JSON; reuse, don't re-pull. (`sl_dump3.py` = quick sample.)

**Stage 1 — Select next 250 unprocessed (VPS, ~0 tokens). ⚠ SUPERSEDED by RULE 24 (S3, Marina-locked) — NO field filters.**
Use **`sl_select_build.py`** (current, decoupled: excludes processed ∪ enriched_index; `sl_select_all.py` = legacy positional selector, `sl_select.py` = retired band-filter): the ONLY exclusion is already-processed/enriched (RULE 19/24). `visits` (`mvis`) is used
**for batch ORDER only** (desc; missing-visits sorted last but KEPT, never dropped) — **never as a gate**. Do NOT filter by
`erf`/`apf`/`pc`/weight: these fields are unreliable and missing≠dead (Marina killed even the catalog-giant `pc>2000` cut:
"pc-данные тоже могут врать… пусть будет"). `cat_flag` from `pc` may still be shown as CONTEXT in the table, but it gates nothing.
> *Historical (pre-RULE-24): `sl_select.py` band-filtered by visits + revenue≤$1M + price≤$350 + cut catalog-giants. That
> approach is retired for niche-exhaust — it silently dropped stores lacking a field, and S4 proved 2 winners sat at visits
> 363/387 (below the old 1k band) → would have been lost. Keep visits for ordering only.*

> **⚠ Stage-1 conservative cut — RETIRED by RULE 24 (S3, Marina-locked). DO NOT field-filter.** The list below
> (price>$350 / rev>$1M / catalog-giant pc>2000 / apparel-bulky) was the pre-RULE-24 cut; it is **superseded** because
> those fields are unreliable (missing≠dead) and even the `pc>2000` cut was killed by Marina. **Now: drop NOTHING at
> Stage 1 except already-processed.** apparel/bulky/oor are recognized later at Stage 2/3 (by `kind`/`product_class` +
> the live read), never pre-dropped. Band selection by visits = ORDER only (RULE 24), reported with counts (RULE 1).

**Stage 2 — Enrich finalists from the LIVE catalog (VPS, Playwright + proxy).** **`sl_enrich4.py` (LIVE — v4.2, 8 workers).**
Implements the full v2 product-centric contract PLUS v4 essence + self-check (`product_class` incl. `diy-home`,
`store_type`, homepage-hero self-check, `new_products_30d`, subdomain-collapsed convergence, class-aware ABC sort,
product-handle link). **v4.2 (Marina, 2026-06-01) — "ни один магазин не тонет на первом проходе":** brings ENOUGH per
store (0-token) that a confident no-open skip is trustworthy → adds the store's **own homepage pitch**, **BOTH heroes**
(best-seller + homepage banner), **long desc + feature bullets**, banner image, and a **`needs_live`** worklist flag
(low hero/desc conf · price-unknown · banner-hero≠pick · unreachable) — the agent MUST live-open every `needs_live` +
unreachable store (op-rule RULE 23). Dropped (Marina): review-count/brand-claim markers (fakeable). **v4.1 speed (0
quality loss):** 8 workers · fast-fail 15s×2. `sl_enrich3.py`
= fallback; `sl_enrich2.py` = retired legacy single-hero. For each store: fetch the **best-selling / frontpage / featured collection**
(sales order = real hero) → fallback `/products.json`. Surface top catalog products + pick a
hero candidate; record REAL price, description, kind (physical / ingestible / skincare / apparel),
пустышка flag, image, within-batch convergence. **Health-check the proxy first** (`sh_proxy_check.py` — the
shared iProyal proxy-check; Store Leads uses the same `cookies/proxy.creds` + dedicated IP as ShopHunter).

> **⭐ PRODUCT-CENTRIC — LIVE in `sl_enrich4.py` (v4).** The unit is
> the PRODUCT, not the store. Stage-2 contract (full in `methods/subagent-spec.md` + `hypotheses/_active.md`):
> (1) **Open-ladder** so no live store is a silent DROP — `best-selling→frontpage→featured→/products.json→homepage HTML`;
> all fail → `reachable:false, reason` = "needs manual look". (2) Return **TOP-3 product candidates** per store,
> each with full desc + **REAL price normalized to USD** + type + `hero_confidence` (high if from a sales-ordered
> collection, low if from `all`/HTML) + `desc_confidence` (ok/empty/mismatched → empty/mismatched MUST be live-WebFetched
> before scoring; we do what ShopHunter only PLANNED at SH-8). (3) **Early signals per product, NOW:** storefront position
> + investment (desc len / #images / #variants / badges) + **convergence within the subcategory** (~27k of the dump, dedupe
> geo-mirrors) — revenue is NOT the selector. **Pre-flight 5 checks before any run** (VPS up · login valid · no duplicate
> worker · proxy healthy · quota OK) + **follow FB RULE 4c** (one-line nohup · sentinel-detect not process · no `pgrep -f`,
> use `[s]l_enrich4` · bracket-kill standalone · NEVER `-o` ssh flags). Every batch: **hand-check a random sample of the
> dropped pile** (loss-measurement → report the number) + **flag interesting stores to the keep-list** (RULE 20, feeds a
> future newest-first monitor). v4 ALSO adds: `product_class` + `store_type` (essence), homepage-hero + desc self-check
> (RULE 22), `new_products_30d`. DEFERRED: the monitor JOB itself, fresh-product job, FB-pixel-as-criterion, ShopHunter
> enrichment (provisional — decide after batch 6 whether it earns its paid sub).

**Stage 3 — Deep-score (chat) — the real filter. NEVER skip / never eyeball the proxy tier.**
- **ENTRY GATE FIRST (RULE 25 + 26 — the S5 fix; updated S18/S19):** run **`sl_accept_chunk.py <enriched.json>` → ACCEPT**
  (it owns the DATA verdict and wraps `sl_qa.py`; reading raw `sl_qa` output and interpreting its ⛔ by hand is what left the
  last funnel step on discipline). Then **`sl_card_parity.py <enriched.json>` → ✅ PARITY PASS** — it proves the FOUNDER's HTML
  (`sl_stage2_table.py`) and the AGENT's text (`sl_project_any.py`) render the same card. **Never** an ad-hoc/partial reader
  (a hand-made reader showing 1 product of 3 is what zeroed S5). State the acceptance **numbers** in the checkpoint, never a
  memorised sentence.
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
- **⚠ Store currency — `/meta.json` CAN LIE (found S19, live case).** `magnetichoop.com` (HK) declares `currency: USD`
  in `/meta.json` while its storefront sells in **HK$** → a HK$680 hoop (real ≈ $87) reached the card as `$680 [out of
  range]` and would have been dropped as too expensive. The S2 learning "the TRUE store currency comes from `/meta.json`"
  is **not always true**. Treat the normalized price as directional; the live site decides (RULE 7).
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
✅ DONE: `bq` advanced query (created≥2020 + multi-cat OR + 25k-window bypass) · table/field calibration ·
first full clean dump (HI≥2020 = 27,052) · **product-centric enricher v4** (product_class/store_type/self-check/
new_products_30d) · **master record + keep-list** (sl_mark_processed, RULE 20) · stage-artifact HTML to Desktop (not PNG — Marina S6).
TO BUILD: multi-country merge in the dumper · the newest-first monitor JOB (deferred, ShopHunter-side) ·
validate the PRICE-CHECK fix on a live price-0 store · then (when stable across more batches) promote rules.
