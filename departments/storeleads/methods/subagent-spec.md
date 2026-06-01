# Store Leads Stage-2 Sub-Agent Spec — "Candidate Sheet"

> **Adapted from ShopHunter's subagent-spec (SH-4) to Store Leads fields.** Defines EXACTLY what the
> Stage-2 enricher writes, so the main agent's keep/cut is accurate and repeatable (no improvising per run).
> **Implemented by `scripts/sl_enrich4.py` (LIVE — Playwright + iProyal proxy, parallel workers).** `sl_enrich3.py`
> = previous version (fallback); `sl_enrich2.py` = legacy single-hero (retired). The v2/v3 boxes below are the
> design history; the CURRENT contract = v4 (the v3 product-centric contract PLUS the v4 essence + self-check fields).

> **⭐ v4 ADDITIONS (Marina-agreed S3, 2026-06-01) — store/product ESSENCE + self-check (all 0-token, VPS):**
> 1. **`product_class`** per candidate — consumer-gadget / appliance / fixture / kitchen / decor / part / material /
>    pro-tool / apparel. STRONG consumer DEVICE words win first (a bidet isn't sunk to "part" because its desc says
>    "adapter"); bias toward "consumer" = the zero-loss-safe direction. ~80% of a "heavy" category self-labels as trade.
> 2. **`store_type`** — single-product-DTC / niche-brand / trade-store / parts-supply / services / catalog-giant.
> 3. **SELF-CHECK (RULE 22):** ALSO pull the homepage featured hero (catches collection-hero ≠ real front hero,
>    e.g. heatka/hanboost); re-fetch a candidate's own product page when its desc is empty/mismatched.
> 4. **`new_products_30d`** — store actively launching = live/test signal + feeds the keep-list monitor (RULE 20).
> 5. **brand_core** collapses subdomains to the registrable root (parts.cleanburn / parts.gingerich.cleanburn = ONE
>    brand) + 2-part TLDs → fixes false convergence.
> 6. **ABC reformula:** trade classes deprioritized, consumer lifted — STILL ONLY A SORT-AID; main agent reads ALL.

