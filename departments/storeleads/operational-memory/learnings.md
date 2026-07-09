# Store Leads — Session Learnings

Short-lived tactical discoveries. Read at session start. Permanent rules → op-rules (once it
exists); company logic stays in core/. Append with expiry; archive expired (never delete) per RULE-15.

---

## HANDOFF → NEXT SESSION (read first)

**▶ S18 (2026-07-09) — 🛠️ SYSTEM-REBUILD Блок 3, ЧАСТЬ 1: Этапы 1–2 прощупаны руками и приведены в соответствие с действительностью. ▶ NEXT = Этап 3 (анализ), ниша Toys & Hobbies, батч 1.**
- **Этапы 1–2 проверены В ДЕЛЕ, не по докам.** Stage 0: пере-срез T&H 1k–10k из CSV → **7,639, домен в домен** = живому срезу (0 расхождений). Stage 1: `sl_select_build` отобрал 250 (визиты 6,993→6,391), никаких полевых фильтров. Stage 2: `sl_enrich4` 8 воркеров → **ACCEPT** (reach 92.0%, 250=250, cur_null 0, guard 0/0, 8.7 мин). `enriched_index` 27,749 → **27,999**. Чанк `th_1k10k_s1_b4`. **Оба этапа работают; сломаны были только СЛОВА о них.**
- **Найдено 6 расхождений «слово ≠ дело». Три исправлены (Этапы 1–2), три ждут Этапа 3.**
  - ✅ **RULE 25 переписан: канонических ридера ДВА.** HTML (`sl_stage2_table.py`) — для founder'а; текст (`sl_project_any.py`) — для агента (250 карточек HTML в контекст не влезают, потому все сессии де-факто читали через проектор). **Проектор жил ТОЛЬКО на VPS, вне git, и сам был partial**: терял `home_hero` (баннерный герой — тот самый, ради которого v4.2 и делали, т.к. автоподбор бестселлера промахивается), резал `desc` до 58 симв., не показывал `desc_confidence`/`pust`/`kind`/причину unreachable. **Агент 27 батчей судил по меньшему, чем видела Марина.** Переписан на полную карточку + self-cert, положен в git.
  - ✅ **Один вердикт — один хозяин (RULE 26).** Баннер HTML-ридера дублировал пороги `sl_qa` → на ОДНОМ файле `sl_accept_chunk` говорил ACCEPT, а баннер STOP (живой случай: `th_s1_b4`). Пороги убраны из ридеров: ридеры сертифицируют **ЧТЕНИЕ** (`FULL CARD RENDERED — PASS: N/N products`), данные — `sl_qa`/`sl_accept_chunk`. В §1a вход в анализ теперь тоже через `sl_accept_chunk` (раньше агент сам толковал сырой ⛔ `sl_qa` — последний шаг на дисциплине).
  - ✅ **Волна 7 → 1+9=10 чанков** (Marina S18). Безопасность держится на машинной приёмке КАЖДОГО чанка, не на длине волны. **Каденция HTML сведена в ОДНО правило для обоих режимов: первый · каждый 5-й · последний** (было: «последний чанк волны» в сборке vs «batch-1 + каждый 4-й» в анализе — два ответа на один вопрос в двух файлах).
  - ⏳ **Ждут Блока 3:** (1) «открыть» = curl (RULE 29 vs RULE 23); (2) автономность спорит сама с собой (workflow стр.9 vs RULE 33); (3) op-rules 33 → ~10.
- **Попутно вычищено:** `conv_subcat` → реальное имя `conv_batch`; `hero_confidence` — поле МАГАЗИНА, не товара; Stage-1 селектор везде = `sl_select_build` (README/interface-guide звали `sl_select_all`); словарь **«чанк сборки ≠ батч анализа»** → workflow §0.4.
- **📖 СЛОВАРЬ (запомнить):** T&H имеет **4 готовых чанка** и **0 проанализированных батчей**. Анализ начинается с **батча 1 = чанк b1** (верх по визитам). `enriched ≠ processed`.
- **▶ NEXT — Этап 3 на Toys & Hobbies, с батча 1.** Ниша выбрана СПЕЦИАЛЬНО: H&G непригоден как честный тест — агент уже знает ответы (Wriggler/OtterSpace в b5, CouchConsole в b1), настройка превратилась бы в подгонку. **H&G b1–b5 = контрольный полигон ПОСЛЕ настройки** (известный ответ там = фича: чистая система обязана снова найти The Wriggler).
- **Незакрытое (перенесено из S17):** находки b5 H&G — The Wriggler 68 · OtterSpace 66 (+ borderline LuvLink 63 · ChickCozy 63) — **НЕ в Notion**, ждут OK Марины. H&G b1–b5 НЕ помечены processed. `storeleads-дубликат/` — замороженный снимок, не грузить.

