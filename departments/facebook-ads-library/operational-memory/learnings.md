# SESSION LEARNINGS

**Active temporary guidance — read at session start, after op-rules.md.**
Contains: short-lived tactical discoveries, category signals, behavioral corrections.
Does NOT contain: permanent operational rules (→ op-rules.md) or keyword verdicts (→ keyword-map.md).

Agent may **APPEND** new entries AND **archive expired entries** at STEP 8.
To archive: move entry to Expired section below. Do NOT delete — move.
Agent must NEVER edit non-expired entries or modify core/ files.

Items expire after the listed session. Marina promotes confirmed patterns via review/promotion-queue.md.

---

## Current Focus

**Sessions 15+: Broad Horizontal Discovery — Performance Signal Keywords**

- **Primary:** Facebook Ads Library via VPS scraper — all broad discovery here
- **Secondary:** Amazon, TikTok, AliExpress — verification only
- **Current strategy:** Using "performance advertising signal keywords" — words that attract aggressive DTC/dropship advertisers regardless of niche (offer hooks, emotional triggers, outcome phrases). Examples: "struggling with", "50% off today", "game changer", "works in seconds". These reveal active DTC operators across ALL categories, not tied to one vertical.
- **Why this works:** Pampers and bloggers don't write "buy 1 get 1 free". DTC operators and dropshippers do. These keywords pre-filter by advertiser TYPE, not topic.
- **After 30 keywords:** analyse the category landscape that emerges → identify the strongest 2-3 categories → go deep with product-specific keywords in those categories.
- **Kids vertical:** data preserved in keyword-map.md. Not the active focus.

---

## Active Learnings

### [2026-05-16] Session 10 — Keyword Audit Database: ~50 keywords weekly monitor
**Type:** Tactical | **Severity:** HIGH | **Confidence:** HIGH (Marina confirmed, Session 10)
**Observation:** Marina proposed building ~50-keyword weekly monitor: run each keyword once per week → track new advertisers appearing/disappearing → Market Pulse Monitor. Current tested: 22 keywords (see keyword-map.md). Build to 50, then weekly pulse scan replaces full discovery sessions for established keywords. Significant long-term research efficiency gain.
**Applies to:** Long-term session planning
**Expires after:** Session 25

---

### [2026-05-16] Session 10/11 — Situation keywords = hidden intersection discovery mode
**Type:** Tactical | **Severity:** HIGH | **Confidence:** HIGH (Marina confirmed; Travel Nest proof of concept)
**Observation:** Situation keywords work differently than product keywords. "Long flight" found Kids Travel Sleep Nest (score 72) — a product that would NEVER appear in "baby product" or "infant toy" keywords. Reason: the moment of pain (child on plane) creates context where Kids × Travel × Sleep intersect. This is the VALUE of situation keywords.
Rules for situation keywords:
- Low yield (0.3-0.5%) is NORMAL — do not abandon mid-session because of noise
- Judge by: is there anything here that wouldn't appear in standard product keywords?
- 65-70% noise = expected, not a signal to pivot keyword
- Estimate 2-3 situation keywords per session to compensate for lower yield
**Applies to:** All sessions with situation/moment keywords
**Expires after:** Session 25

---

~~### [2026-05-16] Session 10/11 — Kids Travel Sleep Nest: open DTC niche~~
> ARCHIVED S18 — expired. Result in reported-products.md.

---

### [2026-05-16] Session 10/11 — Scraper "started" date: structural limitation
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH
**Observation:** Field `started` (campaign start date) — Tier-1 signal for Entry Window scoring. Scraper captures it only when FB explicitly shows it in the card. For many advertisers it returns "?". This is a structural pipeline limitation, not a scraper bug.
Workaround when start date is critical: WebFetch brand/About page → founding date; or WHOIS / domain registration date; or first Amazon/Trustpilot review date.
Important: do NOT make this a mandatory step for every advertiser — only when Entry Window score is decisive for the 65/70 threshold.
**Applies to:** All VPS scraper sessions — Entry Window scoring
**Expires after:** Until `started` field is fixed in scraper (or permanent if never fixed)

