# SESSION LEARNINGS

**Active temporary guidance — read at session start, after op-rules.md.**
Contains: short-lived tactical discoveries, category signals, behavioral corrections.
Does NOT contain: permanent operational rules (→ op-rules.md) or keyword verdicts (→ keyword-map.md).

Agent may **APPEND** new entries AND **archive expired entries** at STEP 8.
To archive: move entry to Expired section below. Do NOT delete — move.
Agent must NEVER edit non-expired entries or modify core/ files.

Items expire after the listed session. Marina promotes confirmed patterns via review/promotion-queue.md.

---

## Current Focus

**Sessions 15+: Broad Horizontal Discovery — Performance Signal Keywords**

- **Primary:** Facebook Ads Library via VPS scraper — all broad discovery here
- **Secondary:** Amazon, TikTok, AliExpress — verification only
- **Current strategy:** Using "performance advertising signal keywords" — words that attract aggressive DTC/dropship advertisers regardless of niche (offer hooks, emotional triggers, outcome phrases). Examples: "struggling with", "50% off today", "game changer", "works in seconds". These reveal active DTC operators across ALL categories, not tied to one vertical.
- **Why this works:** Pampers and bloggers don't write "buy 1 get 1 free". DTC operators and dropshippers do. These keywords pre-filter by advertiser TYPE, not topic.
- **After 30 keywords:** analyse the category landscape that emerges → identify the strongest 2-3 categories → go deep with product-specific keywords in those categories.
- **Kids vertical:** data preserved in keyword-map.md. Not the active focus.

---

## Active Learnings

~~### [2026-05-16] Session 10 — Keyword Audit Database: ~50 keywords weekly monitor~~
> ARCHIVED S25 — expired. Idea preserved in memory project_keyword_audit_system.md + keyword-map.md.

---

~~### [2026-05-16] Session 10/11 — Situation keywords = hidden intersection discovery mode~~
> ARCHIVED S25 — expired. Core rule (low yield normal; judge by unpredictable intersections) preserved in keyword-map.md Meta Rules + S22/23 learnings.

---

~~### [2026-05-16] Session 10/11 — Kids Travel Sleep Nest: open DTC niche~~
> ARCHIVED S18 — expired. Result in reported-products.md.

---

### [2026-05-16] Session 10/11 — Scraper "started" date: structural limitation
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH
**Observation:** Field `started` (campaign start date) — Tier-1 signal for Entry Window scoring. Scraper captures it only when FB explicitly shows it in the card. For many advertisers it returns "?". This is a structural pipeline limitation, not a scraper bug.
Workaround when start date is critical: WebFetch brand/About page → founding date; or WHOIS / domain registration date; or first Amazon/Trustpilot review date.
Important: do NOT make this a mandatory step for every advertiser — only when Entry Window score is decisive for the 65/70 threshold.
**Applies to:** All VPS scraper sessions — Entry Window scoring
**Expires after:** Until `started` field is fixed in scraper (or permanent if never fixed)

---

~~### [2026-05-18] Session 15 — Performance signal keywords: yield baseline established~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 15 — --since=2026-01-01 date filter: no signal improvement~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 15 — Category tracking: 30-keyword experiment~~
> ARCHIVED S25 — expired. Broad Horizontal hypothesis CLOSED S20; superseded by Situation Keywords hypothesis.

---

~~### [2026-05-18] Session 17 — "Gadget" descriptor keywords: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md ("gadget"/"genius gadget" ❌ DEAD).

---

~~### [2026-05-18] Session 16 — Offer/promo keywords: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md Meta Rules (Offer/promo DEAD class).

---

~~### [2026-05-18] Session 16 — "%" symbol in FB Ads Library search: URL encoding failure~~
> ARCHIVED S19 — superseded by S18 quote_plus fix. Word alternatives no longer needed. See S18 entry below.

---

~~### [2026-05-18] Session 18 — Scraper URL encoding: quote_plus fix~~
> PROMOTED S30 — now permanent in op-rules.md RULE 5c (special chars handled via `urllib.parse.quote_plus`; apostrophe → 0 ads, fixed → 364). Removed from Active to avoid duplication with op-rules.

---