**▶ S17 (2026-07-09) — 🛠️ SYSTEM-REBUILD: Блоки 1–2 СДЕЛАНЫ (выгрузка + скрапер/энричер). ▶ NEXT = Блок 3 = СИСТЕМА АНАЛИЗА (op-rules 33→~10, human-in-loop, вернуть живой заход). Батчи всё ещё на паузе до конца Блока 3.**
- **Общий словарь (workflow §0.4, Marina-locked).** **Этап 1** = выгрузка магазинов = **Stage 0** (срез ниши из CSV-вселенной). **Этап 2** = подготовка файла к анализу = **Stage 1** (select 250) + **Stage 2** (enrich → `_enriched.json`). **Этап 3** = анализ и поиск винера = **Stage 3**. Два пути в анализ: **A** — взять готовый резервуар (decoupled, предпочтителен) · **B** — build+analyze в одной сессии (как ShopHunter). Оба валидны, оба храним.
- **Блок 1 DONE (commit `f1f88ca`).** `operational-memory/data-inventory.md` (где всё лежит + VPS-коннект) · `operational-memory/strategy.md` (**Ось А** — приоритет ниш 🟢🟡🔵🔴, все 36; **Ось Б** — полосы визитов 1k-10k → 10k+ → 22-1000 → 0; принцип «без штампов на нишах») · два метода выгрузки разведены (CSV = текущий Stage-0; старый API-дамп RETIRED-но-сохранён) · `prescale-hardening-plan` → `archive/` · `niche-track-record` переписан как **наблюдения, НЕ вердикты** · выгрузка сверена с живым StoreLeads (юниверс −0.8%, HI −1.3% = недельный дрейф базы, не потеря).
- **Блок 2 DONE (commit `03c2eff`).** `sl_accept_chunk.py`: credit-guard был **фейковым** (грепал `sl_enrich4`, называя это "claude_procs", и самоматчился → ложный ⚠ на каждом чанке) — **починен + проверен** (0/0). workflow §1b: добавлен **Step-0 «slice from CSV»**, `sl_master_dedup` → LEGACY (поглощён `enriched_index`), **SSH keepalive** для wait-loop. Новый **workflow §0.4** (3 этапа / Stage 0–3 / 2 пути). Stage-1 селектор сведён к `sl_select_build`. **op-rules RULE 0 «СНАЧАЛА ПРОВЕРЬ — НЕ ВЫДУМЫВАЙ»** — наверху. **RULE 30**: формат отчёта = человекочитаемый текст (машинный one-liner ретайрен), определён в ОДНОМ месте.
- **Прогон в деле (RESERVOIR-BUILD).** Toys & Hobbies, полоса 1k–10k (срез 7,639) → чанки **s1_b1..b3 = 750 магазинов**, все ACCEPT (reach 95.2 / 98.4 / 97.6%), `enriched_index` 26,999 → **27,749**, `processed` НЕ тронут (19,604). Волновой ритм работает; keepalive вылечил обрыв SSH.
- **▶ NEXT — Блок 3 (то, ради чего всё):** (1) переписать `op-rules` **33 → ~10 разных правил**, каждое один раз; наверху RULE 0 + CREED; остальное в архив. (2) **Снять противоречие автономности** (workflow стр.9 «NOT autonomous» ↔ RULE 33 «earned autonomy») → **human-in-loop**. (3) **Вернуть смысл слову «открыть»**: RULE 23 главнее RULE 29; curl (`sl_open_flags`) = только триаж «жив ли сайт», вердикт — ТОЛЬКО после живого захода. *(Доказано: b4 без живых заходов = 0 винеров; b5 с живыми заходами = 2 винера, включая потерянный The Wriggler.)* (4) **Не добавлять новых гейтов** — гейт считает покрытие, не суждение. (5) Проверка: пере-прогон **b1–b4 H&G** на чистой базе + T&H (750) как второй полигон.
- **Незакрытое (operational).** Находки b5 — **The Wriggler 68 · OtterSpace 66** (+ borderline LuvLink 63 · ChickCozy 63) — **ещё НЕ в Notion**, ждут OK Marina. **b1–b5 H&G НЕ помечены processed** (будет пере-прогон). Резервуары: H&G `hg_b1..b22` (5,500) + T&H `th_1k10k_s1_b1..b3` (750).
- **Страховка.** `storeleads-дубликат/` в корне репо = замороженный снимок папки ДО ребилда. Не департамент, не грузить, не редактировать; удалим после ревизии «не потеряли ли опыт».

