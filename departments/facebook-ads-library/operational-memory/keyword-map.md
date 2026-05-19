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
| quality time | S14→S18 retest | 44→392 | ❌ DEAD confirmed | BUG fixed: real count 392; abstract lifestyle phrase attracts all advertiser types; verdict unchanged |
| connect with your | S14→S18 retest | 163→288 | ❌ DEAD confirmed | BUG impact confirmed: real count 288; dominated by apps/B2B/restaurants; conversation card game sub-niche signal ($35-39, below floor) |
| road trip | S14 | 348 | ⚠️ SITUATIONAL | 2 category signals: baby car sun shade + car seat cushion; retry S21 |
| say goodbye to | S15 | 375 (no filter) / 418 (--since=2026-01-01) | ⚠️ LOW YIELD | 1 reportable (Heusom 71 pet grooming); ~60% service/beauty/supplement noise; date filter did NOT reduce noise (418 > 375); strong DTC operators present but diluted |
| game changer | S15 | 363 | ✅ USE | 1 reportable (Dermave 69 women's trimmer); Beddy's zipper bedding category signal; mix of all DTC categories — broad-spectrum performance keyword |
| tiktok made me buy | S16 | 277 | ❌ DEAD | Social-proof phrase; 90% personal brand/influencer content; 0 DTC physical products |
| 50% off today | S16 | 69 | ❌ DEAD | Promo-phrase too narrow (time modifier "today"); FB exhausts phrase in 45s; 0 reportable |
| buy 1 get 1 free | S16 | 164 | ❌ DEAD | BOGO signal = jewelry/apparel/supplements; Blumi Baby swim goggles ~62 (below threshold); 0 reportable |
| half off | S16 | 357 | ❌ DEAD | Discount phrase = retail/apparel/seasonal; "50% off" unusable (% breaks URL encoding); 0 reportable |
| genius gadget | S17→S18 retest | 121→131 | ❌ DEAD confirmed | BUG minimal impact (+10 ads); mass-clone dropship dominates; top products below $39 floor (massager $17, towel holder ~$25) |
| gift idea | S18 | 304 | ❌ DEAD | Gift-occasion phrase = personalized/custom gift services dominate; no white-label DTC physical products |
| perfect gift | S18 | 313 | ❌ DEAD | Gift-occasion class confirmed (re-tested with fixed scraper); 70% custom/personalized gifts, 20% established brands, 0 white-label DTC $39-99 |
| back in stock | S18 | 325 | ⚠️ SITUATIONAL | Urgency signal works; real DTC brands use scarcity; heavy supplement/apparel noise; 282 candidates scanned, 0 scored 65+ |
| gadget | S17 | 296 | ❌ DEAD | Ultra-broad: established brands (FIXD, REVO, HexClad), commodity below $39, пустышки; 0 reportable |
| tired of | S17 | 427 | ❌ DEAD | Broad emotional hook attracts ALL advertiser types — services, clinics, apps, beauty; 0 DTC physical products; confirms S3 WebSearch pattern |
| why didn't I know | S18 | 364 | ⚠️ LOW YIELD | Discovery hook = broad mix (finance apps, pharma, beauty brands); foot comfort sub-niche signal (Koprez $39.99, Bearefoot $44+, Elliosa £20); 0 scored 65+; apostrophe bug fixed (quote_plus) |
| the easiest way to | S18 | 0 (throttled) | ⚠️ RETRY | FB content throttle after 2000 ads/day — page blank, not keyword issue; re-run in fresh session |
| as seen on shark tank | S19 | 584 | ❌ DEAD | Structural: 90%+ genuine Shark Tank alumni = all branded/proprietary/patented; zero white-label opportunity by design |
| use code | S19 | 368 | ❌ DEAD | Universal promo signal used by all brands (apparel, restaurants, services); same dead class as BOGO/50% off |
| money back guarantee | S19 | 0 | ⚠️ RETRY | FB "No ads match" — Marina confirmed same from another account; likely FB glitch; re-test S20 |
| limited time only | S19 | 293 | ❌ DEAD | Universal urgency phrase attracts all categories (fast food, retail, services, apparel); 0 DTC physical products |
| sold out | S19 | 0 | ⚠️ RETRY | FB "No ads match" — same as "money back guarantee"; likely FB glitch; re-test S20 |
| if you suffer from | S20 | 361 | ❌ DEAD | Pain hook = supplements/services/pharma dominate; 15+ candidates checked; 0 DTC physical $39-100 |
| the worst part of | S20 | 262 | ❌ DEAD | Pain narrative = supplements/clinics/services; broad hook attracts all advertiser types |
| the only thing that | S20 | 391 | ❌ DEAD | Universal testimonial phrase — pharma, pizza chains, automotive, all use it; 0 DTC physical |
| before and after | S20 | 344 | ❌ DEAD | Universal transformation = pharma dominant + beauty established brands + automotive; not DTC-specific |
| sold out (retest) | S20 | 0 | ❌ BLOCKED | Retested S20 — same 0-result; FB platform blocks phrase; hypothesis closed; not re-testing |
| free shipping over / struggling with / Embarrassing / in seconds | S20 | 0 each | ❌ BLOCKED | All 4 returned FB "No ads match" — account-level block for these phrases; hypothesis closed |
| tired feet | S21 | ~280 | ✅ USE | Nuvé Silk 74 (callus remover) + Hugterra 70 (neck massager cross-category) — 2 products; situation keyword spans foot-care + WFH pain |
↳ Noise Type: compression socks | shoes/footwear | ↳ Emotional Cluster: pain/relief after standing | ↳ Signal Density: Medium (~15% DTC physical) | ↳ Recurring Categories: callus removers, compression socks
| sore legs | S21 | 258 | ⚠️ LOW YIELD | Compression socks dominate (6+ brands $28-39 below floor); Firefly Recovery patented EMS; established recovery brands; 0 products |
↳ Noise Type: compression socks (50%+) | established recovery brands (Firefly, Vibit, Hyperice) | ↳ Emotional Cluster: recovery/performance after exertion | ↳ Signal Density: Low (<5% white-label DTC $45+) | ↳ Recurring Categories: compression socks, EMS recovery devices
| sitting all day | S21 | 320 | ✅ USE | 3-brand convergence (Celinva Jan/Try Alum Dec/EverCushion Mar 2026) on honeycomb seat cushion; Score 68; ⚠️ Amazon saturated $20-35 |
↳ Noise Type: seat cushions (30%) | WFH ergonomic products | ↳ Emotional Cluster: workplace comfort/chronic sitting pain | ↳ Signal Density: Medium (15-20% DTC physical) | ↳ Recurring Categories: honeycomb gel seat cushion (3 independent brands = category convergence signal)
| back pain | S21 | 0 (×2) | ❌ BLOCKED | FB "No ads match" both attempts; 2-word health-condition term blocked by FB Active ads filter; use "lower back pain" instead |
| lower back pain | S21 | 256 | ⚠️ LOW YIELD | Pharma (40%+) + shoes (15%) + established DTC brands (NeuroMD 90K, Chirp) dominate; seat cushion = K4 duplicate; 0 new products |
↳ Noise Type: pharma/medical (40%) | footwear (15%) | established DTC brands | ↳ Emotional Cluster: pain/recovery (medical-grade) | ↳ Signal Density: Low (<5% new white-label DTC $45+) | ↳ Recurring Categories: seat cushions (K4 duplicate), cervical/neck devices (K2 duplicate), ergonomic pillows
| standing all day | S21 | 0 (×2) | ❌ BLOCKED | FB "No ads match" both attempts; 2-word activity descriptor blocked; reformulate as "feet hurt from standing" or "on my feet all day" |

**Verdict codes:** ✅ USE | ❌ DEAD | ⚠️ RETRY / NARROW / SITUATIONAL / VALIDATION / PRICE / ADULT

---

## Priority Queue — Sessions 15–20 Broad Horizontal Discovery [ЗАКРЫТА]

> ⛔ Hypothesis CLOSED after Session 20. 29 keywords tested → 2 reportable products (both S15). Performance signal keywords do NOT filter for DTC physical product operators. Do NOT continue this queue. New hypothesis TBD.

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
| 17 | back in stock | Urgency | ✅ S18 — ⚠️ SITUATIONAL |
| — | as seen on shark tank | Social proof | ✅ S19 — ❌ DEAD (structural: branded alumni) |
| — | use code | Promo signal | ✅ S19 — ❌ DEAD |
| — | money back guarantee | Credibility phrase | ✅ S19 — ⚠️ RETRY |
| — | limited time only | Urgency phrase | ✅ S19 — ❌ DEAD |
| — | sold out | Urgency phrase | ✅ S19 — ⚠️ RETRY |
| 18 | before you buy | Pre-purchase hook | — Not tested |
| 19 | stop wasting money | Pain + offer | — Not tested |
| 20 | never worry about | Relief hook | — Not tested |
| 21 | this changed everything | Outcome phrase | — Not tested |
| 22 | why didn't I know | Discovery hook | ✅ S18 — ⚠️ LOW YIELD |
| 23 | parents are obsessed | Social proof | — Not tested |
| 24 | everyone is buying | Social proof | — Not tested |
| 25 | the easiest way to | Outcome phrase | ⚠️ S18 — RETRY (throttled) |
| 26 | problem solved | Outcome phrase | — Not tested |
| 27 | instantly | Outcome phrase | — Not tested |
| 28 | works in seconds | Outcome phrase | — Not tested |
| 29 | gift idea | Occasion hook | — Not tested |
| 30 | perfect gift | Occasion hook | — Not tested |

**Kids vertical (on hold, not active priority):**
- baby swaddle, baby bouncer, diaper bag, baby gate, baby wrap, infant, teething, breastfeeding

---

## Active Hypothesis S21 — Situation Keywords: Everyday Worker Problems

> **Status:** Cluster 1 ✅ DONE (S21) — 3 products. S22 Worker Context + Sensation — 7 keywords, 1 product (cold office 66). KEY FINDING: situation keywords yield products ONLY when describing PHYSICAL SENSATION (cold office ✅, tired feet ✅, sitting all day ✅) — NOT context/lifestyle (desk job ❌, meal prep ❌, night shift ❌). Next: Cluster 2 pain-state (afternoon crash, too tired to cook) OR Cluster 3 (brain fog at work, can't focus).
> **Key rule:** Use 3-4 word descriptors with activity context. Avoid 2-word condition terms ("back pain" → blocked; "lower back pain" → 256 ads). Physical sensation keywords outperform context/lifestyle keywords.

| Cluster | Keyword | S | Ads | Verdict | Signal |
|---------|---------|---|-----|---------|--------|
| 1 — Physical | tired feet | S21 | ~280 | ✅ USE | Nuvé Silk 74 + Hugterra 70 — 2 products |
| 1 — Physical | sitting all day | S21 | 320 | ✅ USE | Seat cushion 68 — 3-brand convergence Jan-Mar 2026 |
| 1 — Physical | sore legs | S21 | 258 | ⚠️ LOW YIELD | Compression socks dominate; 0 products |
| 1 — Physical | lower back pain | S21 | 256 | ⚠️ LOW YIELD | Pharma + established brands dominate; 0 products |
| 1 — Physical | back pain | S21 | 0×2 | ❌ BLOCKED | 2-word health term → FB blocked |
| 1 — Physical | standing all day | S21 | 0×2 | ❌ BLOCKED | 2-word activity term → FB blocked |
| 2 — Worker Context | night shift | S22 | 325 | ❌ DEAD | Energy supplements + job platforms; no white-label DTC $45-79 |
↳ Noise Type: energy supplements | job platforms | nurse accessories | ↳ Emotional Cluster: energy/fatigue | shift worker identity | ↳ Signal Density: Low (<5%) | ↳ Recurring Categories: none
| 2 — Worker Context | desk setup | S22 | 194 | ❌ DEAD | Premium branded furniture ($200+); aspirational aesthetic — no DTC entry window |
↳ Noise Type: premium furniture ($200+) | tech accessories | lifestyle content | ↳ Emotional Cluster: productivity/aesthetic | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: ergonomic chairs, standing desks (all above range)
| 2 — Worker Context | ergonomic | S22 | 316 | ❌ ATTRIBUTE | Attribute descriptor: attracts ergonomic chairs $200+ + seat cushion K4 duplicate |
↳ Noise Type: premium ergonomic chairs ($200+) | established orthopedic brands | ↳ Emotional Cluster: workplace comfort/health | ↳ Signal Density: Low (<5%) | ↳ Recurring Categories: seat cushions (K4 duplicate), ergonomic chairs ($200+)
| 2 — Worker Context | meal prep | S22 | 299 | ❌ DEAD | Food delivery services (60%+) + premium appliances ($649 Suvie); no physical product |
↳ Noise Type: food delivery services (60%+) | pet food subscriptions | premium appliances | ↳ Emotional Cluster: convenience / healthy eating | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: meal delivery brands (HelloFresh, HalalMeals, etc.)
| 2 — Worker Context | desk job | S22 | 313 | ❌ DEAD | Job listings + B2B services + premium furniture ($214-629 TopJob); no DTC window |
↳ Noise Type: job listings | B2B services/software | premium furniture ($200+) | ↳ Emotional Cluster: career/work lifestyle | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: ergonomic furniture (TopJob $214-629)
| 3 — Sensation | cold office | S22 | 217 | ✅ USE | Heated desk mat score 66 (Whisper Heat validator); 1 FB advertiser (weak signal); seasonal Oct-Apr |
↳ Noise Type: energy supplements | coffee brands | tactical apparel | ↳ Emotional Cluster: physical discomfort (cold) / warmth desire | ↳ Signal Density: Low (~5%) | ↳ Recurring Categories: compression socks, under-desk heaters
| 3 — Sensation | on your feet all day | S22 | 266 | ❌ DEAD | Footwear-dominated ($99-200+); compression socks below floor; 0 white-label $45-79 |
↳ Noise Type: footwear brands ($99-200+) | compression socks ($20-40) | established shoe brands | ↳ Emotional Cluster: foot pain / standing fatigue | ↳ Signal Density: Very Low (<3%) | ↳ Recurring Categories: work shoes ($99-185), compression socks ($20-40)

**Cluster 2 candidates (Meal/Energy Problems):** "skipping lunch", "too tired to cook", "no time to eat", "coffee not working", "afternoon crash"
**Cluster 3 candidates (Mental Fatigue):** "brain fog at work", "can't focus at work", "overwhelmed at work", "deadline stress", "zoom fatigue"

---

## How to Update

At STEP 8 end of each session, add one row per tested keyword:

```
| keyword | S[N] | [ads count] | ✅/❌/⚠️ [verdict] | [1 line: best signal or reason dead] |
```

If keyword was tested in a prior session and signal changed → add a new row with updated session number, don't edit the old row.

**Extended fields (S21+ — add as footnote below the row when present):**

```
↳ Noise Type: [dominant noise category — e.g. supplements/pharma | services/apps | retail brands | affiliates | mixed]
↳ Emotional Cluster: [core emotional territory advertisers used — e.g. pain/recovery | vanity/confidence | convenience | fear/risk | parental concern]
↳ Signal Density: [physical DTC product density — High (20%+ physical DTC) | Medium (10-19%) | Low (<10%)]
↳ Recurring Categories: [sub-categories appearing 2+ times independently — e.g. compression socks, foot massagers]
```

Fill extended fields only for keywords with 100+ ads. Skip for dead keywords with <50 ads.
These fields feed the Signal Escalation Rule — log them at STEP 8 even if keyword was DEAD, as noise patterns are valuable.
