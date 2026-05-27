# WINNER DETECTION ALGORITHM
# How to find a product that is already selling — but not yet saturated

**STATUS: Strategic reference.**
Signal principles and Entry Zone logic are universal and current.
Signals 2–4 (TikTok organic, Amazon BSR, Minea) reflect the original multi-source architecture — primary discovery is now FB Ads Library via VPS scraper.
For the current session algorithm, see `departments/facebook-ads-library/workflow.md`.

Goal: find a product that IS ALREADY SELLING and someone IS ALREADY MAKING MONEY from it —
but it has not spread everywhere yet, and there is still an entry window.

Do NOT invent new products. Do NOT look for what does not exist yet.
Find what is already working — before it becomes saturated.

---

## Core Principle: Ad budget = proof of market

**If someone launched ads 2 weeks ago and they are still running —**
**the product CONVERTS. Otherwise they would have stopped.**

This is the strongest signal in ecommerce. Nobody burns money for 2 weeks straight without returns.
Active ads = working product = entry is viable.

## Entry Zone

| Active Ads | Runtime | What It Means | Action |
|------------|---------|---------------|--------|
| 1–5 | < 1 week | Test, still unclear | Watch |
| **5–30** | **1–4 weeks** | **Converts, not yet saturated** | **ENTER** |
| 30–100 | > 1 month | Working but competition growing | Enter with caution |
| 100+ | Any | Saturated, CPMs high | Too late |

**Marina's sweet spot: 5–30 active ads, launched 1–4 weeks ago.**

---

## Winner Signals — In Order of Reliability

### Signal 1 (STRONGEST): Active ads running 2+ weeks straight

**Logic:** advertiser pays every day → they are getting sales.
This is not a hypothesis. This is a fact confirmed by someone else's budget.

**How to read in Minea:**
```
[Brand]
15 active ads        ← count (5–30 = good)
/ 3.2k               ← impressions (growing = scaling)
14d Active           ← running 14 days WITHOUT stopping = CONVERTS
28 Apr 2026          ← launch date (2–4 weeks ago = sweet spot)
```

**Launch date:** the longer it has run without stopping, the stronger the signal.
14 days continuous = strong. 30+ days = very strong, but check for saturation.

---

### Signal 2: TikTok organic growing in parallel

**Time window:** Organic momentum → paid ads = typically 3–8 weeks. This is your entry window.

**Example pattern:** product appears on TikTok as DIY/review → 500K views → one month later dropshippers launch ads → two months later: saturation.

---

### Signal 3: Amazon BSR Velocity (product climbing rank fast)

**What we look for:** product moved from position #200+ in category to top 50 within the last 30 days.

**How to check (without Jungle Scout):**
- Search: `site:amazon.com [product] bestseller [category]`
- Look for: "Best Seller" badge, "#1 New Release"
- "X bought in past month" — if this number is rising fast

**Trigger:** `#1 New Release` in Health/Beauty + on sale <6 months = early signal.

---

### Signal 4: Minea Sweet Spot (5–30 active ads)

**Marina's rule (from departments/facebook-ads-library/operational-memory/founder-feedback.md):**
> "Нужно заходить на старте тренда, не после." — Marina, 2026-05-13
> ("Enter at the start of the trend, not after.")

**Minea filter:**
- Active ads: **5–30** = enter. 30–100 = caution. 100+ = too late.
- Impressions growing over last 7 days = active scaling signal
- Ad launched recently (<30 days) + already scaling

**How to read a Minea card:**
```
[Brand]
30 active ads        ← 5 to 30 = good
/ 5k                 ← impressions (higher per fewer ads = more efficient)
1d Active            ← ad is active
13 May 2026          ← launch date (recent = good)
```

---

### Signal 5: Premium brand proves the market, generic attacks from below

**Pattern:**
1. A premium brand exists at $150–400 (NuFACE, Renpho, iRestore)
2. They have been selling for years = market is PROVEN
3. Generic with same function at $49–69 = attack from below
4. Key: the generic must LOOK BETTER, not just cost less

**Examples from product log:**
- Eye massager (84): Renpho $69 → our generic $49 ✅ WINNER
- HF Wand (77): NuDerma $79 → our generic $49–59 ✅ Approved
- Laser Hair Cap (80): iRestore $200 → generic $69 ❌ Rejected (unverifiable result)

**Rule:** Result must be visible and verifiable on camera. Without this — do not enter.

---

## Session Algorithm: Correct Sequence

Note: see departments/facebook-ads-library/workflow.md for current algorithm. The sequence below is the original multi-source version, kept as strategic reference.

```
SESSION START
│
├── 1. Read shared/ + departments/facebook-ads-library/operational-memory/ (what was found, what was rejected, Marina's taste)
│
├── 2. TikTok organic — what is viral RIGHT NOW?
│   └── WebSearch: "[category] TikTok viral May 2026 trending"
│   └── Look for: organic without ads, fresh hashtags
│
├── 3. Minea — filter 5–30 active ads + Health/Beauty + US
│   └── Reject everything with 100+ active ads immediately
│   └── Focus on: new brands (<90 days of ads), growing impressions
│
├── 4. Amazon New Releases — what appeared in last 30–90 days?
│   └── Categories: Health/Beauty, Sports & Outdoors, Personal Care
│   └── Filter: 4+ stars, 50–500 reviews (not empty and not oversaturated)
│
├── 5. For each candidate:
│   ├── Check: does Store URL open? No browser warnings?
│   ├── Check: are there competitor ads?
│   ├── Check: price fits $45–79 (priority) or $39–100 with justification?
│   └── Apply mandatory filters (core/mandatory-filters.md)
│
├── 6. Score those that passed (core/scoring-system.md)
│   └── Apply shared/founder-taste.md layer on top of the number
│
└── 7. Report only 65+. Quality over quantity.
```

---

## What To Do With Every New Source

Before pulling data from any source — answer:

1. **Is this real-time data or an article written by someone?**
   - Article → attribute as "WebSearch mention of [source]"
   - Direct data (Minea card) → attribute as "Minea Meta Ads"

2. **How many active ads does this product have right now?**
   - Unknown → Confidence: Low
   - 5–30 → Confidence: High (if other signals also present)

3. **Does the Store Link open and is it safe?**
   - Do NOT report if not verified

---

## Red Flags — Reject Immediately (do not spend time)

- Looks "everywhere" at first glance → stop, do not score
- 100+ active ads → too late
- Unverifiable result ("improves circulation") → stop
- Price under $39 → stop; price $100–170: score normally, Margin Potential cap 5/10; above $170 → reject
- Store URL inaccessible or flagged as dangerous → stop
- Product already in past sessions → stop (duplicate)

---

## For Multi-Agent Architecture (future)

Each agent should return JSON:

```json
{
  "product_name": "...",
  "score": 0,
  "confidence": "High/Medium/Low",
  "discovery_type": "TikTok organic / Minea ad / Amazon velocity / ...",
  "active_ads_count": 0,
  "days_running": 0,
  "store_url": "...",
  "store_url_verified": true,
  "ad_url": "...",
  "price_range": "$XX-$XX",
  "key_signal": "one sentence why this is interesting",
  "marina_risk_flags": []
}
```

Connector Agent takes JSON from all agents, applies Marina's filters, sorts by score, sends to Notion.
