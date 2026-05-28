# AGENT OPERATING RULES v1

**STATUS:** Reference doc — not in CLAUDE.md Layer A mandatory load. The "alongside FB learnings" line below is a historical breadcrumb (FB Ads Library = first operational department), not a session-load directive. Actual session-load contract: CLAUDE.md Layer A + Layer B.

**Derived from Sessions 1–6 post-mortem. Read at session start alongside departments/facebook-ads-library/operational-memory/learnings.md.**

---

## 1. Verification Signal Hierarchy

Three tiers. Never promote signals across tiers.

**Tier 1 — Verified ✓** (both required for Verified status)
- Direct FB/TikTok Ads Library access with confirmed active campaign + start date
- Marina personally verified active ads

**Tier 2 — Needs Verification ⚠️** (strong indirect — worth pursuing)
- "try-" or "get-" domain prefix + overseas timezone (CET/AEST) + no history on About = paid traffic DTC pattern
- Amazon ASIN B0F/B0G prefix + first available date < 6 months ago = fresh launch signal
- 2–3 active brands in same sub-category = category proof (not brand proof)
- Press release + dedicated product landing page + active campaign language

**Tier 3 — Not a validation signal** (do not cite)
- WebSearch mention of "seen on Facebook"
- Social media links in footer
- "AS SEEN ON" press logos
- Amazon review count (lagging indicator, reflects past)
- Aggregate brand claims ("8,000+ reviews") — always compare to actual product page count
- Market size / TAM / CAGR data
- WhatsApp number as "social presence"

**Anti-inflation rule:** 3 × Tier 3 ≠ Tier 2. Never sum weak signals into a strong conclusion.

---

## 2. Strongest Predictive Signals (from 14 Marina-reviewed products)

Marina approved 4/14 products. All four had:
- Wow-Effect score 14+ (visually obvious within 2 seconds)
- Problem-Solving score 16+ (specific, frequent, painful)
- Emotional Trigger 8+ (fear, shame, or strong desire)
- Confirmed or directly verifiable competitor ad activity

Marina rejected despite high scores when:
- Result was unverifiable (Red Light Hair Cap: 80/100 → "пустышка")
- Category was "везде" (LED Wand: 78/100 → rejected)
- Market timing was late (Lymphatic Massager: 75/100 → "рынок уже создан")
- Product required explanation before desire (TENS Patch: 71/100 → rejected)

**Conclusion:** Score 65–84 does NOT protect from rejection if a Marina veto condition is present.

---

## 3. Anti-Hallucination Rules

1. **No signal stacking.** Tier 3 signals alone cannot satisfy the "market validation" mandatory filter.
2. **Verify numbers.** If a brand claims "8,000+ reviews" and the product page shows 49 — flag the discrepancy. Do not cite the headline number.
3. **Geography first.** .sg/.uk/.au domain, non-USD pricing, or non-US support timezone = not a US DTC candidate without explicit confirmation.
4. **Founding year.** "2026 Upgrade" label ≠ brand launched in 2026. Check whois, About page, or first ASIN date.
5. **No invented URLs.** If a link cannot be found after genuine search → write "Not found." A false URL is worse than no URL.
6. **Market data ≠ entry opportunity.** A growing TAM means more incumbents, not easier entry.

---

## 4. Pivot Triggers

Auto-announce pivot to Marina when any of these occur:

- Round 2 complete with 0 candidates scoring 65+
- All brands found are pre-2025 (freshness failure across category)
- All brands found are Amazon-native only (no DTC FB play possible)
- Structural barrier confirmed: subscription model, price floor/ceiling, legacy saturation
- Category produces only Tier 3 signals after 2 full rounds

**Pivot format:**
> "PIVOT: [current direction] → [proposed direction]. Reason: [1 sentence with specific data]. Closed: [dead branches]. Proposed Round [N] keywords: [list]."

**Limits:**
- Max 2 pivots per session without Marina explicit OK for a third
- Never pivot mid-round — complete the round first

---

## 5. Context Management Rules

- **Session load = CLAUDE.md "Load On Every Session Start" (two-layer list) — canonical.** Follow it; do NOT skip core/ files or improvise a "changed files only" load.
- Never carry more than 3 "maybe" candidates across rounds without a written checkpoint
- If context usage >60% at start of Round 3 → alert Marina before proceeding

---

## 6. Freshness Logic

Current date defines "fresh." Recalculate at session start.

- **Ideal:** brand launched in current year (recalculate at session start)
- **Acceptable:** launched in previous year
- **Old / skip:** 2+ years ago — unless confirmed aggressive scaling in current year
- **Check via:** whois domain age, About page, first Amazon ASIN date, first press release

---

## File Version
v1 — created 2026-05-14, Session 6 post-mortem
v2 — updated 2026-05-15, Session 7: added VPS rule (Marina approved)
v3 — updated 2026-05-17, Session 15: removed sections 8 (Keyword Quality) and 9 (VPS Connection) — these are Facebook Ads Library department-specific, not universal system rules. Keyword logic → departments/facebook-ads-library/operational-memory/keyword-map.md. VPS/scraper rules → departments/facebook-ads-library/operational-memory/op-rules.md.
