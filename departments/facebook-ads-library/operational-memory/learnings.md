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

**The active research direction is NOT hardcoded here** — it lives in
`departments/facebook-ads-library/hypotheses/_active.md` (single source of truth). Read it at
session start. _(As of S21+: Situation Keywords. Broad Horizontal Discovery was CLOSED/FAILED S20.)_

- **Primary discovery:** Facebook Ads Library via VPS scraper.
- **Secondary:** Amazon, TikTok, AliExpress — verification only.

---

## Active Learnings

> **Archived tombstones (S10–S30) — full blocks in `learnings-archive-queue.md`.** Compact migration map below — every finding's permanent home:
>
> | Sessions | Topic class | Migrated to |
> |---|---|---|
> | S10–S11 | Keyword Audit DB; Kids Travel Sleep Nest | memory `project_keyword_audit_system.md`; `reported-products.md` |
> | S15–S20 | Broad Horizontal Discovery hypothesis (perf-signal kw / `--since` / category-tracking / 15+kw pattern / final tally) | `hypotheses/broad-horizontal-discovery.md` status:CLOSED FAILED; queue |
> | S16–S19 | Dead keyword classes (gadget / offer-promo / urgency-credibility / % URL-encoding) | `keyword-map.md` verdicts; S18 `quote_plus` fix superseded |
> | S19 | 0-result phrase anomaly | superseded by S21 FB-block refinement |
> | S21 | FB blocks 2-word terms (refined S27/S28: term-specific, not class) | `keyword-map.md` |
> | S21 | Situation Cluster 1 verdict | `keyword-map.md`; absorbed into S22/23 + S24 active entry below |
> | S22–S25 | Situation Keywords iterations + discriminating principle (negative + positive sides) | `keyword-map.md` "Active Hypothesis S21" (foundational); absorbed into S24 active entry below |
> | S25 | Two new noise classes (spam-story + real-estate); ambient-desk-lamp signal | `rejected-products.md` per-session pattern summaries; Candle Warmer Lamp Marina-Rejected closed |
>
> **PROMOTED (graduated to permanent op-rules):**
> - S18 scraper URL encoding `quote_plus` fix → FB `op-rules.md` RULE 5c
>
> (Per **RULE-15** — see `core/session-health-rules.md` — tombstones collapsed when they exceeded 30 lines / 20% of active file.)

---

### [2026-05-16] Session 10/11 — Scraper "started" date: structural limitation
**Type:** Warning | **Severity:** MEDIUM | **Confidence:** HIGH
**Observation:** Field `started` (campaign start date) — Tier-1 signal for Entry Window scoring. Scraper captures it only when FB explicitly shows it in the card. For many advertisers it returns "?". This is a structural pipeline limitation, not a scraper bug.
Workaround when start date is critical: WebFetch brand/About page → founding date; or WHOIS / domain registration date; or first Amazon/Trustpilot review date.
Important: do NOT make this a mandatory step for every advertiser — only when Entry Window score is decisive for the 65/70 threshold.
**Applies to:** All VPS scraper sessions — Entry Window scoring
**Expires after:** Until `started` field is fixed in scraper (or permanent if never fixed)

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

### [2026-05-24] Session 30 — Positive-moment concrete keywords yield 2/5; cat-vs-dog desk asymmetry; vacuum-compression travel signal
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** MEDIUM (5 keywords S30 + consistent S24/S25)
**Observation:** 2/5 reportable — best positive-emotion session since S25. WORKED: "pack for a work trip" (518) → Rhona TravelVac Pro 74 (cordless 4500Pa vacuum compression + 3 bags, 2+ advertisers); "cat on desk" (552) → Desk-Mounted Cat Bed 76 (Desk Nest $159 "original"+media + Ergo Purrch 96 rev 4.9★ = 2-brand convergence Mar-May 2026). FAILED: "train ride" (502, ambiguous CONTEXT → railroad-tourism + athletic-training + truck-horns), "kitchen table office" (569, pharma "doctor-story" spam magnet; WFH ergonomic objects ABSENT — mirrors S29 working-from-bed), "dog under desk" (500). **CAT vs DOG ASYMMETRY (fresh confirmation of the discriminating principle on the positive side):** the SAME structural pattern "[pet] [position] desk" yields a product for cats (perch ON desk → novel desk-mounted object exists) but NOT dogs (lie on floor → only generic dog-bed, not desk-tied + pet services + POD + spam). The subject's physical behavior determines whether a concrete PHYSICAL OBJECT owns the moment — not the keyword shape. **SIGNAL:** vacuum-compression travel packing = recurring multi-advertiser convergence (Rhona TravelVac + Luux VacPack $79 + The Foldie + generic compression cubes = 4+ independent advertisers); the cordless-electric-pump version is the differentiated gadget vs commodity manual roll-bags.
**Applies to:** S31+ — positive-emotion / pet×office keyword selection; recognize cordless vacuum-compression travel category
**Expires after:** Session 37

---

