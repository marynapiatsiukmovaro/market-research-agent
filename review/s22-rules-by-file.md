# S22 — РАЗБРОС op-rules ПО ФАЙЛАМ: вердикт + САМ ТЕКСТ для вставки
> Один файл-приёмник → **вердикт** (что делаем) + **сам текст, готовый к copy-paste** (дословно из op-rules, не ссылка) + **③ твоя правка**. Где текст надо писать по живому коду — так и сказано, выдуманного текста нет.
> Собрано `scripts/build_rules_by_file.py` из `departments/storeleads/operational-memory/op-rules.md`.

---

## 🗺️ ОБЩАЯ КАРТА — весь op-rules по порядку → куда идёт
Одним взглядом видно, что уходит в ПРАВИЛА, а что разбивается по файлам.

| op-rules | строки | что это | → куда |
|---|---|---|---|
| RULE 0 | L3–11 | сначала проверь | Правило **П1** |
| RULE 0b | L15–43 | неудобство = дефект | Правило **П3** |
| CREED | L47–57 | душа | **CREED** |
| шапка | L60–68 | provenance / порядок загрузки | **удалить** (provenance → хроника) |
| RULE 1 | L74–77 | funnel transparency | Правило **П2** |
| RULE 2 | L79–81 | не менять score молча | Правило **П2** |
| RULE 3 | L83–86 | «не найдено» ≠ «нет» | Правило **П2** |
| RULE 4 | L88–89 | verify before asserting | Правило **П1** |
| RULE 4a | L91–98 | при поломке замедлиться | Правило **П1** |
| RULE 5 | L104–106 | conservative cut | **удалить** (мёртв, отменён 24) |
| RULE 6 | L108–112 | читать всё; тир = сортировка | Правило **П4** |
| RULE 7 | L114–118 | подтвердить героя+цену live | Правило **П5** |
| RULE 8 | L120–123 | browse каждый батч | Правило **П8** |
| RULE 9 | L128–130 | дропшип/бренд ≠ reject | Правило **П9** |
| RULE 10 | L132–135 | high-ticket / bulky вниз | Правило **П9** |
| RULE 11 | L137–140 | honest low-yield валиден | Правило **П9** |
| RULE 12 | L142–146 | Founder Review — отдельный слой | Правило **П9** |
| RULE 13 | L152–155 | тяжёлое на VPS; no parallel claude | Правило **П10** |
| RULE 14 | L157–159 | прокси-дисциплина | Правило **П10** |
| RULE 15 | L161–163 | креды не в чат/git | Правило **П10** |
| RULE 16 | L169–173 | Tier-1 / Tier-2 | Правило **П13** |
| RULE 17 | L175–200 | конец сессии + формат | Правило **П12** · формат → `founder-feedback.md` |
| RULE 19 | L202–208 | mark processed | Правило **П12** |
| RULE 18 | L210–213 | гигиена памяти | Правило **П12** |
| RULE 20 | L217–225 | master-record + keep-list | Правило **П12** · поля → `methods/card-contract.md` |
| RULE 21 | L227–232 | качество > токенов | **CREED** (п.9) |
| RULE 22 | L234–238 | самопроверка энричера | `methods/card-contract.md` |
| RULE 23 | L240–259 | открыть каждый флаг ⚠ | Правило **П5** (⚠ развилка) |
| RULE 24 | L261–270 | анализировать всё; не фильтровать | Правило **П4** |
| RULE 25 | L272–301 | полная карточка + паритет | Правило **П6** · разбор S18 → `history/lessons.md` |
| RULE 26 | L303–324 | QA-gate перед анализом | Правило **П6** · пороги → `methods/pipeline.md` |
| RULE 27 | L325–334 | анализ доказан файлами | Правило **П7** |
| RULE 28 | L336–351 | browse + floor-not-ceiling | Правило **П8** · floor → **CREED** (п.8) |
| RULE 29 | L353–368 | curl ≠ заход | Правило **П5** · истории → `history/lessons.md` |
| RULE 30 | L370–418 | волна сборки 1+9 | Правило **П11** · механика → `methods/pipeline.md` · batched-tier(L390–397) → **удалить** |
| RULE 31 | L420–438 | контракт чекпойнта | Правило **П7** |
| RULE 32 | L440–450 | browse floor = 7 | Правило **П8** |
| RULE 33 | L452–467 | human-in-loop | Правило **П11** · история S15 → `history/lessons.md` |
| Checkpoint shape | L469–476 | форма чекпойнта | `workflow.md` (форма) · как дубль → **удалить** |

