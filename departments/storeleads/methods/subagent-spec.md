# Store Leads Stage-2 Sub-Agent Spec — "Candidate Sheet"

> **Adapted from ShopHunter's subagent-spec (SH-4) to Store Leads fields.** Defines EXACTLY what the
> Stage-2 enricher writes, so the main agent's keep/cut is accurate and repeatable (no improvising per run).
> Implemented by `scripts/sl_enrich2.py` (Playwright + iProyal proxy, parallel workers).

## Where this fits in the funnel
```
Stage 0  Dump via bq (Shopify+Active+Category+Created≥2020, windowed)        [sl_dump_full.py — reuse]
Stage 1  Client-filter + table (price/revenue/weight band) + sort by Est Visits
         → CONSERVATIVE cut: drop only DEFINITE-NO (see discovery-funnel.md "Stage-1 conservative cut")
Stage 2  ← THIS SPEC. Enricher reads the LIVE catalog of survivors, writes a Candidate Sheet.
Stage 3  Main agent reads ALL sheets → live hero+price confirm → Marina Veto + 100-pt score → 65+ forward.
```
Stage 2 runs only on survivors — heavier per-store reading is affordable there.

## Hero selection inside a store (product-level, not store-level)
The store's hero is taken from the **best-selling / frontpage / featured collection** (sales order = real hero),
fallback `/products.json`. Among the top-8 (skip service SKUs: shipping protection / gift card / warranty / subscription):
1. Keep only PHYSICAL products (skip ingestible / skincare / apparel at the PRODUCT level).
2. **Candidate = the first/highest-position physical product whose REAL price is in our band $39–100** (preferred
   $45–79). Hard ceiling $350.
3. If none in band → take the first physical, flag `price-out`. **Do NOT drop the store on price unless ALL its top
   products are out of band** (a store whose #1 is $250 but #2 is $70 stays — candidate = the $70).
> ⚠️ The current `sl_enrich2.py` uses a legacy $39–170 in-range test (kitchen-impulse). Align it to **$39–100** to
> match our locked band — until then the main agent applies the $39–100 judgment at Stage-3.

## Candidate Sheet — fields the enricher writes (per store)
| Field | What | Source | Serves |
|-------|------|--------|--------|
| `candidate` + `tops` | Hero physical product + top-8 sellers with REAL prices | live best-selling collection / products.json | price filter; lets main agent see $70-vs-$250 |
| `price` + `in_range` | REAL price from the live site (NOT the Store Leads estimate) | variant price | Margin (price is the #1 unreliable service field) |
| `niche` / `kind` | type + class (physical / ingestible / skincare / apparel) | title + desc keyword scan | Market / mandatory filters / Veto |
| `desc` | **1–2 lines: what it IS → what pain it solves → wow / пустышка-claim** | body_html (stripped) | the bridge for the main agent to judge Problem/Wow/Emotion |
| `cat_flag` | hero (pc≤300) / mid / catalog-giant (pc>2000) | Store Leads `pc` | high pc = product is one of many = weaker hero |
| `conv_batch` | how many OTHER stores in the batch sell the same type | cross-store title tokens | demand validation |
| `pust` flag | пустышка claim (detox/lymphatic/circulation/"grow back"…) | title+desc scan | Marina Veto |
| `image` | main product image URL | catalog | wow is visual — glance without opening |
| SL metrics | `sl_rev`(erf) · `sl_avg`(apf) · `sl_pc` · `created` · visits(mvis) | from the dump row | context (treat as ESTIMATE) |
| social | FB / IG / TikTok / Pinterest account links | `identifiers` | ad-research / Notion |
| `proxy_score` + tier (A/B/C/DROP) | RELIABLE signals only: in-range + conv + revenue + cat_flag | computed | **revenue/price SORT-AID — NOT quality, NOT final** |

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
- ⚠️ **`niche` label is Kitchen-tuned** in the current script — treat it as noise for non-Kitchen categories; the main
  agent classifies the product type itself at Stage-3.

## Division of labour
- **Enricher (script):** extracts FACTS + flags + ranks (proxy). NEVER judges wow / emotion / problem-strength.
- **Main agent (me):** live hero+price confirm (WebFetch) → Marina Veto + 100-pt judgment using `desc` → 65+ → Notion.

## Success test (Marina's bar)
The sheet is good enough when, reading it, the main agent can confidently say "these N I take forward / these are
definitely not ours" and be ready for deep analysis — without re-opening every store. Numbers float per batch.