~~### [2026-05-18] Session 18 — Broad horizontal discovery: pattern after 15+ keywords~~
> ARCHIVED S25 — expired. Hypothesis CLOSED S20 (see S20 archived entry below).

---

~~### [2026-05-18] Session 19 — Universal urgency/credibility phrases: dead class~~
> ARCHIVED S25 — expired. Verdicts preserved in keyword-map.md.

---

~~### [2026-05-18] Session 19 — FB Ads Library: 0-result anomaly for certain phrases~~
> ARCHIVED S21 — expired. Superseded by S21 finding: "back pain" + "standing all day" consistently blocked (not glitch, but FB policy on certain term types). Updated rule in S21 learning below.

---

~~### [2026-05-18] Session 19 — Broad horizontal discovery: hypothesis performance update~~
> ARCHIVED S22 — expired.

---

~~### [2026-05-18] Session 20 — Broad Horizontal Discovery hypothesis: CLOSED~~
> ARCHIVED S25 — expired. Final tally: 29 keywords → 2 products (both S15). Pivoted to Situation Keywords (S21+).

---

~~### [2026-05-19] Session 21 — FB blocks short health-condition & activity terms in Active ads filter~~
> ARCHIVED S28 — expired. REFINED by S27+S28 data: the block is TERM-SPECIFIC, not "all 2-word health terms". Blocked: "back pain", "standing all day". NOT blocked: "tired eyes" (262, S27), "sore wrists" (74, S28), "wrist pain" (310, S28), "hand strain" (242, S28). Verdicts preserved in keyword-map.md. Practical rule retained: if a 2-word term returns 0, try a 3-4 word variant — but do NOT assume a 2-word health term will be blocked.

---

~~### [2026-05-19] Session 21 — Situation Keywords Cluster 1 (Physical Discomfort at Work) — verdict~~
> ARCHIVED S28 — expired. Core conclusion (situation keywords with a SPECIFIC moment of discomfort outperform generic performance phrases) preserved + refined in S22/23 learning + S24 discriminating principle. Cluster 1 keyword verdicts preserved in keyword-map.md.

---

~~### [2026-05-19] Session 22/23 — Situation Keywords: что работает, что не работает~~
> ARCHIVED S29 — expired (Expires after Session 29). Core conclusion (situation keywords work only when they create a SPECIFIC moment with a concrete object-solution; wide emotional/psychological states fail) is fully absorbed into the S24 discriminating-principle entry below + reconfirmed by S29 (appearance/identity phrases "looking good"/"tired face" = no white-label object → 0). Keyword verdicts in keyword-map.md.

---

### [2026-05-23] Session 24 — Mental/biochemical states DEAD (3rd confirmation) + discriminating principle
**Type:** Pattern | **Severity:** HIGH | **Confidence:** HIGH (S22-S24, 6 keywords)
**Observation:** vagus nerve (193 adv) + overwhelmed (359 adv) → 0 reportable. vagus nerve device cluster IS real & active (Pulsetto, Sensate, Truvaga, Hoolest, Neuvana, Nuropod $900) but ALL branded-proprietary + premium ($150-900) → closed to white-label. overwhelmed = courses/supplements/pharma/charity/SaaS. **Discriminating principle (covers all 24 sessions): a keyword yields white-label physical DTC only if the problem has a PHYSICAL OBJECT as its obvious, immediate solution.** Physical/localized pain or concrete moment (tired feet, sitting all day, long flight) = yes. Wide mental/emotional/biochemical state (burnout, overwhelmed, cortisol, vagus) = market answers with services/pills/apps/branded-premium-devices = no. CLOSE Cluster 2 entirely. Recurring side-signal: weighted comfort animals (pulseofpotential) appeared in BOTH keywords from different advertisers — directional only, Marina vetoed the category.
**Applies to:** keyword selection — Cluster 2 (Stress/Mental) closed
**Expires after:** Session 30

---

~~### [2026-05-23] Session 24 — S25 direction note (non-binding)~~
> ARCHIVED S27 — expired. Superseded: S25/S26/S27 followed the Office×Positive Emotion direction (per _active.md S24 PIVOT + session prompts), NOT the Kids vertical floated in this note.

