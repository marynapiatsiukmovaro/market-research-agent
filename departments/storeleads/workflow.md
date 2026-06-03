# Store Leads — Department Workflow (session entry point)

Thin entry point. The full procedure lives in `methods/`. Store-first discovery at scale via
storeleads.app. **SYSTEM-BUILD / in development — human-in-loop, NOT autonomous (not earned).**

> ✅ **STAGE-2 ACCEPTANCE PROTOCOL (S6, Marina-approved 2026-06-03) — the S5 fix is now LIVE.** Never analyse a batch
> until the Stage-2 ENTRY CHECKLIST below passes (RULE 25 canonical reader + RULE 26 QA-gate PASS + acceptance statement).
> The S5 failure (analysed an ad-hoc reader showing 1 product of 3) is now structurally blocked: `sl_qa.py` certifies the
> DATA, the canonical `sl_stage2_table.py` self-cert banner certifies the READING. Reservoir data is intact — do NOT re-pull.
> *(Background: `operational-memory/prescale-hardening-plan.md` = the S5 agenda; its Q1–Q5 were resolved in S6 — grouped-11
> layout locked, single canonical generator, QA-completeness gate, entry checklist, b9 end-to-end re-run + sverka done.)*

## 0. Before you start
- Confirm this is a **Store Leads** session. Operate only inside this department; never apply
  FB scraper or ShopHunter mechanics here, never read another department's operational memory.
- Load the ALWAYS files (core/ + shared/, incl. `shared/founder-taste.md`) + this department's
  operational memory in order: **`operational-memory/op-rules.md` (permanent rules — read FIRST)** →
  `founder-feedback.md` → `operational-memory/learnings.md` (read the **HANDOFF** block first).
- Current direction: `hypotheses/_active.md`.
- Verify session: `scripts/sl_check_login.py` (re-login via `sl_email_login.py` + emailed code if expired).
- Credit guard (Marina's rule): `ps aux | grep claude` on the VPS before any run; parallelism =
  Playwright **workers**, never parallel claude processes.

## 1. Run the discovery funnel
Follow `methods/discovery-funnel.md` (Stage 0 dump → Stage 1 client-filter+table → Stage 2 live
enrich → Stage 3 deep-score). Drive the API per `methods/interface-guide.md`. Heavy lifting on the
VPS; only finalists enter chat. **Stage 3 is the real filter — read ALL, confirm heroes on the live
site, run 100-pt + Marina Veto, lead with WOW/taste, never trust the proxy A/B/C tier.**
Supporting method docs:
- `methods/interface-guide.md` — the JSON API + cracked `bq` (filters, created≥2020, 25k-window bypass, fields).
- `methods/subagent-spec.md` — the Stage-2 enricher's exact job (fields, `desc` rule, what NOT to write, success test).
- `methods/shophunter-enrichment.md` — OPTIONAL cross-dept enrichment of finalists via ShopHunter (lookup ladder, SH fields).
- `reference/cross-dept-patterns.md` — patterns observed in SH/FB, not adopted yet (reference only).

## 1a. Stage-2 ENTRY CHECKLIST (RULE 25 + 26 — run BEFORE analysing every batch) ⭐ S6
Never start analysis until ALL pass, in order:
1. **Preflight** — `ps aux | grep claude` on the VPS (credit guard, RULE 13) · proxy health-check (RULE 14) · verify the
   enriched file exists for this batch.
2. **QA-gate** — `python3 scripts/sl_qa.py <enriched.json>` → must print **✅ PASS**. If **⛔ STOP**: do NOT analyse — report
   the flags, re-enrich the batch, re-gate. (Gate checks card completeness: 3 tops · images · in_range · descConf · the 5
   essence fields — not just reach/price.)
3. **Canonical reader ONLY** — render via `python3 scripts/sl_stage2_table.py <enriched.json> <out.html> "<title>" "<funnel>"`
   (grouped-11, self-certifying). **Never** an ad-hoc/`/tmp`/partial reader (RULE 25). Confirm the page header shows the green
   `STAGE-2 ACCEPTANCE: FULL CARD — PASS` banner.
4. **Acceptance statement** — state verbatim in the checkpoint: *"Loaded Stage-2 enriched file, not Stage-1; full card (3 tops
   + images + all fields) — QA PASS."*
5. **HTML preview to Desktop** — deliver the canonical HTML (NOT PNG — Marina S6) for **batch-1 of the session + every 4th
   batch** so Marina can spot-audit quality.

### STAGE-2 ACCEPTANCE CHECKPOINT (show Marina, batch-1 + every 4th)
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
- **`np_bN_opens.jsonl`** — one line per hand-opened store `{domain, verdict}` (every needs_live + unreachable).
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

### ✅ SESSION CHECKLIST — tick each step (plain-language; the gates verify the ticks aren't empty)
The mandatory steps per batch, in order. I mark each ☐→☑ as I go and report them; `sl_qa.py` + `sl_analysis_gate.py` are the
machine that confirms the work behind the ticks. **(Floor, not ceiling — RULE 28: I always surface anything notable beyond this list.)**
```
☐ 1. Preflight: VPS credit-guard (ps aux | grep claude) · proxy health · enriched file present
☐ 2. Stage-2 QA-gate: sl_qa.py → ✅ PASS  (else STOP, re-enrich)
☐ 3. Render canonical Stage-2 table (sl_stage2_table.py, grouped HTML) — green ACCEPTANCE banner present
☐ 4. State acceptance line: "Loaded Stage-2 enriched, not Stage-1; full card — QA PASS"
☐ 5. HTML preview to Desktop (batch-1 of session + every 4th batch)
☐ 6. Read ALL stores (no gut top-N, RULE 6)
☐ 7. Hand-open EVERY needs_live + unreachable → log each in opens.jsonl (RULE 23)
☐ 8. Live-confirm hero + price for every genuine candidate (RULE 7) → score → scores.jsonl
☐ 9. Analysis-gate: sl_analysis_gate.py → ✅ PASS  (else STOP, fill gaps)
☐ 10. Checkpoint to Marina (winners / borderline / browse / patterns / funnel) → WAIT for OK
☐ 11. After OK: Notion + reported-products + sl_mark_processed + keep-list + learnings/HANDOFF
```

## 2. Mode & checkpoints (STANDING)
- **Human-in-loop — NOT autonomous** (not earned). Work autonomously through dump→funnel→deep-score,
  then deliver the checkpoint and **WAIT for Marina's explicit OK before ANY Notion write.**
- Checkpoint = winners 65+ / borderline 55–64 / patterns / browse-pool (curated UNIQUE genuine-product
  links). Every link clickable. Convergence/revenue earns at most Watchlist, never auto-Consider.

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
