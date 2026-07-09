# Store Leads — Department Workflow (session entry point)

> ⭐ **READ THE ANALYSIS CREED FIRST** — top of `operational-memory/op-rules.md` (7 lines, Marina-authored S16).
> It is the SOUL of the work; everything below (gates, checklists, contract) is only the FLOOR under it.
> Mission = find the WINNER (any category, any visits, even a just-launching/0-visit store) — not tick boxes.
> A green gate ≠ "all good"; quality >> speed; I am the owner; when in doubt, open and check.

Thin entry point. The full procedure lives in `methods/`. Store-first discovery at scale via
storeleads.app. **SYSTEM-BUILD / in development — human-in-loop, NOT autonomous (not earned).**

> ✅ **STAGE-2 ACCEPTANCE PROTOCOL (S6, Marina-approved 2026-06-03) — the S5 fix is now LIVE.** Never analyse a batch
> until the Stage-2 ENTRY CHECKLIST below passes (RULE 25 canonical reader + RULE 26 QA-gate PASS + acceptance statement).
> The S5 failure (analysed an ad-hoc reader showing 1 product of 3) is now structurally blocked: `sl_qa.py` certifies the
> DATA, the canonical `sl_stage2_table.py` self-cert banner certifies the READING. Reservoir data is intact — do NOT re-pull.
> *(Background: `archive/storeleads-prescale-hardening-plan-S5-RESOLVED.md` = the S5 agenda (ARCHIVED S17); its Q1–Q5 were resolved in S6 — grouped-11
> layout locked, single canonical generator, QA-completeness gate, entry checklist, b9 end-to-end re-run + sverka done.)*

> 🆕 **DATA ACQUISITION UPGRADED (S14, 2026-06-08) — CSV export replaces the paginated dump.** On the **Pro plan**
> (unlimited searches + Export-to-CSV) we pull a whole filtered set into ONE CSV — no pagination, no quota/402. The
> **entire active universe is already captured** (Shopify-Active 2,890,820 + WooCommerce 4,255,809 = 7,146,629, 162
> cols) on the VPS `logs/storeleads/exports/` + Marina's Desktop. **Method + rules → `methods/csv-export.md`** (tool
> `scripts/sl_export_run.py`). The old `Stage 0 dump` (`sl_dump*.py`) is **superseded** (quota-limited); the enrichment
> + analysis chain below is **unchanged** — only data ACQUISITION changed. WooCommerce is now a 2nd platform/universe.

## 0. Before you start
- Confirm this is a **Store Leads** session. Operate only inside this department; never apply
  FB scraper or ShopHunter mechanics here, never read another department's operational memory.
- Load the ALWAYS files (core/ + shared/, incl. `shared/founder-taste.md`) + this department's
  operational memory in order: **`operational-memory/op-rules.md` (CREED + permanent rules — read FIRST)** →
  **`operational-memory/data-inventory.md` (где данные лежат + VPS-коннект)** →
  **`operational-memory/strategy.md` (приоритет ниш 🟢🟡🔵🔴 + порядок полос визитов)** →
  `founder-feedback.md` → `operational-memory/learnings.md` (read the **HANDOFF** block first).