---

### [2026-05-23] Session 25 — Office × Positive Emotion (Cluster 5): yield + discriminating principle (positive side)
**Type:** Pattern | **Severity:** HIGH | **Confidence:** MEDIUM (5 keywords, S25 — first positive-emotion session)
**Observation:** First session of the S24 emotion-pivot (office vertical, love/delight/aspiration instead of pain). 5 keywords: desk plant ✅ (Ivy Gen 2 smart companion planter 72), candle warmer ✅ (Candle Warmer Lamp 70, ⚠️ везде-flag held for Marina), mug warmer ❌, cozy office ❌, aesthetic desk ❌. Yield 2/5 = consistent with situation-keyword norm. CONFIRMS S24 discriminating principle on the POSITIVE side: a positive-moment keyword yields white-label DTC only when the moment has a concrete PHYSICAL-OBJECT solution (companion gadget; flame-free cozy lamp). Fails when keyword is broad-lifestyle (cozy office = home/property search) or maps to the wrong object (mug warmer → the CUP not the device; aesthetic desk → branded-premium gear/furniture). Note: S25 direction was Office×Positive (per session prompt + _active.md S24 PIVOT), NOT the Kids vertical floated in the S24 direction-note.
**Applies to:** S26+ positive-emotion office keyword selection
**Expires after:** Session 31

---

### [2026-05-23] Session 25 — Two new NOISE classes on consumer/lifestyle keywords
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH (heavy across 5 keywords)
**Observation:** (1) Spam engagement-bait "story" accounts — garbage names (BrightMeadow 29, WildGarden7030, CalmMist 29), identical fiction copy ("I know you've been cheating on me", necrotic-fingers, kidney/BP/GLP-1 stories), 19-29 ads each, keyword-stuffed → they dominate fast_filter top-20 by ad-count signal on mug warmer + desk plant. (2) Real-estate/property listings flood broad lifestyle phrases (cozy office → realtors, apartments, sqft/beds/baths, sheds-as-"home office"). Both = pure noise; recognize by garbage-name + fiction-copy / property-listing pattern and skip fast. Possible fast_filter upgrade (advertiser-name + fiction-copy detection) — PROPOSAL, not auto-implemented (see Session Learning Report).
**Applies to:** all consumer/lifestyle keyword sessions — faster noise rejection
**Expires after:** Session 31

---

### [2026-05-23] Session 25 — Recurring SIGNAL: ambient/aesthetic desk lamp
**Type:** Signal | **Severity:** MEDIUM | **Confidence:** MEDIUM (3 keywords)
**Observation:** "Ambient/aesthetic desk lamp" recurred across candle warmer (candle-warmer lamps: MEVA/Glenbrookhome/Docos/Homira — 5+ brands = category convergence), and aesthetic desk (Solara bird lamp). Cozy/aesthetic desk LIGHTING is a recurring positive-emotion territory; candle warmer lamp = strongest convergence (reported 70). Directional only — Marina decides whether to deep-dive the lamp/lighting category next.
**Applies to:** S26+ — potential lamp/lighting deep-dive
**Expires after:** Session 30

---

### [2026-05-23] Session 26 — Recurring SIGNAL: companion plant-care gadget category converging (strengthens Ivy S25)
**Type:** Signal | **Severity:** HIGH | **Confidence:** MEDIUM-HIGH (4 keywords S26 + S25 Ivy)
**Observation:** The companion/AI plant-care gadget category that Ivy Gen 2 (reported S25, score 72) appeared to pioneer is NOT a lone player — it is converging hard. Ivy (store.plantsio.com) recurred across 4 S26 keywords (desk plant S25 → smart planter → desk pet → office plant). Independent siblings surfaced: PlantBot (plantsrobot.com, $89.90 companion-face "Plant Tamagotchi"), LeafyPod (theleafypod.com, $140-217 utility AI auto-watering, CES 2025), SENSO (Soildtech, CES 2026 gamified plant-Tamagotchi sensor, Kickstarter pre-launch). CRITICAL: Ivy's white-label path is now CONFIRMED — generic "Plantbot Upgraded Large Smart Flower Pot Pet Planter Robot" sells on Amazon (B0FNRGMZRQ) + PLANTSIO brand on Amazon (B0C8FKLPMW). Emotional hook = desk companion + "never feel lonely at your desk" + plant-keeping-guilt relief; demo-able face/expressions = strong UGC/wow. This is directional only (Marina decides whether to deep-dive the companion-planter category or treat Ivy as the single bet). The face/companion versions (Ivy/PlantBot, $79-90) fit positive-emotion office theme far better than the utility versions (LeafyPod $140+, no face).
**Applies to:** S27+ — companion plant-care gadget category; Ivy validation
**Expires after:** Session 33

