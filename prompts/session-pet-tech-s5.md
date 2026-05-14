# SESSION START — Pet Tech / Pet Comfort Vertical Deep Dive

## Context
This is a structured vertical research session, not random product hunting.
Goal: build category-level intelligence on Pet Tech / Pet Comfort,
identify 2–5 scalable impulse-buy products, and establish reusable keyword maps for this vertical.

Previous signal: KittySpout (stainless steel cat water fountain, score 77, Consider)
confirmed that Pet Tech supports $39+ pricing and strong Meta ad behavior.

## Load First (mandatory, before any work)
Read in order:
1. brain/system.md
2. brain/mindset.md
3. criteria/mandatory-filters.md
4. criteria/scoring-system.md
5. memory/reported-products.md
6. memory/rejected-products.md
7. memory/founder-taste.md
8. memory/founder-feedback.md
9. memory/founder-goals.md
10. memory/session-learnings.md
11. memory/seen-advertisers.md

---

## Facebook Ads Library — Setup

Platform: Facebook Ads Library (via VPS scraper)
Scraper flags for every round:
  --country=US
  --lang=en
  --since=2026-01-01
  --until=2026-05-14
  --seen=memory/seen-advertisers.md

Manual verification (when needed):
  URL: facebook.com/ads/library
  Country: United States
  Language: English
  Ad category: All ads
  Date range: Jan 1 2026 → May 14 2026

---

## Vertical Scope — Pet Tech / Pet Comfort

### In scope (products likely $39+):
- Automatic feeders (cat/dog)
- Cat water fountains (stainless, wireless, faucet-style)
- Pet cameras (indoor monitoring, treat dispensers)
- GPS trackers (dog/cat collar)
- Pet health monitors (activity, sleep, vitals)
- Cat calming / anxiety devices (pheromone diffusers, calming collars with tech)
- Dog training devices (vibration/sound collar, remote trainers)
- Self-cleaning litter boxes (note: likely above $100 ceiling)
- Pet nail grinders / grooming tech
- Automatic laser toys / interactive play devices

### Out of scope (likely $15-35 — skip immediately):
- Pet hair removers, brushes, combs
- Basic leashes, harnesses, collars (non-tech)
- Pet bowls (non-electric)
- Basic toys (no tech)
- Pee pads, litter (consumables)

Pre-check: before running any keyword, estimate likely price range.
If category typically prices below $39 → skip, note in session log.

---

## Round Structure

### Round 1 — Wide Mapping (run first, before anything else)
Goal: map the vertical, find who is advertising actively right now.

Keywords (start here):
  "automatic cat feeder"
  "dog GPS tracker"
  "pet camera"
  "cat calming"
  "dog training collar"
  "pet nail grinder"

Scraper mode: wide (25 ads per keyword)
Command:
  nohup python3 skills/facebook_scraper.py \
    --since=2026-01-01 --until=2026-05-14 \
    --seen=memory/seen-advertisers.md \
    "automatic cat feeder" "dog GPS tracker" "pet camera" \
    "cat calming" "dog training collar" "pet nail grinder" \
    > logs/fb_round1_s5.log 2>&1 &

After Round 1: announce plan for Round 2. Wait for Marina's OK before running.

### Round 1 Checkpoint
Count products with:
  - Active ads ≥ 3
  - Store price $39–$100
  - Account started 2025 or later

If ≥ 3 such products found → proceed to Round 2 on strongest signals
If < 3 → pivot note: flag which keywords were dead, propose new keyword branches

---

### Round 2 — Medium Depth
Goal: deeper look at 3 strongest keyword signals from Round 1.

Select top 3 keywords by signal density (most active fresh advertisers).
Run 50 ads per keyword.

Command:
  nohup python3 skills/facebook_scraper.py \
    --since=2026-01-01 --until=2026-05-14 \
    --seen=memory/seen-advertisers.md \
    --deep \
    "[kw1]" "[kw2]" "[kw3]" \
    > logs/fb_round2_s5.log 2>&1 &

After Round 2: announce plan for Round 3. Wait for Marina's OK.

---

### Round 3 — Deep Dive
Goal: full category map of the single strongest signal.

Run 150–200 ads on 1–2 best keywords.
Extract: all active advertisers, creative counts, account age, price, creative angles.

Command:
  nohup python3 skills/facebook_scraper.py \
    --since=2026-01-01 --until=2026-05-14 \
    --seen=memory/seen-advertisers.md \
    --deep \
    "[best_keyword]" \
    > logs/fb_round3_s5.log 2>&1 &

---

## Signal Detection — What to Look For

### Strong signal (investigate fully):
- Store registered 2024–2025 (not legacy brand)
- 3–15 active creatives (testing phase, not saturated)
- Multiple hook variations (problem/solution, UGC, authority)
- Visual demonstration product (works on video)
- Price $39–$100 confirmed on store
- No 100K+ reviews on Amazon for this exact product

### Creative-first signal:
Investigate even average products if:
- creatives are unusually strong,
- hooks repeat aggressively across multiple advertisers,
- UGC quality is high,
- comments show emotional buying intent,
- advertiser is scaling rapidly despite generic product.