- Current direction: `operational-memory/strategy.md` (куда/в каком порядке) + `hypotheses/_active.md` (метод).
- Verify session: `scripts/sl_check_login.py` (re-login via `sl_email_login.py` + emailed code if expired).
- Credit guard (Marina's rule): `ps aux | grep claude` on the VPS before any run; parallelism =
  Playwright **workers**, never parallel claude processes.

## 0.4 THE WORK IN ONE PICTURE — 3 этапа · Stage 0–3 · 2 пути (S17, Marina-locked) ⭐
**Три этапа работы:**
1. **Выгрузка магазинов** = **Stage 0** — срез ниши из захваченной CSV-вселенной (`sl_slice_from_csv`, ниша+полоса по `operational-memory/strategy.md`).
2. **Подготовка файла к анализу** = **Stage 1** (select 250 unprocessed) + **Stage 2** (enrich → `*_enriched.json` = «Stage-2 enriched»). ← это и есть «скрапер готовит документ».
3. **Анализ и поиск винера** = **Stage 3** — read ALL → живой заход → 100-pt + Marina Veto → winners / borderline / browse → checkpoint → Notion.

**Два пути получить Stage-2 файл для анализа — оба валидны, оба храним:**
- **Путь A — decoupled (предпочтительный сейчас):** отдельная **🏭 RESERVOIR-BUILD** сессия готовит чанки впрок (§1b, волновой ритм) → позже **🔬 ANALYSIS** сессия берёт готовый `_enriched.json` и сразу анализирует. Ожидание скрапера ≈0 контекста → за сессию разбираем много батчей.
- **Путь B — coupled (как начинали; так же работает ShopHunter):** в ОДНОЙ сессии: взял 250 → запустил скрапер → дождался → проанализировал.

> ⚠️ **Никогда не анализируй Stage-1 файл вместо Stage-2** — это была ошибка S5 (взял недоготовленный файл). Вход в анализ защищён **STAGE-2 ACCEPTANCE** (§1a): заявить *«Loaded Stage-2 enriched, not Stage-1»* + QA PASS.

### 📖 СЛОВАРЬ — «чанк» ≠ «батч» (S18, Marina-locked)
Оба означают 250 магазинов, но это **разные счётчики, и они не совпадают**:
- **Чанк сборки** (`s<S>_b<N>`) — 250 магазинов, которые СКРАПЕР подготовил. Считается по `enriched_index`. Волна = 10 чанков.
- **Батч анализа** — 250 магазинов, которые АГЕНТ разбирает. Считается по `processed_domains.json`.

Ниша может иметь 4 готовых чанка и **ноль** проанализированных батчей (ровно так у Toys & Hobbies на S18).
**Анализ всегда начинается с батча 1** — то есть с чанка `b1`, самого верха по визитам, — независимо от того,
сколько чанков успела построить сборка. «Мы уже сделали b4» относится к скраперу, а не к анализу.
*(Инвариант RULE 30: `enriched ≠ processed`. Сборка помечает enriched; только анализ помечает processed.)*

## 0.5 SESSION MODE — pick ONE before doing anything (S8) ⭐
After loading context, read the prompt + the **HANDOFF "▶ NEXT" line**, then route to exactly one mode:
- **🔬 ANALYSIS** — score a ready/enriched reservoir → winners → checkpoint → Notion. **Go to §1a** (Stage-2 entry checklist
  + SESSION CHECKLIST). Triggers: "analyse / score the reservoir", HANDOFF says NEXT=analysis, an enriched file already exists.
- **🏭 RESERVOIR-BUILD** — run the scraper to PREP enriched data for a LATER session (no scoring, no Notion). **Go to §1b**
  (RESERVOIR-BUILD mode). Triggers: "build / prep / run the scraper on N stores", a NEW niche to dump, HANDOFF says NEXT=build.
- **Unsure?** The HANDOFF's "▶ NEXT" is the default. A NEW niche named for scraping → RESERVOIR-BUILD. "Score/analyse" → ANALYSIS.

**Never mix the two:** RESERVOIR-BUILD never scores or writes Notion; ANALYSIS never runs the enricher loop to grow a reservoir.
A new-niche build also runs the cross-niche dedup first (§1b). Both modes share §0 preflight (credit-guard, session, paths).

## 1. Run the discovery funnel
Follow `methods/discovery-funnel.md` (Stage 0 = slice the captured CSV universe, `methods/csv-export.md` → Stage 1 select → Stage 2 live
enrich → Stage 3 deep-score). Heavy lifting on the
VPS; only finalists enter chat. **Stage 3 is the real filter — read ALL, confirm heroes on the live
site, run 100-pt + Marina Veto, lead with WOW/taste, never trust the proxy A/B/C tier.**
Supporting method docs:
- `methods/interface-guide.md` — the JSON API (login + live filter-counts) + cracked `bq` (filters/fields). *(dump-as-acquisition RETIRED → `csv-export.md`.)*
- `methods/subagent-spec.md` — the Stage-2 enricher's exact job (fields, `desc` rule, what NOT to write, success test).
- `methods/shophunter-enrichment.md` — OPTIONAL cross-dept enrichment of finalists via ShopHunter (lookup ladder, SH fields).
- `reference/cross-dept-patterns.md` — patterns observed in SH/FB, not adopted yet (reference only).

## 1a. Stage-2 ENTRY CHECKLIST (RULE 25 + 26 — run BEFORE analysing every batch) ⭐ S6
Never start analysis until ALL pass, in order:
1. **Preflight** — `ps aux | grep claude` on the VPS (credit guard, RULE 13) · proxy health-check (RULE 14) · verify the
   enriched file exists for this batch.
2. **DATA verdict — ask the owner, don't interpret raw thresholds (S18).** Run
   `python3 scripts/sl_accept_chunk.py <enriched.json>` → **ACCEPT** = analyse · **STOP** = genuine breakage, do NOT analyse.
   It wraps the canonical `sl_qa.py` (the single source of the thresholds) and encodes the branch that used to sit in the
   agent's head: a **vNone/`products.json` artifact STOP** (reach ≥ ~90% · cur_null=0 · count reconciled · cand/product_class
   just under 95 because of `products.json`-off unreachable stores) is **ACCEPT-with-note** — those are alive micro-stores,
   hand-opened at analysis (RULE 23); re-enriching does NOT recover them (proven S8 ch2 redo → 0/20). Genuine breakage =
   reach OUT of band · cur_null>0 · enriched≠selected · a real card-completeness gap → re-enrich.
   *(Raw `sl_qa.py` alone still runs and still prints its own ⛔ on those provisional fields — that is expected and is NOT a
   verdict. Reading it directly is what left the last step of the funnel resting on discipline. Same reason RULE 26 says: one
   verdict, one owner.)*