---

### [2026-05-23] Session 26 — Two operational notes: narrow exact-phrase keywords + pharma "doctor"-spam on plant/wellness keywords
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH (S26)
**Observation:** (1) Hyper-narrow EXACT 2-word phrases can be genuinely thin in FB Ads Library, NOT a scraper bug: "desktop aquarium" = 8 advertisers (re-confirmed WITHOUT --since), "desktop fountain" = 1 advertiser. Back-scroll recovery (RULE 5d) fired repeatedly and found nothing = true exhaustion. Lesson: when a 2-word product phrase scrolls <15 unique even after recovery, it's a rare-phrasing keyword — try the common consumer phrasing ("fish tank", "betta", "tabletop fountain") rather than re-running. (2) Pharma/health "doctor-story" spam (fake cardiologist/kidney/menopause/hair-regrowth/gut narratives, NO DOMAIN, often single ad) now floods even plant/wellness keywords ("office plant") — a growing noise class alongside the micro-drama story-accounts (MYNVWIBCN, Passion Novels) and "scratched writing desk" repost-spam. Recognize by NO-DOMAIN + medical-fear narrative + generic name; skip fast. (3) Confirmed scroll-vs-JSON dedup gap: scraper scrolls more cards than it writes to JSON (desk pet 551 scroll → 201 unique; office plant 505 → 190) — report both numbers; the gap is dedup of repeat impressions + spam clusters, not lost signal.
**Applies to:** S27+ — keyword formulation + noise rejection
**Expires after:** Session 33

---

### [2026-05-23] Session 27 — Eye/screen cluster: heated eye mask = the lone white-label signal; blue-light glasses = hot-but-unsuitable class
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** MEDIUM (2 keywords S27)
**Observation:** "tired eyes" (262) + "eye strain" (229) are near-mirrors. The eye/screen-relief landscape splits into: (a) white-label physical = heated eye mask (Blinkjoy reported 67; warm-compress, legit mechanism) + eye massager (Sakerplus = duplicate of approved S1 product) + monitor light bar (Quntis ~62 sub-threshold); (b) NON-reportable but high-money classes = blue-light glasses (8+ advertisers Lockt/Slickweare/Moonighty/AZZARI/EyeQLenz/TechSpecs/Ocushield — пустышка [efficacy debated, ads themselves admit "clear ones don't work"] + везде + mostly price-floor), vision-correction пустышки (Lunisk "rely less on glasses"), eye supplements (Visiovance lutein), Rx pharma (Lynkuet/Xiidra), vision-surgery services. 2-word health term "tired eyes" was NOT FB-blocked (vs S21 "back pain"/"standing all day" blocked) → blocking is term-specific, not all 2-word health terms. Directional: blue-light glasses is a recurring large commodity cluster to skip fast on any eye keyword.
**Applies to:** S28+ — eye/screen/vision keyword sessions; noise rejection
**Expires after:** Session 33

---

