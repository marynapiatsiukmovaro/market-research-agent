# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**▶ S4 (2026-06-01) — read FIRST. Nursery visits-desc deep-dive, RULE-24 `sl_select_all`, reliability focus.**
- **Enricher unchanged = `sl_enrich4.py` v4.2 LIVE.** Loop per batch: `sl_select_all.py <full> <out> 250` → `sl_enrich4` (8 workers, nohup, sentinel) → read ALL 250 compact + open EVERY needs_live/unreachable live → checkpoint → **STOP for Marina** → `sl_mark_processed.py`. Cadence this session = **checkpoint→STOP every batch** (Marina S4). Permissions: **VPS SSH + WebFetch/WebSearch session-approved** (Marina S4); Notion/git/core-edits still gated.
- **Batches 3–8 done = 1500 stores (visits-desc).** b3 = visits 1,885–12.7M (established-band — 0 winners) · b4 = 692–1,879 · b5 = 447–692 · b6 = 268–447 · **b7 = 167–268 · b8 = 113–167 (decouple-test on pre-enriched data).** **processed_domains total = 3598** (HI 1504 + Nursery b1-2 594 + b3-8 1500 = Nursery 2094/6715; remaining ~4621).
- **6 WINNERS total → IN NOTION (Founder Review PENDING Marina):** b6: **WonderBee Doppler 77** (petiteisland.com; doppler convergence) · **Crib Safety Tent 73** (kindersensebaby.com). b7: **LatchLight 76** (shoplatchlight.com — wearable nursing nightlight + latch tip, novel) · **Roar Wireless Monitor 69** (roaroutside.com — fully-wireless outdoor wedge, ⚠electronics). b8: **Rockit Stroller Rocker 74** (rockitrocker.com.au — clip-on auto-rocker, 700k+ sold) · **Baby Crib Tent / Aussie Cot Net 70** (babycribtents.com — **folded as CONVERGENCE Store Link 2 into the KinderSense card**, premium $159 vs budget $55). **+ Sleepytot 64 founder-KEPT (Marina asked to add despite <65; sleepytot.com.au — velcro-paw dummy-holder comforter).** All in reported-products + Notion.
- **🔑 KEY RELIABILITY FINDING:** both winners sat at visits 363/387 — **DEEP tail, below the old 1k–50k band → old approach would have LOST both.** RULE 24 (no field-filter, visits=order only) + RULE 23 (open every flag) caught them. 0-loss measured 4× (spot-audit of dropped piles). **Funnel (Stage 1→3) is STRONG, loss≈0 within the dump.** Residual loss-risk is UPSTREAM = Stage-0 `category=None` + Store Leads taxonomy mis-tagging (proposal filed).
- **▶ DECOUPLE TEST = DONE & VALIDATED (Marina S4 post-compact).** Both pre-enriched batches (b7+b8) analyzed with **ZERO scraper wait** — instant start on `*_enriched.json`. Invariant `enriched ≠ processed` held (0/250 in processed until mark). Quality identical to b3–6. **Marina's verdict: she prefers this format** — «не ждём, сразу работаем», результаты идут интенсивнее; ноль потерь winner'а сохраняется. Token-cost neutral, big WALL-CLOCK win. → reservoir architecture (proposal #1) is validated in practice; build in a dedicated SYSTEM-BUILD session.
- **▶ NEXT SESSION = RESERVOIR READY. 8 BATCHES PRE-ENRICHED & WAITING (np_batch9–16_enriched.json, 2000 stores, visits 5–113 + 40 missing) on VPS at `logs/storeleads/niches/home-and-garden/nursery-playroom/`. DO NOT re-select/re-enrich.**
  - **Start sequence (decouple — go STRAIGHT to analysis, NO scraper at session start):** (1) load context (CLAUDE.md now lists SL + Layer A + SL op-memory + this HANDOFF); (2) preflight = `ps aux | grep claude` credit-guard + verify reservoir done (`ls np_batch{9..16}_enriched.json` + tail `logs/storeleads/reservoir_prep.log` for `ALL_RESERVOIR_DONE`); (3) analyze np_batch9_enriched.json → read ALL + open every needs_live (small-batch WebFetch + VPS-curl fallback, RULE 23/24) → checkpoint → STOP → `sl_mark_processed` → batch10… same cycle.
  - **Scraper only REFILLS the reservoir** when low — run it in BACKGROUND (token-free) while analysing, or at end-of-session to prep the next day. NEVER block analysis on it. (Prep job tonight: `/tmp/reservoir_prep.sh`, 8×250 sequential + 60s pauses.)
  - After these 2000: ~2,621 Nursery left (incl. MISSING-visits LAST, kept, RULE 24). Full exhaust ≈ 10–11 more batches.
  - **If reservoir prep FAILED/incomplete** (missing enriched files): fall back to `sl_select_all niches/home-and-garden/nursery-playroom/nursery_playroom <out> 250 0` (auto-excludes processed) → enrich → analyse.
- **Proposals filed (`review/promotion-queue.md`, Marina to decide):** (1) **decouple enrichment↔analysis "reservoir" architecture** (Marina's S4 idea — enrich-loop fills reservoir token-free; analysis consumes ready chunks; ⚠`enriched`≠`processed` two-states; parallel SCRAPERS not claude per RULE 13); (2) trust-card for unambiguous off-model needs_live (reduce hand-open at scale); (3) Stage-0 category-None hole. **Build only in a dedicated SYSTEM-BUILD session.**
- **Open:** Founder Review tiers for the 2 winners → log to founder-feedback when Marina sets them.

**▶ S3 (2026-06-01) — read this first; supersedes the v3/v4.1 references below. (Nursery band DONE.)**
- **Enricher = `sl_enrich4.py` v4.2 / v4.2.1 LIVE** (supersedes v4.1/v3/2): product_class (incl. `diy-home`) + store_type,
  desc SELF-CHECK (RULE 22), new_products_30d, subdomain-collapsed conv, class-aware ABC (SORT-AID — read ALL, RULE 6),
  product-handle. **v4.2 = "ни один магазин не тонет на первом проходе" (RULE 23):** brings `home_pitch` (store's own
  homepage value-prop), `home_hero` (banner-featured product shown ALONGSIDE best-seller), long desc + `bullets`,
  `home_img`, and a **`needs_live`** worklist flag → agent live-opens every flagged + unreachable store. **v4.2.1 fix:**
  `needs_live` = CARD-INSUFFICIENT only (desc-bad / price-unknown / unreachable / card-thin / banner-hero-unreadable);
  `hero_confidence=low` is a SOURCE artifact, NOT real uncertainty (it had inflated needs_live to 62% → recalibrated to ~17%).
  Dropped (Marina): review-count/brand-claim markers (fakeable). Stage-2 table shows pitch+BANNER+bullets+needs_live col.
- **NURSERY & PLAYROOM band EXHAUSTED: 2 batches / 594 stores (visits 1k–50k of 6,715).** Consumer-dense niche (contrast
  HI): consumer ~80%, trade ~5%. **Tail (visits <1000 ≈ 5,874) NOT done — Marina: process LATER (next session).**
  `processed_domains.json` = batch1(250)+batch2(344) marked (total 1754 incl. HI 1504). v4.2 result: judged ~280/341 from
  cards, hand-opened ~22 (genuine + must-open); 2 MANUAL mislabels caught live (busybee/burrbaby b1; bebecan/momsbeyond b2).
- **Notion: 12 cards entered (Founder Review by Marina):** 🟡 Consider 3 (Izimini 57, Dingle Dangle 60, JoSeat 68) · 🔵 Watchlist 8
  (Omni 66, Wildride 70, BuddyBottle 68, Kaiya 72, WaterLand 72, Dreamland 70, Ocodile 67, Jili 66) · 🔴 Rejected 1 (Grip Baby 67).
  **Doppler convergence:** the 2 new doppler stores folded into EXISTING cards as Store Link 2 (themommymotherhood→WellnessBaby,
  springbud→FetalPlus) — no new cards. All logged in founder-feedback + keep-list (7 monitors).
- **⭐ FOUNDER CALIBRATION (S3 — big one, in founder-feedback):** SATURATION + SAMENESS + "ad-cost won't clear" = strong
  NEGATIVE, overrides "solves pain + proven category" → such products are 55-62 Watchlist, NOT 67-72. Novel-framing ≠ wow
  without a REAL functional differentiator (Grip Baby crawling-suit = apparel → Reject; WaterLand clever-but-ordinary →
  Watchlist). Apparel off-model unless tactile/functional diff. Stylish design alone → Watchlist; +seasonal/viral hook →
  Consider. **Apply: score the differentiator/gap, not just the pain.**
- **▶ NEXT:** (1) decide tail <1000 (≈5,874) — process later vs skip (Marina parking it); (2) if continuing Nursery, dump tail
  or pick next consumer niche (Cleaning 5,868 / Pets / Dogs / Cats); (3) commit+push done this session.
- **Open:** validate PRICE-CHECK fix on a live price-0 store; v5 idea — split `consumer-other` further; archive S2-PM HANDOFF
  block (RULE 18 — 3 blocks present, keep 2). Throughput-at-scale optimization deferred (RULE 21).

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
