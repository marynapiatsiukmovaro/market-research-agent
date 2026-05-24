# OPERATIONAL RULES — PERMANENT

**These rules never expire. Apply to every session without exception.**
Read BEFORE learnings.md at session start.

Agent may NOT modify this file during scout sessions.
Updates only when Marina explicitly instructs it.

---

## Keyword Execution Protocol

### RULE 0: NEVER advance to next keyword without explicit user approval — UNLESS Autonomous Mode is enabled

**Default (Autonomous Mode OFF):** After each keyword — output checkpoint → STOP → WAIT.
Do NOT launch next scraper, do NOT start background process, do NOT prep next keyword.
"Recommendation: next keyword" in checkpoint = suggestion only. Marina decides.
This applies even when the recommendation is obvious, even when the previous keyword yielded 0 results, even when background launch "seems efficient."

**EXCEPTION — Autonomous Mode (facebook-ads-library department only):** If the session prompt explicitly enables Autonomous Mode, run ALL listed keywords sequentially WITHOUT stopping for confirmation between keywords. Still output the full KEYWORD CHECKPOINT after each keyword. Approved by Marina S30 (tested S30 — worked: 5 keywords, 2 reportable). HARD-STOP conditions still apply and are NEVER bypassed:
- scraper returns <50 ads → STOP + request cookie refresh
- Facebook shows suspicious-activity / automated-behavior warning → STOP
- context usage >70% before STEP 8 → alert Marina first
- a borderline 60–64 candidate needing a founder call → log it + flag explicitly in the report (never silently pass)
- a SCOUT NOTE proposing a NEW direction, a pivot, or adding/substituting keywords NOT in the prompt list → STOP and wait. (Descoping a keyword already confirmed DEAD in keyword-map, with a flag, IS allowed autonomously — as done S30 with "long commute"/"stuck in traffic".)

