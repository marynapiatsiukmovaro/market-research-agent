# DAILY SCOUT WORKFLOW

## Daily Target
- Scan: 15–20 product candidates
- Filter: apply mandatory filters (fast reject)
- Score: score remaining candidates
- Output: 2–5 best products in Scout Mode format (quality over quantity — never force weak products to fill quota)

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
- Target 2–5 products. If fewer than 2 score 65+, output what genuinely qualifies — do NOT lower the bar to fill the quota
- If nothing qualifies → note this in the report and explain why
- If more than 5 score strongly → include all of them (no hard upper limit)

### STEP 6 — Output Scout Mode Reports
- One report per product (use `brain/system.md` output format)
- Save to `outputs/daily-reports/YYYY-MM-DD.md`

### STEP 7 — Save to Notion
- Follow `workflows/notion-update.md`
- One Notion entry per accepted product

### STEP 8 — End-of-Session Checklist (mandatory, do not skip)

**1. Save accepted products** → `memory/accepted-products.md`
- Add one row per reported product: Date, Product, Category, Score, Key Hook, Source

**2. Save notable rejections** → `memory/rejected-products.md`
- Add products that looked promising but failed for a non-obvious reason
- Skip trivially weak products — only log rejections with a lesson

**3. Update patterns if new insight emerged**
- `memory/successful-patterns.md` — recurring winning trait found today
- `memory/failed-patterns.md` — recurring weak pattern found today
- Only update if something new was discovered — don't repeat existing entries

**4. Mark unverified links**
- Any product missing real source links → set Verification to "Needs Verification ⚠️"
- Do not leave blank link fields — write "Not found" explicitly

**5. Save session report**
- Save output to `outputs/daily-reports/YYYY-MM-DD.md`
- Include product count, top scorer, and any notable patterns

**6. Prevent duplicates in next session**
- Confirm accepted-products.md is updated before closing
- Next session STEP 0 will read this file — it must be current

Memory update is not optional. It is what makes the agent smarter over time.

## Frequency
Daily. Run each morning before market activity increases.