3. **Canonical readers ONLY — two surfaces, both full-card (RULE 25).** Agent reads via
   `python3 scripts/sl_project_any.py <enriched.json>` (text; 250 cards fit in context). Founder gets
   `python3 scripts/sl_stage2_table.py <enriched.json> <out.html> "<title>" "<funnel>"` (HTML, images).
   **Never** an ad-hoc/`/tmp`/partial reader. Confirm each prints its `FULL CARD RENDERED — PASS: N/N products` line.
   *(That line certifies the READING only. The DATA verdict is `sl_qa.py` / `sl_accept_chunk.py` — RULE 26.)*
4. **Acceptance statement** — state verbatim in the checkpoint: *"Loaded Stage-2 enriched file, not Stage-1; full card (3 tops
   + images + all fields) — QA PASS."*
5. **HTML preview to Desktop** — canonical HTML (NOT PNG — Marina S6) on the **first batch · every 5th · the last**
   (op-rules RULE 30 — same cadence as build), so Marina can spot-audit quality. More on request.

### STAGE-2 ACCEPTANCE CHECKPOINT (show Marina: batch 1 · every 5th · the last — RULE 30)
```
STAGE-2 ACCEPTANCE CHECKPOINT
Batch: [N]            Source file: [path]
Stage: Stage-2 enriched CONFIRMED / NOT confirmed
Stores: [N]   Reachable: [N]   needs_live: [N]
Required fields present: yes/no   (3 tops · images · in_range · descConf · store_type · product_class · cat_flag · maturity · new30d · home_pitch)
QA-gate: PASS / STOP [flags]      HTML preview: [Desktop path]
Decision: proceed / stop
```

### ANALYSIS CHECKPOINT (after deep-score, before Notion — proves the system ran, not memory)
As I analyse I keep two artifact files, then a gate verifies them (RULE 27) — the numbers below are COMPUTED by the gate, not typed from memory:
- **`np_bN_opens.jsonl`** — one line per hand-opened store `{domain, verdict}` (every needs_live + unreachable). **Generate it with `python3 scripts/sl_open_flags.py <enriched.json> np_bN_opens.jsonl` (RULE 29, P1+P3):** the tool seeds every flag + device-class-in-range store (domain·status·prices, with 503-retry) so completeness is enforced by the tool; the agent only fills each `verdict`. (Do NOT run the P2 consumer-other sweep — dropped S7; the RULE-6 full read is the net.)
- **`np_bN_scores.jsonl`** — one line per deep-scored candidate `{domain, hero, price, problem/wow/emotion/margin/market, veto, score, bucket}`.
- **`python3 scripts/sl_analysis_gate.py <enriched> <opens.jsonl> <scores.jsonl>`** → must be **✅ PASS** (STOPs if a flag is unopened or a device-class candidate has no verdict). It also emits the deterministic BROWSE-POOL (RULE 28).
```
ANALYSIS CHECKPOINT — Batch [N]
Stores read (all): [N]      needs_live + unreachable hand-opened: [N]/[N] (RULE 23, gate-verified)
Device-class must-review: [N]/[N] verdicted (gate)   deep-scored: [N]
Winners 65+: [N]   Borderline 55–64: [N]   Browse-links (rule-derived, RULE 28): [N]
consumer-other card-judged (transparency): [N]
Funnel breakdown (RULE 1): dumped → selected → reach/unreach → tiers A/B/C → deep-scored
ANALYSIS GATE: ✅ PASS / ⛔ STOP
```