> **v2 PRODUCT-CENTRIC contract — NOW IMPLEMENTED in `sl_enrich4.py` (v4 LIVE).** (History: agreed S2 2026-05-31;
> coded in v3; extended + self-check in v4 S3 2026-06-01. The "target / not yet aligned" caveats are GONE — this is live.)**
> The unit of the hunt is the **PRODUCT, not the store** (a store is a box; we pull its 1–2 golden products).
> The enricher's output (the v4 fields are in the ⭐ box at the very top; the v2 core below):
> 1. **Open-ladder** (no silent DROP): `best-selling`→`frontpage`→`featured`→`/products.json`→**homepage HTML**;
>    if all fail → `reachable:false, reason:<why>` = **"needs manual look"**, NOT dropped. (S2: 17/18 "unreachable"
>    were alive — products.json just disabled.)
> 2. **TOP-3 candidates per store** (not 1 hero), EACH with full desc + REAL price + type — so the main agent
>    chooses seeing the picture, and a golden product in slot #2 is never lost.
> 3. **Early signals per product (NOW)** — storefront position + investment (desc len / #images / #variants /
>    badges) + **convergence WITHIN the subcategory** (~27k stores of the dump, NOT the whole universe — Marina S2
>    confirmed this scope is cheap; dedupe geo-mirrors, 7 country-mirrors of one domain ≠ ×7). Revenue is NOT the selector.
> 4. **Currency → USD** (normalize AUD/ZAR/EUR; price is the #1 unreliable field).
> 5. **`hero_confidence`** per candidate: `high` if from a sales-ordered collection (best-selling/featured),
>    `low` if from `all`/homepage HTML — tells the main agent which to live-confirm first.
> 6. **`desc_confidence`** per candidate: `ok` / `empty` / `mismatched` — Marina S2: do what ShopHunter only
>    PLANNED at SH-8 but never coded (we go first). Empty/mismatched → main agent MUST WebFetch the live page
>    before scoring (kills "winner buried by a bad description", SH-7 SlotPro 52→66).
> The enricher emits all of this directly (v4); the main agent still reads the 3 tops, confirms the hero on the
> live site, and scores — judgment stays human (RULE 6/7).

## Where this fits in the funnel
```
Stage 0  Dump via bq (Shopify+Active+Category+Created≥2020, windowed)        [sl_dump_full.py — reuse]
Stage 1  Client-filter + table (price/revenue/weight band) + sort by Est Visits
         → CONSERVATIVE cut: drop only DEFINITE-NO (see discovery-funnel.md "Stage-1 conservative cut")
Stage 2  ← THIS SPEC. Enricher reads the LIVE catalog of survivors, writes a Candidate Sheet.
Stage 3  Main agent reads ALL sheets → live hero+price confirm → Marina Veto + 100-pt score → 65+ forward.
```
Stage 2 runs only on survivors — heavier per-store reading is affordable there.

## Product selection inside a store (product-level, not store-level) — v2 = TOP-3

Source order (the **open-ladder**): **best-selling → frontpage → featured collection** (sales/curated order =
the merchant's own ranking), then `/products.json`, then **homepage HTML**. Among the top items (skip service
SKUs: shipping protection / gift card / warranty / subscription):
1. Keep only PHYSICAL products (skip ingestible / skincare / apparel at the PRODUCT level).
2. **Return the TOP-3 physical candidates** (not one hero), each with full desc + REAL price (USD) + type +
   early signals. Order them by **storefront position** first, then **investment** (desc length / #images /
   #variants / badges). Revenue is NOT the selector (an early winner has none yet).
3. **Price band:** preferred $45–79, acceptable $39–100, premium $100–170 (score with margin penalty), hard
   ceiling $170 retail (>$170 retail = out). Flag each candidate `in_range` / `price-out` — never drop a store
   on price unless ALL its top products are out of band (store whose #1 is $250 but #2 is $70 stays — keep the $70).
4. **Never a silent DROP:** if the open-ladder yields nothing → `reachable:false, reason:<why>` ("needs manual look").

## Candidate Sheet — fields the enricher writes (per store) — v4

> Each store row carries a **`tops3` list of the TOP-3 product candidates**; the per-product fields below
> (`candidate`/`price`/`desc`/confidences/signals) are written **for EACH of the 3**, not just one hero.

| Field | What | Source | Serves |
|-------|------|--------|--------|
| `tops3` | **The 3 best physical candidates** (ordered: storefront position → investment), EACH with its own price/desc/flags | open-ladder: best-selling→frontpage→featured→products.json→homepage HTML | the picture — a golden product in slot #2/#3 is never lost |
| `price` + `in_range` | REAL price **normalized to USD** (NOT the Store Leads estimate; convert AUD/ZAR/EUR/INR) | variant price + currency code | Margin (price is the #1 unreliable field; ShopHunter lost stores to ₹/AUD mistaken for $) |
| `niche` / `kind` | type + class (physical / ingestible / skincare / apparel) | title + desc keyword scan | Market / mandatory filters / Veto |
| `desc` | **1–2 lines: what it IS → what pain it solves → wow / пустышка-claim** | body_html (stripped) | the bridge for the main agent to judge Problem/Wow/Emotion |
| `hero_confidence` | `high` (from a sales-ordered collection) / `low` (from `all` / homepage HTML) | which ladder rung produced it | tells main agent which candidates to live-confirm first |
| `desc_confidence` | `ok` / `empty` / `mismatched` | desc present & matches title? | empty/mismatched → main agent MUST WebFetch before scoring (anti "winner killed by bad desc") |
| `storefront_pos` | position in the merchant's own best-selling/featured order | collection order | the merchant saying "THIS is my main one" — works with zero revenue |
| `investment` | desc length · #images · #variants · badges (Bestseller/As-seen-on) | catalog | effort put in ≠ filler — an early-signal of the store's real hero |
| `conv_subcat` | how many OTHER stores **in the dumped subcategory** sell the same type (**geo-mirrors deduped** — 7 country-mirrors of one domain = 1) | cross-store title tokens over the ~27k dump | demand validation WITHOUT revenue |
| `cat_flag` | hero (pc≤300) / mid / catalog-giant (pc>2000) | Store Leads `pc` | high pc = product is one of many = weaker hero |
| `maturity` | store age + SKU + revenue band — `emerging` / `established` | `created` + `sl_pc` + `erf` | **`established` ≠ drop** (Marina S2): a proven store invisible in ShopHunter/FB is OUR edge, not a reject |
| `pust` flag | пустышка claim (detox/lymphatic/circulation/"grow back"…) | title+desc scan | Marina Veto |
| `image` | main product image URL | catalog | wow is visual — glance without opening |
| SL metrics | `sl_rev`(erf) · `sl_avg`(apf) · `sl_pc` · `created` · visits(mvis) | from the dump row | context (treat as ESTIMATE) |
| social | FB / IG / TikTok / Pinterest account links | `identifiers` | ad-research / Notion |
| `proxy_score` + tier (A/B/C/DROP) | RELIABLE signals only: in-range + conv_subcat + storefront_pos + investment + cat_flag (**NOT revenue** — early winner has none) | computed | **a SORT-AID — NOT quality, NOT final; main agent reads ALL, leads with WOW/taste** |

### How to write `desc` (the key field)
Two short factual lines, in order: (1) **what it is** (object + mechanism: "cordless infrared heated seat cushion");
(2) **what pain it solves** ("portable warmth without heating the room"); (3) **flag** a пустышка-claim or a clear wow.
No marketing fluff. ~200 chars. This is what the main agent reads to judge.

## What the enricher does NOT write (so the main agent doesn't over-trust noise)
- ❌ **Reviews / rating** (`combrs`/`tprs`) — fakeable; a store never advertises 2★. Weak signal, not a selector.
- ❌ **Social follower counts / 30-day growth** — NOT in the Store Leads API (dropped 2026-05-31).
- ❌ **Branded/proprietary auto-penalty** — do NOT auto-reject a brand; a brand store = demand evidence for the TYPE
  we white-label (op-rules RULE 9). Marina decides case-by-case.
- ❌ **FB-pixel / tech-stack as a decider** — context only, not a selection criterion.
- ❌ **Revenue as the candidate selector** — an early winner has no revenue yet; `erf` is context only (and an ESTIMATE).
- ⚠️ **`niche` label is Kitchen-tuned** in the current script — treat it as noise for non-Kitchen categories; the main
  agent classifies the product type itself at Stage-3. (Align/retire this label when the code is rewritten for v2.)

## Anti-hallucination rule (Marina S2 — the scraper GENERATES text; never score on generated text alone)
The enricher writes `desc`/flags by SCRAPING the live catalog — but a script (like a sub-agent) can emit a
plausible-but-wrong string (e.g. wrong currency read as $, a desc pulled from the wrong product, a stale cache).
**RULE:** the enricher's text is a LEAD, never a verdict. The main agent **NEVER scores a 65+/winner on the
enricher's text alone** — every genuine candidate gets a **live-site WebFetch confirm of hero + price + desc**
before scoring (mandatory when `desc_confidence ≠ ok` OR `hero_confidence = low` OR price near a band edge).
This is the structural guard against "we lost/мis-scored a winner because the scraper invented the detail."
(Same discipline that caught the sub-agents inventing line-numbers/flags this session — verify against the source.)

## Division of labour
- **Enricher (script):** SCRAPES facts (real catalog) + computes flags/signals + ranks (proxy sort-aid).
  NEVER judges wow / emotion / problem-strength. Its text = a lead, not a verdict.
- **Main agent (me):** read ALL sheets (no gut top-N) → live WebFetch confirm of hero+price+desc (mandatory for
  low-confidence/edge cases) → Marina Veto + 100-pt judgment → 65+ → checkpoint → (Marina OK) → Notion.

## Success test (Marina's bar)
The sheet is good enough when, reading it, the main agent can confidently say "these N I take forward / these are
definitely not ours" and be ready for deep analysis — without re-opening every store. Numbers float per batch.
