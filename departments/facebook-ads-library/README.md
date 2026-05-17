# Facebook Ads Library Department

This department handles product discovery through direct Facebook Ads
Library scanning via VPS scraper.

## What this department does
- Keyword-First Deep Scan via FB Ads Library
- 500 ads per keyword (hard cap 600) via `methods/facebook_scraper.py`
- Anti-duplicate dedup via `operational-memory/seen-advertisers.md`
- Founder taste calibration via `operational-memory/founder-taste.md`
  and `operational-memory/founder-feedback.md` (these live inside this
  department while taste is still being calibrated — will move to
  `shared/` once stabilized)

## What this department does NOT do
- TikTok Ads Library (future sibling department)
- Instagram Reels search (future sibling department)
- Amazon scraping, Pinterest, Reddit (out of scope for this department)

## Entry points
- Pre-flight check: `pre-flight.md` (VPS connection, FB session, scraper sanity)
- Full session workflow: `workflow.md`
- Active hypothesis: `hypotheses/_active.md` → links to current research direction

## Rules from core/ that this department must follow
- `core/mandatory-filters.md` — hard rejection logic
- `core/scoring-system.md` — 0–100 scoring
- `core/product-requirements.md` — price tiers and product requirements
- `core/operating-rules.md` — Tier signals, anti-hallucination, pivot rules
- `core/session-health-rules.md` — quality monitoring and self-reporting

## Shared resources this department uses
- `shared/notion-schema.md` — Notion DB structure
- `shared/notion-workflow.md` — how to save findings to Notion
- `shared/reported-products.md` / `shared/rejected-products.md` — product logs
- `shared/skills/*` — analysis methods (wow-factor, UGC, sourcing, etc.)
