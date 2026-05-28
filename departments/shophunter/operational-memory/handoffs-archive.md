# ShopHunter — Handoffs Archive

Historical `HANDOFF → NEXT SESSION` blocks moved here per **RULE-15** (memory rotation; see `core/session-health-rules.md`).
Active `learnings.md` keeps only the 2 most recent handoffs (SH-10 + SH-9 as of 2026-05-28).
Plain markdown — search via `grep -rn "SH-N" departments/shophunter/operational-memory/`.

**Move log:**
- 2026-05-28: archived SH-4, SH-5, SH-6, SH-7, SH-8 handoff blocks + the "HANDOFF → SH-4 (SUPERSEDED)" section from `learnings.md`.

---

> _SH-8 handoff below kept for history — T&G 100% done; funnel mechanics + structural safeguards + the 2 pre-loaded dumps (A&P now DONE; **Business & Industrial 356 still ready**) remain valid. SH-9 above is current state._

**✅ SH-8 DONE (2026-05-26) — Toys & Games 788 FULLY PROCESSED + 2 NEW category dumps pre-loaded + structural safeguards added.**
- **T&G 788 done** (B1 [0:197] · B2 [197:394] · combined B3+4 [394:788]; hero 100%, enrich 97-99%, cut clean). **0 reported 65+ + 0 founder-keeps across the WHOLE niche.** Best borderline: engraving pen ×2 (Resparked+Culiau ~64), busy board ×3 (TibaToes/Nooche/Joycat ~64 saturated), Montessori climber/tower ~58. **No "Toys & Games" collection seeded** (Marina: shops "ни о чём" — skip). Files: VPS `logs/shophunter/tg_b{1,2}.json` + `tg_b34.json` + `_hero/_enrich_in/_enriched` + sentinels.
- **T&G = product-dense but LOWEST white-label-fit niche so far** (branded toys + golf mega-cluster ×20+ + commodity TikTok toys + emulators ×8 + magnetic tiles ×6 + RC/drones + mis-niched). Full → `shared/rejected-products.md` SH-8.
- **🆕 2 NEW NEXT-CATEGORY DUMPS PRE-LOADED ON VPS (Marina-requested, both EXHAUSTED cleanly = full surface):** `logs/shophunter/animals_pet_supplies_shops.json` = **860** (12-scroll exhaust) + `logs/shophunter/business_industrial_shops.json` = **356** (12-scroll exhaust). Same field schema. **SH-9 can start immediately (no dump needed).** v2 robust re-verification of both was run for completeness (counts in the SH-8 active-learning below). Reusable dump = `scripts/sh_cat_dump.py "<Cat>" <dest> 8000 <sentinel>` (target 8000 forces exhaustion; category selected by exact label click).
- **🔧 STRUCTURAL SAFEGUARDS ADDED (SH-8, Marina-approved — purely additive) → `methods/discovery-funnel.md` "Structural safeguards" + `subagent-spec.md`:** (1) "Tier A/B/C" → **"Revenue-Tier"** = sort-aid, never quality (read ALL A+B+C); (2) **browse-pool = mandatory** funnel output; (3) **Description-confidence gate** — genuine candidate with empty/mismatched `desc` MUST get a WebFetch verification BEFORE tiering (the SlotPro ~52→66 fix, now structural). `desc_confidence` enricher flag = agreed next CODE change (apply+test next batch run). Does NOT touch the conservative cut / deep-score / human-in-loop.
- **📌 STRATEGY (Marina, SH-8 discussion — for SH-9+):** (a) **Paid ShopHunter DEFERRED** — it does NOT expand the universe (the ~800/category = its TRACKED inventory-depletion subset, NOT the whole Shopify market; verified how it works); may revisit. (b) **Bottleneck #1 = input universe** (traction-biased tracked subset misses emerging stores = the early-window winners). Eventual fix = a **breadth tool (Storeleads ~2.8M stores, revenue-filterable)** as a future department; ShopHunter then = the DEEP-tracking layer we feed our best finds into (Marina's idea — makes its base high-quality). (c) **Newest-First on ~140 mature stores = LOW ROI** → deprioritized. (d) **Batch size 170-200 optimal**, ~200 cap (362 worked but thins per-item attention + 2-worker proxy ~8 min). (e) Marina testing other niches on the $1 trial today/tomorrow → more data before any tool decision. **Deeper "big department" design = AGREED for a later session** (no paid AI-API needed — pre-score via free rules; only flat-fee data sub + cheap rotating proxy if scaling to thousands).
- **NEXT SESSION (SH-9) options (Marina picks):** (a) process **Animals & Pet Supplies (860)** or **Business & Industrial (356)** — both ready on VPS, same funnel + seed niche collection if yield; (b) **Health & Beauty** dump (un-mined, historically our winner-zone — needs a dump run); (c) breadth-tool (Storeleads) pilot + compare on one niche. **Founder Review for the 3 SH-7 cards (Manta Ray, SlotPro, Panda Drum, Birdfy) still Marina-to-set in Notion; SH-8 added no products.**