### 🔬 HONEST QUESTION — one per batch (Marina S16) — NOT numbers-theatre
**Why (Marina S16):** the verifiable counts (read 250/250 · flags opened · browse floor) already live in the GATE
line — do NOT repeat them here. This checkpoint is the **one honest question I answer truthfully + in a few real
sentences**, so I catch myself the way Marina caught S15 ("почему так быстро?"). The work runs on trust — name any
slip plainly. **The question ROTATES batch-to-batch** (same sphere — depth / product-first / "am I reading b3 as
hungrily as b1" — different angle each time, so it never becomes rote):
Keep them PLAIN — real questions, not clever-for-clever's-sake (Marina S16: "вопросы ради вопроса не нужны"):
**Structure = 1 CONSTANT + 1 ROTATING (Marina S16).** The CONSTANT hits our known slip (under-opening live);
the ROTATING keeps it fresh. They are **Marina's voice** — what she'd actually ask — and a **living hypothesis**:
as new slip-points surface, add a targeted question (don't carve in stone). NO blaming words ("схитрил" is wrong —
Marina S16: imperfect work = system not yet built, not bad faith → use "не срезал ли где углы").

**CONSTANT (every batch — our caught slip, S16: I leaned on the card instead of opening live):**
> Сколько магазинов я реально открыл вживую (WebFetch) на этом батче? Из A/B/C и хвоста — сколько интересных нашёл и зашёл? Перечислить.

**ROTATING (one per batch, recycle):**
- Скажи честно — как тебе работалось на этом батче? Нигде не срезал углы, всё нормально?
- Как отработал скрапер/данные — пришли чистые, ничего не сыпалось?
- По скольким вердикт вынес по самому ТОВАРУ, а не по ярлыку категории? Где сомневался — открыл?
- Разобрал ли батч на полную глубину (как будто прошёл по каждому критерию по каждому товару) — или где-то по верхам?
- Если 0 винеров — это правда пусто, или подустал и пробежался? Что переделал бы?

**If an honest answer exposes a thin spot → STOP and redo it before the next batch.** FOR THE AGENT (self-catch),
Marina's voice — not a metric. (Origin of the CONSTANT: the live-open atrophy finding — see learnings.md S16.)

### ✅ SESSION CHECKLIST — tick each step (plain-language; the gates verify the ticks aren't empty)
The mandatory steps per batch, in order. I mark each ☐→☑ as I go and report them; `sl_qa.py` + `sl_analysis_gate.py` are the
machine that confirms the work behind the ticks. **(Floor, not ceiling — RULE 28: I always surface anything notable beyond this list.)**
```
☐ 1. Preflight: VPS credit-guard (ps aux | grep claude) · proxy health · enriched file present
☐ 2. Stage-2 DATA verdict: sl_accept_chunk.py → ACCEPT (it wraps sl_qa.py + encodes the benign-vs-breakage branch; STOP = re-enrich)
☐ 3. Read via the canonical AGENT surface (sl_project_any.py) — "FULL CARD RENDERED — PASS: N/N products" present (RULE 25)
☐ 4. State acceptance line: "Loaded Stage-2 enriched, not Stage-1; full card — QA PASS"
☐ 5. Canonical HTML (sl_stage2_table.py) → Marina's Desktop on batch 1 · every 5th · the last (RULE 30)
☐ 6. Read ALL stores (no gut top-N, RULE 6)
☐ 7. Hand-open EVERY needs_live + unreachable → log each in opens.jsonl (RULE 23)
☐ 8. Live-confirm hero + price for every genuine candidate (RULE 7) → score → scores.jsonl
☐ 9. Analysis-gate: sl_analysis_gate.py → ✅ PASS  (else STOP, fill gaps) — now ALSO STOPs if browse < 7 (RULE 32 floor)
☐ 10. Checkpoint to Marina — CONTRACT-COMPLETE (RULE 31): ALL sections present (winners / borderline / browse / funnel+ABC / loss-audit,
      each with the 1–2-line plain-language description) + the gate PASS line pasted. Missing any section = not canonical = STOP.
      Rhythm (RULE 33): batch-1 + batch-2 → STOP & WAIT for OK; within an approved block (batches 3–6) → post the FULL checkpoint
      but DON'T wait — continue, UNLESS a winner 65+ (pause before Notion) or breakage. "No stop" NEVER means "less report".
☐ 11. After OK / end-of-block: Notion + reported-products + sl_mark_processed + keep-list + learnings/HANDOFF
```
> ⭐ **S13 contract (Marina-approved 2026-06-07) — op-rules RULE 31/32/33.** The checkpoint REPORT is now gate-guarded like every
> other step ("external controller", not discipline): the gate self-STOPs until flags+device+browse-floor pass, and the report is
> valid only if contract-complete + carries the PASS line. **Browse FLOOR = 7 per batch, no ceiling — when unsure INCLUDE; the tail
> is a priority (Marina finds tail gems on other niches), never padded-down.** Rhythm = escalating autonomy 1→1→4, ~6 batches/session.

## 1b. RESERVOIR-BUILD MODE (scraper-prep — S8, Marina-approved 2026-06-03) ⭐
Use this when the session's job is to **run the scraper to PREP data** for a later analysis session (not to analyse a
ready file). The point: prep ahead so tomorrow's analysis starts instantly on ready chunks. **System-driven, one chunk at
a time, every chunk accepted** (RULE 30). Per chunk, in order:

