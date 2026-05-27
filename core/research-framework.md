# Research Framework

This file explains the system's four-layer architecture.
Read it once to understand how the system is organized — then navigate confidently.

---

## Layer 1: Core (stable, universal)

**Location:** `core/`
**Changes:** only when Marina explicitly instructs
**Agent rule:** never modify during scout sessions

Contains winner-product logic that does not change with niche or strategy:
- Scoring system (core/scoring-system.md)
- Mandatory filters (core/mandatory-filters.md)
- Product requirements (core/product-requirements.md)
- Founder identity and goals (core/founder.md)
- Agent role and output format (core/identity.md)
- Operating rules and session health (core/operating-rules.md, core/session-health-rules.md)

---

## Layer 2: Departments (operational, per-channel)

**Location:** `departments/{department-name}/`
**Changes:** as the channel's operational needs evolve
**Agent rule:** work only inside your assigned department

Each department = one sourcing channel. Isolated from all others.

Current departments (operational):
- `departments/facebook-ads-library/` — FB Ads Library via VPS scraper (keyword-first discovery)
- `departments/shophunter/` — ShopHunter store-first discovery (store revenue / longevity / multi-store intelligence)

Future departments (not yet built):
- `departments/instagram/`
- `departments/tiktok-ads/`
- `departments/amazon/`

Each department contains:
- `workflow.md` — **the session entry point: step-by-step session procedure. Every department MUST have one** — even a thin wrapper that points to its main method file (e.g. ShopHunter's `workflow.md` → `methods/discovery-funnel.md`). Routing and the session load-list both target `departments/{dept}/workflow.md`.
- `methods/` — channel-specific tools and scrapers
- `operational-memory/` — permanent rules, learnings, keyword verdicts, founder calibration
- `hypotheses/` — current and archived research directions

**Do not mix department logic.** FB scraper rules do not apply to an Amazon agent, and vice versa.

---

## Layer 3: Hypotheses (temporary, within a department)

**Location:** `departments/{dept}/hypotheses/`
**Changes:** when Marina initiates a new research direction
**Agent rule:** read `_active.md` to find the current hypothesis; treat archived ones as historical only

A hypothesis is a **temporary research mode** — a direction for the next N sessions.
Examples: "Kids Vertical", "Broad Horizontal Discovery", "Home Category Scan", "Emotional Trigger Scan".

One hypothesis is ACTIVE at a time. Others are ARCHIVED.

**Hypotheses are not company strategy.** They are experiments.
Winner-product criteria (Layer 1) do not change when a hypothesis changes.

Structure:
```
hypotheses/
  _active.md                      ← pointer to current hypothesis
  broad-horizontal-discovery.md   ← active hypothesis
  kids-vertical.md                ← archived
  emotional-trigger-scan.md       ← future example
```

To activate a new hypothesis: update `_active.md` and set the old one to "ARCHIVED".

---

## Layer 4: Learnings (tactical, short-lived)

**Location:** `departments/{dept}/operational-memory/learnings.md`
**Changes:** agent appends at end of every session; expires entries after N sessions
**Agent rule:** read after op-rules.md; may override default source priority for the session

Contains discoveries from recent sessions that have not yet been confirmed enough to become permanent rules.

Lifecycle:
1. Agent observes a pattern → appends to learnings.md with expiry date
2. If confirmed across 3 sessions → added to review/promotion-queue.md
3. Marina decides: Promote → op-rules.md or core/; Wait; Reject
4. Expired entries → moved to Expired section in learnings.md (not deleted)

---

## Decision Tree: Where Does This Information Go?

```
Is it a universal winner-product rule?
  YES → core/ (requires Marina approval to change)

Is it specific to one sourcing channel?
  YES → departments/{dept}/operational-memory/op-rules.md

Is it a temporary research direction for the next N sessions?
  YES → departments/{dept}/hypotheses/ (new file, update _active.md)

Is it a short-lived tactical observation from recent sessions?
  YES → departments/{dept}/operational-memory/learnings.md (with expiry)

Is it a keyword verdict (dead / alive / promising)?
  YES → departments/{dept}/operational-memory/keyword-map.md (one row)
```

---

## Common Mistakes to Avoid

- **Do not put FB-specific rules in core/.** Core is channel-agnostic.
- **Do not treat an active hypothesis as permanent strategy.** Hypotheses expire; core criteria don't.
- **Do not let learnings accumulate without expiry dates.** Every learning must have an expiry or be promoted to op-rules.md.
- **Do not cross-contaminate departments.** FB session rules, VPS checks, and scroll depth are invisible to other departments.