### [2026-05-23] Session 27 — Lunch cluster reconfirms specific-product-phrase >> broad-situation-phrase; "portable powered meal device" territory
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** HIGH (3 keywords S27 + consistent with S24/S25)
**Observation:** Specific PRODUCT phrase "heated lunch box" (30 unique adv — thin but real, 563 scroll→30 = heavy ad-repeat + spam, NOT a bug) → Cordless Self-Heating Lunch Box (Luncheaze-validated, score 73). Broad SITUATION phrases "office lunch" (247) + "on the go" (377) → 0 reportable: food-delivery/catering services, job-recruitment, established mega-brands, supplements, banks, apps. This is the Nth confirmation of the S24/S25 discriminating principle (concrete physical-object phrasing wins; broad situation/lifestyle phrasing = service/brand noise). New territory surfaced: "portable powered meal device" — Luncheaze (cordless WARMER, $119-240, white-label $49-69) + Itaki Bento PRO (portable COOKER, $69.95/$140, ~63 sub-threshold, Marina-kept, quality-risk). Both validate that powered lunch gadgets convert; warmer (broad use) > cooker (narrower cook-at-desk behavior + durability concerns). NOTE: micro-drama/fiction NO-DOMAIN story-spam ("I lost my job and home" romantasy ×7, "Chapter 1: Rock Bottom" ×3) now dominates even narrow product keywords (heated lunch box), not just broad lifestyle ones.
**Applies to:** S28+ — keyword selection (prefer specific product phrases); meal-gadget category
**Expires after:** Session 33

---

### [2026-05-24] Session 28 — Commute keywords = broad-situation noise; "car organizer" = clean signal but commodity category
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** HIGH (3 keywords S28 + consistent with S24/S27)
**Observation:** "morning commute" (288) + "long commute" (376) → 0 reportable. Nth confirmation of the discriminating principle: "commute" is a CONTEXT, not an object → market answers with car-dealerships (Mazda/Ford/Honda ×8+), real-estate/leasing, apparel/footwear, makeup, supplements, branded-premium (RayNeo AR/Coldest), + an e-mobility cluster (ebikes/e-skateboards/treadmills positioned as commute-replacements, all out of price/logistics). Recurring commute-relevant angles (car scent diffuser, open-ear/safety audio eyewear, commuter backpack) all branded/commodity. CONTRAST: "car organizer" (164) is a PRODUCT phrase → it surfaces the RIGHT advertiser TYPE (direct DTC, zero dealer noise — cleaner than commute phrases) BUT the entire category is low-price commodity dropship ($5-30: trunk organizers, seatback bags, headrest hooks, cup organizers, trash bags) + Temu/Alibaba direct competition → no differentiated white-label hero $39-100. New failure-mode distinction: commute = WRONG-advertiser-type noise; car organizer = right-type but WRONG-category-economics. Confirms S3 car-organizer note.
**Applies to:** S29+ — keyword selection (commute/context phrases dead; even clean product-phrases can fail on category economics)
**Expires after:** Session 34

