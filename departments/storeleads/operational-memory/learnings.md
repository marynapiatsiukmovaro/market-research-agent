# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**▶ S12-ANALYSIS (2026-06-07) — 🏁🏁 CATS FULLY COMPLETE (b1–b19, 4635 stores). processed = 12854. This session analysed b14–b19 (1385 stores) + marked b13. NEXT: pick next niche — ⚠️ K&D is NOT ready (see below); DOGS reservoir IS ready (~9250 enriched by the parallel S11 prep).**
- **Mode = 🔬 ANALYSIS on the pre-built Cats reservoir** (decoupled prep→analysis model, first full test). **b14–b19 = 6 batches, ALL gates PASS, 0 winners 65+ / 1385 stores.** b15 = **2 borderline** (petarro cat exercise wheel 64 · bxsdesigns Boxscoop patented litter box 61 — both → keep-list, flag-for-founder, NOT Notion). Live-confirm (RULE 7) killed 2 enricher-mispicks in b14/b15 (dog tennis-launcher / $300 litter box surfaced as the real hero). loss≈0 every batch (every needs_live+unreachable hand-opened, gate-verified). HTML previews on Desktop/StoreLeads; artifacts `cats_b{14..19}_opens/scores.jsonl` on VPS.
- **🧩 WHOLE-NICHE RESULT (b1–b19):** **2 winners total** (SiiPet LitterLens 74 · Catboxy Nova 72) — BOTH in **b1 (top-visit tier, visits ≥1020)**, already in Notion since S9. b2–b19 (visits 1014 → vNone, ~4385 stores) = **0 winners**. ⭐ **VISITS-GRADIENT CONFIRMED across all 19 batches** — but treat as an OBSERVATION, not absolute law (many categories ahead; RULE 24 stays — never field-filter by visits). Tail = foreign micro-stores / cat merch / tofu-litter / fountains / high-ticket auto-litter ($130–940) / dev-dropship `.myshopify`.
- **📡 CONVERGENCES (market-intel, b14–b19):** cat **exercise wheel ×4** (petarro $150 · meowza $263 · PawSquad $92 · FelineFit $285 — emerging, but bulky/high-ship RULE 10) · **health-vein** (vetpointbio at-home disease tests · smartylitter/Pacha colour-health litter · felinutri urine-test) · **allergy-topper ×3** (trybuckley/sneezelesscat/thefurrypack — reduce HUMAN cat-allergy via food, but result not camera-verifiable = Veto-risk) · self-clean litter (saturated) · automated balls/laser-toys (saturated).
- **✅ PREP→ANALYSIS MODEL VALIDATED:** 6 batches / 1385 stores in ONE context window, **NO compact** (Marina confirmed <½ context), no scraper wait (instant start off ready chunks), gates PASS ×6, 0 degradation. The reservoir gave a real wall-clock win; the ONE constraint is the in-context full read (RULE 6) — **Marina ACCEPTS this as the price of quality.**
- **🚫 DELEGATION / sub-agent-reader = REJECTED-FOR-NOW (Marina S12).** Quality > speed; delegating the read risks dropping a winner on a sub-agent's filter. NOT permanent — re-openable if future tech delegates without proven quality loss. Main agent keeps reading ALL + opening ALL flags. See `review/promotion-queue.md` (Decided) + memory `feedback_no_delegation`. **Other optimisation proposals stay welcome.**
- **⚠️ NEXT-NICHE REALITY (verified on VPS, S12 — corrects the S12-prompt's "K&D 4000 ready" assumption):** **K&D is NOT ready** — only a ~405-store **Day-1 pilot** (`niches/home-and-garden/kitchen-dining/_index.md`: dump lost S10, 29,150 stores ≥2020 untouched, needs a full re-dump = StoreLeads-quota-bound). **DOGS IS the ready reservoir** — the parallel **S11 prep** has **~9,250 stores enriched (37 chunks)** and is **still building** (chunk b38 live on VPS; `enriched_index.json`). Decoupled model allows analysing the same niche being built. **Marina to pick the next niche after compact.**
- **System Health = ALL GREEN** (Stage-2 acceptance · analysis gate · no data errors · errors prevented via RULE 7 · no winner loss · no degradation · stable across all Cats · analytics ready to scale in QUALITY, throughput stays human-paced by design). *(S9-ANALYSIS block below collapsed per RULE 18 — Cats now complete; full text in git e18cb1a/c9293f0.)*

**▶ S11 (2026-06-07, PARALLEL prep — still running) — 🏭 DOGS reservoir build.** Decoupled `sl_select_build` (enriched_index exclusion, NO SKIP) + `sl_accept_chunk.py` per-chunk acceptance + wave-rhythm (op-rules RULE 30 / workflow §1b updated, Marina-OK). ~37 chunks enriched (~9250 stores), building b38+ on VPS. This block is a pointer — S11 manages its own HANDOFF; do not clobber.

**▶ S10 (2026-06-06) — 🏭 RESERVOIR-PREP + ⚠️ QUOTA WALL + 🧹 SERVER HYGIENE. NO analysis ran (processed still 11219). NEXT: await StoreLeads support reply on Pro upgrade; meanwhile Dogs reservoir is ready to ENRICH (proxy = no quota); Cats b14–b19 tail + K&D re-dump still pending.**
- **Part A DUMPS:** 🐶 **Dogs reservoir DONE** = `niches/pets-and-animals/dogs/dogs_full.json` **21,985** stores (Stage-1 raw, server-reconcile EXACT). Ready for `sl_enrich4` (enrich = PROXY, NOT StoreLeads quota → buildable anytime). 🍳 **K&D dump FAILED + LOST:** original truncated at 25,055/29,182 (cursor-pagination transient — the RECONCILE check caught it), then the partial file was **overwritten to 0 by my fix-script on the same slug → lost (no backup).** Re-dump from scratch when quota returns. Filters (Marina-confirmed): Shopify + Active + **Created≥2020** (NOT 2021), no country.
- **⭐⭐ QUOTA WALL — the key finding:** StoreLeads **Premium ($75) = 2,000 searches/month, EXHAUSTED by the dumps** → `/json/auth/domains` returns **HTTP 402 Payment Required**. Pagination is search-expensive (~1000 page-reqs/dump). Probe `sl_dump3` confirmed (worked at session start, 0 after). **PLAN limit, NOT a system bug** — our dump algorithm is correct (Dogs reconciled exact; HI proved it earlier). **Pro ($250) = Unlimited searches + Export-to-CSV + API** → CSV export = whole filtered niche in ONE file (no pagination/quota/transients) = the structural fix that REPLACES the paginated-dump approach. Elite ($450) = all platforms. Platform-swap = self-serve (Account→Platforms, at billing boundary). **Marina emailed support** (mid-cycle upgrade proration? change 2nd platform on upgrade? does CSV-export consume searches?) — **AWAITING reply.**
- **NEW SCRIPT (UNVALIDATED):** `scripts/sl_dump_full2.py` (VPS) — hardened dumper: retry-on-empty + RECONCILE collected-vs-server + auto-quarter-split on shortfall. **NOT validated (quota blocked the test).** Validate vs a known count (Dogs=21,985) BEFORE trusting. Gotcha: exact-month `cratyyyymm` min==max → 0 (zero-width range broken); use bounded year ranges min<max.
- **🧹 SERVER HYGIENE (Marina-directed):** mapped the VPS (HTML map → Marina Desktop `StoreLeads/VPS-Map.html`). Disk 6.7/75 GB (10% — tons of room, no space pressure). Built **trash** `logs/_trash/` (mv-not-rm). Moved `cookies/shophunter_profile.OLD` (1.4 GB junk) → trash (cookies 1.4G→85M). Wrote **`shared/server-conventions.md`** (+ VPS-root copy `SERVER-CONVENTIONS.md`): one-folder-per-dept · **deletion needs Marina's OK** (mv→_trash, purge only on OK) · hygiene by size-trigger (2-3GB+) only, else hands-off · no-backup→STOP-and-ask. home-improvement KEPT (Marina still wants to analyze it).
- **LESSONS (Marina, S10):** (1) a new/fixed script writes to a **TEST slug first, NEVER over a live file** (caused the K&D loss). (2) **Unprecedented/abnormal situation → STOP and ask**, no hasty overwrite/delete — following rules too literally cost the 25k. (3) Dumps are quota-bound on Premium → **budget dumps**; CSV-export on Pro removes the constraint.

**▶ S9-ANALYSIS (2026-06-05) — collapsed per RULE 18 (superseded by S12 = Cats COMPLETE; full text in git e18cb1a/c9293f0).** Analysed Cats b1–b13: b1 (top-visit) = 2 winners (SiiPet LitterLens 74 · Catboxy Nova 72) + 4 hand-picks → Notion; b2–b13 = 0 winners. First confirmed the visits-gradient (winners in top-visit tier only) + deep-tail convergences (nail-file box, fountains, steam brush, self-clean litter, health-vein). S12 then finished b14–b19 = 0 winners → niche fully exhausted.

**▶ S8-ANALYSIS (2026-06-05) — collapsed per RULE 18 (full text in git).** 🏁 NURSERY-PLAYROOM COMPLETE — full vNone reservoir b1–b11 analyzed → 0 winners 65+ / ~2621 stores (honest reliable zero, vNone tail structurally exhausted), system GREEN 11/11, processed→8219. Hypothesis "vNone still yields winners" NOT confirmed on Nursery (verdict deferred to Cats+). Notion: Yogorgeous Anti-Roll Mat 53 (Watchlist) + Rockit 3-brand convergence. ⭐ Perf-observation: ~85% per-batch context = reading 250 cards (RULE 6) → sub-agent card-reader is the open Tier-2 proposal.

**▶ S8-BUILD (2026-06-04) — collapsed per RULE 18 (full text in git).** Built TWO reservoirs (Nursery vNone 2621 + Cats FULL niche 4635, all enriched/chunked, markers `ALL_RESERVOIR_DONE` / `CATS_RESERVOIR_DONE`) + hardened the system. Durable rules now live permanently in **op-rules (RULE 30)** + **workflow §1b** (RESERVOIR-BUILD mode, ACCEPT-logic, 10-pt checklist) + **`scripts/sl_master_dedup.py`/`master_domains.json`**. Key verified finding (kept): **"unreachable" ≈ store has `products.json` DISABLED** (storefront ALIVE → needs_live hand-open; re-run does NOT recover; truly dead = DNS-000/frozen-402 only). Commit 548f9ee.

**▶ S7 (2026-06-03) — collapsed per RULE 18 (full text in git).** Scale-validation PASSED (Nursery b12–b16, gates GREEN 5/5) + adopted **P1/P3 tooling (op-rules RULE 29** — `sl_open_flags.py` auto-opener makes "opened-but-not-logged" structurally impossible; P2 functional-noun sweep DROPPED) + **founder-feedback APPROVAL FORMAT (RULE 17)**. Winners (Rockit/LatchLight/WonderBee/etc.) in Notion + founder-feedback. Proved StoreLeads v1 scales without losing winners.

**▶ S6 (2026-06-03) — collapsed per RULE 18 (full text in git history).** Pipeline HARDENED → **RULE 25–28** (canonical Stage-2 reader `sl_stage2_table.py` + `sl_qa.py` QA-gate + `sl_analysis_gate.py` + deterministic browse-pool). b9/b10/b11 re-run correctly (the broken S5 read superseded). **#4 convergence-as-SCORE REJECTED** (a 250-store batch isn't market-representative; pattern-noting/SL2-folding STAY, score/tier weighting does NOT). MARINA-FACING CHECKPOINT codified (workflow §2). Winners: Kanga 67 · UpPro 67 · WriggleBum 68 (the one the S5 partial-read LOST — proof hardening works). processed→4348.

**▶ S5 (2026-06-02) — collapsed per RULE 18 (full text in git history).** DIAGNOSTIC session: agent scored 1000 stores off a hand-made `/tmp` reader showing **1 of 3 products** → "0 winners" INVALID; **Marina caught it, not the system.** Root cause = no single canonical Stage-2 reader (→ fixed S6 RULE 25) + no card-completeness QA (→ RULE 26). **Scraper data was CORRECT** — breakage was in READING, not collection. Lesson → memory `feedback_storeleads_full_card_3stage.md` (judge by the full 3-product card).

**▶ S4 (2026-06-01) — collapsed per RULE 18 (full text in git history).** Nursery visits-desc deep-dive (batches 3–8, 1500 stores). **RULE-24 `sl_select_all`** (no field-filter, visits=ORDER only — missing≠absent) + RULE 23 (open every flag) caught 2 deep-tail winners (visits 363/387) the old 1k–50k band would have LOST; 0-loss measured 4×. **DECOUPLE/reservoir test VALIDATED** (`enriched ≠ processed`; instant analysis, 0 scraper wait — Marina prefers it). 6 winners → Notion. Reservoir-architecture proposal filed (built out in S8).

**▶ S3 (2026-06-01) — collapsed per RULE 18 (full text in git history).** Nursery visits 1k–50k band done (594 stores, consumer ~80%). Enricher **v4.2/v4.2.1** (`needs_live` = card-insufficient only; `hero_confidence=low` is a source artifact, recalibrated). 12 Notion cards. **⭐ FOUNDER CALIBRATION (lives in founder-feedback):** SATURATION + SAMENESS + "ad-cost won't clear" overrides "solves pain + proven category" → such products are **55–62 Watchlist, NOT 67–72**; score the **DIFFERENTIATOR/gap, not just the pain**; apparel off-model unless tactile/functional diff; stylish-alone → Watchlist, +seasonal/viral hook → Consider.

**▶ S2 FINAL (2026-05-31) — collapsed per RULE 18 (now the 3rd-oldest HANDOFF; keep only 2 = S4 + S3).** Built the v2
product-centric enricher (then `sl_enrich3`, now superseded by v4.2), ran HI batches 1–4 (800 stores, stable LOW yield —
"heavy"/trade category), wrote 2 HI winners to Notion, matured the department (created op-rules + method docs). The "panic-fix /
invented 81/40%" lesson is permanent in **op-rules RULE 4a**. Full text in git history + `handoffs-archive.md` (batch-200 / PM block).

---

**▶ S2 (2026-05-31 PM) HANDOFF — collapsed per RULE 18 (3rd block; keep only 2).** Its content is fully superseded by
**S2 FINAL** above (same architecture-v2 decision + HI batches 2-3 yield) and lives verbatim in git history + the methods
docs (`hypotheses/_active.md`, `subagent-spec.md`, `discovery-funnel.md`). Nothing lost — removed only to keep the
mandatory-load lean.

---

> **Older session snapshots — DAY 1 (2026-05-30 pilot) + DAY 2 (2026-05-31 strategy/bq-crack/census/full-dump)
> → moved to `operational-memory/handoffs-archive.md`** (RULE 18; full text also in git). They carry the bq/Bleve
> crack, the 12-subcat census, the export-field decisions, and the K&D pilot — reference there if needed.

---

## Active Learnings

### [2026-06-07] S12 — The winner-bearing visits-zone is NICHE-DEPENDENT (opposite of Nursery) → never assume a fixed band (reinforces RULE 24)
**Type:** Pattern / Yield fact | **Severity:** MED-HIGH | **Confidence:** HIGH (Cats fully exhausted, 19 batches / 4635 stores, every gate PASS, loss≈0)
**Observation:** Cats and Nursery gave **OPPOSITE** visits-distributions of winners. **Nursery** (S4): winners hid DEEP (visits 363/387, below the old band). **Cats** (S9+S12): the 2 winners sat ONLY in the TOP-visit tier (b1, visits ≥1020); the entire tail b2–b19 (visits 1014 → vNone, ~4385 stores) = **0 winners** (foreign micro-stores / cat merch / tofu-litter / fountains / high-ticket auto-litter / dev-dropship `.myshopify`). **Lesson: do NOT generalise "winners live deep" OR "winners live up top" into a rule — the winner-zone varies by niche, so the ONLY safe policy is RULE 24 (read EVERY store, visits = ordering only, never a filter).** The visits-gradient is a useful per-niche OBSERVATION for *narration/pacing*, never a gate. Honest low-yield in the tail is valid (RULE 11) — but we only KNOW it's empty because we read all of it (this is also why the sub-agent-reader delegation was rejected, S12 — quality>speed).
**Applies to:** every Store Leads niche dive. **Expires:** Never → reinforces RULE 23/24 + the [2026-06-01] S4 entry below (which now reads as the niche-specific Nursery case, not a universal law).

### [2026-06-01] S4 — Winners live in the DEEP visits-tail; established-band is structurally off-model (measured)
**Type:** Pattern / Reliability fact | **Severity:** HIGH | **Confidence:** HIGH (1000 stores, 4 batches, 4× 0-loss audit)
**Observation:** Nursery visits-desc, 4 batches/1000 stores. **b3 (visits 1.9k–12.7M, established) = 0 winners** — structurally formula/apparel/furniture/mega-brands/catalogs. b4/b5 (low-visits) = 0. **b6 (visits 268–447) = the 2 winners** (Doppler 77 @ v387, Crib Tent 73 @ v363). **Both sit BELOW the old 1k–50k band → the old visits-filter approach would have lost both winners.** This is the concrete proof that RULE 24 (no field-filter; visits=ordering only; missing≠dead) + RULE 23 (open every flag) are not over-insurance — they are load-bearing. 0-loss confirmed 4× by spot-auditing the dropped pile (off-model: apparel/formula/consignment/furniture-oor). **Funnel Stage1→3 = strong, loss≈0 within the dump.** Nursery as a niche = weak white-label-gadget grebe (apparel/formula/furniture-dominated) — honest low-yield (RULE 11), matches Marina's S3 Watchlist pattern. **Residual loss-risk is UPSTREAM (Stage-0 category=None + SL taxonomy mis-tag)** — see promotion-queue.
**Applies to:** every Store Leads niche dive — never stop/gate by visits; the tail is where emerging white-label sits. **Expires:** Never → reinforces RULE 23/24.

### [2026-06-01] S4 — Live-open (RULE 23) cuts BOTH false-negatives AND false-positives; WebFetch has a rate-limit (use VPS-curl fallback + cooldown at scale)
**Type:** Process / Reliability + Scaling | **Severity:** MED-HIGH | **Confidence:** HIGH (b7/b8, ~95 live opens)
**Observation (RULE 23 value, both directions):** hand-opening every `needs_live` proved it catches **two** error types, not one: (1) the known false-NEGATIVE (a winner the card under-sold) AND (2) **false-POSITIVES** — b8 cards labelled `proactivepillow` + `mylittlebean4d` as "Prenatal Doppler" (which would've been a fake doppler-convergence), but live-open showed a maternity **pillow** and a **4D-ultrasound studio**. So the card's candidate-pick can MIS-name a product; only the live site is truth (reinforces RULE 6 "live site = source of truth"). Net both batches: needs_live opened → 0 hidden winners; winners (LatchLight/Roar/Rockit/CribTent) all came from the **card-sufficient** pile found by READING, not from scraper flags. Loss ≈ 0.
**Observation (scaling — NEW):** the live-open layer uses **WebFetch**, which has its own rate-limit — firing ~16 at once returned `429 Too Many Requests` for a sustained window (short 80s/180s cooldowns did NOT clear it). **Fixes that worked:** (a) open in **small batches (~4–6) with pauses**, not one big burst; (b) **fall back to VPS-side curl** (`/tmp/sl_curl.py` pattern — title+meta+price hints, our server, NO WebFetch limit, idle anyway) — used it to finish 13 stores cleanly. **3 stores stayed truly unreachable** (DNS-dead / empty placeholder) via every path = dead/non-public витрины (not launchable; safe to treat as off-model).
**Applies to:** every batch's hand-open step; ESPECIALLY at 2–4k scale. **Expires:** Never → fold the "small-batch + curl-fallback" pattern into the reservoir build (proposal #1 inter-chunk cooldown now covers the OPEN layer too, not just the scraper).

### [2026-06-01] S3 — Scoring stays AS-IS + "open every flag" + re-audit proved no loss
**Type:** Process / Correction | **Severity:** HIGH | **Confidence:** HIGH (Marina-decided + 20-store re-audit)
**Observation:** Marina questioned the 65+ list (saturated baby products scored 66-72 she'd never test). Cross-checked
ShopHunter: SAME pattern there (Swaddelini 72→Rejected, Grownsy 66→Rejected) — my scoring was consistent, not uniquely
broken. **Decision (Marina): keep the scoring system AS-IS — do NOT tighten.** A tighter score would drop a 60→40 and the
agent would then NOT SHOW it → that is how we'd LOSE good products. Instead: report all 65+, SHOW every borderline+browse
regardless of score, accumulate founder-DECISION patterns as department knowledge (founder-feedback), and lead the checkpoint
with an honest wow/differentiation/saturation read. The one real error was inflating Wow-Effect — fix = score Wow accurately
(ordinary=low) WITHOUT cutting the report-set; Founder Review is the filter.
**Second issue — "opened only 22 of 344":** there is NO cap; 22 was the agent's hand-picked "interesting" set. Risk = the
agent's "this is clear, skip" call could be wrong. **Fix (RULE 23 strengthened): open EVERY robot-flagged `needs_live` +
unreachable, not the agent's subset — if flagged=60, open 60.** Re-audit this session: opened 20 dismissed in-range stores →
**all 20 correctly skipped, 0 gems lost** (commodity/apparel/formula/gift/branded/bulky/retailer); remaining ~86 clear-skip
by pitch → ~95% no-loss confidence for this batch; the standing "open every flag" rule makes it ~100% by-design next batch.
**Applies to:** every Store Leads batch. **Expires:** Never → op-rules RULE 23 + founder-feedback governance note.


### [2026-05-31] S2 — `sl_enrich3.py` v2 built + 2 currency/price bugs caught in smoke-test
**Type:** Tactical / Pattern | **Severity:** HIGH | **Confidence:** HIGH (live 5-store smoke ×2)
**Observation:** Built v3 product-centric enricher (top-3, open-ladder incl. homepage-HTML fallback, hero/desc-confidence,
maturity, no-revenue proxy). Smoke-test on 5 HI stores caught two real bugs BEFORE the full batch:
(1) **Store currency must come from Shopify `/meta.json` (`currency` field), NOT the dump's `country` code** — renpho.uk has
dump country=HK but actually sells in GBP; using country mis-converted £109.99 as HKD→$13. `/meta.json` (fallback `/cart.json`)
returns the TRUE store currency (verified renpho.uk→GBP, pacificpowertools→USD). products.json variants carry NO currency, only
a bare number. This is exactly the foreign-currency trap Marina flagged (₹/AUD read as $). (2) **price==0 = "by quote"/installation-
guide/non-buyable → NOT a candidate** (was leaking as price-out noise; now skipped → store DROP-noPhysical if all are 0).
**Applies to:** every Store Leads enrich run. **Expires:** Never → fold into subagent-spec when code promoted.
**FIX-2 (full batch caught a 3rd bug the smoke-test missed):** the homepage-HTML fallback calls `/products/<handle>.json`,
whose `variants`/`images` come back as a **DICT** (`{"0":{...}}`), not a list → `[0]` raised `KeyError: 0` and (no per-store
guard) killed the WHOLE 200-store batch. Fix: `as_list()` normalizes dict-or-list; **every store wrapped in try/except** →
one bad store becomes a MANUAL row with the error reason, never crashes the run. Lesson: a fallback path untriggered in a
5-store smoke can still blow the full batch — always wrap per-item work in try/except in a parallel pool.
**FIX-3 (precautionary — price-0 should never silently drop a live store):** batch-4 (v3) actually showed
**DROP-noPhysical = 10/200** (NOT 81 — an earlier note here falsely claimed 81/40%; that was an unverified number I
wrote without checking the data — corrected. Real tiers: A47/B41/C88/MANUAL14/DROP-noPhysical10, reach 186/200).
The 10 drops are trade stores (craftdoorsusa/flowdrill/butlerlumber/brasscitytile…) whose enriched `clean[]` came out
empty. Cause not yet fully confirmed live (proxy `/products.json` blocked from my local check — cert errors). As a
**precaution** (and consistent with the currency/hero "never trust raw service data" principle): changed `price<=0` from
"skip product" to keep it `price_unknown=True`; a store whose candidates are ALL price-unknown → new tier
**`PRICE-CHECK`** (confirm price on the live site), never a silent drop. Apparel-only still drops on `kind`. ⚠️ This fix
is NOT yet validated on a real price-0 store (my targeted smoke had 0 input — wrong domains). Validate on batch-4's
re-run before trusting. **Lesson (on MYSELF): I asserted "81/40%" with zero data — exactly the hallucination our
desc-confidence/verify-live rules exist to prevent. Verify the number before writing it.**

### [2026-05-30] DAY 1 — Store Leads = clean internal JSON API behind a Shadow-DOM SPA
**Type:** Tactical / Pattern | **Severity:** HIGH | **Confidence:** HIGH (live)
**Observation:** Dashboard text is empty (Vaadin shadow DOM) — judge screenshots. But `/json/auth/domains`
returns rich store-level data (revenue/price/created/reviews/FB-pixel/newest-product) per result → Stage-1
needs NO site visit; only finalists get a live hero-confirmation. Filters = `f:<field>`; pagination `cursor`;
25k/query ceiling; multi-country = AND bug (query per country). **Applies to:** every run. **Expires:** Never → op-rules.

### [2026-05-30] DAY 1 — Stage-3 discipline: never eyeball the proxy A/B/C tier
**Type:** Warning / Correction | **Severity:** HIGH | **Confidence:** HIGH (Marina caught it)
**Observation:** First Stage-3 attempt read the enricher's A/B/C revenue-tier and editorialised scores →
unreliable "no winner". The enricher tier is a revenue/price SORT-AID, not quality. Real Stage-3 = read ALL,
confirm the hero on the live site (enricher mis-picks: bundles; SUSTEAS list implied a grill but the bestseller
was a $33 grater), run 100-pt + Marina Veto, lead with WOW/taste. **Applies to:** every Stage-3. **Expires:** Never → op-rules.

### [2026-05-30] DAY 1 — Pool/sort + niche-yield (Kitchen & Dining)
**Type:** Pattern / Yield fact | **Severity:** MEDIUM | **Confidence:** MEDIUM (1 niche, 1 run)
**Observation:** Default **rank sort surfaces the BIGGEST stores = established brands** → emerging white-label
sits deeper and was under-represented in the first 200. K&D @ rank-sort + $100k–1M = cookware/dinnerware/glass/
knife-collector/decor/food brands + catalog stores dominate; few impulse white-label gadgets, those branded/premium/
saturated (self-heating mug ×2 = convergence but везде). **Fix:** sort by Created↓ / Est Sales↑ (crack the param).
Tier-1 yield fact — do NOT close the niche or add a filter; keep scoring as-is. **Applies to:** niche selection + sort.
**Expires after:** revisit once sort is cracked + a Created-sorted pull is run.

### [2026-05-31] S2 — Unreachable-диагностика батчей 2+3 (18 сайтов проверены вручную)
**Type:** Pattern / Yield fact | **Severity:** MEDIUM | **Confidence:** HIGH (все 18 открыты вручную)
**Observation:** Батч2 13 DROP + батч3 5 DROP = 18 «недоступных» (enricher: tops=0). Проверила КАЖДЫЙ через WebFetch
(как S1, где 11/12 оказались живы). РЕЗУЛЬТАТ S2: **17/18 сайтов реально открываются** — «unreachable» = НЕ мёртвый сайт,
а `products.json` выключен / нестандартный каталог (enricher не достал tops, но homepage жив). НО: проверка контента
показала, что **ни один из 18 НЕ winner** — это локсмит-/HVAC-СЕРВИСЫ (abbeylock, glassmancorp, greatlakesremodeling,
blantonsupplies), trade-лес/материалы (renocarsonlumber, lakeandlumber, nesttile), запчасти-вода (industrialh2o), либо
вне-модель (handlesinc $162 ZAR, squarepeg toilet $77 commodity, carrierathome брендовый Carrier). 1 cert-ошибка
(glassflooringsystems). **Вывод:** в S1 потеря была реальной (11/12 живы И среди них был borderline juggernaut) → проверка
unreachable ОБЯЗАТЕЛЬНА (RULE 1+7). Но в «тяжёлой» HI-категории unreachable-хвост = сервисы/trade, не белые лейблы.
**Применять:** всегда ручная проверка ВСЕХ unreachable (никогда не списывать как «мёртвые» без открытия). **Expires:** Never → подтверждает RULE 1.

### [2026-05-31] S2 — `conv_batch` ложно завышается гео-зеркалами одного домена
**Type:** Warning / Optimization | **Severity:** MEDIUM | **Confidence:** HIGH (живой случай)
**Observation:** Топ конвергенции батча3 (cv6) = ОДНА tapestry на 7 гео-зеркалах glopalstore (mx/nl/at/de/hu/cl/ro-fullmoonloom)
— `conv_batch` посчитал их как 6 «разных магазинов под один продукт». Это ложный сигнал. **Фикс-идея (в копилку оптимизации):**
при подсчёте conv_batch схлопывать домены по корню (убирать гео-префикс + `*.glopalstore.*`) → один источник = 1, не N.
Реальная конвергенция S2: smart-замки fingerprint ×2 (iveise+teeho, б2), бидет-приставки ×3 (buttbuddy+theinushome+desc, б3).
**Применять:** не доверять высокому conv_batch без проверки, что это РАЗНЫЕ бренды, а не зеркала. **Expires after:** когда conv_batch почистят от зеркал.

### [2026-05-31] S2 — VPS ops reliability: 255≠смерть процесса + минимальный nohup (повтор урока SH-2)
**Type:** Warning / Correction | **Severity:** HIGH | **Confidence:** HIGH (потеряла ~30 мин в начале S2)
**Observation:** В начале S2 потеряла время, переоткрывая решённое: (1) SSH exit 255 = ОБРЫВ канала, НЕ смерть удалённого python
— нельзя перезапускать (наплодила дубли скрапера на один прокси-профиль); надо `pgrep -f "[s]l_enrich2"` + опрос sentinel.
(2) Длинная составная команда обрывается, не дойдя до строки запуска → запуск ТОЛЬКО минимальным однострочным `nohup`.
(3) НЕ heredoc по живому SSH (Marina остановила; SH-4 op-rule: писать скрипты локально + scp). (4) `pgrep -fc sl_enrich2` ловит
сам себя → всегда `[s]l_enrich2`. (5) `sl_enrich2.py` принимает 3 ОБЯЗАТЕЛЬНЫХ арг: INF OUTF SENT [workers] — без SENT падает мгновенно.
**Урок процесса (Marina):** при любой заминке СНАЧАЛА свериться с learnings других отделов (FB/ShopHunter), а не изобретать заново.
**Применять:** все VPS-запуски Store Leads. **Expires:** Never → кандидат в op-rules.

### [2026-05-31] S2 — HI-категория ×3 батча = устойчиво низкий white-label выход (600 магазинов)
**Type:** Yield fact | **Severity:** MEDIUM | **Confidence:** HIGH (3 батча, 600 магазинов)
**Observation:** Home Improvement, 3 батча по 200 (визиты от 13.8k вниз до 4k) → 0 уверенных winner 65+ во всех трёх.
Лучшее = borderline: smart-замки (~66-70, но Amazon-насыщено), refinishing kit ($39.99 расходник), бидет ×3 (premium/везде).
Категория структурно «тяжёлая» (RULE 11): доминируют trade/материалы/запчасти/проф-инструмент/сервисы. Воронка РАБОТАЕТ
(честно показывает мусор + ловит немногое стоящее), но HI — не та грядка под Instagram-модель (wow + impulse + проблема).
**Применять:** при выборе следующей ниши предпочесть «потребительские» подкатегории census (Nursery&Playroom, Cleaning, Pets/Dogs/Cats)
— там плотность white-label с wow выше. **Expires after:** revisit если Marina захочет добить оставшиеся ~900 HI.

---

## Expired / Promoted
(none yet)

## How to add a learning
```
### [YYYY-MM-DD] Session — [Title]
**Type:** Pattern / Warning / Signal / Tactical | **Severity:** … | **Confidence:** …
**Observation:** … **Applies to:** … **Expires after:** Session N (or "Never" → op-rules)
```
