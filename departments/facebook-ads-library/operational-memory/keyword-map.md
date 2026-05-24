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

> **Status:** Cluster 1 ✅ DONE (S21) — 3 products. S22 Worker Context + Sensation — 7 keywords, 1 product (cold office 66). S23 Mental Fatigue (burnout/work stress/always tired) — 3 keywords, 0 products. KEY FINDING (corrected S23 by Marina): situation keywords work when creating a SPECIFIC MOMENT of discomfort — physical OR contextual ("long flight" = context, found score 72 ✅). DEAD CLASS: wide psychological/emotional states (burnout, work stress, always tired) → supplements/coaching/apps. S24: vagus nerve (193) + overwhelmed (359) → 0 reportable; vagus device cluster real but ALL branded-premium ($150-900). ⛔ CLUSTER 2 (Stress/Mental) CLOSED — 3rd confirmation. S25 (Office×Positive Cluster 5): desk plant + candle warmer → 2 reportable (Ivy 72, Candle Warmer Lamp 70). S26 (Office×Positive plant/desk-life keywords): smart garden/smart planter/desktop aquarium/desk pet/office plant/desktop fountain → 0 NEW reportable, but STRONG recurring signal — companion plant-care gadget category (Ivy + PlantBot + LeafyPod + SENSO CES2026) converging hard + Ivy white-label confirmed on Amazon; narrow exact-phrase keywords (aquarium 8, fountain 1) genuinely thin.
> **Key rule:** Use 3-4 word descriptors with specific moment context. Avoid wide emotional/psychological states. Avoid 2-word condition terms ("back pain" → FB blocked).

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
| 4 — Mental Fatigue | burnout | S23 | 365 | ❌ DEAD | Wide psychological state: supplements/coaching/apps dominate; orthotics tangential; 0 DTC physical $45-79 |
↳ Noise Type: supplements/vitamins | therapy/coaching services | skincare ("tired face") | ↳ Emotional Cluster: mental fatigue / burnout recovery | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: orthotics/insoles (cross-keyword tangential, below threshold)
| 4 — Mental Fatigue | work stress | S23 | 500 | ❌ DEAD | Wide psychological state: HR/corporate wellness, finance, supplements; 0 DTC physical $45-79 |
↳ Noise Type: HR/corporate wellness services | financial services | supplements/adaptogens | ↳ Emotional Cluster: workplace stress / professional burnout | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: orthotics/nurse shoes (Orthora ~63, below threshold)
| 4 — Mental Fatigue | always tired | S23 | 504 | ❌ DEAD | Energy supplements dominate; compression socks below floor ($29-34); orthotics ~62 below threshold |
↳ Noise Type: energy supplements/vitamins | compression socks ($29-34 below floor) | skincare | ↳ Emotional Cluster: fatigue / energy depletion | ↳ Signal Density: Very Low (<2% DTC physical $45+) | ↳ Recurring Categories: compression socks (Everstride 15K reviews $29-34), orthotics (Xstance ~62)
| 2 — Mental | vagus nerve | S24 | 193 | ❌ DEAD (white-label) | Device cluster REAL & active but ALL branded-premium: Pulsetto/Sensate/Truvaga/Hoolest/Neuvana/Nuropod $900; + coaching/certification, quiz-apps, supplements; 0 white-label physical |
↳ Noise Type: branded VNS devices ($150-900) | coaching/practitioner certification | quiz-apps (theliven/Calm) | supplements | ↳ Emotional Cluster: nervous-system regulation / calm | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: branded vagus devices, weighted comfort animals (pulseofpotential — cross-keyword)
| 2 — Mental | overwhelmed | S24 | 359 | ❌ DEAD | Wide emotional state: courses/Tony Robbins, supplements/CBD, pharma (SPINRAZA), charity, B2B SaaS; 0 physical DTC. NOTE: 1st run hit transient FB skeleton-hang (0 cards) → re-run OK (Marina confirmed FB-side, >50k results) |
↳ Noise Type: courses/info-products | supplements/CBD | pharma | charity | B2B SaaS/subscription | ↳ Emotional Cluster: stress/overwhelm | ↳ Signal Density: Very Low (<1%) | ↳ Recurring Categories: weighted comfort animals (pulseofpotential — same as vagus nerve = recurring signal)
| 5 — Office Positive Emotion | mug warmer | S25 | 99 | ❌ DEAD | Keyword pulls the CUP (POD/artisan mugs) not the WARMER device; no dedicated white-label DTC advertiser for the device; 0 reportable |
↳ Noise Type: spam engagement-bait story-accounts | POD personalized mugs | affiliate deal-aggregators (BESTDEALS.TODAY) | local services (USA Insulation ×11) | ↳ Emotional Cluster: cozy ritual / gifting | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: POD mugs, artisan pottery
| 5 — Office Positive Emotion | desk plant | S25 | 177 | ✅ USE | Ivy Gen 2 smart companion planter 72 (AI-face desk bestie, pioneer sub-niche, no direct competitor in scrape); artisan decor + health-spam noise |
↳ Noise Type: health-spam story-accounts | artisan/handcrafted decor | services (tree-care, EMDR) | supplements | ↳ Emotional Cluster: companionship / cozy / care | ↳ Signal Density: Low (~5%) | ↳ Recurring Categories: artisan plant decor, smart/companion planter (Ivy)
| 5 — Office Positive Emotion | cozy office | S25 | 422 | ❌ DEAD | Real-estate/home-SEARCH phrase → realtors/apartments/sqft + furniture + sheds-as-"home office"; Ivy cross-keyword repeat; 0 NEW reportable |
↳ Noise Type: real-estate listings (dominant) | furniture (heavy) | backyard sheds | Amazon affiliates | ↳ Emotional Cluster: home/space aspiration | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: standing desks/furniture, sheds, candle/ambient lamps
| 5 — Office Positive Emotion | candle warmer | S25 | 93 | ✅ USE | Candle Warmer Lamp 70 (flame-free cozy glow; 5+ fresh DTC: MEVA $119-170, Glenbrookhome $68, Docos, Homira); ⚠️ везде-risk; cleanest keyword of the 5 |
↳ Noise Type: candle/wax consumables (Creative Energy, Magic Candle) | affiliate listicles | misc services | ↳ Emotional Cluster: cozy ritual / safety (no flame) / ambiance | ↳ Signal Density: Medium (~10% — candle warmer LAMP sub-category) | ↳ Recurring Categories: candle warmer lamp (5+ brands = category convergence), ambient lamps
| 5 — Office Positive Emotion | aesthetic desk | S25 | 246 | ❌ DEAD | Branded-premium identity gear (mech keyboards $100-400, RGB Nanoleaf/Lume Cube, Craighill) + heavy furniture + cheap novelty/POD; white-label $39-100 empty |
↳ Noise Type: branded-premium keyboards/RGB | heavy furniture (standing desks) | licensed POD (band desk mats) | Kickstarter | ↳ Emotional Cluster: self-expression / setup identity | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: mechanical keyboards, ambient/aesthetic desk lamps (cross-keyword with candle warmer)
| 5 — Office Positive Emotion | smart garden | S26 | 284 | ❌ DEAD | Indoor hydroponic = real category convergence (Plantaform/Gardyn/Rise/ēdn/Elfsys/MicroBuddy 6+) but ALL premium $170-900 + bulky floor-units + (some) pod-subscription; rest = outdoor landscaping-services/real-estate/lawn-retail; 0 white-label $39-100 |
↳ Noise Type: landscaping services | real-estate listings | lawn/garden retail | supplements (Vitanova) | ↳ Emotional Cluster: outdoor garden aspiration / indoor grow-your-own | ↳ Signal Density: Low (~5%, all out of price/logistics range) | ↳ Recurring Categories: indoor hydroponic systems (premium), outdoor planters
| 5 — Office Positive Emotion | smart planter | S26 | 98 scroll/50 | ⚠️ VALIDATION | Companion-planter CONVERGENCE: Ivy(plantsio) + PlantBot(plantsrobot $89.90) + Amazon white-label confirmed (generic "Plantbot Upgraded" B0FNRGMZRQ); LeafyPod $140-217 sub-threshold ~56; 0 NEW (Ivy = dup S25, signal strengthened) |
↳ Noise Type: spam romance-story accounts (Passion Novels/Read Space) | landscaping/ag-equipment | outdoor cedar/raised planters | 3D-print filament | ↳ Emotional Cluster: companion/care / plant-keeping guilt | ↳ Signal Density: Low (~6%) | ↳ Recurring Categories: companion AI planter (Ivy/PlantBot/LeafyPod), outdoor planters
| 5 — Office Positive Emotion | desktop aquarium | S26 | 8 | ⚠️ NARROW | Hyper-narrow exact phrase; 8 advertisers ALL-TIME (re-confirmed no `--since`); all aquarium hobby/equipment (Xinyou/Glass Aqua/The Ocean Floor), 0 desk-companion DTC product; try "fish tank"/"betta"/"jellyfish lamp" instead |
| 5 — Office Positive Emotion | desk pet | S26 | 551 scroll/201 | ⚠️ SPAM-HEAVY | Companion desk-gadget (Ivy dup + LOOI branded phone-as-face robot + Axonix kids robot $99.99 generic-dropship); heaviest micro-drama spam yet (MYNVWIBCN ×8 "fighter pilot") + POD figurines + Crystal Pets пустышка $46-185; 0 new reportable |
↳ Noise Type: micro-drama spam story-accounts (MYNVWIBCN ×8) | POD/3D figurines (My Mini Mento/Kibifig/Wander Prints) | crystal-decor пустышка | real-estate/vet-software/cat-pharma | ↳ Emotional Cluster: desk companionship / loneliness-at-work | ↳ Signal Density: Low (~4% physical, mostly branded/kids) | ↳ Recurring Categories: companion desk robot (LOOI/Axonix), companion planter (Ivy)
| 5 — Office Positive Emotion | office plant | S26 | 505 scroll/190 | ❌ DEAD | Plant-care SERVICES (interior plantscaping) + heavy pharma "doctor"-story spam dominate; SENSO (Soildtech, CES 2026 plant-Tamagotchi sensor, 9 ads → Kickstarter PRE-LAUNCH, not reportable); Ivy dup; artificial plants commodity; 0 reportable |
↳ Noise Type: pharma/health "doctor"-story spam (kidney/cardio/menopause/hair/gut, NO DOMAIN) | plant-care services | "scratched desk" story-spam ×3 | artificial plants | ↳ Emotional Cluster: low-maintenance greenery / wellness | ↳ Signal Density: Very Low (<3%) | ↳ Recurring Categories: smart plant sensors (SENSO pre-launch), companion planter (Ivy)
| 5 — Office Positive Emotion | desktop fountain | S26 | 1 | ⚠️ NARROW | Hyper-narrow fresh-2026 phrase = 1 advertiser (not even a fountain — "The Big Bin Store"); tabletop fountains = Amazon decor commodity $20-50; Marina chose B (no no-filter re-run); try "tabletop fountain" if revisited |
| Eye/Screen | tired eyes | S27 | 262 | ✅ USE | Rechargeable Heated Eye Mask (Blinkjoy-validated white-label) 67 — warm-compress dry-eye relief, premium $150→white-label $49-69; 2-word health term NOT blocked (262 ads, 81s) |
↳ Noise Type: vision-correction пустышки + eye supplements (Visiovance lutein) | Rx pharma (Lynkuet/Xiidra) | micro-drama story-spam NO-DOMAIN | skincare/eye-patch commodity | ↳ Emotional Cluster: eye relief / vision worry / screen fatigue | ↳ Signal Density: Low (~5% white-label physical) | ↳ Recurring Categories: heated eye mask/massager, blue-light glasses, monitor light bar (Quntis ~62)
| Eye/Screen | eye strain | S27 | 229 | ⚠️ MIRROR | Near-mirror of "tired eyes"; 0 NEW reportable (heated mask/massager = dup; eye massager Sakerplus = dup approved S1); dominated by blue-light-glasses commodity class |
↳ Noise Type: blue-light glasses (8+ adv: Lockt/Slickweare/Moonighty/AZZARI/EyeQLenz/TechSpecs/Ocushield) пустышка/везде | eye supplements | TV-backlight cloned-copy (Trendora/Orbis/Orvinos) | car sun-visor-extender dropship-clones (Flowarmth 20/Forttender 8) | ↳ Emotional Cluster: eye relief / screen protection | ↳ Signal Density: Very Low (<3% new white-label) | ↳ Recurring Categories: blue-light glasses, TV backlight, eye massager (dup)
| Meal/Lunch | heated lunch box | S27 | 30 | ✅ USE | Cordless Self-Heating Lunch Box (Luncheaze-validated white-label) 73 — battery lunch box auto-heats, no microwave; thin exact phrase (1 real DTC adv) but category real & wider under "electric/cordless lunch box"; 563 scroll→30 unique (heavy ad-repeat + spam, NOT a bug — scroll hit target, session OK) |
| Meal/Lunch | office lunch | S27 | 247 | ❌ DEAD | Broad situation phrase → food-delivery/catering services + job-recruitment + pharma story-spam dominate; 0 reportable. Itaki Bento PRO cooker ~63 sub-threshold (Marina-kept); Celinva cushion = S19 dup |
↳ Noise Type: food-delivery/catering services (Lunchdrop/UberEats/Bojangles/RollPlay) | pharma-story-spam NO-DOMAIN (RA ×2, Lubracil) | job listings | marketplace (Rarely Co) | compression socks | ↳ Emotional Cluster: lunch convenience / workplace | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: portable powered meal device (Itaki cooker — adjacent to Luncheaze warmer)
| Situation | on the go | S27 | 377 | ❌ DEAD | Ultra-broad phrase = ALL advertiser types, no product filter (like "gadget"/"tired of"); established mega-brands + supplements + services/apps/banks + game-deal sites; 0 white-label DTC physical in range |
↳ Noise Type: established mega-brands (Lovevery/Sanpellegrino/Carpe/Coleman/Kohl's/Secret/Nature Made) | supplements (Eu Natural/RYZE) | services/apps/banks (AWS/Starlink/Natural Cycles/Fifth Third) | ↳ Emotional Cluster: mobility/convenience (universal) | ↳ Signal Density: Very Low (<1%) | ↳ Recurring Categories: none (too broad)
| Eye/Screen | screen fatigue | S27 | — | ⏭️ SKIPPED | Not tested — Marina skipped; expected 3rd mirror of tired eyes/eye strain (same eye-relief + blue-light landscape) |
| Commute/Situation | morning commute | S28 | 288 | ❌ DEAD | Broad situation → car-dealerships (Mazda/Ford/Honda ×8+)/real-estate/apparel/makeup/supplements; "commute"=context not object → market answers with everything; 0 reportable |
↳ Noise Type: car dealerships | real-estate/apartment leasing | apparel/footwear | makeup | supplements | branded-premium (RayNeo AR/Coldest/Lucyd) | ↳ Emotional Cluster: daily-grind aspiration / mobility | ↳ Signal Density: Very Low (<1% white-label) | ↳ Recurring Categories: car scent diffuser, open-ear/safety audio eyewear, commuter backpack
| Commute/Situation | long commute | S28 | 376 | ❌ DEAD | Mirror of morning commute + e-mobility cluster (ebikes/e-boards/treadmills as commute-replacement, all out of price/logistics); PureGo ozone car-odor device $59 sub-threshold (liability); 0 |
↳ Noise Type: car dealerships | e-mobility/fitness logistics-heavy (ebike/e-skateboard/treadmill/massage-chair) | footwear | jewelry | branded beauty | ↳ Emotional Cluster: commute escape / mobility upgrade | ↳ Signal Density: Very Low (<1%) | ↳ Recurring Categories: car odor/scent device, memory-foam driving seat cushion (= rejected orthopedic cushion S19)
| Product | car organizer | S28 | 164 | ⚠️ COMMODITY | Clean product-phrase signal (direct DTC, NO dealer noise — beats commute phrases on type) BUT entire category low-price commodity dropship $5-30 + Temu/Alibaba direct; no white-label hero $39-100; confirms S3 note; 0 |
↳ Noise Type: generic multi-product dropship (gibberish names) | Amazon/Temu/Alibaba affiliate+direct | car mats (heavy) | dealerships | supplement/novel/fertility spam | ↳ Emotional Cluster: clutter relief / tidy car | ↳ Signal Density: Low (~10% physical but all commodity/below-floor) | ↳ Recurring Categories: trunk organizer, seatback storage, headrest hook, cup organizer, car trash bag (all $5-30)
| Hand/Wrist Pain | sore wrists | S28 | 74 | ⚠️ THIN | Genuinely thin exact phrase (74, NOT FB-blocked); fiction/romantasy NO-DOMAIN spam + wellness-пустышка + off-category convenience-hooks; Reava ThermaWrap hand massager (heat+compression, $99.99) ~63 SOFT; 0 |
| Hand/Wrist Pain | wrist pain | S28 | 310 | ❌ DEAD (white-label) | "пустышка-magnet" pain: copper/hematite/magnetic/red-light bracelets+wraps (10+ adv: Copper Compression/Hematix ×3/Hemios/Vera's ×2/Kovaria) + supplements + medical/insurance services + commodity compression gloves; verifiable tier = commodity or established Amazon; 0 |
↳ Noise Type: пустышка therapy jewelry/wraps (copper/hematite/magnetic/red-light) | supplements | medical services/insurance-brace scam/chiropractors | commodity compression gloves/sleeves | off-category tools w/ wrist-pain secondary hook | ↳ Emotional Cluster: chronic hand/wrist pain relief (medical) | ↳ Signal Density: Very Low (<2% verifiable-result white-label) | ↳ Recurring Categories: copper/therapy bracelets, compression gloves, heat-therapy hand massager (Reava/Movella)
| Hand/Wrist Pain | hand strain | S28 | 242 | ❌ DEAD | "strain" too ambiguous → eye-strain readers (CliC ×3)/cable strain-relief (RJ45 crimper)/gaming strain (Nyxi/Floky)/dog-neck strain; same пустышка/massager tier as wrist pain; Movella heat+vibration wrist device sub-threshold (пустышка-circulation, price hidden); 0 |
↳ Noise Type: reading glasses/eye-strain | off-category tools (nail clippers/pruners/tiller/grinder) | pet (harness) | medical mobility (walker) | supplements | B2B/handcrafted massage tools | ↳ Emotional Cluster: ambiguous "strain" (eye/hand/gaming/effort) | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: heat-therapy wrist massager (Movella/Reava), reading glasses, ergonomic tool versions
| Appearance/Identity | looking good on zoom | S29 | 266 | ❌ DEAD | Broad aspirational 4-word phrase; "zoom"→business-opp/coaching/B2B-agency layer (Grant Cardone/MSP/insurance-recruitment) + commodity skincare + aesthetic services + off-theme novelty (telescopes/night-vision); only on-theme object = branded eMeet webcam; 0 |
↳ Noise Type: business-opportunity/money-coaching (dominant) | insurance/annuity recruitment | commodity skincare/aesthetic services | off-theme novelty optics | story-spam (cat-food "NONE OF IT IS GOING TO WORK") | ↳ Emotional Cluster: look-good-financially/professionally + appearance anxiety | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: auto-adjusting "smart" reading glasses, webcam/ring light (branded), skincare creams
| Appearance | tired face on camera | S29 | 207 | ❌ DEAD | Anti-aging beauty cluster (creams/serums/collagen-masks/cushions/oils) + reject-class devices (RegenMask LED+microcurrent, HiZoo EMS) + supplements + aesthetic surgery + heavy story-spam; one non-skincare gadget (selfie monitor) = cloaked affiliate to food site; 0 |
↳ Noise Type: anti-aging skincare commodity | LED/microcurrent beauty devices (reject-class) | supplements | aesthetic surgery | story-spam (Ozempic/tirzepatide + romance DramaBox/NetShort) | cloaked-affiliate (ad↔store mismatch) | ↳ Emotional Cluster: aging/tired-face-on-Zoom anxiety | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: collagen masks, anti-aging creams, gua-sha/face-sculpt brushes |
| Appearance/Identity | looking good | S29 | 377 | ❌ DEAD | Broadest aspirational phrase = apparel/shapewear/jewelry/swimwear + skincare-commodity (Olay/Native/HausLabs) + branded beauty LED (Qure/Dr Dennis Gross) + пустышка pain-devices (neck EMS/sciatic) + pharma/finance/cars + story-spam; Bawldy head shaver ~54 sub-threshold (commodity Skull-Shaver clone); 0 |
↳ Noise Type: apparel/shapewear/jewelry | skincare commodity | branded beauty-LED devices | пустышка pain-devices | pharma/finance/auto | story-spam | ↳ Emotional Cluster: look-good (body/appearance/identity) | ↳ Signal Density: Very Low (<2% white-label) | ↳ Recurring Categories: shapewear, skincare creams, head/face grooming devices (commodity) |
| Appearance | tired face | S29 | 282 | ❌ DEAD | Mirror of "tired face on camera"; anti-aging skincare commodity + cloned med-spa promo-network (6+ "Derma-Lift $99" city accounts) + pharma (Lynkuet 28 ads/Jardiance) + supplements; all physical beauty-tools in reject classes (dermaplaning/gua-sha brush/HiZoo S24/silk sleep mask); 0 |
↳ Noise Type: anti-aging skincare commodity | cloned local med-spa service network | pharma | supplements | commodity/пустышка beauty tools | ↳ Emotional Cluster: tired/aging appearance | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: collagen/wrinkle creams, med-spa Derma-Lift promo, gua-sha brushes |
| Situation | working from bed | S29 | 235 | ❌ DEAD | Expected ergonomic objects ABSENT (lap desk/bed tray/wedge pillow/backrest = 0 hits); phrase lives in pain/story-narratives not product context; пустышка pain-devices (Vibit plantar fasciitis/CALLIXE-FisioRest neck/mavetto neuropathy cream all fail Veto) + supplements + story-spam; weak "work-from-couch comfort accessory" micro-signal (Niizi desk pillow/genionspace riser/lumos neck light — all commodity/≤floor/low-wow); 0. NOTE: 1st run = React hydration stall (0 cards, skeleton screenshot, session valid) → RULE 5b re-run → 235 |
↳ Noise Type: пустышка pain-devices/creams | supplements | story-spam (cat-food/dog-allergy/romance) | commodity beauty | furniture/mattress | prior-reject brands (Comfrt/Koprez) | ↳ Emotional Cluster: WFH comfort / pain "before bed" | ↳ Signal Density: Very Low (<2%) | ↳ Recurring Categories: couch/bed comfort accessories (commodity), plantar/neck pain devices |
| Situation/Commute | stuck in traffic | S29 | 288 | ❌ DEAD | Confirms S28 commute=CONTEXT-not-object; e-com coaching/agency (dominant) + supplements/GLP-1 + пустышка-therapy-jewelry (Hematix hematite, reject-class S28) + niche/branded vehicle-gadgets (motorcycle cooling/MotorTablet BMW/DAHON bikes) + Praetorian holster (Meta-policy reject) + commodity car-cooling-clip (≤floor); 0 |
↳ Noise Type: e-com coaching/agency (dominant) | supplements/GLP-1 | пустышка therapy jewelry | niche/branded vehicle gadgets | auto-services | story-spam | ↳ Emotional Cluster: commute frustration / escape | ↳ Signal Density: Very Low (<1% white-label) | ↳ Recurring Categories: car cooling gadgets (commodity), motorcycle accessories, commute-replacement bikes

**Cluster 2 candidates (Meal/Energy Problems):** "skipping lunch", "too tired to cook", "no time to eat", "coffee not working", "afternoon crash"
**Cluster 3 candidates (Mental Fatigue — pending):** exhausted, mentally drained (S24)

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