### [2026-05-24] Session 28 — Wrist/hand pain = "пустышка-magnet" pain class; heat-therapy hand massager = emerging sub-threshold sub-category
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** MEDIUM (3 keywords S28 — within-session)
**Observation:** "sore wrists" (74, genuinely thin) + "wrist pain" (310) + "hand strain" (242) → 0 reportable. The pain is localized & physical (so it has physical-object solutions), yet the dominant DTC monetization is UNVERIFIABLE-RESULT therapy that Marina hard-rejects: copper/hematite/magnetic/red-light bracelets & wraps (10+ advertisers on "wrist pain" alone: Copper Compression, Hematix ×3, Hemios, Vera's Copper ×2, Kovaria TheraWrap red-light), + supplements (turmeric/Haritaki), + medical/insurance services (Medicare-brace scam, chiropractors, joint clinics), + commodity compression gloves/braces ($15-30). The legit verifiable-result device tier is either commodity (gloves/braces below floor) or established-Amazon (hand massagers). "hand strain" is noisiest — "strain" disambiguates to eye-strain (CliC readers ×3), cable strain-relief (RJ45 crimper), gaming strain (Nyxi/Floky), dog-neck strain. EMERGING SUB-CATEGORY (directional): heat-therapy wrist/hand massager — 2 fresh single-product DTC, Reava ThermaWrap (heat+compression, $99.99) ~63 SOFT + Movella Wrist Device (heat+vibration, price hidden, "restore circulation/tingling" = пустышка-lean) ~60-63 — both sub-threshold, both пустышка-circulation-adjacent, both vs established Comfier/Breo on Amazon. NOTE per RULE 14: "close the wrist/hand-pain class" would be a Tier-2 generalization → flagged as a PROPOSAL for Marina, not auto-written here.
**Applies to:** S29+ — pain-keyword selection; recognize пустышка-therapy-jewelry cluster (copper/hematite/magnetic/red-light) for fast rejection on any pain keyword
**Expires after:** Session 34

---

### [2026-05-24] Session 29 — Appearance/identity keywords = beauty/service-owned (0 white-label); paired A/B confirms qualifier shifts noise, not yield
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** MEDIUM (4 appearance keywords S29 + consistent with S17/S20/S24)
**Observation:** Full session = 6 keywords, 0 reportable. Four appearance/identity phrases — "looking good on zoom" (266), "looking good" (377), "tired face on camera" (207), "tired face" (282) — ALL 0. The moment "look good / not look tired" is owned by skincare/cosmetics/apparel/shapewear/aesthetic-services/pharma + business-opp-coaching, NOT white-label gadgets → Nth confirmation of the S24 discriminating principle (a keyword yields white-label DTC only if the moment has a concrete PHYSICAL OBJECT as its obvious solution; "appearance" → solution is cream/makeup/clothes/procedure). **Marina's deliberate A/B (paired keywords, qualifier removed):** removing "on zoom"/"on camera" MEANINGFULLY changed noise COMPOSITION but NOT the 0 outcome — "on zoom" added a business-opp/B2B-agency/remote-work layer (Zoom=work calls); bare "looking good" broadened to apparel/shapewear/body; "on camera" added content-creator/camera-gadget + Ozempic-story; bare "tired face" added local med-spa services + pharma. Takeaway: the real lever is whether the qualifier points to a CONCRETE PHYSICAL OBJECT (ring light/webcam/selfie monitor) — here those traces were branded (eMeet)/commodity/cloaked-affiliate, so both versions flopped. Two situation phrases also 0: "working from bed" (235) — expected ergonomic objects (lap desk/bed tray/wedge pillow) had ZERO hits, phrase lives in pain/story-narratives; "stuck in traffic" (288) — reconfirms S28 commute=context-not-object. NEW noise sub-classes logged: cloaked-affiliate (ad describes product X, store is unrelated — soyummy food site / velluci jewelry); cloned local med-spa promo-network (6+ "Derma-Lift $99" city accounts on one creative). NOTE per RULE 14: "close the appearance/identity-phrase class" = Tier-2 generalization → flagged as PROPOSAL in Session Learning Report, not auto-written.
**Applies to:** S30+ — keyword selection (appearance/identity phrases low-priority regardless of qualifier; prefer qualifiers that name a concrete physical object or physical-friction moment)
**Expires after:** Session 35

---

## Expired / Promoted

> Entries with `Expires after: Session N` where N ≤ current session are archived here by the agent at STEP 8.
> Do NOT delete archived entries — keep as historical record.

> **Per-session archival log (Sessions 13–30) moved to `learnings-archive-queue.md`** (S30 cleanup, 2026-05-24) to keep this every-session-read file lean. Inline tombstones remain in Active Learnings above; full archival history lives in the queue file.
> **At STEP 8 going forward:** drop the full "АРХИВАЦИЯ Session N" block into `learnings-archive-queue.md`; leave only the strikethrough tombstone in Active Learnings here.

---

## How to Add a New Learning

**Before adding:** check all Expires after dates in Active Learnings. Archive any entry where N ≤ current session number (move to Expired section above).

Append new entries using this format:

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW / MEDIUM / HIGH / CRITICAL
**Confidence:** LOW (1 weak signal) / MEDIUM (2-3 cases) / HIGH (multiple or founder-confirmed)
**Observation:** what was found (2-5 lines max)
**Applies to:** [keyword category / product type / search method]
**Expires after:** Session [N+7] or "Never" (Never = add to op-rules.md instead, not here)
```

**Where does it go?**
- Expires: Never → op-rules.md (not learnings.md)
- Keyword verdict (this keyword is dead/good) → keyword-map.md (add table row)
- Temporary tactical discovery → learnings.md (here)

**Size rule:** keep Active Learnings under 20 entries total. Archive expired before adding new.

## Promotion Rules

A learning may be added to `review/promotion-queue.md` only if:
- confirmed across **3 sessions**, OR
- **explicitly approved by Marina**

Never self-promote into core/ files.
