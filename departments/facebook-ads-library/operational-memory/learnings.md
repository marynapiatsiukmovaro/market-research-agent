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

~~### [2026-05-16] Session 10 — Keyword Audit Database: ~50 keywords weekly monitor~~
> ARCHIVED S25 — expired. Idea preserved in memory project_keyword_audit_system.md + keyword-map.md.

---

~~### [2026-05-16] Session 10/11 — Situation keywords = hidden intersection discovery mode~~
> ARCHIVED S25 — expired. Core rule (low yield normal; judge by unpredictable intersections) preserved in keyword-map.md Meta Rules + S22/23 learnings.

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

~~### [2026-05-18] Session 15 — Performance signal keywords: yield baseline established~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 15 — --since=2026-01-01 date filter: no signal improvement~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 15 — Category tracking: 30-keyword experiment~~
> ARCHIVED S25 — expired. Broad Horizontal hypothesis CLOSED S20; superseded by Situation Keywords hypothesis.

---

~~### [2026-05-18] Session 17 — "Gadget" descriptor keywords: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md ("gadget"/"genius gadget" ❌ DEAD).

---

~~### [2026-05-18] Session 16 — Offer/promo keywords: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md Meta Rules (Offer/promo DEAD class).

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

~~### [2026-05-18] Session 18 — Broad horizontal discovery: pattern after 15+ keywords~~
> ARCHIVED S25 — expired. Hypothesis CLOSED S20 (see S20 archived entry below).

---

~~### [2026-05-18] Session 19 — Universal urgency/credibility phrases: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md.

---

~~### [2026-05-18] Session 19 — FB Ads Library: 0-result anomaly for certain phrases~~
> ARCHIVED S21 — expired. Superseded by S21 finding: "back pain" + "standing all day" consistently blocked (not glitch, but FB policy on certain term types). Updated rule in S21 learning below.

---

~~### [2026-05-18] Session 19 — Broad horizontal discovery: hypothesis performance update~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 20 — Broad Horizontal Discovery hypothesis: CLOSED~~
> ARCHIVED S25 — expired. Final tally: 29 keywords → 2 products (both S15). Pivoted to Situation Keywords (S21+).

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

### [2026-05-19] Session 22/23 — Situation Keywords: что работает, что не работает
**Type:** Pattern | **Severity:** HIGH | **Confidence:** MEDIUM (S21-S23 data; S23 correction by Marina)
**Observation:** S21-S22 данные: "cold office" ✅, "tired feet" ✅, "sitting all day" ✅ — все физические ощущения. S22 мёртвые: "desk job", "night shift", "meal prep", "ergonomic", "on your feet all day". S23 мёртвые: burnout, work stress, always tired.
НО: "long flight" (S11) — контекстный keyword, НЕ физическое ощущение — дал Kids Travel Sleep Nest score 72 ✅.
ВЫВОД (исправлен Marina S23): ситуационные keywords работают когда создают СПЕЦИФИЧНЫЙ МОМЕНТ боли/дискомфорта — неважно физический или контекстуальный. Не работают: слишком широкие эмоциональные/психологические состояния ("burnout", "work stress", "always tired") → притягивают supplements/coaching/apps. Работают: конкретный момент ("long flight", "cold office", "tired feet") → продукт решает именно этот момент.
Ошибочное правило из черновика S22 ("физическое ощущение = сигнал; контекст = мёртво") ОТОЗВАНО как чрезмерная генерализация.
**Applies to:** S23+ Situation Keywords sessions — keyword selection
**Expires after:** Session 29

---

### [2026-05-23] Session 24 — Mental/biochemical states DEAD (3rd confirmation) + discriminating principle
**Type:** Pattern | **Severity:** HIGH | **Confidence:** HIGH (S22-S24, 6 keywords)
**Observation:** vagus nerve (193 adv) + overwhelmed (359 adv) → 0 reportable. vagus nerve device cluster IS real & active (Pulsetto, Sensate, Truvaga, Hoolest, Neuvana, Nuropod $900) but ALL branded-proprietary + premium ($150-900) → closed to white-label. overwhelmed = courses/supplements/pharma/charity/SaaS. **Discriminating principle (covers all 24 sessions): a keyword yields white-label physical DTC only if the problem has a PHYSICAL OBJECT as its obvious, immediate solution.** Physical/localized pain or concrete moment (tired feet, sitting all day, long flight) = yes. Wide mental/emotional/biochemical state (burnout, overwhelmed, cortisol, vagus) = market answers with services/pills/apps/branded-premium-devices = no. CLOSE Cluster 2 entirely. Recurring side-signal: weighted comfort animals (pulseofpotential) appeared in BOTH keywords from different advertisers — directional only, Marina vetoed the category.
**Applies to:** keyword selection — Cluster 2 (Stress/Mental) closed
**Expires after:** Session 30

