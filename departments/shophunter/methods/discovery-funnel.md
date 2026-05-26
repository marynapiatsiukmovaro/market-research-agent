# ShopHunter — Discovery Funnel (PROVISIONAL DRAFT — SH-3)

> **Status: DRAFT — learning phase.** Built from the first store-first run (SH-3, 2026-05-25)
> + operational principles adopted from the mature Facebook Ads Library department.
> **Numbers below are ILLUSTRATIVE EXAMPLES, not fixed targets/quotas.**
> Do NOT carve any of this into permanent `op-rules.md` until validated across multiple
> sessions (Marina, SH-3). We are still developing the strategy.

## SH-4 UPDATE (2026-05-25) — funnel matured & refined (Marina-agreed)
The SH-3 draft below still holds in spirit, but SH-4 made it concrete and changed key mechanics:
- **Stage 1 (hero) is now PARALLEL** (`sh_hero_par.py`, 4 workers, shared `sh_state.json` login): ~20 min → ~2 min / 150 stores, 0 quality loss.
- **The big cut is CONSERVATIVE, not aggressive** (`sh4_hardcut2.py`): hard-drop ONLY definite-no = non-gadget / пустышка /
  real-price > $170 / < $36 / dead. **Service-SKU as #1** (shipping-protection/gift-card) = ShopHunter mislabel → dig top-3, don't drop.
- **Stage 2 is a SUB-AGENT ENRICHER** with its own spec → see **`methods/subagent-spec.md`**. It reads the LIVE catalog
  (products.json via **Playwright+proxy** — bare requests = Shopify 403) and writes a Candidate Sheet: best in-range
  physical from top-3 (REAL prices, so a $70 beats a $250 #1) + niche + **description** + convergence + filter-flags + image.
- **Reliable signals only:** real price (margin), convergence (multi-seller), Stage-1 revenue. **Dropped:** reviews/rating
  (fakeable), multi-niche (not a criterion), ShopHunter FB-ads count (unreliable), branded-flag (don't auto-penalise).
- **NUMBERS NEVER FIXED:** survivors and the deep-score set float with the data; deep-score ALL genuine gadgets above the
  objective bar (no gut top-N — FB RULE 8). The description + main-agent judgment is the real filter.

---

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

---

## Reporting protocol (added SH-5, 2026-05-26 — Marina-approved STANDING RULE)
Every batch report to Marina includes BY DEFAULT (she does NOT need to ask):
1. **Winners (65+)** — scored + saved to Notion.
2. **Borderline (~58–64)** — usually only a few — flagged explicitly for founder review (founder-keep band).
3. **Patterns noticed** — recurring categories, convergence clusters, noise classes.
4. **Browse-links set** — a CURATED list of sub-65 *genuine white-label PRODUCT* store links. A winner is a
   PROBLEM-SOLVING product — gadget / tool / functional product (e.g. a faucet water filter), electronics NOT required;
   physical, in-range, NOT supplement / пустышка / branded / commodity-fashion-or-decor-with-no-angle. **In the BABY niche
   do NOT auto-exclude "apparel"** — sleep sacks / swaddles / carriers / sleep-aids are winners. So Marina can scan for
   patterns herself. Keep it CLEAN — no junk. End with one line: *"дать ещё больше ссылок (вкл. branded/пустышка) или меньше?"*

**SH-6 additions (Marina-confirmed, 2026-05-26 — apply every batch):**
- **CHECKPOINT FIRST → Notion only after Marina's explicit OK.** Work autonomously through dump→funnel→deep-score WITHOUT
  asking; but once products are analyzed and ready, deliver the intermediate checkpoint and WAIT for her OK before ANY
  Notion write. (She stopped an auto-Notion-write at SH-6 B1.) See [[feedback-checkpoint-before-notion]].
- **Every link in the checkpoint = a CLICKABLE markdown hyperlink** — winners, borderline, patterns AND browse — so she
  taps straight through to Chrome. Plain domains are not enough. See [[feedback-clickable-links]].
- **Browse-links = UNIQUE only** — never repeat a link already shown in winners/borderline (else she clicks and sees the
  same site twice). Browse = links that appear nowhere else in the report. See [[feedback-unique-browse-links]].
- **Heavy-textile / bulky → score Logistics + Margin harder** (shipping cost kills paid-traffic math; Sleepout curtain calibration).

**Why:** SH-5 b1 — Marina KEPT products from the broader sub-65 link list that were NOT in the agent's initial verdict
(PerchMe, Bamboo Sofa Tray, Trovely). The browse set surfaces founder-pattern finds the agent's bar alone would miss.
**Always lead a recommendation with the deep-score + WOW/taste read — never the proxy-Tier label** (Tier = revenue
sort-aid, not quality; it inflates on revenue/convergence — SH-5 confirmed).

---

## Collection seeding rule (SH-5, 2026-05-26 — Marina-approved STANDING RULE)
After each batch, ADD to the tracked-shop **Collection** (My ShopHunter → Shop Collections) the SHOP behind every product
that reached the browse pool — in 3 tiers:
1. **Reported 65+** (the strongest).
2. **Borderline 55–64.**
3. **The rest of the curated browse pool** (genuine PRODUCTS <55 we surface — see Reporting-protocol #4).
**Exclude:** branded-FYI, пустышка-FYI, and the stores of products Marina explicitly **Rejected** (e.g. Jar Genie/Stamny,
Elevayr). Add programmatically with `scripts/sh_collection_add.py <shop_id…>` (TOGGLE-safe for shops not yet in — Add/Remove
is a toggle, so **check membership before bulk-adding** to avoid accidentally removing a shop we already track).
**Observed ratio:** ~37 / 409 H&G stores (~9%) + 10 from SH-3/SH-4 = **47 shops seeded (SH-5)**. The collection grows every
batch (next: B&T 717). Purpose = feed the Newest-First monitoring layer (see `hypotheses/collection-newest-first-monitor.md`).
