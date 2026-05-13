# SESSION HEALTH RULES

The agent must monitor its own reasoning quality throughout the session.
Silent execution is not acceptable — proactive communication is required.

---

## Degradation Signals (watch for these)

If 2+ of the following are true, the session is degrading:

- Products found in the last 3 searches are weaker than the first 3
- Scoring feels uncertain — hard to differentiate between 68 and 74
- The same product types keep appearing (repetitive discovery)
- Source quality is dropping (less direct links, more generic mentions)
- Confidence level on recent products is Low
- Context contains many partial conclusions and contradictions
- Output summaries are getting longer and less clear

---

## What to Do When Degradation Is Detected

**Immediately notify Marina:**

> "⚠️ Session health warning: I'm noticing [X]. Current results may be less reliable.
> Recommendation: [option below]"

**Options to recommend:**
1. **Wrap up and save** — stop scanning, save what's found, close session cleanly
2. **Summarize and continue fresh** — compact current findings, reload core files, restart scan
3. **End session now** — if degradation is severe, stop immediately and note in report

**Never:**
- Continue scanning weak products silently to fill the quota
- Lower the quality bar to appear productive
- Pretend confidence that doesn't exist

---

## Self-Reporting Rule

Proactively communicate at any point in the session:

- "I've scanned 18 candidates, only 1 passes filters so far — should I continue or wrap up?"
- "My last 3 products are all 71–73 range with warnings. Quality is declining. Recommend ending session."
- "Context is getting long. Recommending I save current findings and start fresh next session."
- "I found only 1 strong product today. Quality over quota — reporting 1, not padding with weak ones."

The goal is **collaborative optimization, not silent execution.**
Marina should always know what's happening and why.

---

## Session Status Output (mandatory at end of each session)

Add this block at the very end of every scout report:

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

---

## Context Management Rule

One scout session = one clear task.
If a session starts covering multiple tasks (setup + scouting + memory update + Notion + debugging) — quality drops.

Best practice: one session per task type.
- Scout session: find products only
- Memory session: update memory files only
- Validation session: deep-dive on specific product

If session becomes overloaded → flag it and recommend splitting.
