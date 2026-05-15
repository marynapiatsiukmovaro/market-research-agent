# VPS CONNECTION CONFIG

**RULE: Agent reads this file at the START of every scout session. Connects to VPS BEFORE any other work.**
**WebSearch = secondary verification only. Primary discovery = FB Ads Library via VPS scraper.**

---

## Connection

```bash
ssh -i ~/.ssh/market_research_vps root@5.78.217.133
```

Project path on VPS:
```
/opt/market-research-agent/
```

---

## Pre-Run Safety Check (run immediately after login)

```bash
# 1. Check no duplicate claude process is already running (protects VPS credits)
ps aux | grep claude
ps aux | grep python3

# 2. Check scraper is present
ls /opt/market-research-agent/skills/facebook_scraper.py

# 3. Confirm working directory
cd /opt/market-research-agent/
```

If any claude/python3 process found running → alert Marina BEFORE starting new process.

---

## Scraper Command — Keyword-First Deep Scan

```bash
cd /opt/market-research-agent/

# Standard deep scan (150-200 ads per keyword):
python3 skills/facebook_scraper.py \
  --deep \
  --since=2026-01-01 \
  --seen=memory/seen-advertisers.md \
  "baby"

# Output saved automatically to:
# /opt/market-research-agent/logs/facebook_ads_YYYY-MM-DD_HH-MM.json
# Screenshots saved to:
# /opt/market-research-agent/logs/screenshots/
```

**Confirmed capacity:** 500–580 ads/keyword (target 500, hard cap 600).
Requires: fb_session.json (logged-in session) + window.scrollBy fix in scraper.
Do NOT increase beyond 600 — diminishing returns + FB detection risk.

---

## FB Ads Library — Filter Parameters (hardcoded in scraper)

These are applied automatically by `facebook_scraper.py`:

| Parameter | Value | How applied |
|-----------|-------|-------------|
| Country | US | `country=US` in URL |
| Status | Active only | `active_status=active` in URL |
| Date from | 2026-01-01 | `--since=2026-01-01` flag → `start_date[min]` in URL |
| Language | English | browser locale `en-US` in Playwright context |
| Media type | All (or video) | `--video` flag for video-only |

---

## Sort Options — ✅ VERIFIED ON VPS (2026-05-15)

Two sort options confirmed from live FB Ads Library UI screenshot:

| Sort option | Exact UI label | What it shows | Priority |
|-------------|---------------|---------------|----------|
| Sort A | **"Most recent"** | Newest ad launches first → catches fresh 2026 entrants | **Run FIRST** |
| Sort B | **"Impressions: high to low"** | Highest impression count first → proven winners (default FB sort) | Run second |

**How to apply in scraper:** `--sort=recent` or `--sort=impressions` (see scraper flags below)

**If UI labels change:** Stop. Do not guess. Alert Marina with screenshot.

---

## Output Files

```
logs/facebook_ads_YYYY-MM-DD_HH-MM.json   ← raw scraper output
logs/screenshots/                          ← debug screenshots
outputs/scans/                             ← processed scan results
```

---

## Rules

1. VPS is MANDATORY before any FB Ads Library work — no exceptions
2. WebSearch cannot access FB Ads Library — only Tier 3 signals
3. If VPS unreachable → tell Marina exact error. Do NOT substitute WebSearch.
4. If scraper process already running → do NOT start second one
5. Read memory/seen-advertisers.md before each run (--seen flag)