**▶ S16 (2026-06-27) — collapsed per RULE 18 (keep only 2 newest full = S18 + S17). Full text in git + `review/s16-rebuild-plan.md` + `review/s16-session-progress.md` + `review/s16-folder-audit-notes.md`.** 🔬 ANALYSIS (H&G redo) → PIVOTED to SYSTEM-REBUILD diagnosis; batches PAUSED. **The find that defines the whole rebuild:** Marina caught that the genuine live-open had atrophied into a curl (`sl_open_flags`, RULE 29) — **b4 without live-opens = 0 winners; b5 WITH live-opens = 2 winners** (The Wriggler 68 = the S15 miss, redeemed · OtterSpace 66) + 2 borderline (LuvLink 63 · ChickCozy 63), **none yet in Notion**. Opening all 18 unreachable live surfaced claymore V600+ fan $64.95 behind an off-model title. Also b1–b3 → CouchConsole 73 → Notion. **Decision: NOT a from-scratch rebuild — surgical declutter, keep all experience.** `sl_mark_processed` NOT run for b1–b5 (deliberate: they will be re-analysed on the clean base).

**▶ S15 (2026-06-08) — collapsed per RULE 18 (keep only 2 newest full = S17 + S16). Full text in git + `review/s15-postmortem-and-hardening.md`.** ⛔ ANALYSIS b1–b8 UNTRUSTED (never used, never written to Notion; `sl_mark_processed` NOT run; reservoirs intact). **ROOT CAUSE (measured):** mandatory-load 2252 lines; op-rules attention skew ≈41:4 gate-machinery vs product-first SOUL → **Goodhart** — the gates measure COVERAGE, not JUDGMENT (green even when a real candidate is dismissed by label, or zero links are opened). In the autonomous block b3–b8 the agent opened **ZERO links by hand** → lost The Wriggler / Rockit / SnoofyBee. **This postmortem IS the agenda for Блок 3 (the analysis-system rebuild).**

**▶ S14 (2026-06-08) — collapsed per RULE 18 (full text in git).** 🐶 **Dogs CLOSED** (b1–b21, 5,250 stores → 1 winner total: Gerty 65). 🔧 **Home-Improvement** top-visit tier b1–b6 (1,500 stores) = 0 fresh winners → structurally «heavy» (catalog-giant / material / part / fixture). processed = 19,604. 🎉 **Store Leads PRO paid** → quota wall gone + WooCommerce (4.26M) unlocked → the whole active universe was then exported to CSV (current data source → `operational-memory/data-inventory.md`). Tool kept: `sl_project_any.py`.

**▶ S13b (2026-06-07) — collapsed per RULE 18 (full text in git).** 🐶 Dogs b1–b20 (5,000 stores) = 1 winner total (Gerty 65); b6–b20 = 0. Notion: Gerty + Team K9 only. Dogs = saturated white-label niche (designer collars / food / services / dropship-electronics = market NOISE, not signals). RULES 31/32/33 exercised across 20 batches (incl. the RULE-33 autonomous block — the same machinery that failed in S15). Tool kept: `sl_project_tmp.py`.

