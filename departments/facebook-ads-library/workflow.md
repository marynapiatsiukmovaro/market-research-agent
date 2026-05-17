# DAILY SCOUT WORKFLOW

## Daily Target
- Scan: 15–20 product candidates
- Filter: apply mandatory filters (fast reject)
- Score: score remaining candidates
- Output: 2–5 best products in Scout Mode format (quality over quantity — never force weak products to fill quota)

## Step-by-Step

### STEP -1 — Pre-Session Context (run before loading memory)
Ask Marina (or check prior session notes for):
- "Are there any categories you've been seeing a lot in your own social feed lately?" → log as potential везде risk
- Confirm current date and freshness threshold (ideal = current year, acceptable = current year -1)
- Confirm session type: Scout / Validation / Analysis / Memory-only

### STEP 0 — Load Memory (before scanning anything)
Read these files BEFORE scanning anything:
1. `shared/reported-products.md` — do NOT report any product already logged here
2. `shared/rejected-products.md` — use patterns to skip similar weak products faster
3. `departments/facebook-ads-library/operational-memory/learnings.md` — apply active temporary guidance; if a Current Focus is set, it overrides default source priority for this session
4. `core/operating-rules.md` — core operating principles (verification hierarchy, signal tiers, pivot rules)

### STEP 1 — Scan Sources (15–20 candidates)
- Facebook Ads Library via VPS scraper (primary discovery source)
- Other sources (Amazon, AliExpress, TikTok organic) — secondary verification only
- Skip any product already in memory

**Before each keyword scan round:** announce the plan — which keywords, what strategy, one sentence why. Wait for Marina's OK before starting if the plan is a major direction change.

**When changing direction:** call it explicitly — "PIVOT: [previous direction] → [new direction]. Reason: [1 sentence with specific data]. Closed: [dead branches]." Max 2 pivots per session without Marina's explicit OK for a third.

### STEP 2 — Apply Mandatory Filters
- Check each candidate against `core/mandatory-filters.md`
- Reject fast — do not over-analyze weak products
- Target: 8–10 pass filters out of 15–20 scanned

### STEP 3 — Score Filtered Products
- Apply `core/scoring-system.md`
- Add competitor ad activity check
- Add creative angle count estimate

### STEP 4 — Find Source Links
For each candidate scoring 65+:
- Find real Ad/Source Link (where it was found)
- Find real Store Link (where it is sold)
- If a link cannot be found after a genuine search → write "Not found", do NOT guess or invent a URL
- Missing both links → set Recommendation to "Needs Verification"

### STEP 5 — Select Top Products
- Rank by score
- Minimum score to include: 65+
- Target 2–5 products. If fewer than 2 score 65+, output what genuinely qualifies — do NOT lower the bar to fill the quota
- If nothing qualifies → note this in the report and explain why
- If more than 5 score strongly → include all of them (no hard upper limit)

### STEP 6 — Output Scout Mode Reports
- One report per product (use `core/identity.md` output format)
- Save to `outputs/daily-reports/YYYY-MM-DD.md`

### STEP 7 — Save to Notion
- Follow `shared/notion-workflow.md`
- One Notion entry per reported product (score 65+)
- Set Recommendation: Worth Testing / Needs Verification / Rejected
- Set Competitor Signal: None / Testing / Scaling / Saturated / Legacy Winner
- Set Source: standardized value only (Facebook Ads Library / Amazon Search / TikTok Search / TikTok Shop / Minea / Web Search / AliExpress / Alibaba)
- Set Discovery Keyword: exact search query used to find this product
- Fill Notes: short risk flags or observations (1 sentence each, no analysis)
- Fill Rejection Reason only when Founder Review = Rejected (not just Recommendation = Rejected)
- Leave Founder Review blank — Marina sets this manually, never the agent
- Leave Founder Notes blank — Marina's field only

### STEP 8 — End-of-Session Checklist (mandatory, do not skip)

**1. Save reported products** → `shared/reported-products.md`
- Add one row per reported product: Date, Product, Category, Score, Key Hook, Source

**2. Save notable rejections** → `shared/rejected-products.md`
- Add products that looked promising but failed for a non-obvious reason
- Skip trivially weak products — only log rejections with a lesson

**3. Update patterns if new insight emerged**
- `shared/successful-patterns.md` — recurring winning trait found today
- `shared/failed-patterns.md` — recurring weak pattern found today
- Only update if something new was discovered — don't repeat existing entries