### [2026-05-24] Session 31 — Worker PAIN/CONDITION keyword half is worked out (clean 0/7); consumable + founder-closed + пустышка traps
**Type:** Pattern | **Severity:** MEDIUM | **Confidence:** MEDIUM-HIGH (7 keywords S31 + consistent S21-24/S28)
**Observation:** 0/7 reportable. Seven outdoor/manual/driver worker physical-condition phrases (hands cracked from work 202, working in the cold 225, working outside all day 245, back pain driving 263, coffee in the car 246, driving for hours 295, losing your voice 238) all → 0. They systematically resolve to one of four dead answers: (1) **consumable commodity** (hand balm/salve/lotion-bar, coffee beans/capsules, merino work socks) ≤floor/non-white-label; (2) **founder-closed saturated category** (driving seat cushions ×3 brands Femzene/Housewor/Bodiform = exact S19 reject; posture braces); (3) **пустышка-therapy** (neck/leg/sciatic/circulation devices — Veto class; Nth confirmation of S28 "пустышка-magnet pain class"); (4) **pure context-noise** (auto dealers, trucking/CDL recruitment, supplements, pharma, medical services). This is the pain/condition mirror of office-pain Clusters 1-4 (S21-24): that half is largely worked out. NEW REFINEMENT of the discriminating principle: a worker-condition phrase yields white-label DTC only if the condition's obvious physical solution is (a) a NON-CONSUMABLE object AND (b) not already a saturated/пустышка commodity. "cracked hands→cream", "voice→nothing", "driving back→cushion(closed)" all fail both tests. "expected-object-absent" recurred again (heated-apparel on cold; sun/cooling on outside; car-coffee gadget on coffee-in-car [mirrors S25 mug-warmer→CUP]; voice-amplifier on losing-voice) — 3rd-4th time after S29/S30. Operational confirms: "back pain driving" NOT FB-blocked (263) — block is term-specific to exact "back pain" (S21→S27/S28 refinement). Best non-noise find: Loudcup horn-tumbler (sports-parent, viral) — patent-pending/branded, not white-label, ~58.
**Applies to:** S32+ — keyword selection: deprioritize bare worker pain/condition phrases; prefer positive-emotion concrete-object moments (S25/S30 winners) or specific product-nouns
**Expires after:** Session 38

---

### [2026-05-24] Session 32 — Office/work positive-SITUATION phrases = digital/service/premium-branded/fashion-owned (clean 0/7); meetings→SaaS, work-bag→fashion, sleep→пустышка
**Type:** Pattern
**Severity:** MEDIUM
**Confidence:** MEDIUM-HIGH (7 keywords S32 + consistent S24-S31)
**Observation:** 0/7 reportable + 1 borderline (Traceley slim Find-My tracker ~62). Seven office/work positive-situation phrases (working late tonight 215, work bag essentials 212, weekend project 315, back to back meetings 338, working from coffee shop 218, meetings all day 303, sleeping after night shift 200) → 0. These are CONTEXTS (busyness/late-night/nomad/DIY/sleep), not concrete-object moments → market answers with DIGITAL/SaaS (Granola AI meeting-notes recurring on BOTH meetings keywords + ClickUp/ListKit/CoPilot; micro-drama/novel apps), SERVICES/coaching, PREMIUM-BRANDED tech above ceiling (X-Nomad portable monitor $299-599, Rokid AR $300+ = RayNeo S28 recurring), FASHION/apparel (handbags, non-iron shirts), CONSUMABLES (MAXL detailing spray, mushroom coffee), and ПУСТЫШКА-health (red-light sinus/grounding mat/anti-snoring). THREE sub-findings: (1) **"meetings" keywords = B2B-SaaS-owned** — back-to-back & all-day meetings are near-mirrors, both owned by AI-meeting-notes SaaS + lead-gen software + coaching; a "meeting" is a software/service moment not a physical-object moment (informs the K8 "taking notes at meetings" skip — same landscape). (2) **"work bag essentials" = clean product-phrase but fashion/saturated category** (mirror S28 car-organizer / S30 Luux duffle): right advertiser TYPE, but resolves to fashion handbags (return-risk/везде) + saturated travel backpacks (Oono) + reconfirmed garment-duffels (Halfday/Luux S30). (3) **"sleeping after night shift" = пустышка-magnet** + "expected-object-absent" 5th+ recurrence (blackout mask/white-noise/curtains advertised under direct nouns, not the situation phrase). **Best find = Traceley slim Find-My tracker card ~62** (1894 rev 4.7★, differentiated vs Tile Slim, but sub-$40 floor + tracker везде/branded-dominated) → SOFT, retry S37. NOTE per RULE 14: "office/work positive-SITUATION CONTEXT phrases (busyness/meetings/nomad/sleep) = low-priority class" would be a Tier-2 generalization → flagged as a PROPOSAL in Session Learning Report (joins S28/S29 pending proposals), NOT auto-written.
**Applies to:** S33+ — keyword selection: office/work CONTEXT/situation phrases low-priority (resolve to SaaS/service/premium-branded/fashion); prefer concrete-object moments (S25/S30 winners: desk plant, candle warmer, pack-for-trip, cat-on-desk) or specific product-nouns
**Expires after:** Session 39

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
