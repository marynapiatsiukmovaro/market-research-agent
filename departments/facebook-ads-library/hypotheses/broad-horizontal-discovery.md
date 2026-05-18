# Hypothesis: Broad Horizontal Discovery

**Status:** ARCHIVED — CLOSED Session 20 (2026-05-18)
**Started:** Session 15 (2026-05-17)
**Closed:** Session 20 (2026-05-18)
**Replaces:** Kids Vertical hypothesis (archived — see kids-vertical.md)

---

## Core Idea

Stop searching inside one niche. Instead: use keywords that attract aggressive DTC/dropship advertisers regardless of category.

These are **performance advertising signal keywords** — phrases that Pampers or bloggers would never use, but that DTC operators use constantly:
- Offer hooks: "50% off today", "buy 1 get 1", "free shipping"
- Emotional triggers: "struggling with", "finally a solution", "game changer"
- Outcome phrases: "works in seconds", "see results in", "without leaving home"

This pre-filters by **advertiser type**, not topic. Result: you see active DTC operators across ALL categories simultaneously.

---

## Strategy

**Discovery source:** Facebook Ads Library via VPS scraper (primary, mandatory)
**Verification sources:** Amazon, TikTok organic, AliExpress (secondary only)

**Phase 1 — Broad signal scan (Sessions 15–30 estimate):**
- Run 30+ performance signal keywords
- Observe what DTC categories emerge
- Do not force any single niche

**Phase 2 — Category convergence:**
- After 30 keywords: identify strongest 2–3 emerging categories
- Switch to product-specific keywords within those categories
- Depth over breadth from that point

---

## Keyword Approach

Examples of performance signal keywords to run:
- "struggling with" / "finally works" / "game changer"
- "50% off" / "limited time" / "free gift"
- "works in seconds" / "no more" / "without leaving"
- "as seen on" / "sold out" / "back in stock"
- "for women over 40" / "for busy moms" / "for people who"

Check `operational-memory/keyword-map.md` for tested keywords and their verdicts.

---

## What Counts As a Valid Find

Same scoring rules as always (core/scoring-system.md).
No niche restriction. ANY category is valid if the product scores 65+.
No creative angle requirement changes.

---

## Session Structure

Each session: 1–3 keyword scans → fast filter → WebFetch verification → scoring → Notion save.
Follow `workflow.md` exactly. Announce each keyword round before starting.

---

## Kids Vertical Data

Kids keyword verdicts are preserved in `operational-memory/keyword-map.md`.
The hypothesis itself is archived in `hypotheses/kids-vertical.md`.
Do not revisit Kids as active focus unless Marina instructs.

---

## Success Criteria

Hypothesis is successful when:
- 3+ categories with multiple active DTC advertisers identified
- 5+ products reported at 65+ score across diverse categories
- Clear pattern emerges of which performance keywords yield highest signal density

---

## Conclusion — FAILED (Session 20)

**Result:** 29 keywords tested, ~7900 advertisers scanned, **2 reportable products** (both from S15).

**Why it failed:**
Performance signal phrases ("game changer", "struggling with", "before and after") are used by ALL advertiser types — pharma companies, restaurant chains, automotive brands, service businesses. They do NOT pre-filter for DTC physical product operators. The core hypothesis assumption was wrong.

**Sub-classes tested and results:**
- Outcome phrases ("game changer") → ✅ 1 product found (Dermave)
- Pain hooks ("say goodbye to", "if you suffer from", "the worst part of") → ⚠️ 1 product, then 0
- Universal testimonials ("the only thing that", "before and after") → ❌ 0 products
- Offer/promo phrases → ❌ 0 products (DEAD class)
- Social proof phrases → ❌ 0 products (DEAD class)
- Universal urgency ("sold out", "struggling with") → ❌ FB blocked / 0 products

**Key learning:** Product-specific keywords (Kids vertical S8-S14: 1-3 products/keyword) vastly outperform broad signal keywords. Next hypothesis must use niche-specific or product-specific terms.

**Next hypothesis:** see departments/facebook-ads-library/hypotheses/_active.md
