# KEYWORD MAP — TESTED KEYWORDS SCORECARD

**Purpose:** Track all tested keywords with verdict and signal. Consult before planning next session's keyword strategy.
**Read when:** planning keyword selection. NOT mandatory read every session (unlike op-rules.md and learnings.md).
**Updated:** add 1-2 rows per keyword tested this session (in STEP 8).

---

## Meta Rules — Keyword Types

**Product-specific (2 words):** "baby carrier", "screen time" → HIGH yield (1-3% → reportable). Best for direct product discovery. Prefer these.

**Situation keywords:** "long flight", "road trip" → LOW yield (0.3-0.5%) is NORMAL and expected. Value = unusual category intersections you couldn't predict. Do NOT judge session by yield. Do NOT abandon mid-session because of noise.

**Broad / single-word:** "baby", "kids" → HIGH noise (80%+ irrelevant). Use only for category landscape mapping, not direct product discovery.

**Attribute keywords:** "learning toy", "Montessori toy" → FB matches any ad containing the words — not a product category. Low yield. Replace with specific product names.

**Offer/promo keywords (DEAD class):** "50% off today", "buy 1 get 1 free", "half off" → ❌ CONFIRMED DEAD for DTC physical products $39-99. Attract retail with seasonal discounts, jewelry, apparel, supplements. S16: 590 advertisers across 3 promo keywords → 0 reportable products. Avoid entire class. Also: "%" symbol breaks FB URL encoding → always use word alternative ("half off" not "50% off").

---

## Keyword Scorecard