---

### [2026-05-23] Session 24 — S25 direction note (non-binding)
**Type:** Tactical | **Severity:** MEDIUM | **Confidence:** MEDIUM (one discussion, Marina S24)
**Observation:** After Cluster 2 closed, Marina + agent discussed where to look next. Leaning: deepen the **Kids & Parenting vertical** using the Vertical product-category keyword model (historically highest yield: "baby carrier", "screen time" → 1-3 products/keyword) + possible advertiser-catalog mining. This is a DIRECTION for where to search, NOT a filter — scoring/filters stay unchanged, all categories still eligible. Final hypothesis + keyword list to be confirmed with Marina at S25 start.
**Applies to:** S25 keyword planning
**Expires after:** Session 27

---

### [2026-05-23] Session 25 — Office × Positive Emotion (Cluster 5): yield + discriminating principle (positive side)
**Type:** Pattern | **Severity:** HIGH | **Confidence:** MEDIUM (5 keywords, S25 — first positive-emotion session)
**Observation:** First session of the S24 emotion-pivot (office vertical, love/delight/aspiration instead of pain). 5 keywords: desk plant ✅ (Ivy Gen 2 smart companion planter 72), candle warmer ✅ (Candle Warmer Lamp 70, ⚠️ везде-flag held for Marina), mug warmer ❌, cozy office ❌, aesthetic desk ❌. Yield 2/5 = consistent with situation-keyword norm. CONFIRMS S24 discriminating principle on the POSITIVE side: a positive-moment keyword yields white-label DTC only when the moment has a concrete PHYSICAL-OBJECT solution (companion gadget; flame-free cozy lamp). Fails when keyword is broad-lifestyle (cozy office = home/property search) or maps to the wrong object (mug warmer → the CUP not the device; aesthetic desk → branded-premium gear/furniture). Note: S25 direction was Office×Positive (per session prompt + _active.md S24 PIVOT), NOT the Kids vertical floated in the S24 direction-note.
**Applies to:** S26+ positive-emotion office keyword selection
**Expires after:** Session 31

---

### [2026-05-23] Session 25 — Two new NOISE classes on consumer/lifestyle keywords
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH (heavy across 5 keywords)
**Observation:** (1) Spam engagement-bait "story" accounts — garbage names (BrightMeadow 29, WildGarden7030, CalmMist 29), identical fiction copy ("I know you've been cheating on me", necrotic-fingers, kidney/BP/GLP-1 stories), 19-29 ads each, keyword-stuffed → they dominate fast_filter top-20 by ad-count signal on mug warmer + desk plant. (2) Real-estate/property listings flood broad lifestyle phrases (cozy office → realtors, apartments, sqft/beds/baths, sheds-as-"home office"). Both = pure noise; recognize by garbage-name + fiction-copy / property-listing pattern and skip fast. Possible fast_filter upgrade (advertiser-name + fiction-copy detection) — PROPOSAL, not auto-implemented (see Session Learning Report).
**Applies to:** all consumer/lifestyle keyword sessions — faster noise rejection
**Expires after:** Session 31

---

### [2026-05-23] Session 25 — Recurring SIGNAL: ambient/aesthetic desk lamp
**Type:** Signal | **Severity:** MEDIUM | **Confidence:** MEDIUM (3 keywords)
**Observation:** "Ambient/aesthetic desk lamp" recurred across candle warmer (candle-warmer lamps: MEVA/Glenbrookhome/Docos/Homira — 5+ brands = category convergence), and aesthetic desk (Solara bird lamp). Cozy/aesthetic desk LIGHTING is a recurring positive-emotion territory; candle warmer lamp = strongest convergence (reported 70). Directional only — Marina decides whether to deep-dive the lamp/lighting category next.
**Applies to:** S26+ — potential lamp/lighting deep-dive
**Expires after:** Session 30

---

## Expired / Promoted

> Entries with `Expires after: Session N` where N ≤ current session are archived here by the agent at STEP 8.
> Do NOT delete archived entries — keep as historical record.

> **АРХИВАЦИЯ Session 25 (2026-05-23):** 8 записей архивированы (истекли после Session 25):
> - Session 10 — Keyword Audit Database (50-keyword monitor)
> - Session 10/11 — Situation keywords = hidden intersection discovery mode
> - Session 15 — Category tracking: 30-keyword experiment
> - Session 17 — "Gadget" descriptor keywords: dead class
> - Session 16 — Offer/promo keywords: dead class
> - Session 18 — Broad horizontal discovery pattern (15+ keywords)
> - Session 19 — Universal urgency/credibility phrases: dead class
> - Session 20 — Broad Horizontal Discovery hypothesis CLOSED
> Все keyword-вердикты сохранены в keyword-map.md. Tombstones оставлены в Active секции.

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
