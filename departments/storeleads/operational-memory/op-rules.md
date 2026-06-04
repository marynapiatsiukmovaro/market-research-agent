# OPERATIONAL RULES — PERMANENT (Store Leads)

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

### RULE 25 — Canonical Stage-2 reader ONLY; ad-hoc/partial readers forbidden (S6, Marina-approved 2026-06-03) ⭐ THE S5 FIX
Stage-2 enriched data is read for analysis **ONLY** via the canonical generator **`scripts/sl_stage2_table.py`** (rebuilt S6 →
**grouped-11 layout, Marina-locked**, full v4.2 contract incl. the 4 fields the old table dropped: `store_type · product_class ·
new_products_30d · cat_flag`). **Never build an ad-hoc / `/tmp` / partial reader** — that is exactly what zeroed S5 (a hand-made
reader showed 1 product of 3, no images → invalid "0 winners"). The canonical output **self-certifies**: its page header carries a
`STAGE-2 ACCEPTANCE` banner (auto-computed completeness + PASS/STOP). **A Stage-2 table WITHOUT that banner is NOT canonical → STOP.**
Deliver previews as **HTML, not PNG** (Marina S6). *(Root cause: S5 had no single canonical reader, so an ad-hoc one silently truncated.)*

### RULE 26 — QA-gate PASS + acceptance statement BEFORE any analysis (S6, Marina-approved 2026-06-03)
Before scoring ANY batch: run **`scripts/sl_qa.py <enriched.json>`** (extended S6 to CARD COMPLETENESS — essence fields +
per-product image/in_range/descConf, not just reach/price/cur). It must print **✅ PASS**. If **⛔ STOP**, do NOT analyse — report the
flags and re-enrich. Then state in the human-visible checkpoint, **verbatim**: *"Loaded Stage-2 enriched file, not Stage-1; full card
(3 tops + images + all fields) — QA PASS."* **Two-layer logic:** `sl_qa.py` certifies DATA completeness (scraper output); the canonical
reader's self-cert banner (RULE 25) certifies READING completeness — together they close both S5 holes (the gate alone would have
PASSED S5, since the data was fine; the reader was not). **PASS thresholds = PROVISIONAL (revisit after b10; failure direction is safe —
a false STOP only forces a look):** reach≥90 · ≥1top≥97 · prod_img≥90 · in_range≥99 · descConf≥99 · avgtops≥2.0 ·
store_type/product_class/cat_flag/maturity/new30d≥95 · home_pitch≥90 · price≥95 · cur_null=0. Informational (non-gating): 3tops% ·
social% · home_img/banner% (these legitimately vary). Pairs with RULE 1 (funnel transparency) + RULE 23 (open every needs_live).

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
deduped (RULE 8 unique). The COUNT varies by niche (honest low-yield is fine, RULE 11); the RULE is fixed. `decor` is excluded from the
auto-set (it pulls mis-tagged decals/boards); a genuinely interesting non-device store enters only via my explicit browse-tag (so my
judgment, logged, overrides the proxy class — e.g. spottle in S6).

> **⭐ FLOOR-NOT-CEILING PRINCIPLE (Marina, S6 — applies to ALL gates/rules here).** These checkpoints define the MINIMUM that must
> always be covered — never the maximum. The agent is ALWAYS free to surface more than the rule yields and MUST flag anything notable
> beyond it: an off-pattern outlier, a convergence/pattern, a "this niche looks weak — consider a pivot," a creative angle. A rule must
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
  session). **After her OK, chunks 2..N run AUTONOMOUSLY — NO per-chunk approval.** After EACH chunk post a **one-line
  progress narration** (`"k/N done · reach X% · QA ok / STOP-note · launching next"`) so Marina sees it's flowing without
  pressing buttons. **Consolidated report every ~5 chunks + at the end.** Each chunk is still individually QA'd + count-
  reconciled by the agent (so a failure is caught) — **STOP and surface IMMEDIATELY only on GENUINE breakage** (reach
  out-of-band / worker-crash / count-mismatch / cur_null>0 — NOT a products.json STOP). This beats a silent server-side
  loop (Marina's S4 worry: "вдруг что-то слетело") AND beats per-chunk approval (button-fatigue): narrated, verified,
  hands-off. **NEVER fully fire-and-forget a multi-chunk server loop with no per-chunk check** — narrate + verify each.
  (Parallel SECOND session only after the rhythm here is proven — RULE 13 still bars parallel `claude`; parallelism =
  enrich workers, capped at the proven total on the single ISP-Dedicated IP.)
- **SKIP advances per chunk** (chunk N → `SKIP=(N-1)*250`), because reservoir build does **NOT** mark processed
  (`enriched ≠ processed`; marking happens only at analysis). Same-niche chunks never overlap as long as SKIP advances.

## Checkpoint shape (every batch, before any Notion write)
Winners (65+) · Borderline (55–64, flag for founder call) · Watchlist-signal · Browse-pool (**by the deterministic
RULE 28 rule — count varies by niche, selection fixed; never padded "чтобы было"**) · Patterns · the full funnel breakdown
(RULE 1) **including the explicit A/B/C tier counts** (Marina cross-checks against the ABC split). Every link = a
clickable markdown hyperlink. Then **STOP and wait for Marina's OK before writing to Notion.**
