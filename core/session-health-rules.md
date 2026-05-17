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