---

> _SH-7 handoff below kept for history — A&E 100% done; funnel mechanics + collection structure + calibrations still valid. SH-8 above is current state._

**✅ SH-7 DONE (2026-05-26) — Arts & Entertainment 823-store dump FULLY PROCESSED (4 batches ~206, human-in-loop).**
Matured funnel ran clean on all 823: hero **823/823 = 100%**, enrich reach **98%** (b1 163/168 · b2 174/174 · b3 171/172 · b4 170/172), conservative cut 32-38 dropped/batch (0 winners lost). Funnel files on VPS `logs/shophunter/`: `ae_b{1,2,3,4}.json` (slices) + `_hero/_enrich_in/_enriched.json` + sentinels.
- **YIELD: 2 reported 65+ + 2 founder-kept = 4 Notion cards.**
  - **B1 [0:206]:** **Wooden Kinetic Manta Ray Automaton 66** (EverWoods $149 + Victmax $98 = convergence ×2; "moves like magic" kinetic wow = the niche standout). Borderline: Clyde's leather recolor 64 · Sorso wine 3-in-1 61 · Sculpd pottery 61.
  - **B2 [206:412]:** 0 winners. Borderline: Doctor Who book-nook ~60.
  - **B3 [412:618]:** 0 winners. **Founder-kept: Panda Drum 58** (Marina saw FB ads firsthand → 247 ads/690 rev/72K cust/media; REAL price $159.95 NOT SH-est $45) + **Birdfy 60** (niche-study, cf PerchMe S5 64; branded/166-patents/€139-299).
  - **B4 [618:823]:** 0 winners. **SlotPro slotted quilting ruler 66** (Marina-spotted from browse-pull → verified → rescored ~52→66; 26-channel blade-guide ≠ flat-ruler commodity; convergence ×4-5; quilting-niche). Borderline: AeroBand PocketDrum ~58.
- **COLLECTIONS SEEDED:** NEW niche **"Arts & Entertainment" = 40 shops** (everwoods seed + 39 added, 0 fail) + all 40 also added to general **"Shops"** (added=40 / already=0 / fail=0 → Shops ~100→~140). Verified cross-correct (SlotPro ∈ A&E+Shops, ∉ H&G/B&T). Tool: `sh_collection_manage.py` (toggle-safe — only clicks "Add"). 40 seed-ids in `/tmp/ae_coll_*.log`. **3 niche collections now: Home & Garden 47 · Baby & Toddler 53 · Arts & Entertainment 40.**
- **A&E = LOW white-label-DTC density niche (Tier-1 yield obs, NOT a rule — do NOT close the niche):** surface resolves to POD/personalized gifts (dominant) + apparel/jerseys/socks + craft-hobby kits/supplies (pottery/resin/diamond-painting/embroidery/book-nooks/3D-pens) + musical instruments (branded/niche) + collectibles (anime/replica models) + decor + books + digital. Genuine white-label problem-solvers $45-79 are rare → structurally weaker store-first yield than H&G / B&T. Convergence clusters: leather-care ×3 · slotted-ruler ×4-5 · wine-accessories · diamond-painting ×4 · anti-theft-travel ×2 · bird-cam (Birdfy+PerchMe) · gold-rose ×3 · US-250th patriotic (cross-batch) · Sculpd ×4-geo. Full → `shared/rejected-products.md` SH-7.
- **NEXT SESSION (SH-8) options (Marina picks):** (a) **Toys & Games (788)** — ALREADY dumped+verified on VPS (`logs/shophunter/toys_games_shops.json` = 788, v1=v2) → run same funnel + seed "Toys & Games" niche collection; (b) **Newest-First check-up** on the now 3-niche collection (~140 shops base); (c) Explore PRODUCTS surface / geo-test. A&E 823 = 100% done. **Marina DEFERRED Toys & Games to a fresh session (context preservation).** Founder Review for the 4 SH-7 cards = Marina to set in Notion (agent never sets it).