---

### [2026-05-18] Session 15 — Performance signal keywords: yield baseline established
**Type:** Tactical | **Severity:** MEDIUM | **Confidence:** HIGH (2 keywords, 738 advertisers total)
**Observation:** First 2 performance signal keywords tested ("say goodbye to", "game changer"). Baseline yield: ~1 reportable product per 350-420 advertisers. Expected noise: 60-70% services/apps/beauty/supplements. "game changer" showed better DTC physical product density than "say goodbye to". Neither keyword dominated any single category — signals spread across Pet, Beauty, Home.
**Applies to:** Sessions 15-25 broad horizontal discovery — calibrate expectations per keyword
**Expires after:** Session 22

---

### [2026-05-18] Session 15 — --since=2026-01-01 date filter: no signal improvement
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH (direct test: 375 vs 418 advertisers, same keyword)
**Observation:** Tested "say goodbye to" with and without --since=2026-01-01. Result: date filter produced MORE advertisers (418 > 375), not fewer — and 0 vs 1 reportable product. Conclusion: the filter changes which ads FB shows but does not clean up noise. Do NOT add --since=2026-01-01 as default to all runs. Use only when specifically investigating fresh-entry advertisers for Entry Window scoring.
**Applies to:** All VPS scraper sessions — filter selection
**Expires after:** Session 22

---

### [2026-05-18] Session 15 — Category tracking: 30-keyword experiment needs a running tally
**Type:** Tactical | **Severity:** HIGH | **Confidence:** HIGH (Marina confirmed strategy)
**Observation:** Marina's strategy: run 30 performance signal keywords across 10 sessions → identify which categories appear 3+ times → pivot to product-specific deep-dive in those categories. Current emerging signals after 2 keywords: Pet (Heusom), Beauty/Personal Care (Dermave). Need to track category distribution across all 30 keywords as they are tested. When any category reaches 3+ products across different keywords → flag for deep-dive in next session block.
**Applies to:** Sessions 15-25 — at each STEP 8, count category occurrences from reported-products.md
**Expires after:** Session 25

---

