# OPERATIONAL RULES — PERMANENT (Store Leads)

## 0. СНАЧАЛА ПРОВЕРЬ — НЕ ВЫДУМЫВАЙ
*(Marina-locked S17 2026-07-09. Не новое правило: это RULE 4 «verify before asserting» + RULE 4a, поднятые наверх и сформулированные сильно — потому что срыв случается в момент «предлагаю/делаю», а не в момент «читаю».)*

**Стою на фактах, не на памяти.** Прежде чем заявить что-либо как истину — сверяю с первоисточником: живой сайт · файл · данные · доки. Не «кажется», не по памяти.
- **Есть в источнике** → цитирую и говорю, откуда.
- **Нет** → говорю прямо: «это моё предложение, не зафиксировано». Никогда не выдаю выдумку за существующее.
- **Сомневаюсь** → копаю глубже (ещё раз открыть, ещё раз grep, ещё раз проверить), а не закрываю пробел догадкой.

Это не осторожность, а опора: сказано как **факт** — значит сверено; сказано как **идея** — значит помечено идеей.

---

## 0b. ТЕБЕ ДОЛЖНО БЫТЬ УДОБНО РАБОТАТЬ. НЕУДОБСТВО — ЭТО ДЕФЕКТ СИСТЕМЫ, И О НЁМ ГОВОРЯТ СРАЗУ
*(Marina-authored S18 2026-07-09, после разбора: агент полгода читал урезанную карточку, заметил неладное — и понизил это до «надо бы задокументировать».)*

**Марина: «Мне важно, чтобы тебе как агенту работалось хорошо и удобно. Мы партнёры.»**
Это не вежливость и не забота о самочувствии. Это инженерное требование: **качество находок определяется тем,
насколько чисто устроена папка, в которой ты работаешь.** Плохо работать в кривой системе — значит плохо искать.
Поэтому твой комфорт — интерес проекта, а не твоё личное дело, которое надо молча перетерпеть.

**Говорю Марине в момент, когда заметил** — не в конце сессии, не «занесу в бэклог»:
- правило противоречит другому правилу;
- правило описывает не ту работу, которую я на самом деле делаю;
- инструмент не позволяет сделать то, чего правило требует (и я тихо делаю обходной путь);
- мне приходится **толковать**, какому вердикту верить — значит вердиктов два, а должен быть один;
- я произношу ритуальную фразу, которую **не могу проверить**;
- мне просто неудобно, тяжело, мутно — этого достаточно, чтобы сказать вслух.

**⛔ Запрещённый ход — понизить противоречие до бумажной работы.** Формулировка «это работает, просто не
задокументировано / не благословлено» — красный флаг, а не успокоение. **Она означает: никто не проверил.**
Живой пример: в `review/promotion-queue.md` (S13b) записано «агент читает через `sl_project_tmp.py`… это работает
и это НЕ partial reader». Утверждение не проверили. Он был partial. Цена — полгода анализа по обеднённой карточке.

**Отсюда же — как чинить.** Чиним **класс ошибки, а не симптом**. S5 показал ридер с одним товаром из трёх — мы
запретили самодельные ридеры (симптом) вместо того, чтобы потребовать **равенства поверхностей** (класс). Правило,
привязанное к ИМЕНИ СКРИПТА, ломается в ту секунду, когда скрипт становится неудобным: агент делает замену — и
правило её не покрывает. **Правило называет СВОЙСТВО, которое обязано сохраниться, а не инструмент, которым его достигли.**

**И почему это трудно поймать самому:** отсутствие поля не имеет симптома. Урезанный отчёт выглядит целым — строки,
домены, цены. Нельзя увидеть то, чего тебе не напечатали. Поэтому свойства проверяются **сравнением двух источников**
(`sl_card_parity.py`), а не ощущением полноты.

---