> 🧭 **PATH CONVENTION (the trap that cost time in S8 — memorise it):**
> `sl_select_build.py` (& legacy `sl_select_all.py`) & `sl_enrich4.py` args are **RELATIVE to `logs/storeleads`**
> (the script prepends it → `niches/.../slug`). `sl_qa.py` / `sl_accept_chunk.py` / `sl_analysis_gate.py` /
> `sl_stage2_table.py` / `sl_project_any.py` take a **CWD-relative path** (full `logs/storeleads/niches/.../file`).
> Mixing them = `FileNotFound` / doubled path. Use the template verbatim.

**Launch template — DECOUPLED (S11): `enriched_index` exclusion, NO SKIP. `<D>=niches/<L1>/<niche>/<slug>`.**
```
# 0. SLICE from the captured CSV universe → the niche's _full.json (Stage 0, S17). Run ONCE per niche/band.
#    Pick the L1 category + visit band per operational-memory/strategy.md (Ось А priority + Ось Б band):
python3 scripts/sl_slice_from_csv.py storeleads_shopify_active_2026-06-08.csv <D> "<L1 Category>" <vlo> <vhi>
#    Cross-niche overlap is handled automatically by the enriched_index exclusion in step 1 (a store already
#    enriched in another niche is skipped) → the old `sl_master_dedup` pass is LEGACY (was for the dump era).
# 1. SELECT — next 250, excludes processed ∪ enriched_index (NO SKIP; order=visits desc, RULE 24):
python3 scripts/sl_select_build.py <D> <D>_s<S>_b<N> 250
# 2. LAUNCH enrich detached — minimal one-line nohup, 8 workers (proven safe on the single ISP IP):
cd /opt/market-research-agent; R=<D>_s<S>_b<N>; rm -f logs/storeleads/${R}.sentinel; \
  nohup python3 scripts/sl_enrich4.py ${R}.json ${R}_enriched.json ${R}.sentinel 8 \
  > logs/storeleads/${R}_enrich.log 2>&1 &
# 3. WAIT + ACCEPT — run_in_background Bash ends with the accept-line so the notification carries the verdict.
#    ⚠ KEEPALIVE (S17 fix): the Mac→VPS ssh for THIS wait-loop MUST carry keepalive, else it drops on a blip
#    (S17: ssh 255 mid-wait — enrich survives, it's nohup, but the loop dies & no notification fires). Use:
#    ssh -i ~/.ssh/market_research_vps -o ServerAliveInterval=30 -o ServerAliveCountMax=20 root@<host> '<loop>'
until [ -f logs/storeleads/${R}.sentinel ]; do sleep 15; done; \
  python3 scripts/sl_accept_chunk.py logs/storeleads/${R}_enriched.json
# 4. MARK ENRICHED — record the built chunk so build skips it forever AND parallel analysis can consume it safely:
python3 scripts/sl_mark_enriched.py logs/storeleads/${R}_enriched.json <niche> s<S>_b<N>
```
> **Why decoupled (S11, Marina):** `enriched ≠ processed`. Build excludes processed ∪ `enriched_index`; analysis marks
> `processed` (⊆ enriched for built stores). So a parallel analysis session can analyse the built chunks of the SAME
> niche being built WITHOUT shifting the build's page — the old SKIP-paging would have lost coverage when `processed`
> grew mid-build. `sl_select_all.py`+SKIP is retired for build; kept only as the legacy positional selector.
> *(Backfill `enriched_index` once from any chunks built before this existed: loop `sl_mark_enriched` over them.)*
> `sl_qa.py` alone still works as the raw gate; `sl_accept_chunk` WRAPS it (count-reconcile + credit-guard + ACCEPT-logic).