Outside facebook-ads-library, or when Autonomous Mode is not stated in the prompt → default (wait) applies. Supersedes the prior "No exceptions" wording (updated S30 with Marina's explicit approval). See memory [[feedback-autonomous-mode]] and [[feedback-keyword-wait]].

---

## VPS & Session Setup

### RULE 1: Five mandatory checks before launching scraper

**STEP 0 — Upload Marina's cookies FIRST (if provided in session prompt)**

If Marina provided a cookie string in the session prompt → upload it to VPS BEFORE running any checks.
Reason: check_session.py (check #5) must validate Marina's CURRENT session, not the old file.
Running checks before upload = validating stale data = false SESSION OK.

```bash
# STEP 0 — only if Marina provided cookies in prompt
# Script is at: scripts/update_fb_session.py (permanent, in repo — NOT /tmp)
python3 /Users/marinapetuk/Desktop/АГЕНТЫ/market-research-agent/scripts/update_fb_session.py "<cookie_string>"
scp -i ~/.ssh/market_research_vps /tmp/fb_session_new.json root@5.78.217.133:/opt/market-research-agent/cookies/fb_session.json
# Then proceed to checks 1–5 below
```

**CRITICAL: fb_session.json required format** — `{"cookies": [...]}` (dict with 'cookies' key, NOT a plain list)
check_session.py line: `context.add_cookies(session['cookies'])` → requires dict access.

If Marina did NOT provide cookies → skip STEP 0, proceed directly to check 1.

Run ALL five before every scraper run. If ANY fails → STOP and fix first.

```bash
# 1. VPS accessible
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "echo OK"

# 2. Session file exists at correct path
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "ls /opt/market-research-agent/cookies/fb_session.json"

# 3. Scraper uses JS scroll (not mouse.wheel)
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "grep 'window.scrollBy' /opt/market-research-agent/skills/facebook_scraper.py"

# 4. No existing scraper process running
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "ps aux | grep facebook_scraper | grep -v grep"

# 5. Session still valid
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "python3 /tmp/check_session.py"
# Must return: "SESSION OK: Logged in" + name Mikhail Piatsiuk
# If "SESSION EXPIRED" → update cookies before continuing (see RULE 2)
```

**fb_session.json correct path:** `/opt/market-research-agent/cookies/fb_session.json`
NOT `/root/fb_session.json` and NOT `/tmp/fb_session.json`.

Without valid session: 19-32 ads/keyword (useless). Without JS scroll: same result.

### RULE 2: Cookie re-export process (when session expires)

FB session expires unpredictably — can be hours. Signs: check_session.py → "SESSION EXPIRED", or keyword gives <50 ads despite technically valid session file.

Marina re-exports cookies:
1. Chrome → facebook.com → confirm logged in as **Mikhail Piatsiuk**
2. DevTools (F12) → Network tab → click any facebook.com request → Headers → Request Headers → Cookie → copy entire string (starts with "datr=...")
3. Send string to agent
4. Agent creates fb_session.json and uploads to VPS:
   `scp -i ~/.ssh/market_research_vps /tmp/fb_session.json root@5.78.217.133:/opt/market-research-agent/cookies/fb_session.json`
5. Verify: `python3 /tmp/check_session.py` → SESSION OK → proceed

Required cookies in string (if any missing — session won't work): `c_user`, `xs`, `fr`, `datr`, `sb`

Timing: give cookies at the start of each new session if more than 2-3 hours passed since last successful run.

### RULE 3: --sort=recent flag status

With valid fb_session.json: `--sort=recent` does NOT trigger login wall (confirmed S8 Part 2 + S13).
BUT: scraper often falls back to impressions sort even with the flag. Check URL in scraped data.
Default: run WITHOUT `--sort` (impressions = proven winners) unless there is a specific reason for recent sort.

### RULE 4: FB "automated behavior" warning — Dismiss fix (permanent, Session 14)

FB shows pop-up "We suspect automated behavior on your account" → scraper sees 0 cards.
This is NOT a session loss and NOT a scraper bug — account remains logged in.

Fix is already permanently added to `skills/facebook_scraper.py`:
```python
dismiss_btn = page.locator('div[role="button"]:has-text("Dismiss")')
if dismiss_btn.count() > 0:
    dismiss_btn.first.click()
    human_delay(1, 2)
```
Backup saved: `skills/facebook_scraper.py.bak_s14`

Appears after intense scraping (>300-400 ads per session). Detection: keyword 1 gives normal count, keyword 2 gives 0 — suspect this warning first.

---

## Scraper Invocation — Correct Syntax (RULE 4b)

**CRITICAL: The scraper uses POSITIONAL arguments for keywords, NOT `--keyword=`**

```bash
# CORRECT — keyword is a positional argument
cd /opt/market-research-agent
nohup python3 skills/facebook_scraper.py 'burnout' --deep --output=/tmp/burnout_results.json > /tmp/burnout_scraper.log 2>&1 &
echo PID:$!

# Run fast filter after completion
python3 skills/fast_filter.py /tmp/burnout_results.json --top=20
```

**Supported flags:** `--deep` (500 target) | `--output=FILE` | `--since=YYYY-MM-DD` | `--seen=FILE` | `--sort=recent`
**NOT supported:** `--keyword=`, `--max=`, `--country=`, `--status=` → these become literal keywords to search!

**CRITICAL: Single process rule** — before launching, always:
```bash
ps aux | grep facebook_scraper | grep -v grep || echo NO_SCRAPERS
```
If ANY process found → STOP, kill first → then launch one. Never launch multiple scrapers.

---

## Scraper Depth Rules

### RULE 5: Depth standard — 500 target, 600 hard cap

- **Target:** 500 ads/keyword
- **Hard cap:** 600 — never exceed (detection risk + diminishing returns after 600)
- **Natural stop:** scraper stops at 500-580 after last batch overshoots. This is NORMAL.
- **Scale strategy:** add more keywords (breadth), NOT go deeper on one keyword.

Two scenarios:
- **Broad keyword** (baby, kids): FB exhausts unique advertisers before 500. Natural stop earlier = normal.
- **Specific keyword** (baby carrier, screen time): FB can deliver 500-580 unique advertisers. Stop at target.

### RULE 5b: Any keyword has 500+ ads — low count = scraper bug, NOT keyword limit

**FB Ads Library always has 50,000+ ads indexed for any keyword.** If scraper returns <50 ads:
- This is a scraper/session bug — NOT evidence that the keyword has few advertisers
- Do NOT record low count as a keyword verdict
- Do NOT mark keyword as ❌ DEAD based on low ad count alone

**Root cause (confirmed S18):** FB React renders cards lazily. Scraper may start parsing before cards appear → gets 0 in first batches → triggers early stop. Fix: warm-up scroll (already added to scraper) + stop threshold = 5 batches (not 2).

**If <50 ads returned:**
1. Check session validity first (`check_session.py`)
2. If session OK → scraper stalled early (warm-up didn't work) → re-run the keyword
3. Only after a confirmed full run (session OK + no early stall) → accept the count as real

**Keywords with counts affected by this bug (need re-test):** nursing pillow (~25 ads S8), kids (53 ads S9) — still need re-test. quality time, genius gadget, connect with your, back in stock — re-tested S18, verdicts confirmed, keyword-map updated.

### RULE 5d: Back-scroll recovery — mid-run stall fix (permanent, Session 22)

FB React lazy-loader can stall mid-scroll at ~200-300 ads: scraper gets 0 new cards for 2 batches → without fix, stop triggers at 5 empty batches → early stop (194 ads instead of 500+).

Fix is permanently added to `skills/facebook_scraper.py` (backup: `facebook_scraper.py.bak_s22`):
```python
if no_new_streak == 2:
    print(f"[SCROLL] Stall — back-scroll recovery (up 3000px then down 2000px)...", flush=True)
    page.evaluate("window.scrollBy(0, -3000)")
    time.sleep(2.5)
    page.evaluate("window.scrollBy(0, 2000)")
    time.sleep(2.0)
    no_new_streak = 0  # reset: give 5 more batches after recovery
```

- Triggers at `streak == 2` (not 5) — recovers before stop threshold
- Can trigger multiple times per session if multiple stalls occur
- Confirmed working: ergonomic keyword S22 (recovered at batch 4 → loaded 329 more ads → hit 500 target)
- Root cause: desk setup S22 returned only 194 ads before fix (first run was valid — sessions expired on 2nd run)

### RULE 5c: Special characters in keywords — quote_plus encoding (fixed S18)

Keywords with `'` (apostrophe), `%`, `&`, `#` or other special chars previously returned 0 ads due to broken URL encoding. **Fixed in S18:** `build_search_url()` now uses `urllib.parse.quote_plus(keyword)`. All special characters are now handled automatically — use keyword text literally, no substitutions needed. If a keyword returns 0 ads, check session first (RULE 5b) — do NOT assume special chars are the cause.

### RULE 6: Depth risk map

| Depth | Risk level | Notes |
|-------|-----------|-------|
| 400–600 | LOW | "Heavy researcher" behavior — safe |
| 600–800 | LOW-MEDIUM | Acceptable with human-like delays |
| 800–1000 | MEDIUM | FB anomaly detection activates |
| 1000–2000 | HIGH | Hidden throttling: FB repeats same ads, less diversity |
| 2000–3000 | VERY HIGH | CAPTCHA on next login, soft session ban |

**Hidden throttling detection:** FB shows no error — just repeats the same ads. Detect by: `new_count` drops sharply in batch logs (10-20). If spotted → stop immediately.

---

## Discovery Process Rules

### RULE 7: Candidate list — save to VPS, NOT to chat

After scraping + dedup: run fast_filter.py on VPS → only top 20 come to chat.

**Standard pipeline (run on VPS immediately after every scrape):**
```bash
python3 skills/fast_filter.py /tmp/{keyword}_results.json --top=20
```
- Top 20 candidates → printed to chat (this is ALL that goes to chat)
- Full filtered list → auto-saved to `/tmp/{keyword}_results_candidates.txt`
- Script location: `/opt/market-research-agent/skills/fast_filter.py`

**If fast_filter.py fails:** fix the script on VPS first — do NOT fall back to dumping raw advertiser list to chat. A crash is not a reason to bypass the rule.

Report in chat: `"Fast filter: [N] passed / [total] scraped. Full list: /tmp/xyz_results_candidates.txt"`

Reason: outputting 238 raw advertisers to chat = 40-50% of context window burned for zero benefit. Agent analyzes only top 15-20 anyway. Session 15 confirmed this failure mode.

### RULE 8: Verify ALL candidates above objective threshold — not "top 5"

After fast filter, WebFetch ALL remaining candidates. No subjective pre-selection before WebFetch.

Correct process:
1. Apply ONLY objective filters: clearly digital/service, price floor violation (.gov/.edu, app store, local business), wrong category
2. WebFetch ALL who remain — batches of 3-4 in parallel per response block
3. If 20 candidates → 5 parallel rounds. If 50+ → one additional objective pass first (domain category, ad copy scan) to reduce to 20-30 before WebFetch

NEVER: "Here are the 5 most interesting candidates" before WebFetch. That is subjective selection before having data — it misses winners.

### RULE 9: Parallel verification — 3-4 WebFetch per response block

At verification stage: run 3-4 WebFetch calls simultaneously in one response block.
Speedup: ~30-40% vs sequential.
Apply: when multiple independent candidates need domain/price verification.
Do NOT apply: when result of first fetch is needed to decide on next.

---

## Product Assessment Rules

### RULE 10: Dropship brand ≠ reason to reject

Multiple domains selling one product = demand signal, not red flag.
Dropship operators (DBO Networks, etc.) = pre-validation service. If product is alive 6+ months → demand proven.

Filter by PRODUCT:
```
✅ Price in $39-99?
✅ COGS realistic (Alibaba/AliExpress)?
✅ White-label possible (no concept patent)?
✅ US market applicable?
→ Score normally

❌ NOT by seller type:
- "this is a dropshipper" → NOT a reject reason
- "foreign brand" → NOT a reject reason (check US applicability)
- "multiple sellers" → NOT a reject reason (it IS validation)
```

### RULE 11: Honest 0-result is a valuable result

When keyword yields 0 reportable products after honest scan → useful intelligence, not failure:
- Close that keyword → add to keyword-map.md as ❌ DEAD → move to next keyword
- Do NOT force weak products to avoid "empty session"
- Quality 0-result > 1 forced weak product

### RULE 12: Price $100–170 — score normally with Margin Potential penalty

Products in the $100–170 range are NOT auto-rejected. Score them normally.

Process:
1. Score all dimensions normally
2. Margin Potential: cap at 5/10 for this price range (higher AOV = thinner margins for cold traffic)
3. If total score ≥ 65 → report with Price Range = "Premium $100–170" in Notion
4. Over $170 → reject (outside practical cold traffic DTC range)

Notion already has "Premium $100–170" as a Price Range category — use it.
A strong product at $130 with score 72 should be reported. The score accounts for price via Margin Potential.

---

## Memory Management Rules

### RULE 13: seen-advertisers.md — Rolling 20-session window

`seen-advertisers.md` = active operational file (last 20 sessions). Scraper uses this via `--seen` flag.
`seen-advertisers-archive.md` = historical file (sessions beyond the 20-session window). Never loaded by agent. Never used by scraper.

**Agent rule at STEP 8:**
1. Count `## Session` headers in seen-advertisers.md
2. If count > 20 → move the oldest session block (header + all entries) to seen-advertisers-archive.md
3. Repeat until ≤ 20 session blocks remain in active file
4. **Emergency hard cap:** If active file exceeds ~2500 non-comment lines (high-density exploration edge case), archive oldest session block immediately — regardless of session count. Resume normal 20-session rule after.
5. MOVE only — never delete

**Why rolling sessions (not days or entry count):**
- At 50+ sessions/month, 90 days would accumulate 4000+ entries before rotation
- Sessions are the natural unit of work — file is already structured by session blocks
- Counting headers is instant; rotating one block is atomic
- Self-calibrating: works at 1 session/day or 5 sessions/day without parameter changes
- Expected active file size: ~20 sessions × ~40 entries = ~700–900 entries max

**Agent does NOT load seen-advertisers.md at session start.** The scraper reads it on VPS at scrape time — no agent context cost. Only read if explicitly investigating a specific domain.

---

### RULE 14: Separate DATA from SYSTEM-CHANGING CONCLUSIONS — propose, don't auto-write

**Purpose:** protect the document architecture. Departments record their own work LOCALLY. "Strong documents" (core/ + the distilled founder-taste calibration rules) change behavior across ALL sessions and departments — so they change ONLY by proposal + Marina's OK. Chaotic writes into shared/core docs by any department are prohibited (see CLAUDE.md department isolation). Added S24 — recurring failure (over-generalizing a single case into a system rule; happened S22→corrected S23, S24→reverted).

At STEP 8, classify every intended memory write:

**TIER 1 — Data & specific facts → write freely, in THIS department's folder only:**
keyword results, products found/scored, a SPECIFIC founder decision on a SPECIFIC product (+ the exact reason), session reports, recurring-signal notes, candidate logs. (Normal logging — fast, autonomous, never blocked.)

**TIER 2 — System-changing generalization → PROPOSE ONLY, never auto-write:**
- any new/changed SCORING, FILTER, VETO, or generalized TASTE rule;
- closing/rejecting a whole category or product class; "we no longer take X" / "only take Y";
- a DIRECTION that overrides the active hypothesis;
- any promotion of a learning into core/ or the distilled founder-taste rules;
- anything one department's findings would impose on core or another department.
→ put in SESSION LEARNING REPORT under "Proposed system change (needs Marina's OK)";
→ write ONLY after Marina explicitly approves; route core promotions via review/promotion-queue.md.

**Decision test:** "Would this change behavior on products/keywords BEYOND the specific case I just observed, OR touch a strong document?" If yes → Tier 2. **WHEN IN DOUBT → Tier 2.**

**Sample-size guard:** a conclusion from ONE session / a few keywords is a HYPOTHESIS, not a rule. Record it as a directional observation (Tier 1); a rule needs 3+ confirmations OR Marina's explicit approval.

**Boundary clarifier:**
- "Marina rejected product P because R" = Tier 1 (fact → founder-feedback log).
- "therefore reject all products like P" / a new taste rule = Tier 2 (propose first).