### [2026-05-18] Session 17 — "Gadget" descriptor keywords: confirmed dead class for DTC discovery
**Type:** Warning | **Severity:** HIGH | **Confidence:** HIGH (2 keywords: "genius gadget" 121 unique adv., "gadget" 296 unique adv., 0 reportable)
**Observation:** "Genius gadget" = mass-clone dropship networks + mosquito affiliate clusters (minimal ad spend). "Gadget" = ultra-broad, attracts established brands (FIXD, REVO, HexClad), cheap commodities below $39, and пустышки with dubious claims. "Product signal" keyword sub-class in the 30-keyword list (#10 "genius gadget", #11 "viral product", #12 "as seen on tiktok") likely to perform similarly — these phrases attract affiliate/social-proof content, not cold-traffic DTC operators. Deprioritize remaining "product signal" entries from priority queue.
**Applies to:** Sessions 15-25 — skip remaining "product signal" sub-class from 30-keyword list; focus on pain/outcome phrases
**Expires after:** Session 25

---

### [2026-05-18] Session 16 — Offer/promo keywords: confirmed dead class for DTC physical products
**Type:** Warning | **Severity:** HIGH | **Confidence:** HIGH (4 keywords, 867 advertisers, 0 reportable)
**Observation:** Tested 4 performance signal keywords with offer/promo language: "tiktok made me buy" (277), "50% off today" (69), "buy 1 get 1 free" (164), "half off" (357) → total 867 advertisers → 0 reportable products. Pattern: promo-phrase keywords attract retail brands with seasonal promotions, jewelry/apparel discounts, supplement brands, subscription services — NOT cold-traffic DTC physical product operators in $39-99. Correct performance signal class = outcome/pain phrases ("say goodbye to", "game changer"). Incorrect class = price/offer phrases. Do NOT test remaining offer keywords from the 30-keyword list (#14 "50% off today" and #15 "buy 1 get 1 free" already confirmed dead).
**Applies to:** Sessions 15-25 keyword strategy — skip remaining offer/promo type keywords
**Expires after:** Session 25

---

~~### [2026-05-18] Session 16 — "%" symbol in FB Ads Library search: URL encoding failure~~
> ARCHIVED S19 — superseded by S18 quote_plus fix. Word alternatives no longer needed. See S18 entry below.

---

### [2026-05-18] Session 18 — Scraper URL encoding: quote_plus fix (permanent)
**Type:** Warning | **Severity:** HIGH | **Confidence:** HIGH (confirmed: apostrophe → 0 ads, fixed → 364 ads)
**Observation:** Apostrophes (`'`) and `%` in keywords returned 0 ads due to broken URL encoding. Root cause: scraper used `keyword.replace(" ", "+")` — spaces only. Fix: replaced with `urllib.parse.quote_plus(keyword)` which handles ALL special chars (`'`→`%27`, `%`→`%25`, etc). Confirmed: "why didn't I know" with `'` → 0 ads; without `'` → 364 ads. Now safe to use any keyword text literally. Supersedes S16 "%" warning — word alternatives no longer needed.
**Applies to:** All future scraper runs — already fixed in code (permanent)
**Expires after:** Never → candidate for op-rules.md at next promotion review

---

### [2026-05-18] Session 18 — Broad horizontal discovery: pattern after 15+ keywords tested
**Type:** Pattern | **Severity:** HIGH | **Confidence:** HIGH (15 keywords, ~5000 advertisers total)
**Observation:** After 15+ performance signal keywords (S15-S18): only 2 reportable products found — both from S15 ("game changer" → Dermave 69, "say goodbye to" → Heusom 71). All subsequent keywords: 0 reportable. Pattern breakdown by sub-class: Pain hooks ("tired of", "say goodbye to") — ⚠️ LOW YIELD. Discovery hooks ("why didn't I know") — ⚠️ LOW YIELD. Outcome phrases ("game changer") — ✅ only winner so far. Gift/occasion hooks — ❌ DEAD class. Promo hooks — ❌ DEAD class. Product signal hooks — ❌ DEAD class. Broad emotional hooks — ❌ DEAD class. **Contrast:** Kids vertical product-specific keywords (S8-S14) consistently found 1-3 candidates per keyword. Hypothesis: broad hooks filter by advertiser TYPE weakly — too many digital/service advertisers contaminate. Product-specific or niche-specific keywords filter better.
**Applies to:** Sessions 18-25 — reconsider hypothesis after remaining ~15 keywords; build next hypothesis around product-specific niche keywords
**Expires after:** Session 25

---

### [2026-05-18] Session 19 — Universal urgency/credibility phrases: confirmed dead class
**Type:** Warning | **Severity:** HIGH | **Confidence:** HIGH (4 keywords, 1245 advertisers, 0 reportable)
**Observation:** Tested "as seen on shark tank" (584), "use code" (368), "limited time only" (293) → 0 reportable. All attract all advertiser types equally. "as seen on shark tank" structural failure: 90%+ real Shark Tank alumni = all proprietary/patented. "use code" and "limited time only" are universal ad phrases used by restaurants, retailers, services — no DTC physical product filter. New dead class: **universal ad copy phrases** that any advertiser writes regardless of product type.
**Applies to:** Sessions 20-25 — avoid phrases that restaurants/legal/finance firms also use; prefer pain/problem hooks only physical product advertisers write
**Expires after:** Session 25

---

~~### [2026-05-18] Session 19 — FB Ads Library: 0-result anomaly for certain phrases~~
> ARCHIVED S21 — expired. Superseded by S21 finding: "back pain" + "standing all day" consistently blocked (not glitch, but FB policy on certain term types). Updated rule in S21 learning below.

---

### [2026-05-18] Session 19 — Broad horizontal discovery: hypothesis performance update
**Type:** Pattern | **Severity:** HIGH | **Confidence:** HIGH (19 keywords, ~5600 advertisers, 2 total reportable since S15)
**Observation:** After 19 performance signal keywords (S15-S19): 2 reportable products total, both from S15. Last 12+ keywords: 0 products. Marina confirmed hypothesis is underperforming expectations. Key insight: phrases that service businesses/restaurants also use = not filtering by DTC physical product operator type. Next test (S20-S21): refined sub-class — phrases ONLY physical product DTC advertisers write: "free shipping over", "if you suffer from", "struggling with", "embarrassing". If this sub-class also fails → abandon hypothesis, pivot to product-specific keyword strategy.
**Applies to:** Sessions 20-21 — decision point after testing refined sub-class
**Expires after:** Session 22

---

### [2026-05-18] Session 20 — Broad Horizontal Discovery hypothesis: CLOSED
**Type:** Pattern
**Severity:** HIGH
**Confidence:** HIGH (S15-S20, 29 keywords, ~7900 total advertisers, 2 reportable)
**Observation:** Hypothesis closed after S20. Total: 29 performance signal keywords tested across Sessions 15-20. Result: 2 reportable products — both from S15 ("game changer" → Dermave 69, "say goodbye to" → Heusom 71). Last 14+ keywords: 0 products. Final S20 sub-class tested — pain/narrative hooks ("if you suffer from" 361 adv., "the worst part of" 262 adv., "the only thing that" 391 adv., "before and after" 344 adv.) → all ❌ DEAD. Multiple keywords blocked by FB (0 ads): "struggling with", "embarrassing", "in seconds", "free shipping over", "sold out". Core finding: broad performance signal phrases are used by ALL advertiser types — pharma, retail, restaurants, services, DTC. They do NOT filter for physical product DTC operators. Hypothesis assumption was wrong. New direction: product-specific or niche-specific keywords only.
**Applies to:** S21+ — close hypothesis, pivot to product-specific keyword strategy
**Expires after:** Session 25

---

### [2026-05-19] Session 21 — FB blocks short health-condition & activity terms in Active ads filter
**Type:** Warning | **Severity:** HIGH | **Confidence:** HIGH (4 attempts across 2 keywords: "back pain" ×2, "standing all day" ×2)
**Observation:** 2-word health/activity terms consistently return "No ads match" regardless of retry: "back pain" (2 attempts = 0), "standing all day" (2 attempts = 0). NOT a glitch — confirmed by identical behavior across multiple days. Likely cause: FB's Active ads filter treats these as sensitive health terms. Workaround: longer descriptors bypass the block. "lower back pain" (3 words) → 256 ads ✅. "tired feet" ✅. "sitting all day" ✅. "sore legs" ✅. Rule: if a 2-word health/condition term returns 0 → do NOT retry same form; immediately try 3-4 word variant with activity context.
**Applies to:** All sessions — keyword formulation for health/pain/activity keywords
**Expires after:** Session 28

---

### [2026-05-19] Session 21 — Situation Keywords Cluster 1 (Physical Discomfort at Work) — verdict
**Type:** Pattern | **Severity:** HIGH | **Confidence:** HIGH (5 keywords, S21)
**Observation:** 5 Cluster 1 keywords tested: "tired feet" ✅ (Score 74 + 70), "sitting all day" ✅ (Score 68), "sore legs" ⚠️ LOW YIELD (compression socks dominate), "back pain" ❌ BLOCKED, "standing all day" ❌ BLOCKED. Yield: 3 products from 3 productive keywords — strong hypothesis performance vs. S15-S20 Broad Horizontal (2 products across 29 keywords). Conclusion: Situation keywords (activity + pain context) outperform generic performance signal phrases. Cluster 2 (Meal/Energy) and Cluster 3 (Mental Fatigue) are next — expected similar yield if keywords are 3-4 words with specific activity context. Skip any 2-word condition terms.
**Applies to:** S22+ Situation Keywords sessions — continue hypothesis, use 3-4 word activity descriptors
**Expires after:** Session 28

---

## Expired / Promoted

> Entries with `Expires after: Session N` where N ≤ current session are archived here by the agent at STEP 8.
> Do NOT delete archived entries — keep as historical record.

> **АРХИВАЦИЯ Session 13 (2026-05-16):** 18 записей удалены из основного раздела. Марина подтвердила "ок".
> Archive reference: departments/facebook-ads-library/operational-memory/learnings-archive-queue.md

> **АРХИВАЦИЯ Session 14 (2026-05-17):** 2 записи перемещены (истекли после Session 14):
> - Session 7 — Home/Kitchen: Structurally Weak (expires S14)
> - Session 7 — Мёртвые ключевые слова Home/Kitchen (expires S14)
> Постоянные операционные правила перемещены в op-rules.md. Keyword-паттерны перемещены в keyword-map.md.

> **АРХИВАЦИЯ Session 17 (2026-05-18):** 3 записи архивированы (истекли после Session 17):
> - Session 9 — Broad keywords: pattern map, not winner map (закон "уже" → keyword-map.md)
> - Session 10 — Camp Snap: Screen-Free Kids Camera VALIDATED (результат в reported-products.md)
> - Session 10 — "Screen-free alternative" = strong parental trigger (Kids vertical, on hold)

> **АРХИВАЦИЯ Session 16 (2026-05-18):** 1 запись архивирована (истекла после Session 16):
> - Session 9 — Price >$100 — NOT automatic reject (правило перешло в op-rules.md RULE 12)

> **АРХИВАЦИЯ Session 15 (2026-05-17):** 4 записи архивированы (истекли после Session 15):
> - Session 8 — Keywords: Broad = Noise, Specific = Signal
> - Session 8 — Kids Vertical: Category Map (first pass)
> - Session 8 — Bambora: Category Validator for Baby Ring Sling
> - Session 8 — Post-filter needed for dual-meaning keywords
> Устарели с переходом на Broad Horizontal Discovery (Sessions 15+). Kids-specific сигналы сохранены в reported-products.md и keyword-map.md.

> **АРХИВАЦИЯ Session 20 (2026-05-18):** 5 записей архивированы (истекли после Session 20):
> - Session 7 — НОВЫЙ АЛГОРИТМ: Keyword-First Deep Scan
> - Session 8 Part 2 — Scraper fix: FB Login + JS Scroll confirmed permanent
> - Session 10 — Multi-brand dropship operators = research asset
> - Session 13 — Wonder Quest: STEM/Exploration category signal
> - Session 15 — Magic Playwall: Magnetic Wall Activity category signal
> Hypothesis "Broad Horizontal Discovery" закрыта. Итог: 29 keywords, ~7900 advertisers, 2 reportable (оба S15).

---

## How to Add a New Learning

**Before adding:** check all Expires after dates in Active Learnings. Archive any entry where N ≤ current session number (move to Expired section above).

Append new entries using this format:

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW / MEDIUM / HIGH / CRITICAL
**Confidence:** LOW (1 weak signal) / MEDIUM (2-3 cases) / HIGH (multiple or founder-confirmed)
**Observation:** what was found (2-5 lines max)
**Applies to:** [keyword category / product type / search method]
**Expires after:** Session [N+7] or "Never" (Never = add to op-rules.md instead, not here)
```

**Where does it go?**
- Expires: Never → op-rules.md (not learnings.md)
- Keyword verdict (this keyword is dead/good) → keyword-map.md (add table row)
- Temporary tactical discovery → learnings.md (here)

**Size rule:** keep Active Learnings under 20 entries total. Archive expired before adding new.

## Promotion Rules

A learning may be added to `review/promotion-queue.md` only if:
- confirmed across **3 sessions**, OR
- **explicitly approved by Marina**

Never self-promote into core/ files.
