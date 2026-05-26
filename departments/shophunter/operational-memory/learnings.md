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
⚠ **PRE-FLIGHT:** Baby & Toddler will skew heavily to baby APPAREL/clothing + nursery DECOR + feeding CONSUMABLES — the
genuine white-label GADGET subset (monitors, sleep/sound aids, feeding/bottle devices, safety gadgets, carriers) is a
SMALLER fraction (but baby sleep sacks / swaddles / carriers / sleep-aids ARE winners — do NOT blanket-cut "apparel" in this
niche; see [[feedback-winning-products-not-gadgets]]); the conservative cut + live-description filter handle it.

**Marina's FURTHER idea (AGREED direction) = a TRACKED-SHOP COLLECTION + "Newest First" monitoring layer.** Add proven/
competent shops to a ShopHunter Collection (My ShopHunter → Shop Collections), then check `Products → Newest First` every
2-3 days to catch the NEW products traction-operators launch (early-winner detection BEFORE saturation = the entry-window we
score for). Seed = our vetted 65+/55-64 shops (minus dropship-junk). Build order Marina set: **(1) recon** the add-to-collection
+ Newest-First mechanics on her existing collection (2 shops) → **(2) report feedback** → **(3) bulk-add seed** → **(4) recurring
human-in-loop check-up**. This is a MONITORING layer ON TOP OF category dumps, not a replacement. Other surfaces still open:
Explore PRODUCTS view, geo-test, H&G-by-NEW/growth.

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
**STATUS CONVENTION:** Consider = not-now-but-monitor/may-return (NO rejection reason, stays on radar); Rejected = closed →
Archive. **CRITICAL CALIBRATION: convergence / revenue do NOT make Marina PURSUE — at best they earn Consider/monitor.
Approve/test needs clear WOW + perceived value + category priority.** I over-weighted the titanium ×3 convergence as the
"strongest find"; her call = Consider/monitor ("no wow yet"). SH-5: lead candidate recommendations with WOW + taste read
(from live description), not the convergence count; surface trend/convergence finds as monitor-candidates.

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

_Empty._

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
