# NOTION UPDATE WORKFLOW

For each reported product (score 65+), create one Notion database entry with two parts:
1. **Database properties** (fields in the table view)
2. **Page body** (internal card — opened when clicking the row)

---

## Part 1 — Database Properties (Table Fields)

### Fields agent fills

| Field | Value |
|-------|-------|
| Title | Product name |
| Score | 0–100 |
| Recommendation | Worth Testing / Needs Verification / Rejected |
| Category | Beauty / Health / Fitness / Home / Kitchen / Pet / Tech / Other |
| Price | Actual retail price in $ |
| Price Range | Fits $45-79 / Extended $39-100 / Premium $100-170 / Too Cheap |
| Saturation | Low / Medium / High / Extreme |
| Competitor Signal | None / Testing / Scaling / Saturated / Legacy Winner |
| Ad Platform | Meta / TikTok / Both / Organic only |
| Source | Standardized value only: Facebook Ads Library / Amazon Search / TikTok Search / TikTok Shop / Minea / Web Search / AliExpress / Alibaba |
| Discovery Keyword | Exact search query or discovery path (e.g. "travel pillow Facebook ads", "neck pain TikTok 2026") |
| Emotional Trigger | 1–3 words |
| Creative Angles | Number (e.g. 4) |
| Ad Link | Direct URL to ad or original source — "Not found" if unavailable |
| Store Link | URL of store/site where product is sold — "Not found" if unavailable |
| Store Link 2 | 2nd store URL — ONLY for convergence/parallel candidates (2nd brand selling the same product). Leave empty otherwise. See Convergence rule below. |
| Date Added | Today's date |
| Status | Scouted |
| Notes | Short observations: risks, warnings, anomalies — 1 sentence max per note (e.g. "High saturation", "Medical claims risk") |
| Rejection Reason | 1 sentence — only when Founder Review = Rejected |
| Supplier | Short feasibility note — hidden in Inbox view |
| Supplier Link | Alibaba / AliExpress listing URL — hidden in Inbox view |
| Social Link | TikTok / Instagram post URL — hidden in Inbox view |
| Problem Solved | 1 sentence max — hidden in Inbox view |
| Why It May Work | 2–3 bullet points — hidden in Inbox view |

### Fields Marina fills (agent leaves blank — always)

| Field | Notes |
|-------|-------|
| Founder Review | Marina sets: Approved / Consider / Rejected — never set by agent |
| Founder Notes | Marina's strategic judgment and intuition — never written by agent |
| Test Status | Marina sets when product moves to testing |
| CTR / CPM | Filled after real test data |

### Source Verification Rule
- Ad Link + Store Link both present → Recommendation as scored
- Only one link present → acceptable, note which is missing
- Both missing → set Recommendation to **"Needs Verification"** regardless of score
- Never invent or guess URLs — only real, working links

### Convergence / Parallel Candidates Rule (added S30 — Marina request)
When 2+ DISTINCT brands sell essentially the same product (category convergence — e.g. Desk Nest + Ergo Purrch desk-mounted cat bed):
- Report as ONE primary reportable product, BUT make EVERY brand visible — never let a 2nd brand hide only in the body.
- **Store Link + Store Link 2 fields (BOTH table-visible, clickable):** put brand #1 in `Store Link` and brand #2 in `Store Link 2`. Both render as clickable columns in the table, so Marina sees BOTH stores at a glance without opening Notes (a url field holds only ONE link — that's why a 2nd url column exists, added S30). A populated `Store Link 2` is itself the visual signal "this row has 2 brands".
- **Notes field:** start with `CONVERGENCE — N брендов:` and list each brand + URL + key differentiator (price tier, positioning, review count). For 3+ brands, the 3rd+ links live here + in the body.
- **Page body:** add a `### Convergence brands (N — оба под анализ)` section listing each brand with its store link and 1-line positioning, so Marina can open and analyze each separately.
- **When to split into a SEPARATE Notion card instead of bundling:** if a 2nd brand is materially different enough to be its own test candidate — distinct price tier (e.g. premium vs budget), distinct mechanism, or distinct positioning Marina would test independently — create a second card and cross-reference both in Notes (`parallel candidate: <other card>`). When unsure → bundle + flag, then ask Marina if she wants it split.
- Goal: Marina must be able to SEE and independently analyze every parallel brand, not just the one in the Store Link column.

---

## Notes Field — What to Write

Short, factual observations only. No analysis.

Good examples:
- High saturation — may be too late to enter
- Medical claims risk — check ad policy before testing
- Seen in many stores already
- Supplier unclear — verify before approving
- Long-running competitor ads (13+ months) — window possibly closed

Bad examples (too long — put in Why It May Work instead):
- "This product has strong wow-factor because it solves neck pain visually..."

---

## Part 2 — Page Body Template (Internal Card)

```
## [Recommendation] — Score: [XX]/100

**Saturation:** [Low/Medium/High/Extreme] | **Competitor Signal:** [value] | **Category:** [X] | **Price:** $[XX]

---

### Problem & Trigger
**Problem Solved:** [1 sentence]
**Emotional Trigger:** [1–3 words]

---

### Why It May Work In Ads
- [Hook / visual angle]
- [Audience fit]
- [Impulse-buy factor]

### Creative Angles ([X] total)
1. [e.g. Problem/Solution]
2. [e.g. Transformation / Before-After]
3. [e.g. Social proof / UGC reaction]

---

### Market Evidence
**Competitor Signal:** [None / Testing / Scaling / Saturated / Legacy Winner] — [Platform]
**Signal Detail:** [brief note — number of ads, duration, impressions trend]
**Discovery Keyword:** [exact search query used]

---

### Source Links
- **Source / Ad:** [URL or "Not found"]
- **Store / Where It Sells:** [URL or "Not found"]

⚠️ If either link is missing → "Needs Verification"

---

### Notes
[Short observations, risks, flags — 1 sentence each]

---

### Rejection Reason
[Only when Founder Review = Rejected — 1 sentence]
```

---

## Formatting Rules
- Recommendation + Score + Saturation + Competitor Signal always at the top — instant signal
- No long paragraphs in table fields
- ⚠️ in title for Needs Verification
- Rejected products: Rejection Reason only when Founder Review = Rejected; Why It May Work / Problem Solved can be left blank for rejected products
- Founder Notes is Marina's field — never written by agent

---

## Archive View
Rejected products remain permanently in the database.
Visible in Archive view (Filter: Recommendation = Rejected).
Purpose: anti-pattern memory, duplicate prevention, saturation calibration.
Never delete rejected products.