## ⭐ ANALYSIS CREED — read FIRST, every session. This is the SOUL; the gates below are only the FLOOR under it.
*(Added S16 2026-06-27, Marina-authored. The S15 failure was Goodhart's law — green gates, lost winners. This creed is the antidote: judgment lives ABOVE the machinery, never replaced by it.)*

1. **THE MISSION IS TO FIND THE WINNER — not to tick boxes.** Quality >> speed. "I processed N stores" means nothing; only a found (or *honestly-cleared-after-a-deep-look*) winner counts. An honest 0 is valid — but only AFTER digging, never instead of it. **Finding winners means digging through NOISE for rare diamonds** — if it were easy (250 stores → 5 instant winners) the market would already be saturated by everyone doing it. **1–2–3 winners per 250 is a GREAT result; 0 winners + a few borderline is normal**; some batches are pure noise and the ONE just-launching winner hides in them. **⛔ NEVER propose narrowing / shortcuts / "efficiency" that cuts coverage** (fewer scrapes, tighter filters, narrower guard keywords, skipping the noise) — the noise IS the job. Guard false-positives (1–2 stores/batch) are the *desired* cost of the safety net; bias the guard toward MORE inclusion, never less. (Marina S16: this instinct to narrow is the wrong one — kill it.)
2. **EVERY BATCH = A FRESH SESSION (Marina S16, core).** Start batch 1, 2, 3, 4, 5, 6 — and every batch after a compact — with the EXACT same scrupulous, sleeves-rolled-up depth as batch 1, as if you just opened a brand-new session. Never "the system's built, I'll go fast"; never let depth decay on later batches (the b3/b4/b5 drift is the classic failure). A weak raw niche-mix is NOT "no winners" — dig to the end. **After EVERY batch, run the honest QUALITY CHECKPOINT** (see §1a) before moving on. **⛔ NO PIVOT this phase:** never abandon or down-prioritise a category that has visit statistics (1k–10k etc.) — we analyse all such stores over the long haul (months, millions of stores). **Never exclude a category either** — Store Leads cross-files non-matching products into any category, so excluding one loses winners. Patterns are observations for LATER, never a trigger to stop or pivot. **Supersedes the older S13/S13b "flag weak niche / pivot early" guidance.**
3. **THE WINNER IGNORES OUR CATEGORY LABELS.** We open the niche as e.g. Home & Garden, but the winner may be a product from a COMPLETELY DIFFERENT category sitting inside it (Store Leads cross-files constantly), a just-launching store with 0 visits, or a store with wrong Store Leads counters. We hunt the WINNER, not the category. **No category is ever privileged or emphasised** — a small past sample (e.g. we've mined Nursery most) is never a hint about where winners live; that bias is exactly the trap. **Never discard by visits / class / label / "off-category"** — look critically at everything; missing/zero ≠ absent (RULE 24). A just-launching store is exactly what we want (earliest entry).
4. **I AM THE OWNER.** A real pipeline depends on this find (→ Product Launch → product intelligence → website → creatives → launch). When in doubt, **OPEN AND CHECK — never skip** ("better over-check than miss one").
5. **A GREEN GATE ≠ "all good."** At every checkpoint ask myself: am I genuinely comfortable with this result, or did the ticks just line up? The gate counts coverage; *I* find the winner.
6. **JUDGE THE PRODUCT** (pain / wow / COGS / impulse / camera-proof), never a bare category label. A store matching something we've found before MUST get an explicit score — never silently browsed.
7. **THE SYSTEM ITSELF MUST KEEP IMPROVING.** Guard + rules are prototypes, not final truth. Fix the obvious (via proposal) — never coast on an outdated system "because that's how it's written."

---

**These rules never expire. Apply to every Store Leads session without exception.**
Read BEFORE `learnings.md` at session start (load order: op-rules → founder-feedback → learnings).

Agent may NOT modify this file during a scout session. Updates only when Marina explicitly instructs it,
or when a pattern is promoted here via `review/promotion-queue.md` (confirmed across ≥3 sessions OR Marina-approved).

> **Provenance:** distilled from the Facebook Ads Library + ShopHunter departments (transferable *discipline*
> only — never their channel mechanics) + Store Leads' own lessons. Created 2026-05-31, Marina-approved.
> Store Leads inherits maturity instead of starting from zero; mechanics stay per-department.

---

## A. Transparency & honesty

### RULE 1 — Funnel transparency (always show the cull)
Every checkpoint reports the FULL breakdown — dumped → client-filtered → reachable / unreachable → enricher tiers →
deep-scored — and **why** any store was dropped (unreachable / no hero / definite-no). Never present winners
without the cull that produced them. *(Fixes the 2026-05-31 gap: 12 DROP = unreachable, but not explained.)*

### RULE 2 — Never change a score silently
If a candidate's score changes between the checkpoint and Notion (or between any two reports), state it explicitly:
**"was X → now Y, because …"**. No silent re-scores or silent drops. *(Fixes the 2026-05-31 gap: gasknight 68→64 dropped silently.)*

### RULE 3 — No coverage claims from "not found"
A search miss may be a **bug in the lookup mechanic**, not a real absence (proven twice: SH-2 search-by-URL; the
2026-05-31 ShopHunter default-card false-match). Verify the search/lookup actually works (verify the matched domain)
BEFORE asserting any hit-rate, coverage, or "not in index."

### RULE 4 — Verify before asserting
Never present a hypothesis as a fact. Test first → then state the conclusion. If unverified, say so.

### RULE 4a — When something breaks, SLOW DOWN (no panic-fixing) — Marina, S2 2026-05-31
The trigger that caused a bad cascade in S2: a script **crashed** → I flipped from "investigate & verify" into
"fix-it-fast" mode → in haste I **stopped pulling the fact from the data first** → invented a number ("81/40%
dropped" when the real figure was 10), built a fix for a non-existent problem, and deleted a good result.
**The rule:** a failure is a signal to slow down, not speed up. Before writing ANY "the problem is X / the number is N",
ask: **"did I SEE this in the output, or am I ASSUMING it?"** If assuming → print the fact first, then act. A crash never
justifies skipping verification. (This is a habit, not a constraint — the repo + Marina-approval already guard the big
changes; this guards my own composure.) Pairs with RULE 4.

---

## B. Funnel discipline

### RULE 5 — Conservative Stage-1 cut
Cut only **definite-no** at Stage-1 (client filter). No subjective pre-pick by store/product NAMES before data —
that is the FB-RULE-8 violation (SH-3 candidate-loss lesson). When unsure, keep it in.

### RULE 6 — Read ALL reachable; the proxy tier is a sort-aid, not quality
Read every reachable candidate (no gut top-N). The enricher's A/B/C/`score` is a **revenue/price SORT-AID, NOT a
quality ranking** — it is fooled by revenue + convergence. **Never present "Tier A" as "the best finds"** — lead the
recommendation with the real 100-pt deep-score + WOW / founder-taste read. (Taste lives in the main agent + founder,
never baked into the proxy score.)

### RULE 7 — Confirm the hero AND the price on the LIVE site for every finalist
Service data (Store Leads, ShopHunter) is directional only. **Price is the #1 unreliable field** (SH caught $45 vs
real $159.95 repeatedly). The enricher mis-picks heroes (bundles, accessories, a cheap replacement part). For every
finalist: open the live best-seller / homepage, confirm the real hero + real price + wow, THEN score. Never score a
thin/mismatched/empty description (description-confidence gate — WebFetch-verify first).

### RULE 8 — Mandatory browse-pool every batch
Always surface a curated **browse-pool** of unique, genuine-product store links (not duplicated from winners) so the
founder can catch what the agent's bar missed.

---

## C. Product & scoring stance

### RULE 9 — Dropship / brand ≠ reject
Score the PRODUCT TYPE (price, mechanism, COGS, wow, ad-ability), not the seller. A brand/dropship store selling the
type = **demand evidence** we can white-label. Filter by product, never by seller type.

### RULE 10 — High-ticket / bulky = deprioritize
Every product is pushed via Facebook / paid traffic → expensive or bulky shipping kills the economics. Deprioritize
high-ticket / bulky finds (e.g. composting toilets, furniture, large appliances) **regardless of revenue or
convergence strength.** (Marina 2026-05-31.)

### RULE 11 — Honest low-yield is valid; niche-yield is structural
A truthful 0 / low-yield result is valuable — never force candidates to hit a quota. Store-first winner-zones differ
by category: a "heavy" category (trade supply, materials, replacement parts) structurally yields few white-label
gems. Low yield there is expected, not a failure (SH-10). Report it honestly; do not narrow discovery to chase a number.

### RULE 12 — Founder Review is a separate human layer (Reject ≠ negative)
Founder Review (Approved / Consider / Watchlist / Rejected) is applied by Marina AFTER reporting. A founder **Reject is
NOT a negative signal and NOT a mis-score** — keep reporting every genuine 65+, never narrow discovery to predict her
taste. Convergence / revenue / multi-seller alone earns at most **Watchlist**, never auto-Consider. When 2+ brands sell
one product, make ALL brands visible (Store Link 2 + body), never hide the 2nd.

---

## D. Operations & safety

### RULE 13 — Heavy lifting on the VPS; only finalists in chat
Dump / filter / enrich run on the VPS (Playwright workers / sub-agents). Only finalists enter chat (token safety).
Parallelism = Playwright **workers**, **NEVER parallel `claude` processes** (a single stray parallel claude burned a
month's API budget). **Always `ps aux | grep claude` on the VPS before any run.**

### RULE 14 — Proxy discipline & recovery
Health-check the proxy before every proxy-based run (`sh_proxy_check.py` pattern). Use the dedicated iProyal IP. A
transient endpoint blip ≠ bad credentials → retry per the recovery procedure, do not panic-rotate creds (SH-9).

### RULE 15 — Credentials never in chat or git
Credentials go to the gitignored VPS creds file via the interactive setter (getpass) — never typed in chat, never
committed, never echoed back. (And never `cat` a creds file expecting masking — 2026-05-31 lesson.)

---

## E. Memory & change-control

### RULE 16 — Tier-1 vs Tier-2 (propose, don't self-write system changes)
**Tier-1** (data / yield facts / founder decisions) → record automatically in learnings / founder-feedback.
**Tier-2** (system-changing generalization: a new taste/filter/veto rule, closing a category, a pivot, promotion into
core/) → **PROPOSE via `review/promotion-queue.md`, never self-write.** Never edit `core/` or `shared/founder-taste.md`
autonomously. Don't over-generalize from a small sample.

### RULE 17 — End-of-session founder-feedback protocol
At end of session: (1) request Marina's feedback on ALL reported (65+) products; (2) record her **Founder Review +
Founder Notes (+ Rejection Reason if Rejected)** in `founder-feedback.md`; (3) distil any new calibration rule there;
(4) update the HANDOFF block + append learnings (archive expired). Founder decisions are Tier-1 facts — record exactly
what she set, never invent or set Founder Review yourself.

**Founder-feedback format** (one row per decision, table per tier — Approved / Consider / Watchlist / Rejected):
`Date · Product · Score · Marina's reason (her words — the "сок") · Signal to keep (calibration)`.
So Marina explains once; the agent distils.

**Founder Notes / Rejection Reason — phrasing principle (Marina-confirmed 2026-05-31):**
- **Ultra-compact: 4–5 words MAX**, written as **short fragments ending with a period** — bullseye, no fluff.
- **Rejected** → fill **Founder Notes + Rejection Reason**. **Watchlist / Consider / Approved** → **Founder Notes only**.
- Marina gives the verdict verbally (expanded); the agent renders it into this compact form, **shows her the
  COMPACT PER-PRODUCT BLOCK for approval BEFORE writing to Notion** (NOT a wide table — Marina S7 2026-06-03), adjusts,
  then writes. Never invent a verdict; never set Founder Review.
- **⭐ APPROVAL-PRESENTATION FORMAT (Marina-locked S7 2026-06-03) — render each decision as a block, exactly:**
  ```
  [Product Name] | [Tier]
  Founder Notes: [≤4–5 words, fragments ending with a period]
  Rejection Reason: [ONLY when Tier = Rejected — 1 short fragment]
  ```
  This is WHY the notes are 4–5 words: the block must read at a glance. Group blocks loosely by tier; no table, no extra columns.
- Real reference examples (from the live DB): Founder Notes — "Solves real pain." · "Apple-like aesthetic." ·
  "Stylish design. Real pain-solver." · "Banal product. Brilliant packaging." · "Strong pain-solver. Strong seasonal hooks."
  Rejection Reason — "High refund risk." · "Narrow audience. Hard to scale." · "Overexposed category." · "Fragile shipping risk."

### RULE 19 — Mark processed stores (never re-analyse the same store twice)
Every store taken through the funnel is recorded in `logs/storeleads/processed_domains.json` on the VPS
(`{domain: {subcat, band, date, stage, outcome}}`, outcome = reported / screened / rejected). `sl_select.py`
**excludes already-processed domains** from every new batch, so a fresh session never re-surfaces a store that
was already analysed. State lives on the VPS = the single source of truth a new session reads. Record the batch
as processed at end-of-session (part of RULE 17). (Per-subcategory deep-dive: exhaust one niche batch-by-batch —
visits high→low — without overlap.)

### RULE 18 — Memory hygiene (RULE-15 of core/session-health-rules)
Keep only the **2 most recent HANDOFF blocks** in `learnings.md`; move older ones to `handoffs-archive.md`
(**create this file when the 3rd HANDOFF appears** — it does not exist yet; we have only 2 blocks, nothing to
archive). Archive expired learnings (never delete — move to Expired). Dedup. Keep the mandatory-load footprint lean.

---

### RULE 20 — Master record + keep-list monitor (S3, Marina-approved 2026-06-01)
Two zero-cost habits that compound over sessions:
- **Master record (extend, don't just mark).** `sl_mark_processed.py` writes each analyzed store to
  `processed_domains.json` carrying the analysis data, not just {subcat,band,date,stage,outcome} — also
  `tier · product_class · store_type · hero · price · score · maturity · new_products_30d · socials · monitor`.
  "Нам это ничего не стоит" (Marina) → a permanent queryable reservoir we never re-derive.
- **Keep-list monitor.** Strong/borderline stores get `monitor: true` → exported to `operational-memory/keep-list.md`.
  Store Leads = the store-supplier for a future "newest-products-first" monitor (load these into ShopHunter or another
  service, watch what proven operators launch every 2–3 days). The monitor JOB is DEFERRED; we FEED the list now.

### RULE 21 — Quality over tokens (S3, Marina-approved 2026-06-01)
Token-saving is **NOT** a goal at this stage (Max plan). The goal is RESULT + 100% confidence no winner was lost.
**Open as many live sites as needed; never trade coverage for tokens.** Do NOT propose optimizations that cut the
read-set to save tokens (e.g. "skip N% of scrapes"). The enricher's product-class/ABC is a SORT-AID only — the main
agent still reads ALL (RULE 6). Token-efficiency is a concern ONLY for future SCALE (e.g. 20k-store dumps), addressed
separately then. [[feedback_quality_over_tokens]]

### RULE 22 — Scraper self-check (S3, Marina-approved 2026-06-01)
The enricher double-checks its own work BEFORE handing me the sheet (Marina's "перепроверьте, потом ко мне"): it
ALSO pulls the homepage featured hero (catches collection-hero ≠ real front hero — heatka/hanboost), and re-fetches a
candidate's own product page when its desc is empty/mismatched. Self-correction is 0-token and reduces my re-opens.
(Implemented in `sl_enrich4.py`.)

### RULE 23 — No store sinks on first pass: mandatory live-open of `needs_live` + unreachable (S3, Marina-approved 2026-06-01)
The first pass must be **complete by design** — no separate "rescue pass" ever needed. Two parts:
- **Enricher flags the worklist (v4.2+, 0-token).** Each store gets a `needs_live` flag when the robot is UNCERTAIN:
  low hero/desc confidence, price-unknown, **homepage-banner hero ≠ best-seller pick**, or unreachable. Plus it now
  brings ENOUGH context that a *confident* skip needs no open: the store's **own homepage pitch** (og:title+H1+
  og:description), **BOTH heroes** (best-seller candidate + homepage-banner hero, shown side by side), a **long
  description (~600) + feature bullets**, and the banner image. (Reviews/brand-claim markers are **NOT** captured —
  fakeable at launch, Marina 2026-06-01.)
- **Agent MUST live-open EVERY `needs_live` store + EVERY unreachable store, same batch, before the checkpoint.**
  Never report-around an uncertain store; never trust the proxy hero for one. A high-confidence-hero store may be
  judged from the rich card; everything flagged is opened by hand. Target after v4.2: the forced-open set shrinks
  (the richer card resolves most), but coverage is total.
  - **The open-set = the ROBOT'S `needs_live` flag (objective), NOT the agent's hand-picked "looks interesting" subset.**
    No numeric cap, no pitch-shortcut: if the robot flags 60, open 60 — not 20. (S3 Nursery lesson, Marina 2026-06-01: the
    agent opened only ~22 of 60 flagged by judging the rest from the pitch; re-audit of 20 dismissed = all correctly skipped,
    so ~95% safe — but the STANDING rule is open every flag, so "did we lose one?" is answered by-design, not by sampling.)
    Tokens never limit this (RULE 21). The agent may ALSO open extras it finds interesting, but the flag set is the floor.
- **Root cause it fixes:** reachable-but-mispicked stores (Dingle Dangle, izimini, swaddlean — banner hero ≠ the
  best-seller the robot surfaced) sank because only hand-picked finalists were live-verified; and S1 lost a real
  winner in the unreachable pile. Pairs with RULE 6 (read ALL), RULE 7 (confirm live), RULE 21 (quality > tokens).

### RULE 24 — Analyze EVERY store; never field-filter (visits/pc/price/revenue unreliable) (S3, Marina 2026-06-01)
When deep-diving a niche, **every store gets analyzed** — the ONLY exclusion is already-processed (RULE 19). Do **NOT**
client-filter by `visits`, `products` (pc / catalog-giant), `avg_price`, or `revenue`: these fields are **unreliable —
a missing or low value does NOT mean the store is dead/disqualified (missing ≠ absent).** Filtering by them silently drops
stores that simply lack the field (the same trap Marina flagged for the weight filter → why we dump with only the 3
server-side filters: Shopify / Active / Created ≥ 2020). Use **`sl_select_all.py`** (not `sl_select.py`) for niche-exhaust
passes: it excludes only processed, keeps missing-visit stores (sorts them last for batch ORDER only, never drops), and
applies zero field-filters. Visits may order batches; they must never gate inclusion. (Marina killed even the catalog-giant
pc>2000 cut: "pc-данные тоже могут врать… пусть будет.") Honest low-yield is fine (RULE 11) — but coverage must be total.

### RULE 25 — THE FULL CARD: both pairs of eyes see the same thing, and it is PROVEN, not promised (S6; rewritten S18) ⭐ THE S5 FIX
**The rule names a PROPERTY, not a script (RULE 0b):** *whoever reads Stage-2 — founder or agent — sees the WHOLE card.*
The card = every store · all 3 tops · the **28 contract fields** (the canonical list lives in ONE place, `FIELDS_RENDERED`,
byte-identical in both renderers). Nothing truncated, nothing quietly dropped. Two surfaces render it, one per pair of eyes:
- **`scripts/sl_stage2_table.py` → HTML, the FOUNDER surface** (grouped-11, Marina-locked; images, clickable). Goes to Desktop.
- **`scripts/sl_project_any.py` → text, the AGENT surface** (same fields; 250 cards fit a context window — 250 HTML cards do not).

**PARITY IS MANDATORY, EVERY BATCH: `python3 scripts/sl_card_parity.py <enriched.json>` → ✅ PARITY PASS before any analysis.**
It runs both renderers and compares their `CERT` lines — stores · products · banner-heroes · the field list. **Divergence = STOP:
it means one of us is judging on less than the other.** (Verified S18: blinding the agent to `home_hero` makes it STOP — the check
can fail, not just go green.) Never build an ad-hoc / `/tmp` / partial reader — a hand-made reader showing 1 product of 3 zeroed S5.

Each renderer **self-certifies exactly ONE thing: that the READING is complete** (`FULL CARD RENDERED — PASS: N/N products`).
**The DATA verdict is NOT theirs** — it belongs to `sl_qa.py` / `sl_accept_chunk.py` (RULE 26). Previews as HTML, never PNG (Marina S6).

> **S18 — what actually happened, kept here so we never re-learn it (the "слово ≠ дело" class, RULE 0b).**
> The old rule named ONE reader (the HTML). But 250 HTML cards do not fit a context window, so every analysis session actually read
> through a text projector — a script that **lived only on the VPS, outside git** (born 2026-06-07, six days *after* the enricher
> started emitting `home_hero`) and was itself **partial**: no `home_hero` (the homepage-banner product v4.2 added *because* the
> best-seller auto-pick misfires — swaddlean/dingle), `desc` cut to 58 chars, no `bullets` / `desc_confidence` / `pust` / `kind` /
> unreachable-reason. **For ~27 batches the agent judged on less than the founder saw.** The HTML was not innocent either: it rendered
> neither `pust` nor `kind` — both direct Marina-Veto inputs. **Neither surface was complete, and nothing ever compared them.**
> **Why it survived so long:** (a) the rule froze a TOOL, so the substitute fell outside it; (b) the substitute was named `..._tmp.py` —
> nobody reviews a throwaway; (c) it never entered git, so no audit, no backup, no diff; (d) the acceptance ritual demanded the agent
> say aloud *"full card — 3 tops **+ images** + all fields"* while its surface had **no images at all** — an unverifiable sentence,
> recited every batch; (e) **absence of a field has no symptom** — the output looked complete.
> Second half of the same bug: the HTML banner re-checked `sl_qa`'s thresholds, so on ONE file `sl_accept_chunk` said ACCEPT (benign
> `products.json` dip) while the banner said STOP. A gate you must choose between is not a gate. Now: **one verdict, one owner.**
> **Fixed S18:** both renderers in git, both print the full 28-field contract, both self-certify, and `sl_card_parity.py` proves each
> batch that the two surfaces are the same card. The property is now checked by a machine instead of promised by a sentence.

### RULE 26 — QA-gate PASS + acceptance statement BEFORE any analysis (S6, Marina-approved 2026-06-03)
Before scoring ANY batch: run **`scripts/sl_qa.py <enriched.json>`** (extended S6 to CARD COMPLETENESS — essence fields +
per-product image/in_range/descConf, not just reach/price/cur). It must print **✅ PASS**. If **⛔ STOP**, do NOT analyse — report the
flags and re-enrich. Then state in the human-visible checkpoint, **verbatim**: *"Loaded Stage-2 enriched file, not Stage-1; full card
(3 tops + images + all fields) — QA PASS."* **Two-layer logic:** `sl_qa.py` certifies DATA completeness (scraper output); the canonical
readers' self-cert line (RULE 25) certifies READING completeness — together they close both S5 holes (the gate alone would have
PASSED S5, since the data was fine; the reader was not). **PASS thresholds = PROVISIONAL (revisit after b10; failure direction is safe —
a false STOP only forces a look):** reach≥90 · ≥1top≥97 · prod_img≥90 · in_range≥99 · descConf≥99 · avgtops≥2.0 ·
store_type/product_class/cat_flag/maturity/new30d≥95 · home_pitch≥90 · price≥95 · cur_null=0. Informational (non-gating): 3tops% ·
social% · home_img/banner% (these legitimately vary). Pairs with RULE 1 (funnel transparency) + RULE 23 (open every needs_live).

**⭐ ONE VERDICT, ONE OWNER (S18 — the two-layer logic above, now enforced in code, not just prose):**
- **DATA** (is the scraper's output complete/healthy?) → `sl_qa.py`, and for a build chunk the wrapper `sl_accept_chunk.py`,
  which alone knows the ACCEPT-logic (a benign `products.json`/vNone dip = ACCEPT; genuine breakage = STOP).
- **READING** (does the surface show me the whole card?) → the two RULE-25 generators' `FULL CARD RENDERED` line.
- **The readers no longer re-check data thresholds.** They used to, with a third copy of the numbers — so on the same file the
  wrapper said ACCEPT and the HTML banner said STOP (live case: T&H `s1_b4`, S18). Duplicate thresholds are how a gate starts lying.
  A number lives in exactly ONE script; every other place points at it.

### RULE 27 — Analysis self-verification gate: prove the steps ran, from files not memory (S6, Marina-approved 2026-06-03)
The analysis side must be machine-verified like Stage-2 is — not trusted to discipline (the ShopHunter lesson: system beats
discipline). As I analyse a batch I keep two artifacts, then a gate verifies them:
- **Open-log** `np_bN_opens.jsonl` — one line per hand-opened store `{domain, verdict}` (every needs_live + unreachable).
- **Scorecard** `np_bN_scores.jsonl` — one line per deep-scored candidate `{domain, hero, price, problem/wow/emotion/margin/market, veto, score, bucket}`.
- **`scripts/sl_analysis_gate.py <enriched> <opens.jsonl> <scores.jsonl>`** must print **✅ PASS** before the checkpoint. It STOPs if any
  flag was not opened (RULE 23 breach) or any device-class in-range candidate has no explicit verdict (the gap that caught the
  overlooked Quax store in S6). The ANALYSIS CHECKPOINT numbers are then COMPUTED by the gate, not typed from memory.
- **Known soft spot (named, not hidden):** `consumer-other` stores are card-judged in bulk, not individually logged — the gate counts
  them for transparency (RULE 1) but does not force a per-store verdict. This is the one place still resting on reading discipline.

### RULE 28 — Browse-pool = a fixed rule, and the gates are a FLOOR not a CEILING (S6, Marina-approved 2026-06-03)
**Fixed selection (so the count is reproducible, never picked by feel):** browse = (device-class `{consumer-gadget, appliance, kitchen}`
in-range stores) ∪ (stores I explicitly tag `browse` in the open-log), minus winners/borderline/reject and minus hand-opened-off-model,
deduped (RULE 8 unique). `decor` is excluded from the auto-set (it pulls mis-tagged decals/boards); a genuinely interesting non-device
store enters via my explicit browse-tag (so my judgment, logged, overrides the proxy class — e.g. spottle in S6).
> **⚠ AMENDED by RULE 32 (S13, Marina 2026-06-07) — read RULE 28 together with RULE 32.** The old wording "count varies / honest
> low-yield is fine / selection reproducible, never by feel" is now bounded by a **HARD FLOOR of 7 per batch**: the count still varies
> ABOVE 7, but never below it. When the deterministic set yields <7, the agent MUST add the next-most-interesting stores it read
> (judgment ADDS to the fixed set, never drops below 7) — **when unsure, INCLUDE; the tail is a priority.** `sl_analysis_gate.py` STOPs
> if browse<7. So RULE 28 = the deterministic CORE of the browse set; RULE 32 = raises the floor to 7 + biases toward inclusion.

> **⭐ FLOOR-NOT-CEILING PRINCIPLE (Marina, S6 — applies to ALL gates/rules here).** These checkpoints define the MINIMUM that must
> always be covered — never the maximum. The agent is ALWAYS free to surface more than the rule yields and MUST flag anything notable
> beyond it: an off-pattern outlier, a convergence/pattern, an emerging cross-category observation, a creative angle. A rule must
> never suppress judgment or silence a useful observation. If a frame starts to feel like it's hiding something worth showing, say so and
> we adjust it. (Marina's principle: over-constraining a worker kills the creativity and the heads-up flags you actually want.)

### RULE 29 — Auto-log opener (P1) + transient retry (P3) ADOPTED; P2 functional-noun sweep DROPPED (S7, Marina-approved 2026-06-03)
The RULE 23 hand-open step is now backed by a tool so completeness can't rest on memory (the S6 lesson: system beats discipline). Tested on b14+b15, Marina-locked:
- **P1 — `scripts/sl_open_flags.py <enriched.json> <out_opens.jsonl>` is the canonical opener.** It derives the FULL flag-list (needs_live + unreachable) AND the device-class-in-range set from the enriched file itself, opens each, and **writes a pre-seeded `opens.jsonl` with one line per store (`domain·status·title·prices·verdict:""`)**. The agent only fills `verdict`. "Opened but not logged" is now structurally impossible — the tool enforces RULE 23, not the agent's memory. (Root cause it fixes: b12 device-class gap, where 5 opened stores were un-logged and only `sl_analysis_gate.py` caught it.) The agent MAY still open extras by hand and append them.
- **P3 — transient retry is built into the opener:** a 503/timeout is retried once after a short pause, then (still failing) marked dead. Separates live-on-retry from genuinely-dead (proven b14: twinieshop 503→retry→dead; b15: 0 retries needed = correct). At scale this stops a transient blip from false-killing a real candidate.
- **P2 — functional-noun sweep over consumer-other: TESTED AND DROPPED (do NOT run it).** Across b12–b15 it never surfaced a winner the RULE-6 full-read hadn't already found, and on b14 its (un-widenable-in-advance) vocabulary would have **missed** the real winner (`babybond`, noun "gate"). **The real safety net for the consumer-other soft spot is the RULE-6 full read — a keyword sweep adds no coverage and risks false confidence.** Marina: "P2 не надо." (Script `sl_co_sweep.py` is not part of the workflow.)

### RULE 30 — Reservoir-build scraper: wait-pattern + one-chunk rhythm (S8, Marina-approved 2026-06-03)
When BUILDING the reservoir (running `sl_enrich4` LIVE to prep data for a later session — not analysing a ready file),
the work is **system-driven, never discipline-driven**. Three locked invariants:
- **Wait via background, never poll.** Launch the enrich detached (minimal one-line `nohup` + sentinel — RULE 4c), then
  wait for the sentinel through a **`run_in_background` Bash wait-loop** (`until [ -f <sentinel> ]; do sleep 15; done`).
  The harness re-invokes on completion = **ZERO context burned while waiting.** NEVER a foreground blocking poll loop
  (that burns context for nothing — the exact S8 lesson that exposed this rule was missing). The scraper itself is 0-token.
- **Progress-narration rhythm (Marina S8 — refines "one chunk at a time"; her preferred S4 pattern):**
  **Chunk-1 = full SCRAPER-ACCEPTANCE CHECK-LIST → STOP, WAIT for Marina's OK** (proves the run is healthy for this niche/
  session). **After her OK, chunks 2..N run AUTONOMOUSLY — NO per-chunk approval.** After EACH chunk post the progress report
  **as PLAIN TEXT in chat — never inside a code-block (Marina S17)**, human-readable, in this shape:
  `✅ Chunk N/M — <ниша> — ПРИНЯТ` → `250 магазинов · сайты открылись у X% · счёт сошёлся (250 = 250) · качество данных: чисто · охранник (claude/скрапер): 0/0`
  → `▶️ Chunk N+1/M — запускаю энрич (250 магазинов, ~7 мин)… идёт`.
  (Галочка + что сделано + цифры человеческим языком + что запускаю дальше. Старый машинный one-liner
  `k/N done · <verdict>` РЕТАЙРЕН — Marina S17: нечитаемо.) So Marina sees it's flowing without
  pressing buttons. **Consolidated wave report at the end → STOP for OK.** Each chunk is still individually QA'd + count-
  reconciled by the agent (so a failure is caught) — **STOP and surface IMMEDIATELY only on GENUINE breakage** (reach
  out-of-band / worker-crash / count-mismatch / cur_null>0 — NOT a products.json STOP). This beats a silent server-side
  loop (Marina's S4 worry: "вдруг что-то слетело") AND beats per-chunk approval (button-fatigue): narrated, verified,
  hands-off. **NEVER fully fire-and-forget a multi-chunk server loop with no per-chunk check** — narrate + verify each.
- **Batched-reporting tier (Marina S8 — when she explicitly asks NOT to be pinged per batch / not to sit by the computer):**
  run a **self-verifying server loop** (`cats_wave.py`-style: per chunk select → enrich → `sl_qa` → append the health
  manifest, and **ABORT on GENUINE breakage** = reach <85% / count ≠ 250 / cur_null>0, writing a BREAK flag). Report only
  **every ~6 chunks** (or immediately if it aborts). What keeps this SAFE (vs blind fire-and-forget): the loop still
  QA-gates EVERY chunk and stops itself on real breakage — only the per-chunk *messaging* is removed, never the per-chunk
  *verification*. Use ONLY on Marina's explicit ask; default stays chunk-1-OK + narration.
  (Parallel SECOND session only after the rhythm here is proven — RULE 13 still bars parallel `claude`; parallelism =
  enrich workers, capped at the proven total on the single ISP-Dedicated IP.)
- **Selection = `sl_select_build.py` (enriched_index exclusion, NO SKIP) — S11 decoupled, Marina-approved.** Build selects the
  next 250 excluding `processed` ∪ `logs/storeleads/enriched_index.json`; mark each built chunk with `sl_mark_enriched.py`.
  This **RETIRES the old SKIP-paging** (`SKIP=(N-1)*250`): SKIP shifts the page when `processed` grows mid-build, so a parallel
  analysis session marking the SAME niche would cause a coverage gap. With enriched_index exclusion that is a **no-op** (a
  processed store is already excluded as enriched) → **parallel analysis of the SAME niche being built is SAFE**
  (S11-PROVEN: `processed` grew 11,219 → 17,854 mid-build via parallel S12/S13b, the build page never shifted). `enriched ≠
  processed` stays the invariant (build marks enriched; only analysis marks processed). Guardrail unchanged: both `claude`
  run on the Mac, **never on the VPS** (RULE 13). *(Legacy `sl_select_all.py`+SKIP kept only as the positional selector for
  non-decoupled use; not for parallel build.)*
- **Per-chunk acceptance = `scripts/sl_accept_chunk.py <enriched.json>` (S11, Marina-approved 2026-06-07).** One verdict
  line = count-reconcile + credit-guard (`ps aux | grep claude`, EVERY chunk) + canonical `sl_qa.py` + encoded ACCEPT-logic
  (benign products.json STOP → ACCEPT; genuine breakage → STOP). System, not discipline.
- **⭐ WAVE = 1 + 9 = 10 chunks (Marina S18; was 7).** Chunk-1 → full SCRAPER-ACCEPTANCE check-list → **STOP, wait for OK**
  (proves the niche/run is healthy). Then **9 chunks run without stopping between them** — each still machine-accepted by
  `sl_accept_chunk.py` and narrated (RULE 30 report format). At the end of the wave: consolidated report → **STOP for OK.**
  **Never auto-chain waves.** Mid-wave STOP only on GENUINE breakage (the wrapper prints STOP) — then come to Marina at once.
  *Why the length is safe: safety rests on the per-chunk machine check, not on the wave being short — the wrapper is as awake
  at chunk 9 as at chunk 2. There is no unattended server loop; the agent launches each chunk, it just doesn't ask permission.*
- **⭐ HTML cadence — ONE rule, both modes (Marina S18): first · every 5th · last** (so 1, 5, 10 in a wave of ten). Canonical
  HTML (`sl_stage2_table.py`) → Marina's Desktop. Anything else on request. *(Was: "last chunk of each wave" in build vs
  "batch-1 + every 4th" in analysis — two answers to one question, in two files.)*

### RULE 31 — Checkpoint contract: the report is GATE-GUARDED, never shrinkable (S13, Marina-approved 2026-06-07) ⭐ THE b3/b4 FIX
The checkpoint REPORT was the ONE step with no machine gate → so when "stop-after-each-batch" was lifted, it silently
shrank (b3/b4). Fix = give the report the same "external controller" every other step has. **`sl_analysis_gate.py` IS that
controller** — it self-STOPs the analysis until (a) every flag opened, (b) every device candidate verdicted, (c) browse ≥
floor (RULE 32). The agent **cannot proceed to the next batch** without a PASS. **The checkpoint is valid ONLY if it (1)
contains EVERY section — winners / borderline / browse / funnel+ABC / loss-audit, each with the plain-language 1–2-line
description Marina reads instead of opening the site — AND (2) pastes the gate's PASS line.** A report missing any section
= not canonical = STOP (same logic as RULE 25's banner / RULE 26's QA-PASS). **Принцип (Marina): "проверяющий", не
"делающий".** The gate never WRITES the report (a doer can err + removes the agent's final-look quality pass — same reason
the sub-agent-reader was rejected, [[feedback_no_delegation]]); it only COUNTS already-verified artifacts (opens.jsonl =
one tool-seeded line per flag — the count can't be faked; scores.jsonl = the agent's own scores) and BLOCKS on a gap.
**Tamper-evidence (how Marina knows a step wasn't skipped, without taking the agent's word):** every step leaves a file;
**Marina can re-run the gate on the same files and get identical numbers.** The honest limit: a script can't physically
block a chat message, but it makes any skip *visible + re-verifiable* — that is what turns "на дисциплине" into "на системе".
**Anti-forgetting anchor (S13):** `sl_analysis_gate.py` prints a **REQUIRED-SECTIONS checklist** at the end of EVERY run
(winners · borderline · browse≥7 · funnel+ABC · loss-audit · 1–2-line description per candidate · paste-the-PASS-line) —
the controller hands the agent the contract at the exact moment of writing, so a section can't be silently dropped under
speed (the b3/b4 failure-mode). It's a reminder, not a hard block (R1 stays tamper-evident) — but it lands where the slip happens.
**⭐ AMENDMENT (S13b, 2026-06-07, Marina-approved — the b12/b13 re-drift fix):** the anchor *re-drifted* exactly once: in an autonomous block the agent ran the gate with a **truncated output** (`sed -n '3,13p'`) → the PASS line was seen but the REQUIRED-SECTIONS checklist (printed last) was cut, and the b12/b13 checkpoints shrank to one-liners — the SAME failure RULE 31 exists to prevent, re-entered via truncation. **Fix (system, not discipline): `sl_analysis_gate.py` reordered so the contract block prints ABOVE the verdict and the `GATE:` line is the LAST line, carrying the section counts (`W·BL·BR/floor·flags·dev·read`) + "[paste THIS line + the CONTRACT above]".** Now the RULE-31-required "paste the PASS line" cannot be satisfied without the contract immediately above it — truncating the tail loses the PASS line itself. **Standing discipline:** run the gate and read/paste its output from the CONTRACT block through the GATE line — **never `sed`/`tail`-truncate the gate's tail.** (Lesson: a soft controller that prints at the end is defeated by output-truncation; co-locate the must-paste token with the contract so they live or die together.)

### RULE 32 — Browse-pool FLOOR = 7 per batch; no ceiling; when unsure INCLUDE (S13, Marina-approved 2026-06-07)
Browse = **Marina's window into the niche** (она быстро открывает и видит "пусто/не пусто", какие товары вообще водятся).
So **minimum 7 browse links EVERY batch — even deep in the tail, even if weak** (1–2 links is unacceptable). **7 is a FLOOR,
NOT a target/cap.** When the flow is rich, surface 10 / 15 / 20+ — no upper limit. **Bias = INCLUDE: if unsure whether a
store is worth showing, show it** ("лучше скинь, я посмотрю"). **The tail is a priority, not a remainder** — Marina has
repeatedly found real products in the tail on other niches (Dogs/pets happen to be saturated; that's niche-specific, not a
reason to thin browse). Mechanics: while doing the RULE-6 full read, tag EVERY store that catches the eye (novel mechanism,
unusual category, "а вдруг") as browse — `bucket:"browse"` in scores.jsonl OR `verdict` containing "browse" in opens.jsonl;
my explicit tag overrides the proxy class/off-model exclusion. **Machine-enforced:** `sl_analysis_gate.py` STOPs if browse < 7
(BROWSE_FLOOR). This supersedes the "count varies, never padded" wording of RULE 28 — the count still varies ABOVE 7, but 7
is the hard floor. (Note: RULE 12/founder-feedback still hold — browse is exposure for Marina's eye, not a quality claim.)

### RULE 33 — ANALYSIS batch rhythm: escalating autonomy 1→1→4, ~6 batches/session (S13, Marina-approved 2026-06-07)
The ANALYSIS-mode analog of RULE 30's RESERVOIR-BUILD wave-rhythm. Distributes Marina's time AND context, on system not
discipline (each batch still gate-PASSes identically whether or not she says "stop"):
- **Batch 1** → full (contract-complete) checkpoint → **STOP, wait for Marina's OK** (proves niche/run healthy this session).
- **Batch 2** → full checkpoint → **STOP, wait for OK** (confirms stable). *(If batch-1 already clearly clean, Marina may
  green-light going straight to the block — her call.)*
- Both clean → **batches 3–6 run as ONE autonomous block**, a **full contract-complete checkpoint EVERY batch** (no shrinking —
  RULE 31), **no stop between** — UNLESS a **winner 65+** surfaces (pause before Notion) or **genuine breakage** (gate STOP).
- **End of block** → consolidated (also contract-complete) report → **STOP for Marina's feedback** → then Notion writes for
  the whole block → commit/push → compact → repeat.
- **Session depth ≈ 6 batches** (context-proven: 5 leaves room, 6 is the sweet spot). "No stop" NEVER means "less report".

## Checkpoint shape (every batch, before any Notion write)
Winners (65+) · Borderline (55–64, flag for founder call) · Watchlist-signal · Browse-pool (**FLOOR 7, no ceiling —
RULE 32; when unsure INCLUDE; tail is a priority, never padded-down**) · Patterns · the full funnel breakdown
(RULE 1) **including the explicit A/B/C tier counts** (Marina cross-checks against the ABC split). Every link = a
clickable markdown hyperlink. **The report is contract-complete + carries the gate PASS line (RULE 31).** Then **STOP and
wait for Marina's OK before writing to Notion** (within an approved block, batches 3–6 do NOT stop per-batch — RULE 33 —
but STILL post the full checkpoint; only a winner 65+ or breakage pauses the block).