---

## → `history/lessons.md`
*Хроника — «почему система такая». НЕ грузится. Уже собрана (ступень 4).*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: провенанс + разборы поломок; заново не формулирую, эти блоки уже лежат в history/lessons.md.

**Текст для вставки в `history/lessons.md` (copy-paste, дословно):**

> ⸻ RULE 25 · блок S18 (op-rules L287–301) ⸻
>
> > **S18 — what actually happened, kept here so we never re-learn it (the "слово ≠ дело" class, RULE 0b).**
> > The old rule named ONE reader (the HTML). But 250 HTML cards do not fit a context window, so every analysis session actually read
> > through a text projector — a script that **lived only on the VPS, outside git** (born 2026-06-07, six days *after* the enricher
> > started emitting `home_hero`) and was itself **partial**: no `home_hero` (the homepage-banner product v4.2 added *because* the
> > best-seller auto-pick misfires — swaddlean/dingle), `desc` cut to 58 chars, no `bullets` / `desc_confidence` / `pust` / `kind` /
> > unreachable-reason. **For ~27 batches the agent judged on less than the founder saw.** The HTML was not innocent either: it rendered
> > neither `pust` nor `kind` — both direct Marina-Veto inputs. **Neither surface was complete, and nothing ever compared them.**
> > **Why it survived so long:** (a) the rule froze a TOOL, so the substitute fell outside it; (b) the substitute was named `..._tmp.py` —
> > nobody reviews a throwaway; (c) it never entered git, so no audit, no backup, no diff; (d) the acceptance ritual demanded the agent
> > say aloud *"full card — 3 tops **+ images** + all fields"* while its surface had **no images at all** — an unverifiable sentence,
> > recited every batch; (e) **absence of a field has no symptom** — the output looked complete.
> > Second half of the same bug: the HTML banner re-checked `sl_qa`'s thresholds, so on ONE file `sl_accept_chunk` said ACCEPT (benign
> > `products.json` dip) while the banner said STOP. A gate you must choose between is not a gate. Now: **one verdict, one owner.**
> > **Fixed S18:** both renderers in git, both print the full 28-field contract, both self-certify, and `sl_card_parity.py` proves each
> > batch that the two surfaces are the same card. The property is now checked by a machine instead of promised by a sentence.

