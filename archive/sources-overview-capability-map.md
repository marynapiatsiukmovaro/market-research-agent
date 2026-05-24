# ARCHIVED — Sources Capability Map (legacy, pre-FB / debug-era)

**Archived:** 2026-05-24 (Session 30 cleanup) from `shared/sources-overview.md`.
**Reason:** Facebook department is operationally mature; these detailed capability/debug descriptions
(Minea, WebSearch, WebFetch, TikTok, Amazon) are no longer needed in hot per-session context.
Discovery is FB-only. Kept as historical record. The genuinely operational nuggets
(Marina's 2-weeks-converts rule, store-link check, Meta=VPS) were retained in sources-overview.md.

---

# CAPABILITY MAP (originally config/sources-capability-map.md)

# SOURCES CAPABILITY MAP
# What the agent can ACTUALLY do with each source

Honest map of agent capabilities per source.
Read before each session. Update after new experiences.

---

## MINEA

### Capabilities
- Login via Playwright (headless Chromium) ✅
- Navigate to Meta Ads Library: `https://app.minea.com/en/ads/meta-library` ✅
- Read ad cards as text (`.virtuoso-grid-item`) ✅
- Extract: brand, active ad count, impressions, store URL ✅
- Save screenshots for debugging ✅

### Limitations
- Category filter via UI (filter buttons) — not yet implemented
- Geo filter (US) — not yet implemented
- Cannot view actual ad videos — text card only
- Cannot get CTR, CPM, spend data — Minea does not expose this on free tier
- Cannot scroll deep (currently ~10 cards per load)

### Key Lessons (Session 2, 2026-05-13)
- WITHOUT a category filter, scraper pulls EVERYTHING: jewelry, clothing, dog food
- 10 products scanned = 0 passed filters for exactly this reason
- Health/Beauty category URL parameter needs to be found and hardcoded in scraper
- Virtual scroll: cards load progressively — scrolling required for 20+ cards

### Backlog
- [ ] Find URL parameter for Health/Beauty category filter in Minea
- [ ] Add US market filter (country=US)
- [ ] Increase scroll depth for 20+ cards
- [ ] Add store URL availability check before reporting

### How to Read a Minea Card — Key Fields

```
[Brand name]
15 active ads        ← active ad count (FILTER: 5–30 = sweet spot)
/ 3.2k               ← total impressions
14d Active           ← days the ad has run without stopping
28 Apr 2026          ← launch date (calculate: how many days ago?)
Today                ← last activity
```

**Marina's core rule (2026-05-13):**
> "Если реклама работает 2 недели подряд — продукт КОНВЕРТИТ."
> ("If an ad runs 2 weeks straight — the product CONVERTS.")
> Nobody spends money on ads for 2 weeks without sales.
> Active running ad = proof of market via someone else's budget.

**Filtering priority:**
1. First: how many days active? (≥7 days = interesting, ≥14 = strong)
2. Then: how many active ads? (5–30 = sweet spot)
3. Then: category (Health/Beauty/Fitness + US market)
4. Then: verify store URL

### Login Status (2026-05-13)
- Email: mylovee.store22@gmail.com (from .env)
- Login: WORKING ✅
- Issue resolved: `wait_for_url` redirect detection added

---

## WEBSEARCH (Browser Search)

### Capabilities
- Search any query — returns page titles + snippets ✅
- Find articles like "Best products 2026", "trending TikTok 2026" ✅
- Extract figures: view counts, review counts, prices from article quotes ✅
- Fast (seconds)

### Limitations
- Cannot open TikTok, Instagram, Facebook directly (require login)
- Cannot view real ads in Meta/TikTok Ads Library
- Cannot check "how many active ads right now" — only what articles report
- Cannot watch videos

### Attribution Honesty — CRITICAL
When WebSearch finds an article that MENTIONS TikTok Ads Library:
- DO NOT WRITE: "according to TikTok Ads Library, the product has X views"
- WRITE: "WebSearch mention — article reports X views"
Distinction is fundamental: we were not in TikTok Ads Library, we read someone else's article.

### Good Search Patterns (worked in Session 2)
- `"[product] TikTok viral 2026 Facebook ads reviews Amazon"`
- `"[brand] price Amazon reviews 2026 competitors"`
- `"winning beauty device 2026 $49 $59 $69"`
- `site:amazon.com [product] reviews bestseller`

### Bad Search Patterns (did not work)
- Too generic ("health product winning") — returns SEO junk
- Searching "active ads count" — this data is not publicly indexed
- Queries with "NOT saturated" — Google ignores the NOT operator

---

## WEBFETCH (Opening a Specific URL)

### Capabilities
- Read text from a specific page (Amazon product page, brand site, review article) ✅
- Extract: price, rating, review count, key features ✅

### Limitations
- Amazon product pages often return 500 error — unreliable
- Pages requiring login (TikTok, Instagram, Meta) — will not open
- Cannot access video content on any page

### Mandatory Check (lesson from Session 2)
ALWAYS verify Store Link via WebFetch before reporting:
- Page opens cleanly? → OK
- Error / redirect to strange page? → WARNING, verify manually
- Chrome Safe Browsing flag (dangerous site)? → REJECT immediately

---

## META ADS LIBRARY (facebook.com/ads/library)

### Status: ACCESSIBLE via VPS Scraper (Sessions 8+)
- VPS scraper (5.78.217.133) uses Playwright + fb_session.json (Mikhail Piatsiuk account)
- Full access: keyword search, 500+ ads per keyword, active/impressions sort
- Session cookie required — re-export when expired (see op-rules.md RULE 2)
- Full setup and operation: departments/facebook-ads-library/operational-memory/op-rules.md

### Legacy indirect methods (pre-VPS, backup only — Tier 3 signal)
- WebSearch: `site:facebook.com/ads/library [product]` — surface-level only
- Minea — aggregates Meta ads (no direct access)
- AdSpy, BigSpy — alternatives (not connected)

---

## TIKTOK ADS / TIKTOK SHOP

### Status: NOT DIRECTLY ACCESSIBLE
- TikTok requires login
- TikTok Creative Center (partially public) — worth exploring

### How to Get Data Indirectly
- WebSearch: `site:tiktok.com [product]` — shows public videos
- WebSearch: `[product] TikTok views viral 2026` — articles with figures
- Minea includes TikTok ads on Business plan

---

## AMAZON

### Capabilities (partial)
- WebSearch: `site:amazon.com [product] reviews bestseller` — works ✅
- Amazon Best Sellers pages open via WebFetch (sometimes)
- Can extract: review count, rating, price range, product names

### Limitations
- Direct product pages often return 500 error
- No access to Sales Rank history
- No access to "Bought in last month" data

---

## Session 2 Evaluation (2026-05-13) — Honest Assessment

| Aspect | Score | Notes |
|--------|-------|-------|
| Minea technical | 7/10 | Login fixed, data received. No category filter yet. |
| Minea data quality | 2/10 | 0/10 products passed filters — no category filter |
| WebSearch | 6/10 | Found 2 candidates. One had dangerous store URL. |
| URL verification | 3/10 | Did not check beambo.com before reporting — error |
| Final products | 1 approved (HF Wand 77) out of 2 | Acceptable |
| Session duration | Long | Much time lost fixing technical issues |

---

## Requirements for an Ideal Next Session

### Technical Fixes (backlog)
1. Minea: add Health/Beauty category filter to URL
2. Minea: add US market filter
3. Minea: increase scroll depth to 20+ cards
4. run_scout.sh: test su-scout claude call end-to-end
5. Store URL checker: WebFetch every found URL before reporting

### Documentation (to create)
- [ ] `shared/search-patterns.md` — best search queries by category
- [ ] `shared/url-blacklist.md` — domains with known issues (beambo.com, etc.)
- [ ] `shared/successful-patterns.md` — what actually worked

### Specialist Agents (future architecture)
- **Facebook Agent** — Playwright FB login, Ads Library access
- **TikTok Agent** — TikTok Creative Center scraper
- **Minea Agent** — current scraper + category filter
- **Discovery Agent** — WebSearch + new sources
- **Connector Agent** — aggregates results from all agents, applies Marina's filters, sorts by score, sends to Notion