A strong creative on a weak product often means the mechanism is right
but the execution is early — opportunity window may be open.

### Comment signal:
When available, inspect comments for:
- repeated pain points ("my cat never drinks enough water"),
- "where can I buy this?" buying intent,
- emotional reactions (love, surprise, sharing with partner),
- skepticism (signals unverifiable claims — risk),
- refund complaints (signals product fails to deliver),
- obvious fake engagement (100% positive, no questions — red flag).

Comments are unfiltered market research. One real buying-intent comment
outweighs 10 perfect ad metrics.

### Weak signal (skip fast):
- 1–2 ads only, no creative variation
- Store registered before 2022
- Amazon reviews > 50K for the product type
- Price below $39 or above $100
- No visual demonstration possible

### Saturation signal (do not enter):
- 20+ brands running the same product
- Legacy brands dominating (PetSafe, Furbo, Petlibro — established)
- Product has been on Amazon top sellers for 2+ years
- CPM likely $25+ based on ad volume

---

## Pattern Recognition — Track Psychological Mechanisms

Across all products seen in this session, track which emotional mechanisms appear:
- Anxiety reduction (pet is safe, healthy, not alone)
- Convenience automation (feed/water without thinking)
- Guilt reduction (I'm a good owner even when away)
- Safety monitoring (I can see my pet anytime)
- Health reassurance (vet-approved, clinically tested)
- Boredom reduction (pet is stimulated, happy)
- Status / care signaling (I invest in my pet's wellbeing)

Goal: understand WHY products work psychologically, not only WHAT is advertised.
Products that tap multiple mechanisms simultaneously score higher.
Note dominant mechanism for each product in your analysis.

---

## Pivot Rules

### When to pivot keyword:
- Keyword yields 80%+ noise (services, affiliates, unrelated content)
- All active advertisers are legacy brands
- 0 products at $39+ after full scan

### Stop Digging Rule:
If after deep analysis of a keyword branch:
- no fresh advertisers appear (all accounts 3+ years old),
- hooks repeat identically across brands (no creative differentiation),
- no pricing advantage exists (commodity pricing),
- and products feel commoditized (available everywhere at same price),

→ mark this branch as SATURATED, stop exploration, move to next keyword branch.
Do not spend another round confirming saturation you already see.

### When to pivot vertically:
- 3 consecutive rounds across different keywords yield 0 products at 65+
- Category price consistently below $39 across all sub-categories

When pivoting: announce explicitly as PIVOT — [reason] — [new direction].
Do not silently switch direction.

---

## Scoring — Apply criteria/scoring-system.md

Score every product that passes mandatory filters.
Do NOT score products that fail filters — reject immediately with 1-line reason.

Minimum score to report: 65/100
Target score for full analysis: 75+
Score 85+ → deep analysis automatically

---

## Output Format (mandatory)

### In chat — SHORT only:
[Product Name] | Score XX | Worth Testing / Needs Verification
→ [1–2 lines: why it's interesting or what's the risk]

Full product card → Notion only (not in chat)

### Notion entry — for every product scoring 65+:
Fill all fields per config/notion-config.md
Page body: include Problem, Emotional Trigger, Why It May Work, Creative Angles
Language: Russian
Founder Notes / Founder Review: leave blank — Marina fills manually

---

## Round Announcement Protocol

Before each round:
State: keywords chosen + why + what you expect to find.
Wait for Marina's OK before running scraper.

When changing direction mid-session:
State: PIVOT — [reason] — [new direction]

---

## Rejection — Fast Filter Before Scoring

Reject immediately (no scoring needed) if:
- Price < $39 or > $100 (unless exceptional justification)
- Established brand (not white-label sourceable)
- Result unverifiable / pseudoscience
- Only 1 creative angle visible
- General dropship store (multiple unrelated categories)
- Domain already in seen-advertisers.md

---

## End of Session — Mandatory Protocol

Run full Learning Protocol (workflows/daily-scout.md STEP 8):

1. Update memory/seen-advertisers.md — add all reviewed domains
2. Update memory/reported-products.md — add scored 65+ products
3. Update memory/rejected-products.md — add notable rejections + patterns
4. Append new learnings to memory/session-learnings.md if patterns found
5. Append to memory/proposed-core-updates.md if pattern confirmed
6. Save all products scoring 65+ to Notion (workflows/notion-update.md)
7. Git commit all memory file changes

Git commit message format:
  "Scout session 5: [X products found] — Pet Tech vertical, [N] rounds"

---

## Session Health — Self-Monitor

Flag and report to Marina if:
- 4+ consecutive rounds yield 0 products at 65+
- All signals are legacy brands (no fresh advertisers)
- Price floor failing consistently in chosen keyword cluster
- Context approaching limit — summarize and ask how to proceed

---

## Vertical Intelligence — Accumulate This

At end of session, summarize:
- Which keywords had highest signal density
- Which keywords were dead (add to session-learnings.md)
- Price range confirmed for each sub-category found
- Saturation level per sub-category
- Dominant psychological mechanism per product found
- Which creative angles appeared most often
- Whether new emerging sub-categories exist beyond KittySpout's niche

This becomes the Pet Tech category map — reused in future sessions.