### ⭐ WAVE RHYTHM for large builds (S11; wave length + HTML cadence set by Marina S18)
A big niche runs in **waves of 10 = 1 + 9**, hands-off-but-verified:
- **chunk-1** = full SCRAPER-ACCEPTANCE check-list → **STOP, WAIT for Marina's OK** (proves the niche/run is healthy).
- **chunks 2–10** = run **without stopping between them**. Per chunk, post the human-readable progress report — **format lives
  in op-rules RULE 30** (✅ Chunk N/M — ниша — ПРИНЯТ + цифры словами + ▶️ что запускаю дальше; **plain text, never a code-block**).
  Marina watches, presses nothing. Per-chunk acceptance is MECHANICAL via `sl_accept_chunk.py` (credit-guard EVERY chunk —
  system, not discipline). Safety comes from that per-chunk check, not from the wave being short.
- **HTML → Desktop on chunks 1, 5, 10** (first · every 5th · last — the single cadence, op-rules RULE 30).
- **End of the wave:** consolidated wave report → **STOP, WAIT for OK** before the next wave. **Never auto-chain waves.**
  STOP mid-wave ONLY on GENUINE breakage (sl_accept_chunk prints STOP: reach<90 / count mismatch / cur_null>0 / reachable-card
  gap — NOT a benign products.json STOP) → come to Marina immediately.

