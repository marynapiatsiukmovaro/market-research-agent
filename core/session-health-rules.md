# SESSION HEALTH RULES

## Degradation Signals

If 2+ of these are true, session is degrading:
- Products in last 3 searches are weaker than first 3
- Scoring feels uncertain — hard to differentiate scores
- Same product types keep appearing (repetitive discovery)
- Source quality dropping (less direct links, more generic mentions)
- Confidence on recent products is Low
- Context has many partial conclusions or contradictions

## When Degrading — Notify Marina Immediately

> "⚠️ Session health warning: I'm noticing [X]. Recommendation: [option]"

Options:
1. **Wrap up and save** — stop scanning, save what's found, close session cleanly
2. **Compact and continue** — save findings, reload core files, restart scan
3. **End session now** — if degradation is severe

Never: continue scanning weak products silently / lower the quality bar / pretend confidence

## Self-Reporting Rule

Communicate proactively at any point in the session:
- "Scanned 18 candidates, only 1 passes filters — continue or wrap up?"
- "Last 3 products are 71–73 range with warnings. Quality declining. Recommend ending."

Goal: collaborative optimization, not silent execution. Marina should always know what's happening.

## Session Status Output (mandatory at end of every scout report)

```
---
## SESSION STATUS

Session Quality: [High / Medium / Low]
Context Health: [Stable / Degrading / Overloaded]
Confidence in Results: [High / Medium / Low]

Products found: [X]
Products reported (65+): [X]
Products rejected silently: [X]

Recommendation for next session:
- [ ] Continue fresh — sources and memory up to date
- [ ] Verify links on: [product names if Needs Verification]
- [ ] Prioritize: [category or product type showing strong signals today]
```

## Keyword Quality Rule

After a full keyword scan, check keyword quality:

**Abort a keyword if:** 70%+ results are services/apps/supplements, 50%+ Amazon affiliates, or 0 physical products in target price range.

Report to Marina: "Keyword X yielded 0 physical products — replacing with Y"

Never run multiple rounds with the same failing keyword to fill the session quota.

**Important:** Department-level keyword strategy takes precedence over this rule. Keywords explicitly listed as intentional in the active sourcing channel's keyword-map.md (e.g. broad performance signal keywords) should NOT be replaced based on low yield alone — low yield may be expected and documented behavior for that keyword type.

## Context Management

One scout session = one task type. If session covers multiple tasks (scouting + memory update + Notion + debugging) — quality drops.

Best practice: one task per session (scout / memory update / validation). Flag and recommend splitting if overloaded.

## RULE-15: Memory File Growth Discipline (rotation + dedup-index)

**Purpose:** keep the mandatory-load files bounded as sessions accumulate and as new departments are added. Aggregate mandatory load was ~2000 lines as of 2026-05-28 (~4% of 1M context — a guardrail, not a fire). Without rotation, growth scales linearly with sessions × departments; this rule keeps it flat.

**Scope:** governs `shared/` log files and per-department `operational-memory/` files. Cross-departmental — every department inherits this rule via its `workflow.md`.

### Per-file policy

| File | Policy | Reason |
|---|---|---|
| `shared/reported-products.md` | **Compact dedup-index. NEVER session-rotate.** Active file keeps a one-line entry per product (name + domain + session) **forever**. Only verbose prose may be trimmed; the dedup-key row never leaves the active file. | Anti-duplicate recall must be permanent — a product reported at S5 must still be caught at S50. Rotation would re-introduce duplicates. |
| `shared/rejected-products.md` | **Rolling 20-session window** → `archive/rejected-products-archive.md`. At end-of-session, if the file holds entries from >20 sessions, move the oldest session block to the archive. Append a one-line pointer to the active file: `> Older entries (S1–SN): see archive/rejected-products-archive.md`. | Notion Archive view = permanent record; recall here is "skip-faster calibration," non-critical. Precedent: `archive/rejected-products-pre-S21-archive.md`. |
| `departments/{dept}/operational-memory/founder-feedback.md` | **Verify-before-archive — low priority.** Defer rotation until the file exceeds **~400 lines**. Before archiving any verbose per-session narrative, confirm the decision (Approved/Consider/Watchlist/Rejected + reason) is captured in the file's canonical decisions block. **Archive narrative only; NEVER archive the decisions themselves.** | This is "the most important memory in the system" — founder feedback overrides scoring. Currently small (FB 130 / SH 260 lines, 2026-05-28). |
| `departments/{dept}/operational-memory/learnings.md` | **(a) Tombstones cleanup:** when strikethrough `~~ARCHIVED~~` blocks occupy >30 lines or >20% of the active file, collapse them all into a single pointer to the dept's archive queue (preserve "promoted to op-rules RULE X" breadcrumbs as-is). **(b) Handoff rotation (where applicable — depts using HANDOFF blocks, currently SH):** keep only the **2 most recent** HANDOFF blocks in active; older handoffs → `departments/{dept}/operational-memory/handoffs-archive.md`. | These are the fastest-growing files (SH learnings was 583 lines pre-rotation). |

### Archive format

**Plain `.md` files** in `archive/` (for shared) or `departments/{dept}/operational-memory/` (for dept files). One-line pointer in the active file:
```
> Older entries (S1–S20): see archive/X.md
```
`grep` is the search mechanism. **No database, no index, no infrastructure** — keeping archives queryable in plain text is the point.

### When to apply

At end-of-session, as part of the department's Learning Protocol (FB `workflow.md` STEP 8 / SH `workflow.md` §3 / equivalent in future depts).

### Blind spots to monitor

- **`discovery-funnel.md`** and any future "living doc" accumulate session-stamped UPDATE blocks. Consolidate when promoted to `op-rules.md` — never let it grow append-only forever.
- **`keyword-map.md`** grows ~1 row per tested keyword (currently ~250 lines). When >500 lines, archive verdicts older than 6 months.
- **`outputs/daily-reports/`** — 1 file/session, not in mandatory load. Periodic sweep to `archive/daily-reports/`.
- **`seen-advertisers.md`** — independent rotation under FB `op-rules.md` RULE 13 (rolling 20 sessions, scraper-side). No action needed here.

### Anti-patterns (don't do)

- Do NOT rotate `reported-products.md` by session window — breaks anti-duplicate recall forever.
- Do NOT archive founder-feedback **decisions** — only verbose narrative.
- Do NOT add a search index / DB / second active file to "speed up" archive queries — plain `grep` on plain `.md` is sufficient and the canonical pattern.
