# ShopHunter — Session Learnings

Short-lived tactical discoveries from recent sessions. Read at session start.
Does NOT contain permanent rules (those go to `op-rules.md` once it exists) or
company-level logic (that stays in `core/`).

Discipline mirrors the FB department: append new entries with an expiry; archive
expired entries; never delete — move to the Expired section. A pattern confirmed
across 3 sessions OR explicitly approved by Marina may be promoted to a permanent
rule via `review/promotion-queue.md`.

---

## HANDOFF → NEXT SESSION (read first)

**✅ SH-10 DONE (2026-05-27) — 4 pre-loaded niches FULLY PROCESSED (1876 stores, human-in-loop): Health & Beauty 804 · Sporting Goods 829 · Luggage & Bags 211 · Software 32.**
- **Funnel rock-solid:** hero 99–100% every batch, conservative cut held (drop only definite-no), enrich reach 89→100% (one slow-store stretch on L&B B2 — process alive, finished at secs=239; NOT a proxy failure). Proxy stable all day (single dedicated IP 63.88.222.123, every `sh_proxy_check.py` = OK). Files on VPS `logs/shophunter/`: `hb_b{1..4}`, `sg_b{1..4}`, `lb_b{1,2}`, `sw_b1` + `_hero/_enrich_in/_enriched` + sentinels.
- **YIELD = 1 reported winner + 1 winner-quality convergence (2 Notion actions):**
  - ✅ **SaveLix Anti-Choking Device 77** (savelix.com) — H&B B3. Suction choking-rescue (LifeVac-class), max fear/protection trigger, demonstrable, white-label, 10K+ families/2800+ rev. **Mis-niched family-SAFETY device in H&B.** anti-choking ×4 convergence (SaveLix+SaveVac+VitalBreath+AirGuard) → **SaveVac added as Store Link 2.** Notion card created (Source=ShopHunter, SH-fields filled, Founder Review LEFT for Marina).
  - ✅ **Aerpack Vacuum Bags + electric pump ~72** (aerpack.com) — L&B B1. Same TYPE as already-reported **Rhona TravelVac Pro 74** (FB-dept) → Marina chose **add as Rhona Store Link 2** (NOT a new card). Vacuum-compression now ×10 cross-department (Rhona+Luux+Aerpack+Magic Travel+CompressPak+VacBird+VacPack+Backvac+Tilliv+Zephyr).
- **NO collections seeded this session** (Marina decided per-niche: none had "wow" shops — like T&G/B&I). The 4 niche collections from prior sessions are unchanged: Home & Garden 47 · Baby & Toddler 53 · Arts & Entertainment 40 · Animals & Pet Supplies 36.
- **⭐ KEY STRATEGIC FINDING — the FB "winner-zone" (Health & Beauty devices) does NOT transfer to store-first.** ShopHunter's H&B tracked surface is DOMINANTLY пустышка-device (red-light/LED/lymphatic/circulation/hair-growth) + consumable beauty + relief-massagers; Tier-A almost all пустышка. Genuine white-label devices present are all commodity/branded-dupe/floor (hair-stylers/body-shavers/showerheads/water-flossers/eye-massagers/IPL). Keyword-first filters to the clean device BY SYMPTOM; store-first surfaces the WHOLE пустышка-dense category → H&B store-first yield ≈ medium (A&P-level), NOT the top zone. **Do NOT close H&B; expect пустышка-density, apply the visual-verifiability gate hard.** (Tier-1 yield fact, NOT a system rule — keep scoring as-is.)
- **Niche-yield ranking now (store-first white-label-fit):** H&G / B&T (best) > A&P ≈ **H&B** (medium, пустышка-dense) > A&E / T&G > **SG** ≈ **L&B** (thin, structural-reject-dominated) > B&I ≈ **Software** (lowest). SG = bulky/golf/pickleball/recovery-пустышка; L&B = fashion-bag-везде + vacuum-compression(only signal); Software = digital/non-physical.
- **NEW reusable script:** `scripts/sh_export_tracked.py` — exports all tracked-shop collections grouped by niche (joins seed-id files/add-logs vs category dumps → NAME·domain·SH-link). The full tracked-shop backup list was delivered to Marina in chat (≈174 shops: H&G 46, B&T 53, A&E 39, A&P 36) for re-loading on the paid ShopHunter later.
- **NEXT SESSION (SH-11) options (Marina picks):** (a) **dump + process a fresh category** (e.g. Electronics, Furniture, Office Supplies, Apparel/Accessories, Vehicles & Parts) — same matured funnel; (b) **breadth-tool (Store Leads) pilot** to fix bottleneck #1 (the ~800/category tracked-subset ceiling — emerging early-window winners are missed) → **hypothesis recorded in `hypotheses/storeleads-breadth-source.md`** (SH-10 discussion: Store Leads $75 as breadth source feeding our funnel, paired-with-or-without ShopHunter; $75+~$50 = $125 combo; test Dropship.io 7-day trial first). NOT yet a committed strategy — directional hypothesis; (c) Newest-First check-up on the 4 niche collections (deprioritized, low ROI on mature shops). All SH-3→SH-10 niches 100% done. **Founder Review for SaveLix + the SH-7/SH-9 cards = Marina to set in Notion.**

---

> _SH-9 handoff below kept for history — A&P 860 + B&I 356 done; funnel/proxy/Notion-schema notes still valid. SH-10 above is current state._