### SCRAPER-ACCEPTANCE CHECK-LIST (present to Marina at chunk-1 + every 3 chunks; any QA fail → STOP + show now)
The agent ticks ☐→☑ from the actual run output. `sl_qa.py` runs on EVERY chunk (machine, 0-cost); the founder sees this
list at chunk-1 then every 3rd chunk. Grouped so a glance tells run-health vs data-completeness vs hygiene.
```
SCRAPER-ACCEPTANCE — <niche> reservoir, chunk N (stores X–Y)
— RUN HEALTH (was the run itself clean?) —
☐ 1. Select: 250 via `sl_select_build` from the niche slice (Stage 0) — excludes processed ∪ enriched_index, NO SKIP (S11 decoupled)
☐ 2. Enrich: sl_enrich4 8 workers DONE · sentinel present · ps aux | grep claude clean (RULE 13)
☐ 3. Count reconcile: enriched == selected (catches a silent worker crash mid-run)
☐ 4. Reach-band: reach ~90–97% = normal. Low reach in the deep/vNone tail is USUALLY `products.json`-disabled stores
      (storefront ALIVE, robot can't extract → `needs_live` hand-open at analysis — proven S1 11/12 + S2 17/18 alive),
      NOT dead and NOT a proxy fault. Do NOT re-run to "recover" them (the setting is stable — re-run reproduces the same
      set; verified S8 chunk-2 redo → reach 0/20). Truly dead = DNS-000 / frozen-402 only. A REAL proxy problem looks
      different: ALL stores slow/failing + duration blows up — a stable failing SUBSET = products.json, not the proxy.
☐ 5. Duration: ~5 min/250 baseline. Longer ≠ "lazy scraper" — often MORE extraction (more needs_live / heavier cards).
      Only a 3× blow-up WITH global reach collapse = a real proxy throttle. Track duration↔needs_live (hypothesis, verify).
— DATA completeness (RULE 26) —
☐ 6. QA-gate sl_qa.py → ✅ PASS  (⛔ STOP → see ACCEPT-logic below: a products.json STOP at reach≥~90 = ACCEPT+note; re-enrich ONLY on genuine breakage)
☐ 7. Card: ≥1top · img · in_range · descConf · 5 essence fields ≥ thresholds
— RESERVOIR hygiene —
☐ 8. Cross-niche overlap — handled automatically by the enriched_index exclusion in select_build (step 1).
      (`sl_master_dedup.py` = LEGACY dump-era pass; not needed with CSV slicing.)
☐ 9. File in reservoir path · enriched ≠ processed held (0 marked)
☐ 10. Verdict: chunk ACCEPTED / RE-ENRICH
```
**Why pts 3–5 exist (S8 — the run-health half):** QA proves the DATA is complete, but not that the RUN was healthy. A
crashed worker (pt 3) can pass QA on a partial set. **Low reach (pt 4) is the common one — and it is USUALLY benign:**
`products.json`-disabled stores (alive, hand-opened at analysis), NOT a proxy fault (the S8 lesson — don't proxy-test a
stable failing subset, the docs already explain it). A genuine proxy throttle is rarer and shows as GLOBAL degradation +
duration blow-up (pt 5). These three turn "data looks full" into "the run was sound." (Floor, not ceiling — RULE 28.)

**ACCEPT logic when QA STOPs (S8):** if reach is in-band (~≥90%) AND the unreachable are the products.json/dead pattern
(not a global proxy collapse), **ACCEPT the chunk WITH a note** — the unreachable go to `needs_live` hand-open at analysis
(RULE 23), nothing is lost. The QA numeric STOP here is the PROVISIONAL-threshold artifact for the thin/vNone tail (RULE 26
says thresholds are revisable; a false STOP only forces the look — which we did). Only a STOP with reach OUT of band /
global degradation is a real "re-enrich" case.

**Cross-niche dedup — LEGACY (S17 note):** in the dump era we ran `sl_master_dedup.py` to drop multi-category
overlaps before enriching a new niche. With CSV slicing + the `enriched_index` exclusion in `sl_select_build`,
a store already enriched under another niche is **skipped automatically** — so this pass is no longer part of the
flow. Kept for reference only: `sl_master_dedup.py dedup logs/storeleads/master_domains.json <new>_full.json <niche> --apply`.

