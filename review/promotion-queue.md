# PROPOSED CORE UPDATES

**Marina reviews this file and decides. Agent only adds items — never promotes automatically.**

Items here are candidates for promotion into core documents.
They come from departments/facebook-ads-library/operational-memory/learnings.md when a pattern is confirmed across multiple sessions.

Agent may APPEND new items. Agent must NEVER self-promote items into core files.
Marina sets each item to: **Promote → Wait → Reject**

---

## Pending Review

### QA reach/cand threshold too strict for the vNone (missing-visits) segment — Store Leads S8
**Observation (n=11 chunks, the full Nursery vNone tail = 2621 stores, `np_s8_health_manifest.jsonl`):** the deep vNone tail structurally runs **reach ~89–95% / cand ~88–94%**, so `sl_qa.py` numeric-STOPs on **8 of 11 chunks** — purely from a higher share of **`products.json`-disabled micro-stores** (storefront ALIVE, robot can't extract → flagged needs_live → hand-opened at analysis). The reachable cards are perfect every time (img/in_range/descConf ~100%, cur_null=0, 0 worker crashes). The STOP here forces a look but the data is sound — it is the provisional-threshold (95, RULE 26) being unrealistic for a segment whose natural reach ceiling is ~94–97%.
**Proposal:** add a **vNone/missing-visits segment threshold** to `sl_qa.py` (or a flag) — e.g. for visits-missing batches treat **reach ≥ ~90 + products.json-pattern** as PASS-with-note (cand/product_class/new30d allowed to track reach down to ~88), keeping the STOP for genuine breakage (reach OUT of band / global degradation / count mismatch / cur_null>0). Visits-bearing batches keep the current 95.
**Why it matters:** otherwise the whole vNone deep tail reads as "STOP" by default → noise that erodes the gate's signal (an alarm that always fires is ignored). RULE 26 explicitly flagged the thresholds as PROVISIONAL/revisable.
**⚠ Guardrail:** the products.json-off stores are NOT skipped — they become needs_live hand-opens at analysis (RULE 23). The relaxation is only about the numeric gate label, never about coverage.
**Affected:** `scripts/sl_qa.py` (segment-aware thresholds); workflow §1b ACCEPT-logic note; RULE 26 thresholds.
**Confidence:** High (n=11, one full niche tail; the pattern is the documented S1/S2/S8 products.json cause).
**Recommendation:** Promote (small, segment-scoped; failure direction stays safe).
**Added:** 2026-06-04, Session S8. **Source learnings:** S8 HANDOFF.

### Decouple enrichment from analysis — "enrichment reservoir" architecture (Store Leads, Marina S4)
**Observation:** Current Store Leads sessions are SERIAL — send scraper → wait 7–22 min → check → analyze → send next → wait again. The wait blocks the whole session. Enrichment (Playwright scraper) costs ~0 tokens; analysis (read-all + open-needs_live + score) is the token/context-bound part.
**Proposal (Marina's idea):** split into two independent contours. **Contour A — Enrichment:** a loop (`sl_enrich_loop.py`-style) that repeatedly select_all→enrich4→mark `enriched`→next 250, unattended on the VPS, building a persistent "reservoir" of ready candidate-sheets for a whole niche (or several). **Contour B — Analysis:** a session pulls READY enriched chunks from the reservoir and goes straight to deep-score→checkpoint→Notion, never waiting on the scraper. Enables 2–4k stores/analysis-session and parallel enrichment across niches.
**Why it matters:** removes wall-clock wait (NOT a token win — Marina noted this correctly; enrichment is already ~0 tokens). The throughput unlock toward Marina's scale goal (4k/session × N sessions).
**⚠ Critical guardrails (must be in the build, or quality breaks):**
  1. **`enriched` ≠ `processed` — TWO separate states.** The enrichment loop marks a store `enriched` (card filled); ONLY the analysis agent marks `processed` (analyzed+checkpointed+Notion). If the loop marked `processed`, analysis would skip the store = **winner loss.** Keep `processed_domains.json` for analyzed; add a separate `enriched_index`.
  2. **Parallelize SCRAPERS, never `claude` (RULE 13).** "4 parallel sessions" is safe ONLY if it means 4 parallel enrichment loops (no claude) on different niches; parallel claude-analysis = the month-budget-burn risk. Hard boundary.
  3. **Staleness handled by RULE 7** (finalist live-confirm at analysis time re-checks price/hero) — so a reservoir card aging a few days is fine.
  4. Keep 250-chunks + per-chunk sentinels + per-store try/except (already in v4.2) — a bad store/chunk never breaks the run. **+ a brief inter-chunk COOLDOWN (e.g. 30–60s, proxy/session rest) between consecutive 250-chunks (Marina S4).** NEVER run 500-at-once and NEVER double the worker count — 16 simultaneous Playwright workers = too much / breakage risk. The unit stays 250 × 8 workers, sequential, with pauses. (S4 chained b7→b8 ran back-to-back with NO pause and quality held — but the cooldown is the safe pattern for unattended scale.)
  5. **Auto QA-gate per enriched chunk (Marina S4 — "scraper убеждается что всё чётко").** After each chunk, compute the quality metrics and FLAG the chunk for re-run if any falls outside the healthy band: `reach<90%` · `cand%<95%` · `price%<95%` · `cur_null>0` · `empty_tops_reach>5%` · `avgtops<2`. 0-token, automatic; a flagged chunk is re-enriched before it enters the analysis reservoir. **Baseline (S4, 6 batches incl. the chained b7/b8 — proven zero degradation):** reach 232–248 · cand 98–100% · price 97–99% · desc 90–95% · pitch 87–99% · tops3 98–100% · avgtops 2.64–2.85 · cur_null 0 everywhere. b7/b8 (chained/back-to-back, sequential) were statistically identical to single-batch runs → sequential chaining is safe.
**Affected:** new `scripts/sl_enrich_loop.py` + state-file design; `departments/storeleads/methods/discovery-funnel.md` (two-contour flow); `op-rules.md` (RULE 13 parallelism boundary restated for the loop).
**Confidence:** High (architecture sound; validated by this session's serial-wait pain + ~0-token enrichment cost).
**Recommendation:** Promote (build in a dedicated SYSTEM-BUILD session, not a scout session).
**Added:** 2026-06-01, Session S4. **Source learnings:** S4 HANDOFF.

### Trust the rich card for unambiguous off-model `needs_live` (reduce hand-open at scale) — Store Leads S4
**Observation:** RULE 23 = open EVERY `needs_live`+unreachable by hand. S4 evidence (1000 stores): in the established/apparel/formula bands, ~all flags resolve to unambiguous off-model (formula=ingestible, apparel-brands, literal-non-baby like plant-shops/groceries). Hand-opened 36/36 in b3 → all off-model; 4× measured 0-loss audits. The hand-open of these adds ~0 loss-reduction but is the main throughput bottleneck.
**Proposal:** keep mandatory hand-open for `product_class ∈ {consumer-gadget, consumer-other, decor}` + price-edge + unreachable + banner-hero≠pick; ALLOW card-judgment (no hand-open) for `kind ∈ {ingestible, apparel}` + literal-non-baby identity, with a logged sample audit each batch to keep the classifier honest. Pairs with the decouple proposal to actually hit 4k/session without quality loss.
**Why it matters:** the only analysis-cost lever that doesn't touch the quality gates on the products that could actually BE winners.
**⚠ Risk:** must keep a per-batch random loss-audit of the card-judged off-model pile (don't let the classifier drift silently). This is a CHANGE to RULE 23 → Marina-approval required (RULE 23 was Marina-locked S3).
**Affected:** `op-rules.md` RULE 23.
**Confidence:** Medium-High (36/36 + 4× 0-loss this session — but one niche).
**Recommendation:** Wait (gather 1–2 more niches of 0-loss evidence before relaxing a Marina-locked rule).
**Added:** 2026-06-01, Session S4.

### Stage-0 coverage hole — `category=None` + Store Leads taxonomy mis-tagging (the one residual loss-risk)
**Observation:** The verification funnel (Stage 1→3) is empirically ~0-loss (S4, 4× measured + caught 2 deep-tail winners old method would lose). The remaining loss-risk is UPSTREAM at the dump: ~400k/2.85M active Shopify have NO category, and Store Leads' category tags are imperfect (S4 saw trophies/period-pads/ultrasound-service mis-tagged INTO Nursery → the same error tags real Nursery stores OUT, making them invisible to a category-filtered dump).
**Proposal (Marina to design later — her loss-idea):** a complementary discovery path that doesn't rely on category (e.g. app-install / keyword / cross-niche sweep), OR accept+document the boundary ("we never claim full-universe coverage; category-filtered = a known subset"). Also: when moving to a new H&G sub-niche, report the cross-niche overlap count (already free — `sl_select_all` prints `already-processed`).
**Why it matters:** it's the ONLY place a real winner can still be lost — not because verification misses it, but because it never enters the funnel.
**Affected:** `methods/discovery-funnel.md` (data-trust map already notes the None blind spot — elevate it), Stage-0 design.
**Confidence:** High (documented blind spot + S4 mis-tag evidence).
**Recommendation:** Wait (Marina will design; capture now so it's not lost).
**Added:** 2026-06-01, Session S4.

### QA-gate hardening — price sanity-clamp + dead-store-rate metric (Store Leads S5)
**Observation:** Two reservoir-quality issues surfaced while analysing the pre-enriched b9/b10:
  (1) **Price-parse anomaly** — `keep-closer.com` (b9) carried hero price `1184000.0 USD` for a toddler hip carrier whose real/avg price ≈ $155. A broken variant/currency parse can mis-tier or mis-display a store (not a loss — RULE 6 reads all + RULE 7 live-confirms finalists — but a "ready" reservoir should be clean before it reaches the agent).
  (2) **Dead/suspended витрины rise in the deep tail** — b10 (visits 47–77) had 9 unreachable incl. HTTP 402 Payment Required (coziekids, trendoasis) and 500 (storkofstamford) = Shopify stores suspended/dormant. Correctly caught as unreachable (0 loss), but the agent only learns the dead-rate AFTER opening them.
**Proposal:** extend the per-chunk auto QA-gate (`sl_qa.py`, the proposal-#1 prototype) with two more checks, computed at enrichment time (0-token):
  - **Price sanity-clamp:** flag any hero `price` that converts to >$1000 while the store `avg_price` <$200 → set `PRICE-CHECK` (re-parse), same as the existing price-unknown path.
  - **Dead-store-rate metric:** report `unreachable% + HTTP-402/500 count` per chunk so reservoir quality is visible BEFORE analysis (and a chunk with an abnormal dead-rate can be re-pulled).
**Why it matters:** keeps the reservoir "ideal" before it reaches the agent (Marina S5: "подготовка должна быть идеальной"); makes deep-tail dead-rate a measured signal rather than a surprise.
**⚠ Note:** purely additive to `sl_qa.py` — do NOT change scripts mid-run; build with the proposal-#1 reservoir/QA work in a SYSTEM-BUILD session.
**Affected:** `scripts/sl_qa.py` (+ the reservoir-prep QA-gate in proposal #1).
**Confidence:** High (both observed live in b9/b10).
**Recommendation:** Promote (fold into the proposal-#1 reservoir build).
**Added:** 2026-06-02, Session S5. **Source learnings:** S5 b9/b10 loss-audit.

### ✅ PROMOTED (S6, Marina-OK 2026-06-03 → implemented in op-rules RULE 25+26, workflow.md, method docs) — Stage-2 ACCEPTANCE discipline — canonical-reader-only + mandatory QA-gate before analysis (Store Leads S6) ⭐ THE S5 FIX
**Observation:** S5 zeroed not because of the scraper (b9 re-enrich this session = byte-for-structure identical to the reservoir; full contract intact, composition 250/250) but because the agent analysed from an **ad-hoc `/tmp` reader that showed 1 product of 3, no images**, and from an "эталон" table (`sl_stage2_table.py`) that itself dropped 4 collected fields (`store_type·product_class·new_products_30d·cat_flag`). Two structural holes: (1) no single canonical Stage-2 reader → an ad-hoc reader can silently truncate; (2) no completeness check forces the agent to confirm it sees the FULL card before scoring.
**Proposal — two NEW op-rules (Tier-2, Marina to approve before I write them into `op-rules.md`):**
  - **RULE 25 — Canonical Stage-2 reader ONLY.** Stage-2 is read for analysis ONLY via `scripts/sl_stage2_table.py` (rebuilt S6 → **grouped-11 layout, Marina-locked**, full v4.2 contract incl. the 4 dropped fields). Ad-hoc / partial readers are forbidden. The canonical output **self-certifies**: it embeds a `STAGE-2 ACCEPTANCE` banner in the page header (auto completeness + PASS/STOP). A Stage-2 table WITHOUT that banner is not canonical → STOP. (The 3 `/tmp` S5 readers were retired to `.RETIRED-S5` this session.)
  - **RULE 26 — QA-gate + acceptance statement BEFORE any analysis.** Before scoring any batch: run `scripts/sl_qa.py <enriched.json>` (extended S6 to card-completeness) → must print **✅ PASS**; if **⛔ STOP**, do NOT analyse — report and re-enrich. The agent then states in the human-visible checkpoint, verbatim: **"Loaded Stage-2 enriched file, not Stage-1; full card (3 tops + images + all fields) — QA PASS."**
**Two-layer logic:** `sl_qa.py` certifies DATA completeness (scraper output); the canonical generator + self-cert banner certify READING completeness. Together they close both S5 holes (the gate alone would have passed S5 — the data was fine; the reader was not).
**QA PASS thresholds (PROVISIONAL — Marina-OK'd S6, revisit after b10; failure direction is safe = a false STOP only forces a look):** reach≥90 · ≥1top≥97 · prod_img≥90 · in_range≥99 · descConf≥99 · avgtops≥2.0 · store_type/product_class/cat_flag/maturity/new30d≥95 · home_pitch≥90 · price≥95 · cur_null=0. Informational (not gating): 3tops% · social% · home_img/banner% (legitimately vary). b9 healthy reference: reach 98.8 · prod_img 99.2 · in_range 100 · avgtops 2.64 · essence 98–100.
**Onboarding (RULE 4-of-prescale-plan):** `workflow.md` gets a Stage-2 entry checklist = preflight (`ps aux|grep claude`) → enrich → **`sl_qa.py` PASS** → **canonical `sl_stage2_table.py`** → acceptance statement → analysis. Plus the Phase-4/5 checkpoint shapes (STAGE-2 ACCEPTANCE CHECKPOINT + ANALYSIS CHECKPOINT) and HTML-preview cadence (every batch-1 + every 4th; **HTML not PNG** — Marina S6).
**Affected:** `op-rules.md` (new RULE 25 + 26), `workflow.md` (Stage-2 entry checklist + 2 checkpoint shapes), `methods/subagent-spec.md` + `methods/discovery-funnel.md` (point Stage-2/3 at the canonical reader + gate), `methods/interface-guide.md` (sl_stage2_table = grouped-11 canonical + sl_qa extended + HTML delivery; /tmp readers retired). Implements & supersedes the card-completeness half of items #1(QA-gate) and #49 above.
**Confidence:** High (the fix is built + proven this session: QA PASS on healthy b9 + reverify; QA STOP on an S5-simulated truncated card caught avgtops/img/essence).
**Recommendation:** Promote (RULE 25 + 26 + grouped-11 lock). Thresholds: adopt provisional, confirm after b10.
**Added:** 2026-06-03, Session S6. **Source learnings:** S6 Phase-1 sverka + Phase-3 build.

---

## How to Add a New Item

Append to Pending Review using this format:

```
### [Short name]
**Observation:** what was consistently found across sessions
**Why it matters:** impact on product selection, scoring, or filtering
**Affected file(s):** which file would change (`core/` / `departments/{dept}/` / `shared/`)
**Confidence:** High / Medium / Low
**Recommendation:** Promote / Wait / Reject
**Added:** [YYYY-MM-DD], Session [N]
**Source learnings:** operational-memory/learnings.md entries [list dates]
```


---

## Decided

| Date | Item | Decision | Notes |
|------|------|----------|-------|
| 2026-05-17 | Output format — no product card in chat | ✅ Promoted | Implemented in core/identity.md — chat = Score + 1-2 lines + Recommendation only |
| 2026-05-17 | Pivot communication + round reporting | ✅ Promoted | Implemented in workflow.md STEP 1 — round announcement + pivot format added |
| 2026-05-17 | Keyword-First Discovery Algorithm | ✅ Promoted | Already in workflow.md STEP 1 + CLAUDE.md strategy — no additional change needed |
| 2026-05-17 | Pet vertical AOV ceiling $79→$120 | ✅ Promoted (expanded) | Resolved as universal rule: $100–170 = score normally with Margin cap 5/10. Updated mandatory-filters.md + scoring-system.md + op-rules.md RULE 12. Applies to ALL categories, not just Pet. |
| 2026-05-24 | RULE 7 — fast_filter.py technical pipeline | ✅ Promoted | Already implemented in op-rules.md RULE 7 (pipeline + script path + failure rule). Pending item was stale — synced during S30 cleanup audit. |
| 2026-06-03 | Stage-2 ACCEPTANCE discipline (canonical reader + QA-gate) — the S5 fix | ✅ Promoted | S6: op-rules RULE 25 (canonical `sl_stage2_table.py` grouped-11 + self-cert banner) + RULE 26 (`sl_qa.py` PASS + acceptance statement). Wired into workflow.md (Stage-2 entry checklist + 2 checkpoint shapes), subagent-spec, discovery-funnel, interface-guide. Thresholds PROVISIONAL → revisit after b10. |
| 2026-06-03 | Analysis self-verification gate + browse-pool rule + floor-not-ceiling | ✅ Promoted | S6: op-rules RULE 27 (`sl_analysis_gate.py` — open-log ⊇ flags + verdict per device candidate; numbers gate-computed) + RULE 28 (deterministic browse rule, count varies/selection fixed) + ⭐ FLOOR-NOT-CEILING principle (gates = minimum coverage, agent always surfaces notable/creative beyond them — Marina's anti-over-constraint). Built `sl_analysis_gate.py`; proven on b9 (caught overlooked Quax + calibrated browse v1→v2). Workflow.md gets the plain-language SESSION CHECKLIST (tick-off). Known soft spot logged: consumer-other bulk card-judged. |
| 2026-06-03 | Convergence as a SCORE input (S6) | 🔴 Rejected | Marina S6: a 250-store batch (or even the full ~6.7k niche) is NOT representative of the market → within-batch repetition can be a FALSE signal (similar stores may cluster in one batch by chance). Convergence stays a NOTED observation only (still fold true same-product duplicates into one Notion card); never weights a score or tier. Judge each product on its own merit. (workflow.md #4 updated accordingly.) |
| 2026-06-03 | S7 analysis-side tooling: P1 auto-log opener + P3 retry (ADOPT) / P2 functional-noun sweep (DROP) | ✅ Promoted (P1+P3) / 🔴 Rejected (P2) | S7 scale-validation, tested b14+b15, Marina-approved. **P1+P3 → op-rules RULE 29 + workflow §1a:** `scripts/sl_open_flags.py` is the canonical opener — seeds `opens.jsonl` with every needs_live+unreachable+device-class store (status·prices, 503-retry built in); agent only fills verdict → "opened-but-not-logged" structurally impossible (fixes b12 device gap). **P2 dropped:** across b12–b15 never found a winner the RULE-6 full-read missed, and on b14 its narrow vocab would have lost the real winner (babybond/"gate"); full-read is the real net, a sweep adds false confidence. Marina: "P2 не надо." |
