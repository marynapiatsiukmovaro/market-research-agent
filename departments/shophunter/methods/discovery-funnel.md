# ShopHunter — Discovery Funnel (PROVISIONAL DRAFT — SH-3)

> **Status: DRAFT — learning phase.** Built from the first store-first run (SH-3, 2026-05-25)
> + operational principles adopted from the mature Facebook Ads Library department.
> **Numbers below are ILLUSTRATIVE EXAMPLES, not fixed targets/quotas.**
> Do NOT carve any of this into permanent `op-rules.md` until validated across multiple
> sessions (Marina, SH-3). We are still developing the strategy.

## Core idea
ShopHunter surfaces STORES with traction; scoring needs PRODUCTS. The funnel progressively
narrows a large cheap pool down to a few deeply-scored candidates — **all heavy filtering on
the VPS, only the finalists enter chat.**

## Stages (numbers illustrative)

**Stage 0 — Dump (VPS, cheap).** Explore Shops → category checkbox → infinite-scroll harvest
→ JSON on VPS. (H&G default surface ≈ 830 stores, SH-3.) The dump persists — reuse it, do not re-scrape.

**Stage 1 — Working slice.** Process a bounded slice (e.g. first ~250), not the whole dump at
once, so each session has a measurable workload.

**Stage 2 — Open ALL of the slice (VPS) — NO subjective pre-pick.** Open every store; extract
product name + price + SH category + created date + key claims. **Never hand-pick "the ones
that look good" by name before seeing data** — that loses winners (FB RULE 8; it was the SH-3
mistake: I cut 103→12 by reading names).

**Stage 3 — Objective noise-cut (VPS).** Drop ONLY certain noise on objective criteria:
supplement/пустышка (name+category), price >$170 or clearly <floor, dead/closed store,
digital/service, pure catalog-tier. Survivor count is NOT fixed — if a slice is clean, many
survive, and that is fine.

**Stage 4 — Intermediate scoring/ranking (VPS) — the key middle stage.** Rank survivors on
cheap PROXY signals (revenue-estimate, hero-shape/low-SKU, FB-ads bridge, growth %, category
fit, price-in-range) → a mid-tier shortlist of genuinely promising candidates (illustratively
~30–50). **This stage exists so a low-noise slice still gets narrowed** — it prevents dumping
200 survivors into chat.

**Stage 5 — Finalist batch to chat.** Tighten with stricter proxy + a quick claims/white-label
read → top batch (illustratively ~7–20) enters chat. Only here do we spend chat context.

**Stage 6 — Deep scoring (chat).** Full `core/scoring-system.md` (100 pts + Marina Veto) on the
finalists → report 65+ → `shared/reported-products.md` + Notion.

## The numbers are illustrative (Marina, SH-3)
250 / 170 / 30–50 / 7–20 are EXAMPLES of progressive narrowing, not quotas. Discipline:
each stage applies stricter criteria than the last; never force a fixed count; **never skip a
narrowing stage just because the previous one cut little.**

## Principles adopted from Facebook Ads Library (what worked — keep)
- **VPS-side heavy lifting, chat gets only finalists** (FB RULE 7) — biggest token saver.
- **Verify ALL above an objective threshold, never top-N by gut** (FB RULE 8) — anti-candidate-loss.
- **Parallel verification** in batches of 3–4 when fetching product pages (FB RULE 9).
- **Revenue/metrics = ESTIMATE** — corroborate (ads, reviews, multiple sellers, longevity) before calling a winner.
- **Tier-1 vs Tier-2 / no sharp conclusions** (FB RULE 14): record data + directional observations
  freely; do NOT turn one run into a permanent rule, a category close, or a pivot. Permanent rules
  only at 100% confidence or 3+ confirmations (Marina, SH-3).
- **End-of-session memory + handoff** so the next session resumes without re-deriving.
- **Human-in-loop checkpoints** — ShopHunter has NOT earned autonomous mode (FB earned it at S30).

## NOT ported from FB (channel-specific — irrelevant here)
Scraper/cookies/scroll-depth caps, keyword-map, seen-advertisers, autonomous mode, FB pre-flight.
ShopHunter has its own mechanics — see `methods/interface-guide.md`.