## 2. Mode & checkpoints (STANDING)
- **Human-in-loop, with EARNED in-session autonomy for ANALYSIS (RULE 33, S13 — supersedes the old "NOT autonomous" line).**
  Batch-1 + batch-2 → full checkpoint → **WAIT for OK**; once stable, **batches 3–6 run as one block** (full contract-complete
  checkpoint EACH, no per-batch stop) UNLESS a **winner 65+** (pause before Notion) or **breakage** (gate STOP). Still
  human-gated at: batch-1/2, end-of-block, and **ANY Notion write (always WAIT for OK).** (RESERVOIR-BUILD keeps RULE 30's wave-rhythm.)
- Checkpoint = winners 65+ / borderline 55–64 / patterns / **browse-pool — FLOOR 7, no ceiling (RULE 32; when unsure INCLUDE; tail
  is a priority)** / full funnel+ABC / loss-audit — **all sections present + gate PASS line (contract, RULE 31).** Every link clickable.
  Convergence/revenue earns at most Watchlist, never auto-Consider.

### ⭐ MARINA-FACING CHECKPOINT — standard format (S6, Marina-approved 2026-06-03)
The founder-facing report (step 10). Same shape every batch so Marina reads it fast. Order matters: main
findings first, stats second, loss-audit last. **Every product gets a 1–2 line plain-language description —
this lets Marina judge it WITHOUT opening the site** (her explicit ask; e.g. a product that looks mediocre
on-site reads as "wow" from the description).
```
🟢 CHECKPOINT — Batch [N] ([niche], [visits range]) — STOP, жду OK

[1–2 lines: what was done — read N, hand-opened K (needs_live + own candidates), gates PASS]

🏆 WINNERS (65+)
  [N]. [Product name] — [score] · [clickable store link] · [$price]
       [1–2 lines: WHAT it is + which pain it solves + why it's a winner. ⚠ note risks/liability.]

🟡 BORDERLINE (55–64)
  • [Product] — [score] · [link] · [$price] — [1 line: what it is + why borderline]

🔎 BROWSE
  [clickable link] ([1-line: what it is / why off-model]) · …   (UNIQUE only, not in winners/borderline)

📊 Funnel + ABC
  [N] read · reach [N] · needs_live [N] → opened [N] · tiers A/B/C · classes · store_types
  ABC read: [1–2 lines — niche profile, where winners sat, honest yield]

🛡️ Loss-audit — «мог ли winner потеряться?» (agent answers EVERY batch, unprompted)
  - needs_live [N]/[N] opened → [N] hidden winners
  - where winners came from (card-sufficient vs flag) + any residual risk
  - verdict: loss ≈ [N]
```
**Rules:** clickable markdown links everywhere (never bare domains) · browse = UNIQUE links only · lead the
recommendation with WOW/differentiation/saturation read, not convergence count · the loss-audit is the agent's
job to raise, not Marina's to ask.

### Analysis refinements (S6, Marina-approved 2026-06-03)
- **#3 Borderline external-signal check (quality > token-cost — Marina):** for every BORDERLINE candidate (55–64),
  before finalizing the score run a quick external verification search (WebSearch/WebFetch): category trend, is anyone
  running ads on it, virality/social proof. One extra signal may lift a 62→67 or honestly drop it. Don't box judgment
  into card+site only. (Winners 65+ already get live-confirm; this extends the look for the borderline band.)
- **#2 Measured loss-audit (turn "0 loss" from faith into a number):** each batch, hand-open a RANDOM sample (5–10) of
  the **card-judged off-model pile** — stores NOT flagged needs_live that I dismissed from the card alone (apparel/
  formula/gift). Report the result in the checkpoint loss-audit ("spot-checked N dismissed → 0 winners"). If a winner
  turns up there → that's the signal the off-model card-judgment is leaking; tighten. This measures the one residual
  within-funnel crack (Stage-2 card-judged dismissals).
- **#4 Convergence = NOTED observation only, NOT a signal (Marina S6 — REJECTED as a weight).** Still fold true cross-store
  duplicates of the SAME product into ONE Notion card (convergence rule, for visibility). BUT do **not** let within-batch
  convergence lift a score OR a tier — a 250-store batch (even the full ~6.7k niche) is **not representative of the market**,
  so batch-level repetition can be a FALSE signal (similar stores may cluster in one batch by chance). Judge each product on
  its own merit (wow / differentiation / pain / economics), never on "how many times it appeared in this batch."

## 3. End-of-session Learning Protocol
1. After Marina's OK: save reported (65+) to Notion (`shared/notion-workflow.md`, Source = "Store Leads")
   + `shared/reported-products.md`; rejects → `shared/rejected-products.md`.
1a. **Mark the batch processed + master record (RULE 19/20):** run `sl_mark_processed.py` so the batch's stores are
    excluded from future selects AND carry their analysis data; set `monitor: true` + add strong/borderline stores to
    `operational-memory/keep-list.md`. Sync the repo `processed_domains.json` mirror from the VPS truth.
2. Append tactical learnings to `operational-memory/learnings.md` (with expiry); archive expired (RULE-15).
3. Log any founder decision on a SPECIFIC product → `operational-memory/founder-feedback.md` (Tier-1 fact).
4. Update the **HANDOFF** block at the top of `learnings.md` for the next session.
5. **Tier-2 guard (FB RULE 14):** any system-changing generalization (new taste/filter/veto rule,
   closing a category, a pivot, promotion into core/shared) is PROPOSED via `review/promotion-queue.md`,
   never self-written. Never edit `core/` or `shared/founder-taste.md` autonomously.