**✅ SH-9 DONE (2026-05-27) — Animals & Pet Supplies 860 + Business & Industrial 356 BOTH FULLY PROCESSED (human-in-loop).**
- **Funnel:** hero 96.7→100%, conservative cut held 187-195 survivors/batch (−19 to −28, only definite-no), enrich reach 88→98→98→**100%** (B1 88% = a mid-session proxy blip; B2-B4 clean after fix). Files on VPS `logs/shophunter/`: `ap_b{1,2,3,4}.json` + `_hero/_enrich_in/_enriched` + sentinels; curated seed `ap_seed_ids.txt` (36 ids) + `ap_seed_domains.txt`.
- **YIELD: 2 reported 65+ + 3 founder-keep = 5 Notion cards (all Source=ShopHunter, SH-fields filled, Founder Review LEFT for Marina):**
  - ✅ **Uah Pet Wireless Cat Water Fountain 67** (uahpet.com) — winner-zone reconfirm (cat fountain ×7 convergence; cordless angle; white-label the TYPE).
  - ✅ **Karate Kitty 70** (karatekitty.com) — wearable arm-puppet cat toy + hand-protection; viral UGC; **Marina-spotted from browse-pool (proxy buried it B|47 → 70 on deep-score, cf SlotPro)**.
  - 🟡 **Dog Dock V2 62** (waggingrightsusa.com) — hard-bottom dog car seat, founder-kept "нравится стиль/изучу"; lead of dog-car-seat ×15+ convergence; $222K/wk single-product.
  - 🟡 **CatCam 2K 54** (meowmerch.org) — POV pet collar camera, founder-kept (funny "what does my pet do" hooks, better on a dog).
  - 🟡 **Pro Cat Wrap 60** (calmcozycat.com) — cat grooming/vet restraint wrap, founder-kept (problem genuinely relevant); $307K/wk.
- **A&P = MEDIUM white-label density** (>A&E/T&G, slightly <H&G/B&T). ~50% surface mis-niched off-niche (skincare/whitening/perfume/supplements/kids-toys) + very dense consumable/ingestible reject. Dominant convergence = COMMODITY/bulky (car-seat ×15+, harness ×8+, bed ×10+, fountain ×7 [winner-zone], litter ×5, feeder+cam ×3, nail-care ×5). Full → `shared/rejected-products.md` SH-9.
- **COLLECTION SEEDED:** NEW niche **"Animals & Pet Supplies"** (seed uahpet + ~35 added) + all also into general **"Shops"**, via toggle-safe `sh_collection_manage.py` (run `ap_seed_collection.sh`). **4 niche collections now: Home & Garden 47 · Baby & Toddler 53 · Arts & Entertainment 40 · Animals & Pet Supplies ~36.** (verify exact count via dialog-`list`, not page count.)
- **B&I 356 DONE (2 batches `[0:178]`/`[178:356]`; hero 96.6→100%, enrich 98%):** **0 reported 65+ / 0 founder-keeps / NO collection seeded** (Marina: skip, like T&G). Only borderline = Smart Chicken Coop Door (coopandroost.com $125, ~62 — not kept). **B&I = LOWEST white-label-fit niche of all processed** (orthopedic/anti-snoring pillows ×30 + medical/пустышка devices + ⚠ tactical/armor/weapons/gas-masks [Meta-policy reject] + B2B pro-supplies tattoo/dental/welding + bulk-detergent + decor/POD + galaxy-projectors). Files: `bi_b{1,2}.json` + `_hero/_enrich_in/_enriched` + sentinels. Full → `shared/rejected-products.md` SH-9. **Yield ranking: H&G/B&T > A&P > A&E/T&G > B&I (lowest).**
- **🔧 PROXY incident + FIX (SH-9):** our proxy = iProyal **ISP Dedicated** (single fixed IP `63.88.222.123:12323`, individual user/pass, NOT shared). A mid-session transient endpoint blip (TCP-timeout to the IP, VPS internet fine) was misdiagnosed by me at first; **recovery = don't change creds (re-entering identical creds didn't fix it — TIME did), use iProyal "Test now", short wait + ONE gentle retest.** Full RECOVERY PROCEDURE in the Active Learnings block below. "Reset credentials" only fixes AUTH errors, not TCP timeouts. If blips recur → 2nd cheap dedicated IP as backup (proposed, needs Marina OK).
- **🔧 NOTION live-schema reconciled (verify-before-asserting):** live DB has **NO `Status`** field (only `Test Status`); `Price Range` options are EN-DASH exact (`$45–79`/`Extended $39–100`/`Premium $100–170`/`Too Cheap`); no `Supplier Link`/`CTR`/`CPM`. Fixed `shared/notion-schema.md` + `notion-workflow.md`. **`create-pages`: send Date as `date:Date Added:start`=YYYY-MM-DD; do NOT send `Status`.**
- **NEW reusable scripts (VPS+repo):** `sh_render_candidates.py` (compact A+B+C deep-score view), `sh_proxy_diag.py`/`sh_proxy_diag2.py` (proxy localization: direct-internet vs TCP-to-proxy vs curl-through-proxy), `ap_resolve_ids.py` (domains→shop_ids), `ap_seed_collection.sh`.
- **🆕 4 NEXT-CATEGORY DUMPS PRE-LOADED ON VPS (Marina-requested SH-9, all 12-scroll EXHAUSTED = full surface):** `logs/shophunter/health_beauty_shops.json` = **804** · `luggage_bags_shops.json` = **211** · `sporting_goods_shops.json` = **829** · `software_shops.json` = **32** (Software genuinely tiny — software rarely sold via physical Shopify tracking). Same field schema (shop_id/domain/rev_week/sku/country verified). **SH-10 can start immediately (no dump needed).** Dump wrapper = `scripts/prep_next_dumps.sh`; reusable `sh_cat_dump.py "<Cat>" <dest> 8000 <sentinel>`. _(v1 12-scroll-exhausted + valid; optional v2 robust re-verify via `sh_cat_dump_v2.py` at SH-10 start if extra assurance wanted.)_
- **NEXT SESSION (SH-10) plan:** process the 4 pre-loaded dumps with the SAME matured funnel (hero→cut→enrich→deep-score→checkpoint→Notion) + seed a niche collection per category IF yield warrants (skip if "ни о чём", like T&G/B&I). **Prioritize HEALTH & BEAUTY (804)** — un-mined + historically our WINNER-ZONE (beauty/health devices were the strongest FB-dept category) → expect the best yield of the four; watch for пустышка/branded-proprietary (NuFACE-class) + ingestible/skincare-consumable reject. Luggage & Bags (211) = expect travel/compression/organizer (watch bulky + fashion-bag везде). Sporting Goods (829) = expect fitness/recovery/outdoor (watch commodity + bulky). Software (32) = tiny, quick pass. **A&P 860 + B&I 356 = 100% done. Founder Review for the 5 SH-9 cards = Marina to set in Notion.** Also still open: breadth-tool (Storeleads) pilot.

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

