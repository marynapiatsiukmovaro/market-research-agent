# NOTION CONFIGURATION

## Database: Product Tracker
Location: MOVARO HQ → 📦 Product Research → Product Tracker
Data source ID: 35b53ba8-196e-8006-83fc-000bd9676ed9

---

## Field Order (table view + opened page — same sequence)

| # | Field | Type | Notes |
|---|-------|------|-------|
| 1 | Recommendation | Select | High Priority / Worth Testing / Medium Potential / Needs Verification / Rejected |
| 2 | Saturation | Select | Low / Medium / High / Extreme |
| 3 | Score | Number | 0–100 |
| 4 | Title | Title | Product name |
| 5 | Price | Number | Actual retail price in $ |
| 6 | Category | Select | Beauty / Health / Home / Fitness / Kitchen / Pet / Tech / Other |
| 7 | Price Range | Select | Fits $39-79 / Too Cheap / Too Expensive |
| 8 | Emotional Trigger | Text | 1–3 words |
| 9 | Problem Solved | Text | 1 sentence max |
| 10 | Ad Platform | Text | Meta / TikTok / Both / Organic only |
| 11 | Creative Angles | Number | count of identified angles |
| 12 | Competitor Ads | Checkbox | yes/no |
| 13 | Source | Text | platform where found |
| 14 | Supplier | Text | short feasibility note |
| 15 | Why It May Work | Text | 2–3 bullet points |
| 16 | Date Added | Date | — |
| 17 | CTR | Number | actual CTR if tested |
| 18 | CPM | Number | actual CPM if tested |
| 19 | Status | Status | Not started / In progress / Done |
| 20 | Ad Link | URL | direct link to ad or original source |
| 21 | Social Link | URL | TikTok / Instagram profile or post |
| 22 | Store Link | URL | where the product is sold |
| 23 | Supplier Link | URL | Alibaba / AliExpress listing |
| 24 | Notes | Text | extra observations |

---

## Source Verification Rule
- Ad Link + Store Link both present → Recommendation as scored
- Only one link present → acceptable, note which is missing
- Both missing → Recommendation = **Needs Verification** (regardless of score)
- Never invent URLs — only real, working links

---

## Formatting Rules
- Scannable in under 10 seconds per entry
- No long paragraphs — concise text only
- Always fill: Score, Recommendation, Saturation (top 3 = instant signal)
- 🔥 in title for High Priority (85+)
- ⚠️ in title for Needs Verification

---

## Status Field Usage
- Not started → newly added, not yet reviewed
- In progress → under evaluation / sourcing check
- Done → decision made (test launched or rejected)