---

> _SH-6 handoff below kept for history — B&T 100% done; its funnel mechanics, niche-collection structure, and process calibrations are STILL VALID. SH-7 above is current state._

**✅ SH-6 DONE (2026-05-26) — Baby & Toddler 717-store dump FULLY PROCESSED (4 sub-batches, human-in-loop).**
Matured funnel ran clean on all 717: hero **99–100%**, enrich **97–100%**, conservative cut 14–19 dropped/batch (0 winners lost). Funnel files on VPS `logs/shophunter/`: `bt_b{1,2,3,4}.json` (slices), `_hero/_enrich_in/_enriched.json`, sentinels; seed accumulator `bt_collection_seed.json` + final `bt_collection_final.json` (53 ids).
- **B1 `[0:180]`:** 5 winners 65+ (Swaddelini 72, WEMOH dual-cam car monitor 71, Sleep Like Goldilocks temp-predictor 67, Veba milk-freshness monitor 66 [Needs-Verif/Shark-Tank], Baby's Brew bottle warmer 66 +BabyBuddy) + 2 founder-keep (Peazy Pouch food-maker 62 "novel idea"; Little Manta lounger 55 = ad-research asset).
- **B2 `[180:360]`:** 2 winners 65+ (Grownsy baby food maker 66 +Bear NutriEase conv; Sleepout blackout curtain 65 ⚠heavy-textile shipping).
- **B3 `[360:540]`:** 0 new winners + 2 founder-keep (FetalPlus fetal-doppler store 63 "compare vs WellnessBaby 83"; Sleepy Baby motorized-tapper 60).
- **B4 `[540:717]`:** 0 new winners (pure convergence-confirmation).
- **TOTAL Notion: 7 winners 65+ + 4 founder-keep = 11 cards.** B3/B4 honest 0-winner = normal store-first (don't catastrophize).
- **COLLECTION SEEDED + RE-ORGANIZED INTO NICHES (Marina's structure):** 53 B&T shops bulk-added to the general **"Shops"** collection (53 ADDED / 0 FAIL, 0 overlap) → Shops now ~100. Then split into per-niche collections: **"Baby & Toddler" = 53** (the B&T shops) + **"Home & Garden" = 47** (prior SH-3/4/5 shops). A shop lives in BOTH "Shops" + its niche. Verified cross-correct (B&T ∈ Baby&Toddler+Shops, ∉ Home&Garden; vice-versa; Shops intact for all).
  - **Tool: `scripts/sh_collection_manage.py`** (TOGGLE-SAFE create/add/verify/list — only clicks "Add", never "Remove"). **Reliable membership = the dialog's per-collection Add/Remove label** (the `/collections/shops` page UNDERCOUNTS due to DOM virtualization — never trust the page count). Full mechanic in `methods/interface-guide.md`.
- **NEXT-CATEGORY DUMPS PRE-LOADED ON VPS (Marina-requested, completeness VERIFIED via 2 robust runs each):** `logs/shophunter/arts_entertainment_shops.json` = **823** (v1=v2, 0 diff) + `logs/shophunter/toys_games_shops.json` = **788** (v1=v2, 0 diff). Same field schema. SH-7 can start processing immediately (no dump needed).
- **B&T PATTERNS (Tier-1):** 🔥 convergence-dense niche — **bottle warmer ×8** (Baby's Brew flagship), **carrier ×15+** (commodity/branded → monitor; type reported Ring Sling 73), **baby food maker ×7** (Grownsy/Bear flagship), **breast pump ×8** (branded/competitive), **swaddle ×3**, **baby-car-cam ×2** (WEMOH), **baby-patter/motorized-soother ×2** (Sleepy Baby+Baby Patter — NEW micro-category), pregnancy/postpartum-belt cluster, smart-baby-monitor mini-cluster. **B&T surface heavy with mega-brands** (LÍLLÉbaby/Tula/Ubbi/Infantino/SNOO/Bugaboo/Cybex/UPPAbaby/Babymoov/Béaba/Momcozy/Elvie/VTech/CuboAi) + fashion-bags/plushies/supplements/decor-lamps noise (revenue-inflated → Tier-A but NOT ours). Pre-flight skew (apparel/decor/feeding-consumables) confirmed.
- **⚠️ SAFETY (ShopHunter HARD-reject class):** inclined infant sleepers + prone cushions + baby floats = FDA-BANNED / drowning-risk (Anytoyz Incline Bed, Babocush, Mambobaby). Never report. → **Marina (2026-05-26): keep as a ShopHunter-level reject, NOT promoted to core.**
- **NEW Marina process calibrations SH-6** (full → founder-feedback.md, folded into `methods/discovery-funnel.md` Reporting protocol): (1) CHECKPOINT FIRST → Notion only after OK; (2) ALL checkpoint links CLICKABLE; (3) browse-links UNIQUE only (no dup of winners/borderline); (4) heavy-textile/bulky → score logistics+margin harder; (5) Tier A/B/C = machine revenue sort-aid, Collection seed = manual judgment-pick across ALL tiers (count ≠ Tier-A; B1 14 seeded ≠ 24 Tier-A).

**NEXT SESSION (SH-7) options (Marina picks):** (a) **process Arts & Entertainment (823) or Toys & Games (788)** — both ALREADY dumped+verified on the VPS, run the same matured funnel (hero→cut→enrich→deep-score) + seed into "Shops" + a new niche collection; (b) **Newest-First check-up** on the now niche-organized collection (un-park the parked hypothesis — base ~100 + per-niche makes Similar/Ads/Products cleaner; scrape Products→Newest-First → seen-id dedup → cut/desc → surface NEW); (c) Explore PRODUCTS surface (different index) or geo-test US→UK/DE/AU. B&T 717 is 100% done. **NOTE (2026-05-26): Marina's founder-review pass is DONE — all SH-5/SH-6 statuses + Founder Notes + Rejection Reasons are SET in Notion AND mirrored to `founder-feedback.md` (Decisions table). Nothing pending.**

---

> _SH-5 handoff below kept for history — its funnel mechanics, PROXY note, seeding rule, and Newest-First-monitor idea are
> STILL VALID. SUPERSEDED parts (now DONE in SH-6 above): "NEXT SESSION = Baby & Toddler", the SH-6 execution plan, "Collection
> holds 47 shops", and "grow the collection next session" — B&T is 100% processed + the collection is now ~100 and split into
> niche sub-collections. Read the SH-6 block above for current state._

**SH-5 DONE (2026-05-26) — H&G master dump FULLY PROCESSED (830/830).** Ran the matured funnel on the remaining
**409 stores = `new[300:709]`** in 3 sub-batches (b1 150 / b2 150 / b3 109). Per-batch: hero 98–99%; conservative cut via
NEW clean parametrized `scripts/sh5_cut.py` (drop ONLY dead / no-physical-in-top3 / пустышка-hero / all-extreme-price w/
[$25,$220] pad; service-SKU dig; ~12–18 dropped per 150, nothing lost — Tier-C leak-checks all clean); enrich reach
**97–100%** (2-worker paced proxy = the validated config, NO throttle — better than SH-3's ~76%); per-stage PNG renders via
NEW `scripts/sh5_render.py` (args: `<TAG> <stages>`; stage-5 reads `<TAG>_verdict.json`).

**YIELD (409 stores):** b1 → **2 reported** (nulooa DeepVac **66**, Hago Smart Coffee Maker 3-in-1 **65**) + 1 founder-kept
(Spray Blender 53) + monitor-convergence (titanium boards now ×4: +Taima $386K/wk, +Jouvane stainless). b2 → **0 reported**
+ Sans Water Purifier $824K/wk = money-only monitor. b3 → **0 reported** + **PerchMe Smart Bird Feeder Camera $90 = 64
borderline** (Bird Buddy-class — the session's ONLY genuine-WOW find). **cookinate Juice&Milk Maker** = convergence 2nd-brand
for OroMilk → added as OroMilk **Store Link 2** (Marina-spotted). All 65+ + founder-kept in Notion + reported-products.md.

**H&G STATUS: 830-store master dump is now 100% processed** (SH-3 150 + SH-4 300 + SH-5 409).

**NEXT SESSION = BABY & TODDLER (Marina-chosen).** Stage-0 dump DONE this session: **`logs/shophunter/baby_toddler_shops.json`
= 717 stores** (US 608 / AU 29 / GB 20 / DE 15 / IN 9; 197 with FB ads; infinite-scroll exhausted cleanly at 717 — same
clean-exhaust pattern as H&G 830). **COUNT VERIFIED (SH-5):** a 2nd robust re-run (`sh_cat_dump_v2.py` — slower scroll +
back-scroll recovery ×4) produced an IDENTICAL set — 717 vs 717, 0 diff. 717 is the true ceiling of ShopHunter's tracked-shop
Explore-Shops surface for B&T (NOT the whole Shopify baby market — Marina expected ~1500; ShopHunter only indexes traction
stores). To go wider later: try sort variations / Explore PRODUCTS (different index). Same field schema as the H&G dump. Reusable dump script = **`scripts/sh_cat_dump.py
"<Category>" <dest> [target] [sentinel]`** (generalized from sh_hg_dump.py; category set via checkbox-click on the label).
Run the SAME matured funnel on it (hero → conservative cut `sh5_cut.py` → enrich → deep-score; renders `sh5_render.py`).
**SH-6 EXECUTION PLAN (Marina-set):** process the 717 in **4 sub-batches of ~180** — `new[0:180] / [180:360] / [360:540] /
[540:717]` (order of baby_toddler_shops.json; fresh dump, NO dedup needed). **Cadence = per-batch CHECKPOINT + WAIT for
Marina's explicit "go" before the next** (human-in-loop, NOT autonomous). Each batch report (Reporting protocol): winners 65+
→ Notion · borderline 55–64 flagged · patterns · browse-links by default. **Collection seeding = collect qualifying shops
across ALL 4 batches → show Marina ONE list at session END → bulk-add once** (`sh_collection_add.py`, toggle-safe) per the
Collection seeding rule. Screenshots ONLY on request.
⚠ **PRE-FLIGHT:** Baby & Toddler will skew heavily to baby APPAREL/clothing + nursery DECOR + feeding CONSUMABLES — the
genuine white-label GADGET subset (monitors, sleep/sound aids, feeding/bottle devices, safety gadgets, carriers) is a
SMALLER fraction (but baby sleep sacks / swaddles / carriers / sleep-aids ARE winners — do NOT blanket-cut "apparel" in this
niche; see [[feedback-winning-products-not-gadgets]]); the conservative cut + live-description filter handle it.

**Marina's FURTHER idea (AGREED direction) = a TRACKED-SHOP COLLECTION + "Newest First" monitoring layer.** Add proven/
competent shops to a ShopHunter Collection (My ShopHunter → Shop Collections), then check `Products → Newest First` every
2-3 days to catch the NEW products traction-operators launch (early-winner detection BEFORE saturation = the entry-window we
score for). Build order Marina set: (1) recon ✅ → (2) feedback ✅ → (3) bulk-add seed ✅ → (4) recurring human-in-loop check-up ⬅ NEXT.
**SEED DONE (SH-5): the Collection now holds 47 shops.** = the FULL curated browse pool from the 409 H&G stores (37) + the
strong/borderline shops from the previous session SH-3/SH-4 (10). Marina's seeding RULE (now formalized in
`methods/discovery-funnel.md` — Collection seeding rule): add the shop of EVERY browse-pool product in 3 tiers — (1) reported
65+, (2) borderline 55–64, (3) the rest of the curated browse pool (<55 genuine products); EXCLUDE branded-FYI, пустышка-FYI,
and stores of Marina-Rejected products (Jar Genie/Stamny + Elevayr were excluded). Scripts (reusable): `sh_collection_add.py
<shop_id...>` (shop-detail → "Add/Remove from Collection" → "Add"; **TOGGLE-safe — check membership before bulk-add**),
`sh_collections_recon{,2}.py`. ~37/409 H&G (~9%) + 10 SH-3/SH-4 = 47.
**CHECK-UP JOB = PARKED HYPOTHESIS** (Marina: not now — grow the base first). Full spec in
`hypotheses/collection-newest-first-monitor.md` (Newest-First scrape → seen-product-id dedup → cut/description filter →
surface NEW; ~2-3-day human-in-loop cadence). Un-park when the collection is large enough.
**GROW the collection:** next session, after processing B&T (717), add its 65+/55-64/browse shops with the same `sh_collection_add.py`.
This is a MONITORING layer ON TOP OF category dumps. Other surfaces still open: Explore PRODUCTS view, geo-test, H&G-by-NEW/growth.

**SIGNAL-DENSITY pattern (Tier-1 observation, not a rule):** going deeper into the H&G dump (b1→b3), genuine white-label
gadgets thinned and the tail concentrated in supplements / apparel / decor / branded-appliances; best-WOW finds got sparser
(PerchMe was the standout). **Marina calibration:** this 409-store yield is a GOOD result vs FB keyword discovery — do NOT
catastrophize a 0-reportable batch.

**FUNNEL FILES on VPS (`logs/shophunter/`):** `sh5_b{1,2,3}.json` (raw), `_hero.json`, `_enrich_in.json`, `_enriched.json`,
`_verdict.json`, `_stage{1..5}_*.png`. Scripts: `sh5_cut.py`, `sh5_render.py` (both in repo + VPS).

> _SH-4 handoff below kept for history — its handoff-files list, PROXY note, and the "write scripts locally + scp" op-rule
> are STILL VALID; only the "process the remaining 409" task is now DONE._

---

**SH-4 DONE (2026-05-25) — funnel matured + 6 products to Notion** (5 from the 151–300 / 301–450 batches below + TempMaster from the SH-3 re-run). Processed H&G stores **151–300 AND 301–450**
(deduped vs SH-3 by shop_id; the two dumps are DIFFERENT runs — only 121/150 SH-3 stores appear in the 830 master).
**5 reported to Notion:** Titanium Cutting Board **76** (CONVERGENCE: Titavos + ChopChop + Life Upgrade = 3 stores),
Sneakertizer **65** + Electric Shoe Dryer **65** (CONVERGENCE: shoe-care ×2), OroMilk **61** + CoolClip **60** (founder-KEEP, scored <65).

**FOUNDER DECISIONS (SH-4, Marina) → full record + status convention in `operational-memory/founder-feedback.md`.**
Approved (pursue): **OroMilk** (health trend + stylish). Consider/monitor: TempMaster, Electric Shoe Dryer, Sneakertizer,
Plantagotchi, **both titanium boards** (×3 convergence → "no wow YET, good trend → monitor, may return"), CoolClip (seasonal)
(+ FB-dept Desk Cat Bed, Rhona). Rejected/closed: Jar Genie ("weak economics"), Elevayr ("weak effectiveness/saturated").
**STATUS CONVENTION (SH-4 — ⚠ SUPERSEDED SH-6, see note below):** Consider = not-now-but-monitor/may-return (NO rejection reason, stays on radar); Rejected = closed →
Archive. **CRITICAL CALIBRATION: convergence / revenue do NOT make Marina PURSUE — at best they earn Consider/monitor.
Approve/test needs clear WOW + perceived value + category priority.** I over-weighted the titanium ×3 convergence as the
"strongest find"; her call = Consider/monitor ("no wow yet"). SH-5: lead candidate recommendations with WOW + taste read
(from live description), not the convergence count; surface trend/convergence finds as monitor-candidates.
> **⚠ SUPERSEDED SH-6:** the "Consider = monitor/may-return" terminology in this SH-4 block is now SPLIT — that monitor/
> may-return meaning moved to the new **Watchlist** tier; **Consider = launch-shortlist only**. Convergence/revenue now earns
> at most **Watchlist** (not Consider). Canonical 4-tier convention → `founder-feedback.md` STATUS CONVENTION + `shared/notion-schema.md`.

**MAJOR SYSTEM UPGRADE this session (all Marina-agreed) — the funnel is now:**
`dump → parallel hero (Stage-1) → conservative cut → Stage-2 sub-agent enricher → main-agent deep-score`.
1. **A+B parallel scraper** (`sh_hero_par.py`, `sh_hero_arg.py`): 4 workers share ONE login via exported
   `cookies/sh_state.json` (`sh_export_state.py`) — no profile-lock fight — + `wait_for_selector("Top Products")` +
   original scroll cadence + retry. **20 min → ~2 min / 150 stores, 150/150 hero, 0 quality loss** (validated vs sequential).
2. **Conservative Stage-1 cut** (`sh_rank_soft.py`, `sh4_hardcut2.py`): hard-drop ONLY definite-no (non-gadget /
   пустышка / real-price > $170 / < $36). **Service-SKU as #1** (shipping-protection/gift-card) = ShopHunter MISLABEL →
   DIG top-3 for the real hero, do NOT drop the store. Survivor count FLOATS (never a fixed quota).
3. **Stage-2 sub-agent enricher** (`sh_enrich_final.py`; spec = `methods/subagent-spec.md`): reads the LIVE products.json
   via **Playwright + residential proxy** (bare `requests` gets Shopify **403 bot-block** regardless of proxy — MUST use a
   real browser through the proxy; verified 200). Per store writes a **Candidate Sheet**: best IN-RANGE physical from
   top-3 with REAL prices (so a $70 beats a $250 #1 — Marina's rule) + niche + **DESCRIPTION** (the bridge for the main
   agent to judge problem/wow/пустышка) + convergence + filter-flags + image. Proxy-score = price-in-range + convergence
   + Stage-1 revenue (RELIABLE signals only). Runs only on survivors (~93) → fast (34–57s).
4. **DROPPED as signals (Marina decisions):** reviews/rating (fakeable — never show 2★ + advertise), multi-niche
   (not a criterion), **ShopHunter FB-ads count** (linkage unreliable / wrong account), branded-flag (don't auto-penalise
   — some branded stores still worth a look). **ShopHunter PRICE is unreliable** → confirm on live site
   (Prone Pillow SH$169→real$39; Cow Keyholder SH$9→real$789; Mellow Mat SH$163→real$329).
5. **Division of labour:** sub-agents = FACTS + flags + ranking (never judge wow/emotion); MAIN AGENT = Marina Veto +
   100-pt judgment on the description. **Deep-score ALL genuine gadgets above the objective bar — no gut top-N** (FB RULE 8).
   The DEEP-SCORE is the real filter; pre-narrowing by gut loses winners.

**SH-3 first-150 RE-RUN — DONE this session (validation):** ran the full new system on the first-150
(`hg_sh3_final.json`, reach 134/150). **Result: NO genuine winner was lost by the old by-name cut** — the new system
independently reconfirmed Titavos (Tier A), Plantagotchi (Tier A), Stamny (Tier B), correctly demoted Elevayr/EkoVibe (C),
and surfaced bonuses (Keyf espresso/ZAIA/Orré) that turned out non-viable on enrichment (store closed / 404 / branded).
One founder-keep added: **TempMaster Warming Mat 59** (miller.market, <65, save-for-reference). System validated.

**HANDOFF FILES on the VPS (`/opt/market-research-agent/logs/shophunter/`) — next session loads these:**
- `hg_shops_1000.json` — 830 H&G master dump (persists from SH-3).
- `hg_sh3_final.json` — first-150 enriched Candidate Sheets (SH-3 re-run, new system).
- `hg_sh4b_final.json` — stores 301–450 enriched Candidate Sheets.
- Already-processed shop_ids: SH-3 first-150 + SH-4 `new[0:300]` (the 151–300 + 301–450 batches). Dedup against these.

**NEXT SESSION — START HERE:** process the **remaining ~409 NEW stores** = `new[300:709]` of the master (where
`new` = master minus the SH-3 150 by shop_id). Same matured funnel. Proxy note below.

**PROXY (raise with Marina before changing):** our `proxy.creds` = a STICKY single IP (`63.88.222.123`, confirmed 5/5);
Shopify rate-limits `/products.json` per-IP, so Stage-2 throttles under a big 4-worker burst (first-150 hit reach 8→39).
Workaround that WORKED: 2 workers + retry/backoff + pacing → reach 134/150 (slower, ~7 min). A ROTATING iProyal endpoint
would restore 4-worker speed — BUT Marina will ALSO use this proxy for Instagram/Facebook, so **discuss with Marina before
switching** (don't change unilaterally). Only ShopHunter `sh_*` scripts use `proxy.creds` (FB/others go direct — verified).

**Op-rule earned (→ promote):** write VPS scripts LOCALLY + `scp` them — NEVER heredoc over a live SSH (SSH drops
mid-write under Chromium load → corrupt file; cost 2 failed launches in SH-4). Always `-o ServerAliveInterval=10`;
launch long jobs with a MINIMAL one-line `nohup` SSH (long combined commands drop before reaching the launch line).

---

## HANDOFF → SH-4 (SUPERSEDED — kept for history)

**Done in SH-3 (2026-05-25) — FIRST store-first discovery run:** validated the full Explore-Shops
discovery mechanics live (see SH-3 learnings below). Dumped **830 Home & Garden stores** (no country/sort
filter, default order) to VPS file **`/opt/market-research-agent/logs/shophunter/hg_shops_1000.json`**
(persists across sessions; fields: name·myshopify-handle·shop_ads·rev_day/week+chg·fb/ig·country·sku·currency·shop_id).
Infinite-scroll **exhausted at 830** = that's how many H&G stores this surface exposes by default.
Distribution: tiers hero≤20SKU=309 / small-cat=222 / catalog80+=299; **US=680 (82%)**, GB36/AU21/DE21/SE11;
rev/wk almost all >$2K (10-50K=393, 50-200K=240, 200K+=105); **200/830 have FB ads (FB-bridge subset)**.
A first 150-store batch (`hg_shops.json`) was also analysed end-to-end → **1 reportable candidate found:
Titavos Titanium Cutting Board, score 76** (NOT yet in Notion). Marina screenshots delivered to Desktop.

**Marina-agreed FUNNEL for SH-4 → full spec in `methods/discovery-funnel.md` (PROVISIONAL).**
Run it on the EXISTING dumps (don't re-scrape). Stages: dump → working slice (~250) → **open ALL** on VPS
(no subjective pre-pick — fixes SH-3 103→12-by-name mistake, FB RULE 8) → objective noise-cut → **intermediate
proxy-scoring on VPS** → top finalists to chat → deep 100-pt scoring. **NUMBERS (250/170/30-50/7-20) ARE
ILLUSTRATIVE, NOT QUOTAS** (Marina, SH-3): each stage narrows by stricter criteria; the intermediate stage
exists so even a low-noise slice still narrows (never dump 200 survivors to chat); never force a fixed count.
**HERO per store = read its ShopHunter "Top Products" block (Revenue Week) — this is RELIABLE (Marina-verified: Titavos #1=Titanium Cutting Board $28K/wk, Plantagotchi #1=AI Planter $11K/wk). Do NOT grab the competitor "Top Revenue Producers" label (that was the SH-3 parser bug). Corroborate hero with products.json catalog + featured product.**
Also: **carry-over candidates** = Titavos (DONE: saved to Notion SH-3; still confirm ad-count via FB-Archive bridge +
Alibaba titanium COGS); **Revelle** (tryrevelle.store) — RESOLVED via ShopHunter Top Products: hero = Lymphatic Drainage Red-Light
Massager $69 ($64K/wk) = ПУСТЫШКА (unverifiable result, hard-reject) → DROP, not a carry-over) and **Valia Collective** (8 SKU, $444K/mo Kitchen — no
custom domain shown, re-open).

**NEXT SESSION (SH-4) — START HERE:** continue the 830 dump → analyze **stores 151-300** from `hg_shops_1000.json`
(DEDUP against the ~150 already done in SH-3 = `hg_shops.json`, by shop_id — skip overlaps). Same funnel; hero via
`scripts/sh_hero_v2.py` (the verified "Top Products" parser). Run `sh_proxy_check.py` first (proxy health). Helper scripts
already on VPS: sh_topproducts_batch.py (true-hero over a list), sh_rank_v4.py (classify+rank), sh_gt_proxy.py (external enrich).

**PER-STORE METHOD (Marina Q, SH-3):** read the **TOP FEW products** from "Top Products" (NOT just #1) — a store can
have 2+ winners (e.g. Titavos: Cutting Board $28K/wk + Frying Pan $20K/wk). #1 = primary candidate; also scan #2-3 if
founder-taste fits. **WE make the final pick:** ShopHunter ranks by revenue, but we CHOOSE by taste / white-label / price /
пустышка-check. products.json + the live site corroborate catalog + exact price + claims. The "Top Products" parser is
VERIFIED → no need to manually eyeball every store (spot-check occasionally; the SH-3 bug is fixed).

**Priority carry-over: Orré electric back brush** — get its real domain via the store's ShopHunter "View on Shopify Store"
link, then score (only genuinely-new founder-taste gadget from SH-3; myshopify handle 404'd).

**Watch:** revenue = ESTIMATE (corroborate); SH category taxonomy is UNRELIABLE (weight-loss supplement
tagged "Gardening›Hydroponics›Nutrient"); noise = supplements/пустышка + Nordic-dropship + mature giants;
hero ≤20 SKU vs catalog 80+; foreground SSH reliable for ~3-4min dumps (830 took ~6min, exhausted clean).

**Deferred from SH-2 (low priority):** 9 "-" Product-Tracker rows never inspected (travelerpillow,
puredailycare, luncheaze, itakico, glenbrookhome, toucanbaby, desknest, ergopurrch, kaizenkidz) — do NOT
infer SH coverage from them.