---

## Active Learnings

### [2026-05-27] Session SH-10 — FB "winner-zone" ≠ store-first winner-zone; niche-yield is category-structural
**Type:** Pattern / Strategic yield fact | **Severity:** HIGH | **Confidence:** MEDIUM-HIGH (4 full niches, 1876 stores, Marina-direct)
**Observation:** Processed 4 pre-loaded niches end-to-end → 1 reported winner (SaveLix 77) + 1 convergence (Aerpack→Rhona SL2). Durable take-aways:
- **The historical FB-keyword "winner-zone" (Health & Beauty devices) does NOT carry over to store-first ShopHunter.** The H&B tracked surface is пустышка-device-dominated (red-light/LED/lymphatic/circulation/hair-growth) + consumable beauty + relief-massagers; the clean white-label devices keyword-search surfaces (eye/scalp/posture/callus) appear here only as commodity/branded-dupe/floor. **Discriminating mechanism:** keyword-first filters to the device BY SYMPTOM; store-first exposes the WHOLE category, and beauty's whole category is пустышка-dense. → Apply the visual-verifiability gate hard on H&B; don't expect top yield. (Tier-1 fact — do NOT add a filter or close the niche.)
- **Yield is category-STRUCTURAL, reconfirmed (Nth time):** H&G/B&T (best) > A&P ≈ H&B (medium) > A&E/T&G > SG ≈ L&B (thin) > B&I ≈ Software (lowest). SG = bulky-equipment + golf/pickleball/cycling-niche + recovery-пустышка; L&B = fashion-bag-везде (structural reject) with vacuum-compression as the only white-label signal; Software = digital/non-physical (not a viable store-first niche).
- **Convergence handling reconfirmed (Marina, SH-10):** when a fresh ShopHunter find is the SAME product TYPE as an already-reported winner (Aerpack vs Rhona vacuum-compression), Marina prefers **Store Link 2 convergence on the existing card**, not a duplicate report (cf cookinate→OroMilk SH-5, SaveVac→SaveLix this session). Mis-niched winners are real: SaveLix (family-safety) surfaced in H&B; score the PRODUCT, ignore the niche tag.
- **Funnel/proxy stable across 1876 stores** (hero 99-100%, enrich 89-100%, single dedicated IP all day). Enrich can have a slow-store stretch (L&B B2 = 239s) — detect DONE by sentinel, the process is alive (don't relaunch).
**Applies to:** SH-11+ niche selection + scoring expectations + convergence handling. **Expires after:** durable (yield = Tier-1 fact; convergence rule already standing).

### [2026-05-27] Session SH-9 — PROXY = iProyal ISP DEDICATED; transient endpoint blip ≠ bad creds (RECOVERY PROCEDURE)
**Type:** Operational safeguard / Recovery procedure | **Severity:** HIGH | **Confidence:** HIGH (Marina dashboard screenshots + same creds worked on retry)
**Proxy identity (CONFIRMED via Marina's iProyal dashboard):** Product = **ISP Dedicated**, 1 proxy, US, port **12323**, format HOST:PORT:USER:PASS, **individual user/pass (NOT shared)**, IP `63.88.222.123` is **FIXED/dedicated** (no rotation, no backup endpoint by design). This is why the creds are bound to that exact IP and the residential gateway `geo.iproyal.com` REJECTS them (curl exit 56) — different product. Do NOT try to switch to `geo.iproyal.com` (tested non-destructively SH-9: rejected).
**What happened:** Mid-session the proxy started timing out — raw TCP to `63.88.222.123` failed on ALL ports (12323/443/80) from the VPS, while VPS direct internet + egress to high ports on OTHER hosts worked fine. Marina re-entered the EXACT SAME creds and it worked again → **the creds were never wrong; TIME fixed it, not the re-entry.**
**Root cause (honest, given ISP Dedicated):** a **transient unreachability of the dedicated ISP node** — a brief routing blip between the VPS (`5.78.217.133`) and the iProyal node, or short node-side maintenance. NOT an abuse-cooldown of a shared gateway (the IP is hers alone). A rapid BURST of connections (B1 enrich retries + my repeated back-to-back proxy checks/diagnostics) MAY also trip node-level flood protection, so still avoid bursting. Rare for a dedicated ISP IP.
**RECOVERY PROCEDURE (match the tool to the symptom — do NOT reflexively change creds):**
1. **Confirm it's the proxy path:** `curl -sS -m15 https://api.ipify.org` direct from VPS (returns VPS IP = internet OK) + raw `socket.create_connection((PROXY_HOST,PORT),10)` (TCP_FAIL = node unreachable). Direct OK + proxy TCP fail → proxy node, not us.
2. **TCP-timeout symptom → creds are NOT the problem.** The saved `cookies/proxy.creds` are correct & stable. **"Reset credentials" in the iProyal dashboard ONLY helps an AUTH failure (HTTP 407 / curl exit 56 after CONNECT), NOT a TCP timeout** — don't waste the once-per-hour reset on a timeout.
3. **Use the iProyal dashboard "Test now" button** (instant, free): proxy alive there but unreachable from VPS → transient VPS↔node routing blip → short wait. Dead there too → node issue → wait/support.
4. **STOP all proxy hits; do ONE gentle `sh_proxy_check.py` per check** (no back-to-back bursts — they can prolong/trip flood protection). Wait a few minutes between checks. Today it cleared within ~10–20 min.
5. **Work is never lost:** hero+cut survivors persist in `ap_b*_enrich_in.json` — relaunch enrich when the node answers.
**FAST-FAILOVER (only if blips RECUR — proposed, needs Marina OK):** add a 2nd cheap dedicated ISP IP (~$5/mo) as backup so enrich can switch to IP#2 instantly. Not needed for a one-off.
**Applies to:** every ShopHunter proxy-based run. **Expires after:** Never → promote to op-rules when that file is created.



### [2026-05-26] Session SH-8 — Toys & Games (0-yield) + 2 new dumps + structural safeguards + strategy
**Type:** Pattern / Result / Founder strategy | **Severity:** HIGH | **Confidence:** HIGH (Marina-direct)
**Observation:** Full build/strategy in the HANDOFF above. Durable take-aways:
- **T&G = product-dense but LOWEST white-label-fit niche so far** (0 reported / 788). With A&E (SH-7), confirms both are structurally weaker store-first than H&G / B&T. Numbers float — a 0-yield niche is a VALID result; never force.
- **ShopHunter's universe ceiling now understood + verified:** it tracks inventory-depletion on a CURATED added-store subset (~800/category), not the whole Shopify market. **Paid tier ≠ more coverage** → deferred. A **breadth tool (Storeleads ~2.8M, revenue-filterable)** is the real fix for bottleneck #1; pair it with ShopHunter as the DEEP layer (feed best finds in — Marina's idea).
- **3 structural safeguards baked in** (Revenue-Tier rename · mandatory browse-pool · **Description-confidence gate** = WebFetch-verify empty/mismatched desc before tiering, the SlotPro fix). The discipline→structure conversion Marina asked for; purely additive. `desc_confidence` enricher flag = next code change (apply+test next run).
- **Watchlist CONFIRMED kept:** Consider = launch-intent (product, now) vs Watchlist = signal/category radar (may-return) — both "yellow", different questions; pair Watchlist with a periodic revisit ritual or it collapses to soft-Reject.
- **Completeness method:** clean 12-scroll exhaust + v2 robust re-verification = the dump-completeness signal Marina wants for next-session dumps.
- **Batch size 170-200 optimal** (~200 cap); 362 worked (0 loss) but thins per-item attention + 2-worker sticky-proxy ~8 min.
**Applies to:** SH-9+ funnel + strategy + scaling design. **Expires after:** durable.

### [2026-05-26] Session SH-7 — Arts & Entertainment processed + niche-yield + founder/browse calibrations
**Type:** Pattern / Result / Founder calibration | **Severity:** HIGH | **Confidence:** MEDIUM-HIGH (1 full niche, Marina-direct)
**Observation:** Full build/yield in the HANDOFF above. Durable take-aways:
- **A&E is a LOW white-label-density niche (Tier-1 yield fact, NOT a system rule):** 823 stores → only 2 genuine 65+ (Manta Ray automaton, SlotPro ruler) + 2 founder-keeps. Surface dominated by POD/personalized gifts, apparel, craft-hobby kits/supplies, branded music instruments, collectibles, decor, digital. Record as factual yield; **do NOT close the niche or add a filter** — keep scoring as-is (numbers float with data; honest 0-winner batches B2/B3/B4 are normal store-first results, per SH-5).
- **Browse-pool value RE-CONFIRMED (SH-5 lesson, 2nd time):** SlotPro quilting ruler sat in the sub-65 browse list (rapid scan ~52); Marina asked about it → verification showed a genuinely differentiated 26-channel blade-guide mechanism (≠ flat-ruler commodity) → rescored ~66 and reported. **Always surface the curated genuine browse-pull — the agent's fast bar misses real products the founder's eye catches.**
- **Founder firsthand FB-sighting = a real corroboration signal:** Marina recognized Panda Drum from her own FB Ads Library analysis → kept it. ShopHunter ad-count was 0/N-A (unreliable, as always), but the dump's `shop_ads`=247 + the live site (690 rev, 72K customers, CNBC/WSJ) confirmed heavy advertising. Cross-checking the live store + founder memory beats the SH ad number (reconfirms SH-4).
- **ShopHunter PRICE unreliable AGAIN (Nth confirmation):** Panda Drum SH-est/enrich matched a $45 SKU; real hero = $159.95 (Premium). ALWAYS confirm price on the live site before scoring/Notion (caught at deep-score, as designed).
- **Convergence ≠ pursue (reconfirmed):** strong clusters (leather-care ×3, slotted-ruler ×4-5, bird-cam, etc.) = demand validation only; led recommendations with WOW + taste read, kept Competitor Signal at Testing (not inflated to Scaling on convergence). Birdfy/SlotPro = convergence cards with Store Link 2 + all brands in Notes.
- **Funnel rock-solid at 100% hero / 98% enrich across 4 batches** — parallel hero (4w) + 2-worker paced proxy held; sticky IP 63.88.222.123 stable all session. Collection seeding via toggle-safe `sh_collection_manage.py` clean (40/40 to Shops, 39+seed to new A&E niche, 0 fail).
**Applies to:** SH-8+ funnel + reporting + niche-yield expectations. **Expires after:** durable (yield = Tier-1 fact; browse/founder calibrations already standing rules).

### [2026-05-26] Session SH-5 — H&G dump finished + Marina process calibrations
**Type:** Pattern / Founder calibration | **Severity:** HIGH | **Confidence:** HIGH (Marina direct, this session)
**Observation:** Full build/yield in the HANDOFF above. Durable calibrations from Marina (SH-5):
- **proxy-Tier (A/B/C) = a REVENUE/price SORT-AID, not a quality ranking.** It gets fooled by revenue+convergence (b1 Tier-A = 2 titanium boards + 1 apparel false-positive; b2 Tier-A = branded vacuums + JarBuddy-on-rejected-Jar-Genie; b3 Tier-A = a $40 water jug). The 100-pt deep-score (read ALL of A+B+C, FB RULE 8) is the real filter. **Never present "Tier A" to Marina as "the best finds" — always lead the recommendation with the deep-score + WOW/taste read.** (Optional future tweak she's open to: rename to "revenue-tier". Do NOT bake taste into the proxy score — taste = main-agent + founder.)
- **Keep the conservative Stage-1 cut AS-IS while testing** (Marina): survivor counts run high (132–135/150) on purpose — "in doubt, keep & deep-score" protects winners; bigger Stage-1 filtering would need more data. Don't over-optimize the cut now.
- **Stage screenshots = ON-REQUEST, NOT a standing rule** (Marina corrected — memory [[feedback-stage-screenshots]]). Default = no screenshots unless asked.
- **ShopHunter store-first yield is GOOD vs FB keyword discovery** — a 0-reportable batch is a normal pass, not a failure; report yield factually, don't catastrophize "weak batch".
- **browse-links workflow — CONFIRMED by Marina (SH-5) → PROMOTED to `methods/discovery-funnel.md` (Reporting protocol):** each batch report includes BY DEFAULT (no request needed): winners 65+, borderline ~58–64 (usually a few), patterns noticed, AND a curated list of sub-65 genuine-PRODUCT store links for Marina to scan for patterns + a one-line "more/less links?" offer. Rationale: in b1+b3 Marina kept products from the broader sub-65 link list that weren't in the initial verdict.
- **Score winning PRODUCTS, not "gadgets" (Marina SH-5):** a winner solves a real problem — gadget / tool / functional product (e.g. a beautifully-branded faucet water filter), electronics NOT required. In the BABY niche do NOT blanket-cut "apparel" — sleep sacks / swaddles / carriers are proven winners. See [[feedback-winning-products-not-gadgets]].
- **Convergence handling reconfirmed:** cookinate Juice&Milk Maker → OroMilk Store Link 2 (Marina-spotted 2nd brand). And I caught myself over-inflating Competitor Signal Testing→Scaling on convergence → reverted to Testing (convergence ≠ inflate signal — the SH-4 lesson, applied).
**Applies to:** SH-6+ reporting + funnel. **Expires after:** durable (browse-rule already promoted to discovery-funnel; proxy-tier-rename optional).

### [2026-05-25] Session SH-4 — Funnel matured (parallel + conservative cut + sub-agent enricher) + 2 convergence clusters
**Type:** Pattern / Result | **Severity:** HIGH | **Confidence:** HIGH (Marina co-designed + validated live)
**Observation:** Full build detailed in the HANDOFF above. Durable take-aways:
- **No fixed numbers anywhere** (Marina, repeated): survivors / deep-score set FLOAT with the data — never a quota,
  never gut top-N. Objective bar = physical white-label gadget + real price $39–170 + not clear supplement/пустышка/
  apparel/decor. Deep-score everything that clears; in doubt → keep & deep-score (the 100-pt + Veto is the real filter).
- **The DESCRIPTION (live product text) is the bridge** that lets the main agent judge problem/wow/пустышка — far more
  truthful than reviews/ratings (fakeable) or FB-ads count (ShopHunter linkage unreliable). Money-based proof that IS
  reliable = convergence (multiple independent sellers) + revenue estimate.
- **2 convergence clusters found:** (1) **titanium cutting board** ×3 (Titavos + ChopChop + Life Upgrade) — reinforces
  the SH-3 Titavos thesis hard; (2) **shoe-care / shoe-dryer** ×2 (Sneakertizer UV+heat + Veladux electric) within one
  session. Convergence = the strongest reliable validation signal in store-first discovery.
- **Stage-2 leaks still need the main agent's semantic read:** name/product_type classification let supplements slip
  into Tier A (Manna Gold, Ormus, "Daily Essentials", nasal spray) — the live DESCRIPTION caught them. Path A confirmed
  (main agent does the semantic cut; no paid LLM on the VPS for now).
**Applies to:** SH-5+ funnel. **Expires after:** promote the funnel mechanics to op-rules once re-validated on the SH-3 re-run.

### [2026-05-24] Session SH-1 — Explore Shops search needs the BARE DOMAIN, not the full product URL
**Type:** Tactical / Warning
**Severity:** MEDIUM
**Confidence:** HIGH (confirmed live with renpho.com)
**Observation:** In Explore → Shops, the "Search Shops" box matches a store by its
domain/handle, NOT a full product path. Searching `renpho.com/collections/eye-massager`
did NOT surface the store; stripping to `renpho.com` returned the shop (id 8346304597).
Rule: when taking a Store Link from our records/Notion, strip it to the bare domain
(everything up to the first slash after .com) before searching.
The shop page then exposes: store revenue (Day/Week/Month + trend), **Store Creation Date**,
**SKU count**, **tracked-by-N-users**, **Competitor Analysis** (rival stores + their revenue +
top products), and a **"View on Facebook Ads Archive"** link (built-in FB cross-reference).
**Applies to:** every Explore Shops lookup that starts from a known store link
**Expires after:** Never → promote to `op-rules.md` when that file is created (permanent operational fact)
**⚠ REFINED in SH-2 (below): bare domain ALONE is INSUFFICIENT — strip only the PATH, then try full URL / www / bare / name.**

---

### [2026-05-24] Session SH-2 — [CORRECTED] Search by FULL URL — bare domain alone is NOT enough (refines SH-1)
**Type:** Warning / Correction (supersedes the SH-1 bare-domain rule)
**Severity:** HIGH (this bug caused ~12 false "not in index" results in SH-2)
**Confidence:** HIGH (Marina confirmed live + diagnostic)
**Observation:** "Search Shops" is a RELEVANCE search. Bare domain matches only stores whose canonical
domain is stored WITHOUT www (renpho.com, nuvebrand.com). It FAILS (0 results) for stores stored WITH
www: `seattosleep.co.uk` → 0, but `https://www.seattosleep.co.uk` (full URL, as Marina pasted) → found
(id 61584507067); the name with spaces "seat to sleep" also found it. A product PATH still breaks it
(SH-1: renpho.com/collections/… → 0).
**Rule (corrected):** strip only the PATH after the domain; then try IN ORDER until a hit:
(1) full Store Link URL as-is (https://www.…), (2) https://www.+domain, (3) bare domain,
(4) brand NAME as words (de-concatenate: seattosleep→"seat to sleep"). ALWAYS open the result and
confirm the shop's shown domain matches before trusting — search returns multiple relevance matches,
the right store may not be first, and a store's canonical domain may differ from our saved Store Link
(e.g. Camp Snap may be campsnap.com, not campsnapcamera.com).
**Applies to:** every Explore Shops lookup.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — "Not in index" came from a SEARCH BUG; the 9 unfound stores are UNEXPLAINED (no coverage claim)
**Type:** Warning / Open question
**Severity:** HIGH
**Confidence:** MEDIUM
**Observation:** The over-stripping bug made SH-2 mark ~12 stores "-"/"not found". After the corrected
search (full URL + brand name), 3 were recovered — seattosleep (id 61584507067), nuface (id 7425785,
$2M/mo, branded ref), camp snap (id 74473832752 — matched by NAME; its SH domain ≠ campsnapcamera.com).
9 were still not found via domain+name: travelerpillow, puredailycare, luncheaze, itakico, glenbrookhome,
toucanbaby, desknest, ergopurrch, kaizenkidz. ⚠ Do NOT conclude anything about ShopHunter's coverage from
this — we have NOT inspected those 9 (they may be established brands under a different stored domain/name,
or genuinely absent), and 9 links is no sample for a tool with tens of thousands of stores (Marina's
correction — avoid overgeneralizing from a tiny sample). NEXT: open/inspect the 9 directly (correct stored
domain? on Shopify? real size) BEFORE any coverage statement.
**Applies to:** the 9 "-" rows; keep any unverified coverage claim OUT of strategy.
**Expires after:** Session SH-4.

### [2026-05-24] Session SH-2 — Notion: the 4 SH fields are ShopHunter-DEPARTMENT-ONLY
**Type:** Pattern / Rule (Marina-approved)
**Severity:** MEDIUM
**Confidence:** HIGH
**Observation:** Added to the shared Product Tracker: **SH Link** (url), **SH Store Created** (text — converted
from date in SH-2; description was lost on conversion, re-add if wanted), **SH Rev W/M** (text "week / month"),
**SH SKU/Country** (text "N / US"). The other 3 field descriptions say "ShopHunter dept only — FB Ads agent
leaves blank" → the FB-department agent must NOT fill these.
Provenance decision (Marina): do NOT add a separate "Department" field — instead add value **"ShopHunter"**
to the existing **Source** field for FUTURE ShopHunter-discovered products; NEVER rewrite existing Source
values (TikTok/WebSearch/Facebook/Amazon are accurate — today's enrichment did NOT change Source).
For a store not found, put **"-"** in SH Link (visible "checked, absent"). **Notes** may now hold
store/infrastructure observations (multi-geo domains, store-name≠product, price discrepancies), not only product notes.
**Applies to:** every Notion write from ShopHunter.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — Shop-data semantics (what the numbers mean)
**Type:** Signal
**Severity:** LOW
**Confidence:** HIGH
**Observation:** (1) Revenue = ESTIMATE — corroborate before calling a winner. (2) Store Created: ~half
show N/A; when present, dates are varied/plausible (2016–2025) → field usable for mature-vs-fresh; the
9/2/2022 shared by renpho+nuve was isolated. N/A handling RESOLVED in SH-2 (Marina opt a): SH Store Created
converted to TEXT, literal "N/A" written to the 14 N/A rows, existing dates preserved as date-mentions. (3) SKU count
reveals store TYPE: mono-brand hero (2–9 SKU: Hoppie, Rhona, WagWells) vs big catalog/dropship
(KittySpout 481, Cherrypick 216, Levide 147) — high SKU = product is one of many, weaker as a hero-brand.
(4) Competitor Analysis = free convergence/saturation map per store, incl. multi-geo same-brand variants
(renpho.eu/IE, renpho.uk/GB) → record in Notes. (5) Shopify Apps can flag white-label supplier (Nuvé uses
"SUPLIFUL: White Label Products"). (6) Store NAME ≠ our product name (Rhona store = "Rhona's FloatSeat+™").
**Applies to:** reading any shop page.
**Expires after:** Never → op-rules.md.

### [2026-05-24] Session SH-2 — VPS scraping ops (reliability)
**Type:** Tactical
**Severity:** MEDIUM
**Confidence:** HIGH
**Observation:** (1) A `run_in_background` SSH to the VPS DROPPED (exit 255) but the remote python KEPT
RUNNING — DO NOT relaunch (parallel runs fight over the single browser-profile lock + burn credits);
instead poll `pgrep -f` and read the incremental JSON. (2) A wait-loop using `pgrep -f "sh_batch.py"`
matches ITS OWN command line → never exits; use a distinct marker. (3) Scripts MUST save results
incrementally (per store), not only at loop end. (4) Under headless-Chromium load, VPS sshd briefly
returns "banner exchange: invalid format" — transient, retry. (5) Foreground SSH runs were reliable;
background ones dropped. Helper scripts: sh_batch.py (compact extractor), sh_recheck.py (name/URL retry),
sh_diag.py (search diagnostic) in /opt/market-research-agent/scripts/.
**Applies to:** all VPS ShopHunter scripts.
**Expires after:** Never → op-rules.md.

### [2026-05-25] Session SH-3 — Explore Shops grid: discovery mechanics validated
**Type:** Tactical | **Severity:** MEDIUM | **Confidence:** HIGH (live run, 830 stores)
**Observation:** Store-first discovery works. (1) Categories are a TREE (Google taxonomy) — clicking the
category TEXT only expands sub-categories; to FILTER, click its sibling `<input type=checkbox>` then the
Search button (top-right, x≈1255). (2) Grid VIRTUALIZES the DOM (~48 cards held) → must harvest
incrementally per scroll, keyed by shop_id; filter links to `^/shops/\d+$` only (product sublinks in "Top
Revenue Producers" otherwise inflate counts ~5×). (3) Shop DETAIL page = value-BEFORE-label
(`$202K…Week`, `SE…Country`, `4…SKUs`) — opposite of grid cards. (4) Sort options: Search Relevance /
Revenue / Revenue %Change / Ads / Ads %Change (Daily+Weekly). (5) No result-count text visible; depth =
scroll-to-exhaustion (H&G default = ~830). Helper scripts on VPS: sh_hg_dump.py (incremental dump),
sh_hg_filter.py (tier fast-filter), sh_open_batch.py (detail extractor), sh_render_table.py (screenshot table).
**Applies to:** every Explore Shops discovery run. **Expires after:** Never → op-rules.md when created.

### [2026-05-25] Session SH-3 — Noise classes in H&G + the candidate-loss lesson (adopt FB RULE 8)
**Type:** Pattern / Warning | **Severity:** HIGH | **Confidence:** MEDIUM (1 category, 1 run)
**Observation:** ShopHunter "Home & Garden" carries predictable NOISE (expected, like FB keyword noise, just
thinner): (a) **supplements/wellness/пустышка** (Tonum/Motus weight-loss $59.99, Setu, Auri, SugarbearPRO,
Primal Harvest, Hydroh hydrogen-water $69.99) — and **SH category taxonomy is UNRELIABLE** (Motus tagged
"Gardening›Hydroponics›Nutrient"); (b) **Nordic dropship stores** (SE/DK, Swedish generic-AliExpress
products); (c) **mature giants** (PERGOLUX $2M/wk+207 ads, Hurom, Baby Brezza — not white-label); (d)
**dead/closed** (My Little Dreamy "opening soon", Fridgezy $0). **CANDIDATE-LOSS LESSON:** in SH-3 I cut
103 shortlist→12 by reading NAMES = subjective pre-pick before data = FB RULE 8 violation ("verify ALL above
objective threshold, never top-N by gut"). Fix = the SH-4 funnel (open ALL → objective noise-cut →
intermediate score → top to chat). **METHODOLOGY INSIGHT:** store-first surfaces STORES but scoring needs
the PRODUCT → there is an extra drill-down (store→hero product→price); Explore PRODUCTS may be a more direct
path — worth a comparison test (directional, NOT a conclusion). **Applies to:** SH-4+ funnel design + noise
rejection. **Expires after:** Session SH-10 (or promote if reconfirmed).

### [2026-05-25] Session SH-3 — FIRST full funnel run: result + bot-block/proxy + hero-selection fix + candidates
**Type:** Pattern / Result | **Severity:** HIGH | **Confidence:** MEDIUM-HIGH (1 full run)
**Observation:**
- **Funnel flow worked end-to-end:** 150 H&G dump → Stage1 supplement-by-name cut (−14) → Stage2 open ALL real
  stores on VPS via `/products.json` → **103 LIVE / 9 HOME / 7 CLOSED (HTTP 402 "Unavailable Shop") / ~15 unreachable**
  → Stage2b classify+rank on REAL data → **59 clean Tier A** (physical + price $39-170; dropped supp14/apparel6/POD5/out-range19)
  → deep-scored top 8.
- **BOT-BLOCK / PROXY (key infra finding):** raw `urllib` from the VPS = blocked (403/402); headless Playwright
  works individually but the **DATACENTER IP gets rate-limited under burst** (first run 113/136 DEAD incl. known-live
  titavos). **Paced (4-7s delay + retry) recovered 103/136 (~76%).** FIX = residential proxy — Marina bought **iProyal
  US ISP-residential (SH-3)**. Re-run through proxy recovers the ~33 closed/unreachable + removes pacing need. Use
  **HTTP/HTTPS proxy** (Chromium/Playwright does NOT support SOCKS5 auth). Creds via `scripts/set_proxy_creds.py`
  (getpass, → `cookies/proxy.creds`, gitignored, chmod 600).
- **HERO-SELECTION — RESOLVED (SH-3, Marina-verified via the live ShopHunter UI):** The reliable hero source IS
  ShopHunter's **"Top Products" section (Revenue Week)** on the shop page. Marina's screenshots confirm it MATCHES the
  real catalog AND our scoring: **Titavos #1 = Titanium Cutting Board ($28K/wk); Plantagotchi #1 = AI Smart Planter
  ($11K/wk).** ShopHunter product data is RELIABLE here.
  ⚠️ **MY SH-3 EXTRACTOR HAD A BUG (the cause of the earlier confusion):** `sh_top_revenue.py` searched the text
  "Top Revenue Producers" and took the FIRST match — but that label belongs to each COMPETITOR card under
  "Competitor Analysis", NOT the store's own section (headed **"Top Products"**). So it reported a COMPETITOR's products
  as the store's (the "rust spray / laser pen / fans" were competitors'). PROOF: Elevayr has only 1 catalog product (the
  pillow) yet the buggy script returned 3 fans → impossible → competitor data. The earlier "ShopHunter is garbage"
  conclusion was caused by THIS bug, not by ShopHunter.
  **FIX:** parse the store's **"Top Products"** block (with the Revenue-Week toggle), NOT the first "Top Revenue Producers"
  string. Corroborate with `products.json` (real catalog) + featured product. **Our 4 candidates were scored on the RIGHT
  products.** Secondary heuristics (products.json max-price, og:title) can mislabel on multi-product stores → prefer the
  "Top Products" section.
  **VERIFIED (SH-3):** correct parser = `scripts/sh_hero_v2.py` — it reproduces Marina's live screenshots exactly
  (Titavos #1 = Titanium Cutting Board $28K/wk; Plantagotchi #1 = AI Smart Planter $9799/wk; Stamny #1 = Jar Genie
  $7980/wk → all 3 candidates WERE scored on the right hero; Elevayr = actually a fan store, CryoFan $35.99 = below floor).
  Parse the store's own **"Top Products"** block (NOT the "Top Revenue Producers" label, which sits in "Competitor
  Analysis" higher up — that was the SH-3 bug). **SAFETY NET PROVEN:** "Top Products" also returns the hero for FAILED
  external stores (frozen-402 / DNS-dead / empty-json) — tested on Revelle/Hogar88/Cuvera/Rugify → **no candidate is lost**
  (Marina's #1 priority). External store opening is needed only for enrichment (exact current price / claims).
- **CANDIDATES (recorded so not lost — NOT yet in Notion; Marina: ONE batch after the proxy rerun):**
  🟢 **Stamny Jar Genie** (automatic one-button jar opener, $95, 10K customers, stamny.com) = **Score 73, Worth Testing**
  — arthritis/weak-grip/elderly, demonstrable wow, white-label-able; risks $95 top-range + Amazon jar-opener saturation + ad-count unconfirmed.
  🟡 **Elevayr Cloud Nursing Pillow** (~$65, hands-free waist-strap vs Boppy, elevayr.co) ~64 borderline (saturated category, no reviews seen).
  🟡 **Plantagotchi AI Smart Planter** ($99.99, myplantagotchi.com) ~62 borderline — companion-planter = RECONFIRMS the
  Ivy/PlantBot signal from FB dept (S25-26); but no reviews + discount-spam.
  🔴 Rejects: Breazy "portable AC" (пустышка-overpromise + return-risk + везде), Homaider fondue (commodity/narrow),
  Novima grill-brush ($69.99 overpriced commodity), Plunate (sub-floor commodity).
- **Titavos flag:** funnel revealed titavos.com is MULTI-NICHE (shilajit supplement + frying pan + cutting board) →
  weakens the hero-brand thesis (already in Notion SH-3 — reconsider at review).
**Applies to:** SH-4 funnel refinement (true-hero fix) + proxy rerun + the one Notion batch. **Expires after:** Session SH-10.

### [2026-05-25] Session SH-3 — Marina founder feedback on the 3 ShopHunter candidates (Tier-1 facts)
**Type:** Founder decision | **Severity:** HIGH | **Confidence:** HIGH (Marina direct)
**Observation:**
- **Elevayr Cloud Nursing Pillow (~64) → REJECTED (Recommendation=Rejected, archived in Notion, not hard-deleted).** Reason: "нет вау" (no wow). Scoring was correct; just no wow. Do not re-surface this nursing-pillow type.
- **Plantagotchi AI Smart Planter (~62) → KEEP / strong positive.** Marina confirmed it = the SAME product as **Ivy Gen 2** (store.plantsio.com/products/ivy-gen-2), which the FB dept already found; actively selling; identical product in the Plantagotchi store → China-sourceable. Companion-planter signal reconfirmed across BOTH departments. (NOT a new rule — this is the concrete PROOF that core's existing "60-64 = SOFT, revisit" pays off; no duplicate rule written.)
- **Stamny Jar Genie (73) → KEEP** (Marina kept on record). **Titavos → stays in Notion**, Marina sets Approved/Rejected herself.
- **Notion safety confirmed good:** hard-delete is intentionally not available → mark Recommendation=Rejected + reason, product stays in Archive view (Marina approved this as correct system design).
**Applies to:** Notion retention; scoring-threshold handling. **Expires after:** Never (founder facts).

### [2026-05-25] Session SH-3 — Proxy safeguard plan (Marina-requested)
**Type:** Operational safeguard | **Severity:** MEDIUM | **Confidence:** HIGH (Marina-requested)
**Observation:** Residential proxies occasionally have provider maintenance/downtime (rare; Marina has hit it on iProyal — support confirms "technical works, wait"). Plan:
- **Health-check FIRST:** `scripts/sh_proxy_check.py` (fetch api.ipify via proxy → expect 200 + exit IP). Run at the start of every store-opening job; never run blind.
- **On failure A→B→C:** A = retry 2-3× (transient blip). B = fall back to PACED-NO-PROXY mode (proven ~76% yield) → continue, flag "proxy down — partial run". C = persistent → alert Marina: "proxy unreachable, likely iProyal maintenance — check dashboard / ping support, retry later".
- **Diagnostic order (esp. future 24/7):** if store-opening starts failing → SUSPECT THE PROXY FIRST (run health-check), not the VPS / ShopHunter.
**Applies to:** every proxy-based run. **Expires after:** Never → op-rules when created.

### [2026-05-25] Session SH-3 — Clean funnel pass with TRUE heroes (v4)
**Type:** Result | **Severity:** MEDIUM | **Confidence:** HIGH (verified parser)
**Observation:** Ran `sh_topproducts_batch.py` over ALL 150 stores (no Stage-1 name-cut, per Marina) → **148/150 real heroes**
extracted from ShopHunter "Top Products". Classified by the REAL hero: physical 124 / supplement 11 / пустышка 6 /
apparel 4 / POD 3. Clean **Tier A (physical hero + $39-170) = 71** → `hg_tierA_v4.json`. True-hero surfaced NEW physical
candidates the flawed pass had hidden: **ZAIA hot-air styling brush ($202K/wk), Keyf portable espresso ($75),
Orré electric back brush ($60), Valia full-face respirator ($110), EkoVibe neck massager ($118), Miller warming mat
($160)** + confirmed **Titavos** cutting board ($28K/wk). **Caveat:** the name-based classifier still leaks some
supplement/apparel with non-obvious titles (Tonum "motus", "Metabolic+", "Stem Cell Restore", jorts/snow-boots) → real
пустышка/supplement filtering happens at DEEP-SCORING on actual product+claims (Marina: don't trust name-cut).
**Applies to:** SH-4 candidate selection. **Expires after:** Session SH-10.

---

## Expired / Promoted

**Expired at SH-10 (2026-05-27) — durable substance preserved in `methods/discovery-funnel.md` + the SH-3/SH-4 handoff blocks above; archived in place (tagged "Expires after: Session SH-10"):**
- SH-3 "Noise classes in H&G + the candidate-loss lesson (adopt FB RULE 8)" — superseded: FB RULE 8 (verify-all, no gut top-N) is now baked into the funnel + structural safeguards; noise classes documented per-niche in `shared/rejected-products.md`.
- SH-3 "FIRST full funnel run: result + bot-block/proxy + hero-selection fix + candidates" — superseded: hero-selection ("Top Products" parser = `sh_hero_par.py`), proxy (iProyal, see SH-9 entry), and the SH-3 candidates are all resolved/in Notion.
- SH-3 "Clean funnel pass with TRUE heroes (v4)" — superseded: true-hero extraction is the standing `sh_hero_par.py` mechanic; name-classifier-leaks-caught-at-deep-score is now the Description-confidence gate (discovery-funnel.md).
(Entries left physically in place under "Active Learnings" for full history; they are no longer active guidance.)

---

## How to add a learning

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW / MEDIUM / HIGH / CRITICAL
**Confidence:** LOW (1 case) / MEDIUM (2–3) / HIGH (multiple or founder-confirmed)
**Observation:** what was found (2–5 lines)
**Applies to:** [store type / category / discovery path]
**Expires after:** Session [N+7]   (use "Never" → promote to op-rules.md instead)
```