**4. Mark unverified links**
- Any product missing real source links → set Verification to "Needs Verification ⚠️"
- Do not leave blank link fields — write "Not found" explicitly

**5. Run Learning Protocol**

**5a. Archive expired learnings first:**
Before adding anything, check every entry in `departments/facebook-ads-library/operational-memory/learnings.md`.
Any entry with `Expires after: Session N` where N ≤ current session → move to the Expired section at the bottom of learnings.md.
This is allowed — archiving is not editing. Keep file under 20 active entries total.

**5b. Update keyword map:**
Add one row to `departments/facebook-ads-library/operational-memory/keyword-map.md` for each keyword tested this session.
Format: `| keyword | S[N] | [ads] | ✅/❌/⚠️ verdict | [1-line signal or reason dead] |`

**5c. Append new learnings (only what's truly new):**
Append to `departments/facebook-ads-library/operational-memory/learnings.md` if any of these were observed:
- new category signal (brand as category validator, open vs closed niche)
- new behavioral correction (agent error caught and fixed)
- new situational pattern (unexpected category intersection found)
- product angle discovery (new hook or trigger worth tracking)

Do NOT append:
- keyword verdicts → keyword-map.md (step 5b)
- permanent rules (Expires: Never) → op-rules.md (requires Marina confirmation)
- trivial confirmations of existing learnings

**5d. Promote if confirmed:**
Append to `review/promotion-queue.md` only if a learning was confirmed across **3 sessions** OR explicitly approved by Marina — never after one session alone.

**Promotion queue check:** Count unreviewed items in `review/promotion-queue.md`. If 3+ unreviewed items exist → mention under "Founder review needed" in the SESSION LEARNING REPORT. Marina initiates a Review session at her discretion — no automatic action by agent.

NEVER edit non-expired entries. NEVER modify core/ files.

**6. Save session report**
- Save output to `outputs/daily-reports/YYYY-MM-DD.md`
- Include product count, top scorer, and any notable patterns

**7. Prevent duplicates in next session**
- Confirm shared/reported-products.md is updated before closing
- Next session STEP 0 will read this file — it must be current

**8. Deliver Session Learning Report** (add after Session Status block)

```
---
## SESSION LEARNING REPORT

Products found: [X scored 65+] | Strongest signal: [product + key reason]
False positives: [products that looked strong but failed + why] / None
Repeated patterns: [pattern seen 2+ times this session] / None

### A. Product Intelligence
- Saturation: [market saturation signals found]
- Pricing: [price range observations]
- Hooks: [creative / hook patterns that appeared]
- Market proof: [premium brands, ad duration, review velocity]
- Rejection reasons: [non-obvious failure patterns]

### B. Discovery Intelligence
- Keywords that worked: [specific queries that yielded real products]
- Keywords that failed: [queries → noise / affiliates / wrong category]
- Filters that helped: [ad duration, country, media type, date range]
- Search paths to repeat next session:
- Search paths to abandon:
- Launch-stage signals seen: [ad behavior patterns = new entrant]

Failed paths summary: [1 sentence] / None
Proposed core updates: [items added to review/promotion-queue.md] / None
Founder review needed: [items requiring Marina's decision] / None
Test next session: [specific keyword / angle / category to explore]
```

Memory update is not optional. It is what makes the agent smarter over time.

**9. Generate HANDOFF block** (mandatory, paste into daily report)

```
## HANDOFF FOR SESSION [N+1]

Critical context:
- Last unresolved hypothesis: [what remains open]
- Highest priority action: [1 specific action]
- Active candidates needing verification: [product + specific check]
- Closed hypotheses (do not reopen): [list]

Memory state:
- Files updated this session: [list]
- Open Notion items: [links if any]

Recommended next session type: [Scout / Memory / Validation / Analysis]
Next session startup prompt: [verbatim prompt to paste]
```

## Session Type Separation

One session = one task type. Do not mix.

| Type | Purpose | Output |
|------|---------|--------|
| Scout | Product discovery and scoring | Daily report + shared/reported-products.md update |
| Validation | Deep dive on one product (85+ score only, or explicit request) | Validation report |
| Memory | Update memory files only | Updated files + git commit |
| Analysis | Systems review (like post-mortem) | Framework document |

If session becomes overloaded (>70% context used before STEP 8): save critical files first, defer Notion/git to next Memory session.

## Frequency
Daily. Run each morning before market activity increases.