| Keyword | Session | Ads | Verdict | Best Signal / Key Finding |
|---------|---------|-----|---------|--------------------------|
| baby carrier | S8 | 561 | ✅ USE | Bambora 73 — open DTC entry window; WildBird exited to retail |
| baby monitor | S8 | 576 | ❌ DEAD | Owlet, Nanit legacy tech dominate; no DTC opening |
| nursing pillow | S8 | ~25 | ⚠️ RETRY [BUG: S18 scroll fix] | Low count = scraper early-stop bug; needs re-run with fixed scraper |
| stroller | S8 | partial | ⚠️ RETRY | Hoppie 65 found; needs full 500-ad session |
| sleep baby | S9 | 267 | ⚠️ NARROW | 2 borderline at 66-67; retry as "sleep sack baby" or "baby swaddle" |
| baby | S9 | 349 | ❌ LAST RESORT | 35% big brands + pharma; use only with recent sort, not impressions |
| toddler | S9 | 327 | ❌ REPLACE | Replace with product-specific (e.g., "potty training", "toddler chair") |
| child safety | S9 | 327 | ❌ DEAD | 60% local services + pharma; zero DTC physical products |
| mom life | S9 | 375 | ❌ DEAD | UGC/affiliate heavy; established FMCG; 0 reportable |
| kids | S9 | 53 | ❌ DEAD [BUG: S18 scroll fix] | Count unreliable (scroll bug); FMCG noise confirmed in visible ads; verdict ❌ likely holds but count was understated |
| Montessori toy | S9 | 81 | ❌ REPLACE | Dropship/established; retry as "busy board", "wooden stacking toy" |
| sensory toy | S9 | 198 | ❌ ADULT | 45%+ adult stress products; retry as "baby sensory toy" |
| potty training | S9 (via toddler) | — | ⚠️ PRICE | 3 active DTC brands, but $7-37 — below price floor |
| screen time | S10 | 313 | ✅ USE | Camp Snap 77; Thoson 67; "screen-free" = strong parent hook |
| learning toy | S10 | 247 | ❌ DEAD | Attribute keyword; retail + subscription; 0 reportable |
| long flight | S10/11 | 314 | ⚠️ SITUATIONAL | Travel Nest 72 found; good intersection keyword |
| rainy day | S10/11 | 370 | ❌ DEAD | Generic domestic situation; no acute pain; 0 reportable |
| bored kids | S13 | 266 | ✅ USE | Wonder Quest 70; seasonal peak April-May |
| keep kids busy | S13 | 362 | ❌ DEAD | Subscription economy dominates; 0 DTC physical products |
| screen free | S13 | 294 | ⚠️ VALIDATION | Confirms Camp Snap + Thoson; ironic app noise; NOT for new discovery |
| quality time | S14 | 44 | ❌ DEAD [BUG: S18 scroll fix] | Count unreliable (scroll bug); abstract phrase verdict likely holds but needs re-test with fixed scraper |
| connect with your | S14 | 163 | ❌ DEAD | B2B/service keyword; 0 DTC physical products |
| road trip | S14 | 348 | ⚠️ SITUATIONAL | 2 category signals: baby car sun shade + car seat cushion; retry S21 |
| say goodbye to | S15 | 375 (no filter) / 418 (--since=2026-01-01) | ⚠️ LOW YIELD | 1 reportable (Heusom 71 pet grooming); ~60% service/beauty/supplement noise; date filter did NOT reduce noise (418 > 375); strong DTC operators present but diluted |
| game changer | S15 | 363 | ✅ USE | 1 reportable (Dermave 69 women's trimmer); Beddy's zipper bedding category signal; mix of all DTC categories — broad-spectrum performance keyword |
| tiktok made me buy | S16 | 277 | ❌ DEAD | Social-proof phrase; 90% personal brand/influencer content; 0 DTC physical products |
| 50% off today | S16 | 69 | ❌ DEAD | Promo-phrase too narrow (time modifier "today"); FB exhausts phrase in 45s; 0 reportable |
| buy 1 get 1 free | S16 | 164 | ❌ DEAD | BOGO signal = jewelry/apparel/supplements; Blumi Baby swim goggles ~62 (below threshold); 0 reportable |
| half off | S16 | 357 | ❌ DEAD | Discount phrase = retail/apparel/seasonal; "50% off" unusable (% breaks URL encoding); 0 reportable |
| genius gadget | S17 | 121 | ❌ DEAD [BUG?: S18 scroll fix] | May have stalled early; mass-clone dropship + mosquito affiliates confirmed in visible ads; verdict ❌ likely holds but re-test recommended |
| gift idea | S18 | 304 | ❌ DEAD | Gift-occasion phrase = personalized/custom gift services dominate; no white-label DTC physical products |
| perfect gift | S18 | 313 | ❌ DEAD | Gift-occasion class confirmed (re-tested with fixed scraper); 70% custom/personalized gifts, 20% established brands, 0 white-label DTC $39-99 |
| back in stock | S18 | 0 [BUG: scroll fix] | ⚠️ RETRY | Scroll bug confirmed — 0 ads = page not loaded, NOT keyword limit; re-run with fixed scraper |
| gadget | S17 | 296 | ❌ DEAD | Ultra-broad: established brands (FIXD, REVO, HexClad), commodity below $39, пустышки; 0 reportable |
| tired of | S17 | 427 | ❌ DEAD | Broad emotional hook attracts ALL advertiser types — services, clinics, apps, beauty; 0 DTC physical products; confirms S3 WebSearch pattern |

**Verdict codes:** ✅ USE | ❌ DEAD | ⚠️ RETRY / NARROW / SITUATIONAL / VALIDATION / PRICE / ADULT

---

## Priority Queue — Sessions 15+ Broad Horizontal Discovery

**Strategy:** Performance advertising signal keywords — attract DTC/dropship operators across ALL niches.
These keywords filter by ADVERTISER TYPE (aggressive D2C performance marketers), not by product topic.

**30 keywords for broad discovery phase (Sessions 15-25):**

| # | Keyword | Type | Status |
|---|---------|------|--------|
| 1 | struggling with | Pain hook | — Not tested |
| 2 | tired of | Pain hook | ✅ S17 — ❌ DEAD |
| 3 | say goodbye to | Pain hook | ✅ S15 — ⚠️ LOW YIELD |
| 4 | finally a solution | Pain hook | — Not tested |
| 5 | the secret to | Curiosity hook | — Not tested |
| 6 | you need this | Desire trigger | — Not tested |
| 7 | game changer | Outcome phrase | ✅ S15 — ✅ USE |
| 8 | life changing | Outcome phrase | — Not tested |
| 9 | must have | Desire trigger | — Not tested |
| 10 | genius gadget | Product signal | ✅ S17 — ❌ DEAD |
| 11 | viral product | Social proof | — Not tested |
| 12 | as seen on tiktok | Social proof | — Not tested |
| 13 | tiktok made me buy | Social proof | ✅ S16 — ❌ DEAD |
| 14 | 50% off today | Offer signal | ✅ S16 — ❌ DEAD |
| 15 | buy 1 get 1 free | Offer signal | ✅ S16 — ❌ DEAD |
| 16 | selling out fast | Urgency | — Not tested |
| 17 | back in stock | Urgency | — Not tested |
| 18 | before you buy | Pre-purchase hook | — Not tested |
| 19 | stop wasting money | Pain + offer | — Not tested |
| 20 | never worry about | Relief hook | — Not tested |
| 21 | this changed everything | Outcome phrase | — Not tested |
| 22 | why didn't I know | Discovery hook | — Not tested |
| 23 | parents are obsessed | Social proof | — Not tested |
| 24 | everyone is buying | Social proof | — Not tested |
| 25 | the easiest way to | Outcome phrase | — Not tested |
| 26 | problem solved | Outcome phrase | — Not tested |
| 27 | instantly | Outcome phrase | — Not tested |
| 28 | works in seconds | Outcome phrase | — Not tested |
| 29 | gift idea | Occasion hook | — Not tested |
| 30 | perfect gift | Occasion hook | — Not tested |

**Kids vertical (on hold, not active priority):**
- baby swaddle, baby bouncer, diaper bag, baby gate, baby wrap, infant, teething, breastfeeding

---

## How to Update

At STEP 8 end of each session, add one row per tested keyword:

```
| keyword | S[N] | [ads count] | ✅/❌/⚠️ [verdict] | [1 line: best signal or reason dead] |
```

If keyword was tested in a prior session and signal changed → add a new row with updated session number, don't edit the old row.
