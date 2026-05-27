# NOTION CONFIGURATION

## Database: Product Tracker
Location: MOVARO HQ → 📦 Product Research → Product Tracker
- **Database (page) ID:** `35b53ba8-196e-80bf-9be2-e6a4eb49059e`
- **Data source ID (collection) — pass THIS as `data_source_id` to the Notion `create-pages` MCP tool:** `35b53ba8-196e-8006-83fc-000bd9676ed9` (verified working SH-7/SH-8; the page-id above is NOT accepted as a data_source_id).

---

## Field Schema

> **⚠ VERIFIED AGAINST LIVE DB 2026-05-27 (SH-9) — read before any Notion write:**
> The live data source was fetched and reconciled. Discrepancies that WILL break `create-pages`/`update-page`:
> - **NO `Status` field exists** (only **`Test Status`** Not Started/Testing/Scaling/Killed). Do NOT send `Status`. New scouted products simply omit it.
> - **`Price Range` options use EN-DASH and exact strings:** `$45–79` · `Extended $39–100` · `Premium $100–170` · `Too Cheap` (a stray hyphen dupe `Extended $39-100` also exists — do not add more). Sending `Fits $45-79` etc. creates junk duplicate options.
> - **NO `Supplier Link`, `CTR`, `CPM` fields** in the live DB (there is one unnamed number field `""`). Do not send them.
> - **`Source` and `Ad Platform` are TEXT** (free text), not Select — any string is accepted.
> - **`Date Added` is a date** → send expanded key `date:Date Added:start` = `YYYY-MM-DD` (NOT a flat `Date Added`).
> Everything else below matches the live schema. The rows below are the intended USAGE; where they conflict with this block, this block wins.

| # | Field | Type | Options / Notes |
|---|-------|------|-----------------|
| 1 | Title | Title | Product name |
| 2 | Score | Number | 0–100 |
| 3 | Recommendation | Select | Worth Testing / Needs Verification / Rejected |
| 4 | Founder Review | Select | Approved / Consider / Watchlist / Rejected — **set by Marina only, never by agent** (see Founder Review — Definitions) |
| 5 | Category | Select | Beauty / Health / Fitness / Home / Kitchen / Pet / Tech / Other |
| 6 | Price | Number | Actual retail price in $ |
| 7 | Price Range | Select | EXACT (en-dash): `$45–79` / `Extended $39–100` / `Premium $100–170` / `Too Cheap` |
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
| 18 | ~~Status~~ | — | ❌ NOT in live DB — do NOT send. (Only `Test Status` exists, field #22.) |
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
| 30 | SH Link | URL | **ShopHunter dept ONLY** — link to the store's ShopHunter page (or "-" if not found). |
| 31 | SH Store Created | Text | **ShopHunter dept ONLY** — store creation date literal from ShopHunter (or "N/A"). |
| 32 | SH Rev W/M | Text | **ShopHunter dept ONLY** — store revenue week / month (estimate). |
| 33 | SH SKU/Country | Text | **ShopHunter dept ONLY** — SKU count / country. |

> **⚠ Department-scoped fields (added 2026-05-24, Session SH-2):** the four `SH *` fields (30–33) are filled
> **ONLY by the ShopHunter department.** The **Facebook Ads Library agent does NOT touch them — always leave blank.**
> They carry ShopHunter store-intelligence and are irrelevant to products sourced via Facebook Ads Library.
> Each field's Notion description repeats this. ShopHunter-discovered products use Source = "ShopHunter";
> never rewrite the Source of existing FB/TikTok/WebSearch/Amazon products.

---

## Founder Review — Definitions

**4 tiers** (traffic light + a study/radar tier — Watchlist added SH-6, 2026-05-26 by Marina):

| Value | Color | Meaning |
|-------|-------|---------|
| *(blank)* | — | Not yet reviewed by Marina. Default for all new products. |
| Approved | 🟢 green | Marina is truly willing to test NOW. Rare, ultra-high-signal. |
| Consider | 🟡 yellow | Genuinely **EVALUATING TO LAUNCH** — Marina's real shortlist she'd actually test. Keep this tier clean (launch-candidates only — NOT a "tracking" bucket). |
| Watchlist | 🔵 blue | Valid/proven **SIGNAL** or interesting to **STUDY**, but **NOT the business model right now** → keep on radar, **MAY RETURN**. No Rejection Reason; **NOT archived; category stays OPEN (keep monitoring)**. For validated-but-off-model finds (e.g. titanium boards/cookware convergence) + "won't sell but want to study the store" (ad-research assets). |
| Rejected | 🔴 red | Strong, clear objective failure (везде / unverifiable result / overheated market / weak economics) → Rejection Reason + Archive. Do NOT use for uncertain products — leave blank or **Watchlist**. |

> **Consider vs Watchlist (the key distinction):** Consider = "I'd actually launch this" (clean shortlist); Watchlist =
> "good signal / worth studying, but not for me now — keep on radar." Convergence/revenue alone earns at most **Watchlist**,
> never auto-Consider. The dashboard/shortlist view shows **Approved + Consider only** (Watchlist/Rejected excluded = no noise).

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

### View 2: "💡 Shortlist" (linked view, separate page)
Filter: Founder Review = Approved OR Consider
Visible: all columns including Founder Notes, Why It May Work, Problem Solved, Test Status, CTR, CPM
Sort: Score descending
Purpose: Marina's clean **LAUNCH SHORTLIST** — only products she'd actually test (Approved + Consider). Watchlist + Rejected stay OUT to keep it noise-free. (SH-6: this is exactly why Watchlist was added — to de-noise this view.)

### View 3: "🔵 Watchlist / Radar" (linked view)
Filter: Founder Review = Watchlist
Visible: Title, Score, Category, Price Range, Competitor Signal, Notes, Date Added
Sort: Score descending
Purpose: validated/interesting-but-off-model finds to MONITOR + possibly revisit (titanium boards, ad-research stores, etc.). Category stays OPEN — never closed/archived. (Recommended — create in Notion if not present.)

### View 4: "🗄 Archive" (permanent rejected record)
Filter: Recommendation = Rejected OR Founder Review = Rejected
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
