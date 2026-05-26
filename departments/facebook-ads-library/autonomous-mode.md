# AUTONOMOUS MODE — Facebook Ads Library Department ONLY

**STATUS: 🧪 TESTING — first trial = Session 30 (one office session). Not yet permanent.**
**SCOPE: This file governs ONLY the `facebook-ads-library` department.**
Autonomous Mode is a DEPARTMENT-LEVEL capability, never core. It depends on this
department's specific guardrails (FB pre-flight checks, scraper depth caps, hydration-stall
recovery). **It must NEVER be enabled in another department** (e.g. ShopHunter) until that
department has built and battle-tested its OWN autonomous-mode file with its OWN guardrails.
Do NOT copy this file blindly into a new department.

---

## What it is
A session mode where the agent runs a FULL pre-authorized batch of keywords WITHOUT
per-keyword approval, self-paces, and delivers ONE consolidated report at the end.
It replaces the human checkpoint (RULE 0) with automatic guardrails — safe only because
those guardrails are hard-coded below.

## Activation (never the default)
Only when Marina explicitly writes **"autonomous run"** (or the session prompt sets it)
AND provides up front: (1) the full keyword list (or "niche + N keywords"), (2) fresh cookies.
Absent an explicit trigger → RULE 0 stays in force (stop + wait after every keyword).

## What changes vs RULE 0
| | RULE 0 (default) | Autonomous Mode |
|---|---|---|
| Advance to next keyword | wait for Marina's "ok" | run full batch, no stop |
| Checkpoints | full checkpoint to chat each keyword | one-line log per keyword to a running file; full report at END |
| Marina's involvement | continuous | start (list + cookies) + final review only |

## Auto-guardrails that REPLACE the human checkpoint (non-negotiable)
1. **Pre-flight 5 checks + credit-guard before EVERY scraper launch** (op-rules RULE 1).
   Any fail → auto-halt, do not continue.
2. **Single-process rule** — `ps aux | grep facebook_scraper` before each launch; never 2 scrapers.
3. **Depth caps:** 600 ads/keyword (RULE 6) + **session total cap ~2,000–2,500 ads** → then auto-halt.
   (No human watching → over-scraping = FB throttle/detection risk.)
4. **Hydration-stall / 0-card auto-recovery (RULE 5b):** 0 cards → re-run keyword ONCE.
   Still 0 → skip keyword, log it, continue. Never loop a failing keyword.
5. **FB "automated behavior" / restricted visibility → HARD STOP**, save state, wait for Marina.
   Do NOT push through (matches session-prompt restriction rule).
6. **Cookie expiry mid-batch → STOP + request fresh cookies** (agent cannot self-refresh).
7. **Degradation stop** (session-health-rules): 3+ consecutive anomalies (0-card stalls /
   broken counters) → halt + flag.

## Hard-stop conditions (auto-halt + wait for human)
Any pre-flight fail · FB visibility restriction · session/cookie expiry · total-ads cap reached
· 3+ consecutive degradation signals · context approaching limit (save critical first).

## What stays HUMAN (never autonomous)
- Founder decisions Approved / Consider / Watchlist / Rejected — Marina only.
- Tier-2 system changes (new scoring/filter/veto/class-closure) — proposal only (RULE 14).
- Pushing through any FB visibility restriction.

## What the agent MAY do autonomously
Scrape the batch · fast_filter · verify candidates (WebFetch) · score · capture ANY 65+
(cross-category rule) WITHOUT stopping the batch · STEP 8 memory writes · Notion logging of
reported (65+) products (Tier-1 data logging).

## Reporting cadence
Per keyword → one compact line (count + verdict + any 65+ flag) appended to a running log.
At END → full checkpoint table for all keywords + all 65+ candidates + STEP 8 + Session
Learning Report + Handoff. A mid-run 65+ find is captured but does NOT halt the batch.

## Token / budget protection
- Background scraper + harness notification (no polling) to conserve context & budget.
- Credit-guard (`ps aux | grep claude` on VPS) before each launch; NEVER run claude on the VPS.
- If context exceeds ~60% before STEP 8 → save critical files first, defer Notion if needed.

---

## Trial checklist (Session 30)
- [ ] Marina triggers "autonomous run" + gives full keyword list + fresh cookies.
- [ ] Agent runs batch end-to-end under the guardrails above.
- [ ] Agent delivers ONE consolidated report.
- [ ] Marina reviews: did guardrails hold? was the report sufficient without per-keyword stops?
- [ ] If yes → change STATUS to PERMANENT (remove TESTING) at next promotion review.
