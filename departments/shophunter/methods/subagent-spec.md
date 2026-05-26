# ShopHunter Stage-2 Sub-Agent Spec — "Candidate Sheet"

> **Status: AGREED with Marina (SH-4, 2026-05-25).** This is the job description for the
> Stage-2 enrichment workers (the VPS scraper "sub-agents"). It defines EXACTLY what they
> write and how, so the main agent's keep/cut is accurate and repeatable.
> Implemented by `scripts/sh_enrich3.py` (Playwright + residential proxy, parallel).

## Where this fits in the funnel
```
Stage 0  Dump (Explore Shops, all H&G stores)                         [done once, reused]
Stage 1  Hero per store (ShopHunter "Top Products") + light tiering   [parallel, ~2 min/150]
         → CONSERVATIVE cut: remove only DEFINITE-NO (non-gadget / пустышка / >$170 / <$36)
Stage 2  ← THIS SPEC. Sub-agents read LIVE catalog of survivors, write a Candidate Sheet.
Stage 3  Main agent reads sheets → Marina Veto + 100-pt judgment scoring → 65+ go forward.
```
Stage 2 runs ONLY on survivors (smaller set) — that is why heavier per-store reading is affordable here.

## The Candidate Sheet — fields the sub-agent writes (per store)

| Field | What | Source (easy, from products.json) | Serves |
|-------|------|-----------------------------------|--------|
| `candidate` + `all_tops` | Best in-range physical product + ALL top-3 sellers with REAL prices | live catalog matched to ShopHunter Top Products | mandatory price filter; lets main agent see $70-vs-$250 |
| `price` + `in_range` | REAL price from the live site (NOT the ShopHunter estimate) | variant price | Margin |
| `niche` / type | Product category | product_type + title | Market / Problem |
| `desc` | **1–2 lines: what the product IS → what pain it solves → wow / пустышка-claim if any** | body_html (stripped) | the bridge for the main agent to judge Problem / Wow / Emotion / пустышка |
| `convergence` | How many OTHER stores sell this product type (or match to a known winner) | KNOWN-winner match + cross-store | real demand validation |
| `flags` | `ingestible` / `skincare` / `apparel` / `пустышка` / `price-out` | keyword scan of title+desc+price | mandatory filters + Marina Veto |
| `image` | Main product image URL | catalog image | wow is visual — glance without opening the store |
| `proxy_score` | RELIABLE signals only: price-in-range + convergence + Stage-1 revenue | computed | **Revenue-Tier** sort-aid (NOT the final score, NOT a quality rank — read ALL A+B+C) |
| `desc_confidence` (SH-8 — ⚠ PLANNED, not yet emitted by the enricher) | `ok` / `empty` / `mismatched` — does the live `desc` actually describe the candidate product? | desc length + title-vs-desc token overlap | **flags candidates that need a WebFetch verification BEFORE tiering** (Description-confidence gate — see discovery-funnel.md Structural safeguards). **Until the enricher emits it, the MAIN AGENT applies the gate by judgment** (empty/mismatched desc on a genuine in-range physical → WebFetch before scoring). |

### How to write `desc` (the key field — clear rule)
One or two short lines, factual, in this order:
1. **What it is** (object + mechanism): "cordless UV+heat shoe dryer".
2. **What pain it solves**: "dries & de-odorises wet sports shoes overnight".
3. **Flag if present**: a пустышка-claim (unverifiable result — circulation/detox/lymphatic/"grow back"), or a clear wow (visible transformation).
Keep marketing fluff out. ~200 chars max. This is what the main agent reads to judge.

## What the sub-agent does NOT write (decided with Marina, SH-4)
- ❌ **Reviews / rating** — fakeable; a store never shows 2★ and advertises it. Empty signal.
- ❌ **Multi-niche / catalog breadth** — not a selection criterion.
- ❌ **FB-ads count from ShopHunter** — ShopHunter's FB-Archive linkage is unreliable / often the wrong account. Do not decide on it.
- ❌ **Branded/proprietary flag** — do NOT auto-penalise branded; sometimes such a store is worth a look (Marina decides case-by-case).

## Selection rule inside a store (product-level, not store-level)
Among the store's top-3 sellers (skip service SKUs: shipping protection / gift card / warranty):
1. Keep only PHYSICAL products (skip ingestible/skincare/apparel at the PRODUCT level).
2. **Candidate = the highest-revenue physical product whose REAL price is in $39–170.**
3. If none is in range → take the highest-revenue physical (flag `price-out`) — do NOT drop the store on price unless ALL its top products are out of range.
   (So a store whose #1 is $250 but #2 is $70 stays, candidate = the $70.)

## Division of labour
- **Sub-agent (script):** extracts FACTS + flags + ranks (proxy). Never judges wow / emotion / problem-strength.
- **Main agent (me):** Marina Veto + judgment scoring (Problem / Wow / Emotion / 3+ angles / white-label) using `desc` → full 100-pt score → 65+ goes forward to Notion.

## Success test (Marina's bar)
The sheet is good enough when, reading it, the main agent can confidently say
"these N stores I take forward / these are definitely not ours" and be ready for deep analysis —
without re-opening every store. Numbers are never fixed; they float per batch.
