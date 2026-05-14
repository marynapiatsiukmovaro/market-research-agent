# NOTION CONFIGURATION

## Database: Product Tracker
Location: MOVARO HQ → 📦 Product Research → Product Tracker
Data source ID: 35b53ba8-196e-80bf-9be2-e6a4eb49059e

---

## Field Schema

| # | Field | Type | Options / Notes |
|---|-------|------|-----------------|
| 1 | Title | Title | Product name |
| 2 | Score | Number | 0–100 |
| 3 | Recommendation | Select | Worth Testing / Needs Verification / Rejected |
| 4 | Founder Review | Select | Approved / Consider / Rejected — **set by Marina only, never by agent** |
| 5 | Category | Select | Beauty / Health / Fitness / Home / Kitchen / Pet / Tech / Other |
| 6 | Price | Number | Actual retail price in $ |
| 7 | Price Range | Select | Fits $45-79 / Extended $39-100 / Premium $100-170 / Too Cheap |
| 8 | Saturation | Select | Low / Medium / High / Extreme |
| 9 | Competitor Signal | Select | None / Testing / Scaling / Saturated / Legacy Winner |
| 10 | Ad Platform | Select | Meta / TikTok / Both / Organic only |
| 11 | Source | Select | Facebook Ads Library / Amazon Search / TikTok Search / TikTok Shop / Minea / Web Search / AliExpress / Alibaba |
| 12 | Discovery Keyword | Text | Exact search query or discovery path that led to the product |
| 13 | Emotional Trigger | Text | 1–3 words |
| 14 | Creative Angles | Number | count of identified angles |
| 15 | Ad Link | URL | direct link to ad or original source |
| 16 | Store Link | URL | where the product is sold |
| 17 | Date Added | Date | — |
| 18 | Status | Select | Scouted / Under Review / Approved / Archived |
| 19 | Notes | Text | Short agent observations: risks, warnings, anomalies — 1 sentence max per note |
| 20 | Rejection Reason | Text | 1 sentence — filled only when Founder Review = Rejected |
| 21 | Founder Notes | Text | Marina's judgment — set by Marina only, never by agent |
| 22 | Test Status | Select | Not Started / Testing / Scaling / Killed |
| 23 | Problem Solved | Text | 1 sentence — hidden in Inbox view |
| 24 | Why It May Work | Text | 2–3 bullet points — hidden in Inbox view |
| 25 | Supplier | Text | short feasibility note — hidden in Inbox view |
| 26 | Supplier Link | URL | Alibaba / AliExpress listing — hidden in Inbox view |
| 27 | Social Link | URL | TikTok / Instagram profile or post — hidden in Inbox view |
| 28 | CTR | Number | actual CTR if tested |
| 29 | CPM | Number | actual CPM if tested |

---

## Founder Review — Definitions

| Value | Meaning |
|-------|---------|
| *(blank)* | Not yet reviewed by Marina. Default for all new products. |
| Approved | Exceptionally strong product Marina is truly willing to test. Rare, ultra-high-signal. |
| Consider | Strategically interesting — worth tracking. NOT a testing queue. Strategic intelligence memory only. |
| Rejected | Strong, clear objective failure (везде / unverifiable result / overheated market). Do NOT use for uncertain products — leave blank or Consider. |

**Founder Review is NEVER set by the agent.** Agent may include a soft suggestion in the Notes field only.
Founder Notes is NEVER written by the agent. Marina's field only.

---

## Competitor Signal — Market Stage Semantics

| Value | Meaning | Action |
|-------|---------|--------|
| None | No ads found | Higher risk — organic signals only |
| Testing | New ads, early stage, small spend | Watch — may be emerging |
| Scaling | Active ads, recent launch, growing impressions | Enter — sweet spot |
| Saturated | 100+ active ads, many brands, high CPMs | Too late |
| Legacy Winner | Long-running dominant campaigns, window permanently closed | Do not enter |

---

## Source — Standardized Values

Use only these values in the Source field. Do not write long descriptions.
Put query details into Discovery Keyword.

- Facebook Ads Library
- Amazon Search
- TikTok Search
- TikTok Shop
- Minea
- Web Search
- AliExpress
- Alibaba

---

## Notes Field — Rules

Notes = short agent/system observations, risks, warnings, anomalies.

Examples:
- High saturation
- Medical claims risk
- Weak differentiation
- Seen in many stores
- Supplier unclear
- Long-running competitor ads — may be too late

Do not use Notes for analysis. Analysis goes into Why It May Work or Problem Solved subpages.

---

## Notion Views

### View 1: "📥 Inbox" (main operational)
Visible: Title, Score, Recommendation, Founder Review, Category, Price Range, Competitor Signal, Saturation, Ad Platform, Source, Date Added
Hidden: Notes, Founder Notes, Rejection Reason, Problem Solved, Why It May Work, Supplier, Supplier Link, Social Link, Test Status
Sort: Date Added descending

### View 2: "💡 Intelligence" (linked view, separate page)
Filter: Founder Review = Approved OR Consider
Visible: all columns including Founder Notes, Why It May Work, Problem Solved, Test Status, CTR, CPM
Sort: Score descending
Purpose: strategic reference — products Marina has evaluated and approved

### View 3: "🗄 Archive" (permanent rejected record)
Filter: Recommendation = Rejected
Visible: Title, Score, Category, Rejection Reason, Date Added only
Purpose: anti-pattern memory, duplicate prevention, historical calibration
Never delete rejected products.

---

## Source Verification Rule
- Ad Link + Store Link both present → Recommendation as scored
- Only one link present → acceptable, note which is missing
- Both missing → Recommendation = **Needs Verification** (regardless of score)
- Never invent URLs — only real, working links

---

## Status Field Usage
- Scouted → newly added from session
- Under Review → Marina is evaluating
- Approved → Founder Review set, ready to test
- Archived → rejected or no longer active

---

## Test Status Usage
- Not Started → product approved, testing not yet begun
- Testing → active ad test running
- Scaling → test positive, scaling spend
- Killed → test concluded, product not pursued further (final decision)