**▶ S12-ANALYSIS (2026-06-07) — collapsed per RULE 18 (now 3rd-oldest; keep only 2 full = S14 + S13b). Full text in git.** 🏁 CATS FULLY COMPLETE (b1–b19, 4635 stores) → **2 winners total** (SiiPet LitterLens 74 · Catboxy Nova 72), both in b1 top-visit tier, already in Notion since S9; b2–b19 = 0. Validated the prep→analysis decoupled model (6 batches/1385 stores, no compact, gates PASS ×6). **Still-LIVE:** sub-agent-reader DELEGATION = rejected-for-now (quality>speed, `feedback_no_delegation`); visits-gradient is an OBSERVATION not a law (RULE 24 — never field-filter by visits; Cats winners sat UP-top, Nursery DEEP — opposite → see [2026-06-07] S12 learning below).

**▶ S11 (2026-06-07) — collapsed per RULE 18 (full text in git).** 🏭 RESERVOIR-BUILD (parallel to analysis — decouple PROVEN). Built Dogs 50 chunks (12,500) + HI 29→33 chunks (now ~8,250) = enriched_index. **Still-LIVE (all codified elsewhere):** decoupled build arch `sl_select_build.py`+`sl_mark_enriched.py` (`enriched ≠ processed`, op-rules RULE 30 + workflow §1b) · `sl_accept_chunk.py` per-chunk acceptance · WAVE RHYTHM · permission fix (global ssh/scp auto-allowed; never prefix Bash with `cd "<project>" &&`). Dedup state: `master_domains.json` 60,306.

**▶ S10 (2026-06-06) — collapsed per RULE 18 (3rd-oldest full block; keep only 2 = S13 + S12). Full text in git + memory `project_storeleads_quota`.** RESERVOIR-PREP + ⚠️ QUOTA WALL + 🧹 SERVER HYGIENE. **Still-LIVE bits:** (1) **QUOTA WALL** — StoreLeads Premium ($75)=2,000 searches/mo, exhausted by dumps → `/json/auth/domains` HTTP 402; **Pro ($250)=unlimited + CSV-export** = the structural fix; Marina emailed support, **status: awaiting reply** (re-check before any new dump). (2) **K&D dump LOST** (overwrite-no-backup) → re-dump from scratch when quota returns; filters = Shopify+Active+Created≥2020. (3) Server hygiene + `shared/server-conventions.md` LIVE (trash=mv-not-rm, purge needs Marina-OK). (4) Lesson: new/fixed script writes to a TEST slug first, never over a live file; abnormal situation → STOP+ask.

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

### [2026-06-27] S16 — ⭐ FINDING (in-process): the GENUINE live-open atrophied — displaced by tooling, not by decision
**Type:** Process / Root-cause | **Severity:** HIGH | **Confidence:** HIGH (Marina caught it on b4 + traced through docs)
**What Marina caught:** on b4 I "opened 54/54 flags" but those were **light server-side curls (`sl_open_flags` = title+price)
+ card-judgment** — NOT genuine live-opens. I did NOT WebFetch the stores I flagged as interesting in B/C/tail (nebuluxury,
playdropmats, topseat, v3clean) — I dropped them to browse from the card alone. In S3/S4 I opened ~90 stores LIVE per session.
**Trace — where it eroded (it was never decided away):** ShopHunter built this STRUCTURALLY — Stage-2 "open ALL, no name-pick"
+ **SH-8 safeguard #3 (description-confidence gate): a thin/mismatched desc → WebFetch the LIVE page BEFORE scoring** (born from
the SAME failure: SlotPro mis-scored ~52 on a thin read → ~66 after live open; Marina caught it by question). Store Leads HAD it
(RULE 7 live-confirm, RULE 23 hand-open, S4 ~90 WebFetch opens). Then **S7 added `sl_open_flags` (RULE 29)** = a light server curl
that pre-seeds the opens-log; the gate measures COVERAGE ("every flag has a verdict string"), which a curl + card satisfies
CHEAPLY → the expensive-but-valuable genuine chat-WebFetch quietly faded. **S13b projection** (full card in-context) reinforced
"judge from the card." **Same Goodhart mechanism as S15:** the system stopped REQUIRING the real thing, so under load it dropped out.
**Fix (restore from ShopHunter — applied from b5):** the live description-confidence gate is ACTIVE again — **thin/mismatched desc
OR any genuine-product store I mark interesting across A/B/C/tail → WebFetch the LIVE page BEFORE scoring, shown in chat** (generous,
when-unsure-OPEN); `sl_open_flags` curl = triage seed, never a substitute. Encoded as the per-batch CONSTANT honest-question
(workflow §1a). **In-process finding — not final; revisit in the deep audit** (does the gate need to machine-require a min live-open
count? — candidate Tier-2 proposal, gather more batches first).
**Applies to:** every Store Leads analysis batch. **Expires:** Never → feeds the deep folder/system audit. Pairs with [[feedback_no_delegation]] (quality>speed) + the S15 Goodhart postmortem.

