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

### [2026-05-15] Session 7 — НОВЫЙ АЛГОРИТМ: Keyword-First Deep Scan
**Type:** Tactical | **Severity:** CRITICAL | **Confidence:** HIGH (Marina confirmed)
**Observation:** Old approach (product hypothesis → search) is limited by agent's imagination. New baseline:
1. Choose category → generate 20 keywords → run FB Ads Library → 200-500 ads/keyword → fast filter
2. Market shows what it's testing RIGHT NOW. Winners come from here — not from prediction.
Key requirement: VPS scraper. WebSearch = Tier 3 signal, cannot replace FB direct access.
Session structure: 5-15 sessions per niche. Depth over breadth.
**Applies to:** All future scout sessions — this is the baseline algorithm
**Expires after:** Session 20

---


### [2026-05-15] Session 8 Part 2 — Scraper fix: FB Login + JS Scroll confirmed permanent
**Type:** Tactical | **Severity:** HIGH | **Confidence:** HIGH (561 ads confirmed in live test)
**Observation:** Two fixes unlocked full scraper capacity (now permanent in code):
1. SCROLL: `page.mouse.wheel()` did not trigger FB lazy-load. Replaced with `page.evaluate('window.scrollBy(0, N)')` → 28 → 561 ads/keyword.
2. LIMIT: Removed `[:25]` hard cap in parse_ad_cards. Now parses all cards.
Incremental parsing (every 5 scroll steps → parse → dedup by Library ID) solves virtual DOM recycling.
BEFORE: 28 ads/keyword. AFTER: 500+ ads/keyword. This is permanent — do not revert.
**Applies to:** All VPS scraper sessions — verify these fixes still in place if scraper gives <50 ads
**Expires after:** Session 20 (or until scraper architecture changes)

---

---



### [2026-05-16] Session 10 — Multi-brand dropship operators = research asset
**Type:** Tactical | **Severity:** HIGH | **Confidence:** HIGH (Marina confirmed, Session 10)
**Observation:** When brand footer shows "Operated by [Company LLC]" (e.g., DBO Networks) → research asset, not red flag. These operators already spent significant ad budget testing products. How to use:
1. Find their ACTIVE catalog (not just current brand)
2. 404 on product = they killed it (failed the test) → skip
3. Product active 6+ months = demand validated → candidate for white-label evaluation
4. Don't analyze their marketing tactics — focus on WHAT they sell and HOW LONG
**Applies to:** All sessions — response to multi-brand dropship operators
**Expires after:** Session 20

---


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

### [2026-05-16] Session 13 — Wonder Quest: STEM/Exploration category signal
**Type:** Signal | **Severity:** MEDIUM | **Confidence:** MEDIUM (1 advertiser, Jan 2026)
**Observation:** Wonder Quest 4K Discovery Microscope (thewonderquest.net) — operated by DBO Networks LLC. $49.99 DTC, single active FB advertiser Jan 2026, COGS ~$12-20 Alibaba. Hook: "kids team up instead of fight" (sibling cooperation). White-label viable: generic kids digital microscope widely available. Score 70. Weak single signal vs Camp Snap (50+ campaigns), but confirms STEM/exploration category is alive on FB.
**Applies to:** Kids/STEM exploration category — next sessions
**Expires after:** Session 20

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

### [2026-05-18] Session 15 — Magic Playwall: Magnetic Wall Activity category signal
**Type:** Signal | **Severity:** MEDIUM | **Confidence:** MEDIUM (1 advertiser, score 62)
**Observation:** Cherrypick (shopcherrypick.com) → Magic Playwall — magnetic wall-mounted activity board for kids. Jan 2026, 1 active ad, UGC creator (UGCbyTosin). Score 62 — did not reach threshold. Reason: only 1 FB advertiser, price/COGS unverified, no Alibaba validation. Category signal: "magnetic wall activity board" = growing Pinterest/Etsy trend. If second DTC advertiser found → category opens. Next step: run keyword "magnetic activity board" to check for additional brands.
Notion: https://www.notion.so/36253ba8196e81bcab5bd8e20a7b81ec
**Applies to:** Kids vertical — wall activity category
**Expires after:** Session 20

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

### [2026-05-18] Session 16 — "%" symbol in FB Ads Library search: URL encoding failure
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH (direct test: 0 results for "50% off")
**Observation:** Keyword "50% off" returned 0 ads. Root cause: "%" in URL query string breaks percent-encoding (FB sees malformed URL). Fix: always use word alternatives — "half off" instead of "50% off", "percent" instead of "%", etc. This applies to all future keyword planning. Tested "half off" as proxy → 357 advertisers (working). Rule: if a planned keyword contains "%" → replace with word form before running.
**Applies to:** All future keyword planning and scraper runs
**Expires after:** Session 25

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
