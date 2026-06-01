# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

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

**▶ S2 FINAL (2026-05-31) — ARCHITECTURE v2 designed + BUILT (sl_enrich3) + 4 HI batches run. Caркас готов; начали тестировать. (DONE)**
- **State in one line:** the funnel SKELETON is built and runs end-to-end on the new product-centric scraper; we have begun
  testing it on real batches. Next sessions = keep running batches, hardening each stage step by step.
- **Scraper v3 BUILT & LIVE: `scripts/sl_enrich3.py`** (on VPS + repo). Replaces sl_enrich2 (kept as fallback). Implements the
  v2 contract: open-ladder (best-selling→frontpage→featured→/products.json→**homepage HTML**, no silent DROP → `MANUAL`/
  `PRICE-CHECK` instead), **TOP-3 candidates/store** each with desc, **currency→USD via `/meta.json`** (NOT country code),
  `hero_confidence`, `desc_confidence`, `maturity` (established≠reject), convergence with **geo-mirror dedupe**, proxy_score
  with **NO revenue term**. 3 real bugs caught+fixed while building (currency-from-meta, price-0 region artifact→PRICE-CHECK,
  variants-as-dict + per-store try/except). Also new: `scripts/sl_table_shot.py` renders a funnel-stage JSON → PNG table
  (Marina wants stage screenshots on her Desktop — Stage1/Stage2 delivered S2).
- **Batches done: HI 1–4 = 800 stores processed** (`processed_domains.json` on VPS, 600 clean keys verified vs dump + b4's 200).
  **HI ×4 = stable LOW white-label yield** — category is structurally "heavy" (trade/materials/parts/services). Funnel WORKS;
  HI just isn't the grebe for our Instagram model. **Nothing written to Notion this session** (Marina decided not to enter b2/b3/b4).
  Batch-4 best by SCORE: GoSpray HVLP paint sprayer **72** (inokraftshop, demo-able wow); smart-lock convergence ×4 only **60**
  (Amazon-saturated) — proof that SCORING beats the convergence signal (lead with the 100-pt score, never conv/tier — RULE 6).
- **▶ NEXT SESSION PLAN (Marina-agreed):**
  1. **Run HI batch 5** (the band's last ~700 → ~200 fresh; processed auto-excludes) to finish hardening on a known category.
  2. **Then SWITCH category** to a more consumer subcategory from the census (Nursery & Playroom 6,729 / Cleaning 5,868 /
     Pets / Dogs / Cats) where white-label-with-wow density is higher. Fresh `sl_dump_full.py` on that subcat.
  3. **Per batch use the FULL founder report shape** (Worth-Testing 65+ / Borderline 55–64 / Watchlist / **Browse-pool 10–15
     unique links** / Patterns) — ALWAYS score each candidate 100-pt; never ship 3 links or a convergence list (S2 mistake).
  4. **Keep-list** of interesting stores → grows toward feeding ShopHunter's parked newest-first monitor.
  5. **MEASURE ShopHunter hit-rate** on a batch's finalists (creds live on VPS) when convenient.
  6. Optional code: align desc/price confidence display in `sl_table_shot`; validate PRICE-CHECK fix on a live price-0 store.
- **Process lesson (RULE 4a added):** a crash flipped me into panic-fix → I invented "81/40% dropped" (real=10) + lost the
  founder-report format near session end. Long session + lots of churn = my discipline degraded. **Keep sessions shorter;
  when something breaks, SLOW DOWN and verify the number from data before acting.** The repo + Marina-approval guards held.

---

**▶ S2 (2026-05-31 PM) — ARCHITECTURE v2 designed + 2 more HI batches run (earlier handoff, superseded by S2 FINAL above).**
- **Ran HI batches 2 + 3** (visits 6.8k–13.8k, then 4k–6.7k; processed-excluded, 400 now marked processed on VPS
  `logs/storeleads/processed_domains.json`). Both = 0 confirmed winners 65+. **HI ×3 batches (600 stores) = stable
  low white-label yield** — structurally "heavy" (trade/materials/parts/services). Funnel WORKS; HI is just not the
  grebe for our Instagram model. Best borderline: smart-locks (~66-70, Amazon-saturated), bidet-attachment ×3
  (premium/везде), tub-tile refinishing kit ($39.99 consumable). **Nothing written to Notion** (Marina: "не вносим, потом обсудим").
- **Verified all 18 "unreachable"** (b2 13 + b3 5) by hand: **17/18 actually load** — products.json disabled ≠ dead site.
  But none were winners (locksmith/HVAC services, trade-lumber, parts, off-model). Confirms RULE 1+7: ALWAYS check
  unreachable (S1 had a real loss), but HI's unreachable tail = services/trade.
- **⭐ ARCHITECTURE v2 AGREED (Marina) — PRODUCT-CENTRIC.** Written into `hypotheses/_active.md` (ARCHITECTURE v2
  block), `methods/subagent-spec.md` (v2 contract), `methods/discovery-funnel.md` (Stage-2 v2 note). **Unit of hunt =
  PRODUCT not store.** Revenue NOT the main signal (early winner has none). Scraper v2 = (1) open-ladder
  best-selling→frontpage→featured→products.json→**homepage HTML**, no silent DROP; (2) **TOP-3 candidates/store** each
  with desc+REAL price(USD)+type+`hero_confidence`+`desc_confidence`(ok/empty/mismatched); (3) early signals NOW =
  **storefront position + investment + convergence WITHIN the subcategory** (~27k of the dump, NOT the universe — Marina
  confirmed scope cheap; dedupe geo-mirrors); (4) currency→USD; (5) **pre-flight 5 checks + FB RULE 4c** (one-line nohup,
  sentinel-detect, no `pgrep -f`, bracket-kill, no `-o` ssh flags). PLUS every batch: **loss-measurement** (hand-check a
  random sample of the dropped pile → report the number) + **keep-list** of interesting stores (START NOW — feeds
  ShopHunter's parked newest-first monitor; **Store Leads = the store-supplier for it**). DEFERRED (Marina): the monitor
  JOB itself (lives in ShopHunter), fresh-product job, FB-pixel-as-criterion, ShopHunter-enrichment (MEASURE hit-rate first).
- **NEXT (the agreed sequence):** (a) I go deep into FB + ShopHunter docs/code MYSELF (1M context — don't over-shard to
  sub-agents where accuracy matters; sub-agents hallucinated line numbers/flags this session — verify against real code,
  RULE 4) to confirm nothing missed for the product-centric model; (b) then align `sl_enrich2.py` to the v2 contract;
  (c) test on **HI batch 4** as the proof run + **measure ShopHunter hit-rate** on finalists + a random sample.
- **VPS reliability lesson (lost ~30 min at S2 start, now in Active Learnings):** SSH exit 255 = dropped channel, NOT a
  dead process — poll, don't relaunch (spawned scraper dupes); launch ONLY a minimal one-line `nohup`; never heredoc over
  live SSH; `pgrep -f` self-matches → use `[s]l_enrich2`; `sl_enrich2.py` needs 3 args INF OUTF SENT. **Process rule: at
  ANY hiccup, check FB/ShopHunter learnings FIRST before reinventing.**

---

> **Older session snapshots — DAY 1 (2026-05-30 pilot) + DAY 2 (2026-05-31 strategy/bq-crack/census/full-dump)
> → moved to `operational-memory/handoffs-archive.md`** (RULE 18; full text also in git). They carry the bq/Bleve
> crack, the 12-subcat census, the export-field decisions, and the K&D pilot — reference there if needed.

---

## Active Learnings

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
