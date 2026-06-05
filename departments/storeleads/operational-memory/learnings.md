# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**▶ S9-ANALYSIS (2026-06-05) — 🏁 CATS deep-tail EXHAUSTED. b1–b13 of 19 ANALYZED. processed = 11219 (b1–b12 marked; b13 read + gate-PASS, 0 winners, NOT yet marked). 6 products IN NOTION (Founder Review PENDING). Marina called STOP at b13 → NEXT = PIVOT.**
- **Mode = 🔬 ANALYSIS on the pre-built Cats reservoir** (`cats_s1_b1–b19_enriched.json`, marker `CATS_RESERVOIR_DONE`, 4635 stores/19 chunks). Canonical pipeline ran clean **13/13 batches** (sl_qa → sl_fullcard read-ALL-250 → sl_open_flags P1 → sl_analysis_gate → checkpoint → mark_processed). **Both gates PASS ×13, 0 degradation.** b1 = products.json QA-STOP (ACCEPT-logic); b6–b13 = same products.json-off STOP at reach 87–93% (vNone deep tail, cur_null=0, reachable cards perfect → ACCEPT + hand-open, NOT re-enrich). ~1050 hand-opened across b6–b13, loss≈0.
- **RESULT: b1 (top-visit tier) = 2 WINNERS** (SiiPet LitterLens 74 · Catboxy Nova 72). **b2–b13 = 0 winners 65+ / ~3000 stores** (honest reliable zeros, every gate PASS). **+4 b1 Marina hand-picks → Notion** (Teazys 64 · Wagstro 57 · PawSwing 62 +HeyKitten SL2 · KittyLawn 52). 6 Notion cards total **PENDING Founder Review**.
- **⭐ STRUCTURAL FINDING — VISITS-GRADIENT in Cats CONFIRMED (13 batches).** Winners concentrate in the TOP-visit tier (b1, visits ≥1020). The entire tail (visits 1014→11→vNone, b2–b13) = foreign micro-stores / cat merch-tees-mugs / commodity tofu-tapioca-litter / breeders-catteries / dev-test .myshopify / saturated me-too → 0 winners. **DIFFERS from Nursery** (winners hid deep at visits 363/387). ⚠ Still NO field-filter by visits (RULE 24) — gradient justifies a CHEAPER reader for the tail, not skipping it.
- **📡 DEEP-TAIL CONVERGENCES (market-intel — most-cloned Cats products right now):** ① **Nail File Box** (cat self-files claws while scratching) — 8+ brands + refill-paper appearing = clearest EMERGING trend, real nail-trim pain (grammycat/jenori/purrfectpedibox/kittypedi/chimeow/blissfulpaws/starseawe + brightchoice refills). ② **"dehydrated-by-design" stainless fountains** — 10+/batch, HOPELESSLY oversaturated (do-not-enter). ③ **3-in-1 steam grooming brush** — 10+ dropship clones. ④ **self-cleaning litter** (Neakasa/Litter-Robot clones $200–600). ⑤ **pheromone diffusers** + **taurine supplements** (6+) + **PrettyLitter-style colour-change health-monitoring litter** (the genuine "health vein"). ⑥ **desk-clamp cat bed** (desknest convergence — already Notion Consider-76) + **hidden litter-box furniture**.
- **THROUGHPUT (observe-only):** reading 250 full cards/batch = ~85% context; reading ~3000 tail-stores for 0 winners = the concrete waste. **▶ Tier-2 PROPOSAL still open (promotion-queue): sub-agent card-reader** — reads all 250, returns only {deep-score candidates + browse + off-model class summary} → 3–4× stores/context, read-all preserved. Visits-gradient makes it MORE valuable (cheap reader for the structurally-empty tail).
- **▶ NEXT (Marina STOP at b13): PIVOT to a fresh niche's TOP-visit tier** (Dogs / Cleaning / other consumer) — winner-density lives there (per the gradient). Cats b14–b19 (~1635 stores, vNone tail) = expected ~0, deprioritized. To resume Cats: artifacts `cats_b{6..13}_opens/scores.jsonl` on VPS; b13 just needs `sl_mark_processed cats s1_b13` (NO re-read — already analyzed, gate PASS).
- *(S8-ANALYSIS block below = Nursery COMPLETE. S8-BUILD + S7 collapsed to git per RULE 18.)*

**▶ S8-ANALYSIS (2026-06-05) — 🏁 NURSERY-PLAYROOM COMPLETE (read FIRST). Full vNone reservoir b1–b11 ANALYZED → 0 winners 65+ / ~2621 stores (honest reliable zero, vNone tail structurally exhausted — confirms S7). System GREEN 11/11.**
- **processed = 8219** = HI 1504 + **Nursery 6715/6715 ✅ (subcategory DONE)**. Nothing left in Nursery. **NEXT = Cats reservoir analysis** (`cats_s1_b1–b19_enriched.json` in `logs/storeleads/niches/pets-and-animals/cats/`, 4635 stores / 19 chunks, ALREADY BUILT S8 — marker `CATS_RESERVOIR_DONE`). master_domains.json = 12854.
- **Pipeline ran clean every batch (b1–b11):** sl_qa → sl_stage2_table (canonical) → read ALL → sl_open_flags (needs_live+device) → live-confirm/VPS-curl → sl_analysis_gate → checkpoint → mark_processed. **Both gates PASS ×11; ACCEPT-logic correctly handled 8 QA-STOP** (products.json-off vNone artifact, reach 89–95%; cur_null=0 throughout → PROCEED+hand-open, NOT re-enrich; b2 redo→0/20 proved re-enrich futile). ~620 hand-opened, loss≈0 on all spot-audits. **0 degradation across 11 batches.**
- **⭐ HYPOTHESIS RESULT (Marina S8):** "no-visit-rating (vNone) stores still yield winners" = **NOT confirmed on Nursery** — the whole vNone tail = apparel/keepsake/personalized/feeding-commodity/dropship/services/dev-test-demo + deep-tail .myshopify.com clones. This is ONE slice; **final verdict deferred until Cats + next subcategories** analyzed. Deep tail also surfaced convergence-only signals (3 retractable gates → S7 BabyBond; 3 stroller-rockers → S4 Rockit) — reconfirm known winner-MECHANISMS, give no new winners.
- **Notion writes (2026-06-05):** Yogorgeous Anti-Roll Changing Mat 53 (yogorgeous.com.au — **founder-kept 🔵 Watchlist**) · **Rockit card = 3 convergence brands** (Store Link 2 = babymarstore RockaBaby b2; body + RockingRide rockingride.com b7 — all same clip-on stroller-rocker mechanism). All honest-zero batches logged in reported-products b1–b11 + Nursery-COMPLETE summary row. keep-list +2 (yogorgeous, babymarstore).
- **⭐ PERFORMANCE OBSERVATION (Marina S8 — observe only, no change):** ~1250 stores/context before compact; this session did b6–b11 (6 chunks ≈ 1121 stores) in one window. **~85% of per-batch context = reading ~250 full cards (RULE 6); persists in history.** NOT scraper (0-token), NOT live-verify, NOT checkpoint. Reservoir = WALL-CLOCK win only, does NOT cut read-context. Weak tail = same read-tokens as strong niche but 0 winners → **Cats (fresh niche) = better token-ROI**. **Hypothesis to test later (Tier-2, propose first): sub-agent reads cards & returns only candidates+off-model summary → 3–4× stores/context without losing read-all guarantee.**
- *(S8-BUILD block below = how the reservoirs were made. S7 = scale-validation. Older = git.)*

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