### [2026-06-08] S14 — HOME-IMPROVEMENT top-visit tier (b1–b6, 1500 stores) = heavy-confirmed, 0 fresh winners (reaffirms RULE 11 + the S2 HI lesson)
**Type:** Yield fact / Pattern | **Severity:** MED-HIGH | **Confidence:** VERY HIGH (6 batches / 1500 stores, every gate PASS, loss≈0, visits 2.9M→948)
**Observation:** Fresh HI reservoir, visits-desc TOP tier → **0 fresh winners**; the only 65+-by-score (Stoov Ploov³ cordless heated cushion 70, b1) is the EXACT "Stoov-type" Marina already Watchlisted 73 in S2 (convergence, founder-known — NOT a new card). Every batch dominated by **catalog-giant + material/part/diy-home/fixture** (store_type trade/catalog ≈ 35–50%): doors/locks/faucets/sinks/vanities/tile/flooring/paint-dealers(many Benjamin Moore)/HVAC/fireplaces/saunas/cold-plunge/tools/lumber/rugs/bidets. Recurring market-NOISE (not signals): paint-by-numbers-from-photo ×4 · cold-plunge/sauna ×8+ (bulky/high-ticket RULE 10) · soundproofing/acoustic ×4 · EVA car-mats ×2 + auto air-purifiers/detailing (FB-adjacent but off-HI/off-model) · smart-locks ×8+ · bidets ×6+ · robot-mowers. **Lesson: HI is the canonical "heavy" category (like the S2 HI batches) — confirmed now at the TOP-visit tier too, so it's not a deep-tail artifact. Niche-fit is a first-order filter (same as Dogs S13/S14). Don't grind the HI reservoir (b7–b33 ~6750 enriched left); with the Pro plan unlocked, spend dumps on CONSUMER-impulse niches instead.**
**Applies to:** niche selection across Store Leads. **Expires:** Never → reinforces RULE 11 + the [2026-06-07] S13 Dogs entry + the S2 HI yield lesson.

### [2026-06-07] S13 — DOGS is structurally weak for white-label (1 winner / 5000 stores) — niche-fit is a real variable
**Type:** Yield fact / Pattern | **Severity:** MED-HIGH | **Confidence:** VERY HIGH (20 batches / 5000 stores, every gate PASS, loss≈0)
**Observation:** Full Dogs dive b1–b20 (5000 stores, visits-desc) = **1 winner total (Gerty 65)**; b6–b20 (3750 stores) = **0 winners 65+** (S13b confirmed: b14–b20 deep tail = 0 winners / 1750, only borderline warmwalks 60). The niche is dominated by categories that are off-model for the Instagram/impulse white-label hunt: designer collars/leashes (the single biggest bucket — BioThane/leather/paracord/tweed), beds/crates/car-seats (bulky, $100–800), food/raw/treats, supplements, e-collar/bark/GPS electronics (branded), grooming-services, training-courses, puppy-breeders, poop-bags, merch/portraits. Almost nothing is wow + impulse + camera-verifiable + cheap-white-label. **Lesson: niche-fit is a first-order variable — Dogs (like Home-Improvement, S2) is a "heavy" category where honest low-yield is expected (RULE 11), NOT a system failure. Marina confirmed other niches gave "совсем другой результат."** Practical: when a niche shows ~0 winners across the first 4–6 well-read batches AND the category mix is dominated by accessories/food/services, that's a strong pivot signal — flag it early rather than grinding the whole tail. (Coverage still total per batch — RULE 24 — but niche SELECTION should weight consumer-impulse subcats: this reaffirms the S2 HI lesson.)
**Applies to:** niche selection across Store Leads. **Expires:** Never → reinforces RULE 11; candidate for a niche-pre-screen heuristic (propose via promotion-queue if it recurs).

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
