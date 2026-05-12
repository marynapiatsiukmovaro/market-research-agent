# DAILY SCOUT WORKFLOW

## Daily Target
- Scan: 15–20 product candidates
- Filter: apply mandatory filters (fast reject)
- Score: score remaining candidates
- Output: 5 best products in Scout Mode format (minimum 3, quality over quantity)

## Step-by-Step

### STEP 0 — Load Memory (before scanning anything)
Read `memory/accepted-products.md` and `memory/rejected-products.md`.
- Note all product names and categories already found
- Do NOT report any product already in accepted-products.md
- Use rejected-products.md patterns to skip similar weak products faster
- This step prevents duplicates across sessions

### STEP 1 — Scan Sources (15–20 candidates)
- TikTok Ads Library: search trending categories
- Meta Ads Library: check active ads in target niches
- Amazon Movers & Shakers: top gainers today
- AliExpress trending: new arrivals with momentum
- TikTok organic: #tiktokmademebuyit, trending products
- Skip any product already in memory

### STEP 2 — Apply Mandatory Filters
- Check each candidate against `criteria/mandatory-filters.md`
- Reject fast — do not over-analyze weak products
- Target: 8–10 pass filters out of 15–20 scanned

### STEP 3 — Score Filtered Products
- Apply `criteria/scoring-system.md`
- Add competitor ad activity check
- Add creative angle count estimate

### STEP 4 — Find Source Links
For each candidate scoring 65+:
- Find real Ad/Source Link (where it was found)
- Find real Store Link (where it is sold)
- If a link cannot be found after a genuine search → write "Not found", do NOT guess or invent a URL
- Missing both links → set Recommendation to "Needs Verification"

### STEP 5 — Select Top Products
- Rank by score
- Minimum score to include: 65+
- Target 5 products. If fewer than 5 score 65+, output what genuinely qualifies — do NOT lower the bar to fill the quota
- If fewer than 3 qualify → note this in the report and explain why

### STEP 6 — Output Scout Mode Reports
- One report per product (use `brain/system.md` output format)
- Save to `outputs/daily-reports/YYYY-MM-DD.md`

### STEP 7 — Save to Notion
- Follow `workflows/notion-update.md`
- One Notion entry per accepted product

### STEP 8 — Update Memory (mandatory, do not skip)
After every session, update memory files:

**`memory/accepted-products.md`** — add each reported product:
- Date, Product name, Category, Score, Key hook, Source

**`memory/rejected-products.md`** — add notable rejections:
- Date, Product name, Reason rejected

**`memory/successful-patterns.md`** — if you noticed a recurring winning trait, add it

**`memory/failed-patterns.md`** — if you noticed a recurring weak pattern, add it

Memory update is not optional. It is what makes the agent smarter over time.

## Frequency
Daily. Run each morning before market activity increases.
