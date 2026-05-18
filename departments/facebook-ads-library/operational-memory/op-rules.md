# OPERATIONAL RULES — PERMANENT

**These rules never expire. Apply to every session without exception.**
Read BEFORE learnings.md at session start.

Agent may NOT modify this file during scout sessions.
Updates only when Marina explicitly instructs it.

---

## VPS & Session Setup

### RULE 1: Five mandatory checks before launching scraper

**STEP 0 — Upload Marina's cookies FIRST (if provided in session prompt)**

If Marina provided a cookie string in the session prompt → upload it to VPS BEFORE running any checks.
Reason: check_session.py (check #5) must validate Marina's CURRENT session, not the old file.
Running checks before upload = validating stale data = false SESSION OK.

```bash
# STEP 0 — only if Marina provided cookies in prompt
python3 /tmp/update_fb_session.py   # create fb_session_new.json from cookie string
scp -i ~/.ssh/market_research_vps /tmp/fb_session_new.json root@5.78.217.133:/opt/market-research-agent/cookies/fb_session.json
# Then proceed to checks 1–5 below
```

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

**Keywords with counts affected by this bug (need re-test):** nursing pillow (~25 ads S8), kids (53 ads S9), quality time (44 ads S14), perfect gift (28 ads S18), back in stock (0 ads S18) — all marked in keyword-map.md with ⚠️ BUG flag.

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