> ⸻ RULE 29 · истории (op-rules L358–368) ⸻
>
> - **Running it to make `sl_analysis_gate.py` turn green is FORBIDDEN.** That is exactly how S15 happened: the gate
>   counts lines in a file, a curl produces lines, and three real winners (The Wriggler · Rockit · SnoofyBee) were lost
>   behind a green dashboard. Proven both ways: b4 with no live opens = 0 winners; b5 with live opens = 2 winners.
> - **The old wording of this rule said the tool "opens each" and "enforces RULE 23."** It never did. A rule that
>   describes work nobody does protects nothing (RULE 0b). *(Historical note: P1 was adopted S7 to make "opened but not
>   logged" impossible — that goal stands; the claim that a curl satisfies RULE 23 does not.)*
> - **P3 — transient retry stays:** a 503/timeout is retried once after a pause, then marked dead. Separates
>   live-on-retry from genuinely-dead (proven b14: twinieshop 503→retry→dead). At scale this stops a blip from
>   false-killing a real candidate.
> - **P3 — transient retry is built into the opener:** a 503/timeout is retried once after a short pause, then (still failing) marked dead. Separates live-on-retry from genuinely-dead (proven b14: twinieshop 503→retry→dead; b15: 0 retries needed = correct). At scale this stops a transient blip from false-killing a real candidate.
> - **P2 — functional-noun sweep over consumer-other: TESTED AND DROPPED (do NOT run it).** Across b12–b15 it never surfaced a winner the RULE-6 full-read hadn't already found, and on b14 its (un-widenable-in-advance) vocabulary would have **missed** the real winner (`babybond`, noun "gate"). **The real safety net for the consumer-other soft spot is the RULE-6 full read — a keyword sweep adds no coverage and risks false confidence.** Marina: "P2 не надо." (Script `sl_co_sweep.py` is not part of the workflow.)

> ⸻ RULE 4a · история S2 (op-rules L92–98) ⸻
>
> The trigger that caused a bad cascade in S2: a script **crashed** → I flipped from "investigate & verify" into
> "fix-it-fast" mode → in haste I **stopped pulling the fact from the data first** → invented a number ("81/40%
> dropped" when the real figure was 10), built a fix for a non-existent problem, and deleted a good result.
> **The rule:** a failure is a signal to slow down, not speed up. Before writing ANY "the problem is X / the number is N",
> ask: **"did I SEE this in the output, or am I ASSUMING it?"** If assuming → print the fact first, then act. A crash never
> justifies skipping verification. (This is a habit, not a constraint — the repo + Marina-approval already guard the big
> changes; this guards my own composure.) Pairs with RULE 4.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `methods/card-contract.md`
*Контракт карточки — что робот отдаёт (задание скрипту).*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: блоки op-rules описывают МЁРТВУЮ карточку v4.2 — не переносить; файл пишется по живому коду (_TEST).

**Текст для вставки:** — готового текста НЕТ — это задача: снять контракт с _TEST-скриптов. «28 полей» выкинуть.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `methods/pipeline.md`
*Механика прогона — команды, пороги, шаблоны.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: весь технический прогон RULE 30 → сюда, КРОМЕ «batched-tier» (L390–397, удаляю — спорит с волной 1+9).

**Текст для вставки в `methods/pipeline.md` (copy-paste, дословно):**

> ⸻ RULE 30 без batched-tier · часть 1 (op-rules L370–389) ⸻
>
> ### RULE 30 — Reservoir-build scraper: wait-pattern + one-chunk rhythm (S8, Marina-approved 2026-06-03)
> When BUILDING the reservoir (running `sl_enrich4` LIVE to prep data for a later session — not analysing a ready file),
> the work is **system-driven, never discipline-driven**. Three locked invariants:
> - **Wait via background, never poll.** Launch the enrich detached (minimal one-line `nohup` + sentinel — RULE 4c), then
>   wait for the sentinel through a **`run_in_background` Bash wait-loop** (`until [ -f <sentinel> ]; do sleep 15; done`).
>   The harness re-invokes on completion = **ZERO context burned while waiting.** NEVER a foreground blocking poll loop
>   (that burns context for nothing — the exact S8 lesson that exposed this rule was missing). The scraper itself is 0-token.
> - **Progress-narration rhythm (Marina S8 — refines "one chunk at a time"; her preferred S4 pattern):**
>   **Chunk-1 = full SCRAPER-ACCEPTANCE CHECK-LIST → STOP, WAIT for Marina's OK** (proves the run is healthy for this niche/
>   session). **After her OK, chunks 2..N run AUTONOMOUSLY — NO per-chunk approval.** After EACH chunk post the progress report
>   **as PLAIN TEXT in chat — never inside a code-block (Marina S17)**, human-readable, in this shape:
>   `✅ Chunk N/M — <ниша> — ПРИНЯТ` → `250 магазинов · сайты открылись у X% · счёт сошёлся (250 = 250) · качество данных: чисто · охранник (claude/скрапер): 0/0`
>   → `▶️ Chunk N+1/M — запускаю энрич (250 магазинов, ~7 мин)… идёт`.
>   (Галочка + что сделано + цифры человеческим языком + что запускаю дальше. Старый машинный one-liner
>   `k/N done · <verdict>` РЕТАЙРЕН — Marina S17: нечитаемо.) So Marina sees it's flowing without
>   pressing buttons. **Consolidated wave report at the end → STOP for OK.** Each chunk is still individually QA'd + count-
>   reconciled by the agent (so a failure is caught) — **STOP and surface IMMEDIATELY only on GENUINE breakage** (reach
>   out-of-band / worker-crash / count-mismatch / cur_null>0 — NOT a products.json STOP). This beats a silent server-side
>   loop (Marina's S4 worry: "вдруг что-то слетело") AND beats per-chunk approval (button-fatigue): narrated, verified,
>   hands-off. **NEVER fully fire-and-forget a multi-chunk server loop with no per-chunk check** — narrate + verify each.

> ⸻ RULE 30 без batched-tier · часть 2 (op-rules L398–418) ⸻
>
> - **Selection = `sl_select_build.py` (enriched_index exclusion, NO SKIP) — S11 decoupled, Marina-approved.** Build selects the
>   next 250 excluding `processed` ∪ `logs/storeleads/enriched_index.json`; mark each built chunk with `sl_mark_enriched.py`.
>   This **RETIRES the old SKIP-paging** (`SKIP=(N-1)*250`): SKIP shifts the page when `processed` grows mid-build, so a parallel
>   analysis session marking the SAME niche would cause a coverage gap. With enriched_index exclusion that is a **no-op** (a
>   processed store is already excluded as enriched) → **parallel analysis of the SAME niche being built is SAFE**
>   (S11-PROVEN: `processed` grew 11,219 → 17,854 mid-build via parallel S12/S13b, the build page never shifted). `enriched ≠
>   processed` stays the invariant (build marks enriched; only analysis marks processed). Guardrail unchanged: both `claude`
>   run on the Mac, **never on the VPS** (RULE 13). *(Legacy `sl_select_all.py`+SKIP kept only as the positional selector for
>   non-decoupled use; not for parallel build.)*
> - **Per-chunk acceptance = `scripts/sl_accept_chunk.py <enriched.json>` (S11, Marina-approved 2026-06-07).** One verdict
>   line = count-reconcile + credit-guard (`ps aux | grep claude`, EVERY chunk) + canonical `sl_qa.py` + encoded ACCEPT-logic
>   (benign products.json STOP → ACCEPT; genuine breakage → STOP). System, not discipline.
> - **⭐ WAVE = 1 + 9 = 10 chunks (Marina S18; was 7).** Chunk-1 → full SCRAPER-ACCEPTANCE check-list → **STOP, wait for OK**
>   (proves the niche/run is healthy). Then **9 chunks run without stopping between them** — each still machine-accepted by
>   `sl_accept_chunk.py` and narrated (RULE 30 report format). At the end of the wave: consolidated report → **STOP for OK.**
>   **Never auto-chain waves.** Mid-wave STOP only on GENUINE breakage (the wrapper prints STOP) — then come to Marina at once.
>   *Why the length is safe: safety rests on the per-chunk machine check, not on the wave being short — the wrapper is as awake
>   at chunk 9 as at chunk 2. There is no unattended server loop; the agent launches each chunk, it just doesn't ask permission.*
> - **⭐ HTML cadence — ONE rule, both modes (Marina S18): first · every 5th · last** (so 1, 5, 10 in a wave of ten). Canonical
>   HTML (`sl_stage2_table.py`) → Marina's Desktop. Anything else on request. *(Was: "last chunk of each wave" in build vs
>   "batch-1 + every 4th" in analysis — two answers to one question, in two files.)*
>
> Плюс числа-пороги из RULE 26: reach≥90 · ≥1top≥97 · descConf≥99 · in_range≥99 · cur_null=0.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `methods/scripts.md`
*Реестр действующих скриптов. Имена — только здесь.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: реестр собрать по факту (VPS); сейчас имена в правилах врут (TEST↔канон, долг №1).

**Текст для вставки:** — готового текста НЕТ — это задача: сверить с кодом. Форма записи: `имя · что делает · жив/мёртв`.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `workflow.md`
*Форма процесса и чекпойнта.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: сюда — только ФОРМА чекпойнта (содержание не дублирую; «Checkpoint shape» = дубль RULE 31/32/33).

**Текст для вставки в `workflow.md` (copy-paste, дословно):**

> ⸻ «Checkpoint shape» (op-rules L469–476) ⸻
>
> ## Checkpoint shape (every batch, before any Notion write)
> Winners (65+) · Borderline (55–64, flag for founder call) · Watchlist-signal · Browse-pool (**FLOOR 7, no ceiling —
> RULE 32; when unsure INCLUDE; tail is a priority, never padded-down**) · Patterns · the full funnel breakdown
> (RULE 1) **including the explicit A/B/C tier counts** (Marina cross-checks against the ABC split). Every link = a
> clickable markdown hyperlink. **The report is contract-complete + carries the gate PASS line (RULE 31).** Then **STOP and
> wait for Marina's OK** — every batch, no exceptions (RULE 33). Nothing goes to Notion before her explicit OK.
> *(S20: the old tail here said "within an approved block, batches 3–6 do NOT stop per-batch — RULE 33" — it cited RULE 33
> while stating the opposite of it. Leftover from the pre-S19 wording; removed, not re-decided.)*

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `founder-feedback.md`
*Формат решений Марины. 🔴 Красная линия — сам файл не трогаем.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: формат заметок из RULE 17 → дословно в шапку founder-feedback.

**Текст для вставки в `founder-feedback.md` (copy-paste, дословно):**

> ⸻ RULE 17 · формат заметок + approval-блок (op-rules L181–200) ⸻
>
> **Founder-feedback format** (one row per decision, table per tier — Approved / Consider / Watchlist / Rejected):
> `Date · Product · Score · Marina's reason (her words — the "сок") · Signal to keep (calibration)`.
> So Marina explains once; the agent distils.
> 
> **Founder Notes / Rejection Reason — phrasing principle (Marina-confirmed 2026-05-31):**
> - **Ultra-compact: 4–5 words MAX**, written as **short fragments ending with a period** — bullseye, no fluff.
> - **Rejected** → fill **Founder Notes + Rejection Reason**. **Watchlist / Consider / Approved** → **Founder Notes only**.
> - Marina gives the verdict verbally (expanded); the agent renders it into this compact form, **shows her the
>   COMPACT PER-PRODUCT BLOCK for approval BEFORE writing to Notion** (NOT a wide table — Marina S7 2026-06-03), adjusts,
>   then writes. Never invent a verdict; never set Founder Review.
> - **⭐ APPROVAL-PRESENTATION FORMAT (Marina-locked S7 2026-06-03) — render each decision as a block, exactly:**
>   ```
>   [Product Name] | [Tier]
>   Founder Notes: [≤4–5 words, fragments ending with a period]
>   Rejection Reason: [ONLY when Tier = Rejected — 1 short fragment]
>   ```
>   This is WHY the notes are 4–5 words: the block must read at a glance. Group blocks loosely by tier; no table, no extra columns.
> - Real reference examples (from the live DB): Founder Notes — "Solves real pain." · "Apple-like aesthetic." ·
>   "Stylish design. Real pain-solver." · "Banal product. Brilliant packaging." · "Strong pain-solver. Strong seasonal hooks."
>   Rejection Reason — "High refund risk." · "Narrow audience. Hard to scale." · "Overexposed category." · "Fragile shipping risk."

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `where-things-live.md`
*Пути и команды — без меняющихся цифр.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: собрать пути и команды.

**Текст для вставки в `where-things-live.md` (copy-paste, дословно):**
>
> Перед любым запуском на VPS: `ps aux | grep claude` (credit-guard).
>
> Прокси: health-check перед прогоном (`sh_proxy_check`).
>
> VPS-коннект (host · ключ · база) + где лежат processed_domains · keep-list · резервуары.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `peculiarities.md ⭐ новый`
*Частные случаи: симптом → что это скорее всего → что делать.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: создать файл; формат по этапам.

**Текст для вставки в `peculiarities.md ⭐ новый` (copy-paste, дословно):**
>
> reach упал ниже нормы → скорее всего products.json выключен, магазин ЖИВ → открыть руками, не перезапускать.
>
> SSH оборвался посреди прогона → энрич выжил под nohup → ждать sentinel, не перезапускать.
>
> при обвале reach → сначала прогнать прежнюю версию скрапера на тех же данных, потом гипотеза (S21).

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---

## → `⛔ УДАЛИТЬ · git помнит`
*Мёртвое и дубли — не переносим никуда.*

**② МОЯ ВЕРСИЯ (агент).** Вердикт: удалить, откат через git.

**Текст для вставки:** — не вставляется никуда. На удаление: RULE 5 (мёртв) · «batched-tier» (L390–397) · «(This is a habit…)» (L97–98) · «Checkpoint shape» (дубль). Шапку op-rules сжать до 2 строк.

**③ ПРАВКА МАРИНЫ:**
> _(вычеркни / оставь / добавь)_

---
