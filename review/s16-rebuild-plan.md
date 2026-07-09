# Store Leads — REBUILD PLAN + PROBLEM STATEMENT (set S16 2026-06-27)

> ✅ **STATUS (S18, 2026-07-09): Блоки 1–2 ВЫПОЛНЕНЫ и ПЕРЕПРОВЕРЕНЫ РУКАМИ.** Block 1 = data-acquisition + strategy (`f1f88ca`).
> Block 2 = scraper/enricher prep (`03c2eff`). **S18: прошёл Этапы 1–2 вживую на новом чанке T&H `s1_b4`** — оба работают;
> сломаны были только СЛОВА о них. Исправлены 3 расхождения «слово ≠ дело»: два канонических ридера (агентский проектор был
> partial и вне git) · один вердикт — один хозяин (баннер спорил с приёмкой на одном файле) · волна 1+9 и единая каденция HTML.
> **Остался Блок 3 — система АНАЛИЗА** (op-rules 33→~10 · human-in-loop · вернуть живой заход · не плодить гейты).
> Проверка: сначала **Toys & Hobbies с батча 1** (честный полигон), затем **H&G b1–b5** (контроль на потерю — ответ известен).
> Актуальное состояние → `departments/storeleads/operational-memory/learnings.md` (HANDOFF **S18**).

> **Purpose (Marina S16):** capture the problem + the staged plan to rebuild a CLEAN base, so next session
> we execute it step-by-step (Marina will formalize/approve each step). **We delete NOTHING — the system works;
> we declutter: archive the junk, keep the clean experience.** This doc = the starting point for that work.
> **Decision (agent + Marina): NOT a from-scratch rebuild — surgical declutter + rewrite the ONE rotten file (op-rules).**

## THE PROBLEM (why the folder went heavy — root cause)
1. **⚠️ CORRECTED S17 (Marina) — the old wording here was WRONG and misled the next session.**
   The old text said: *«ShopHunter was simple because the HUMAN (Marina) was the quality backstop; Store Leads chased
   SCALE, so we replaced the human with machine gates.»* **Both halves are false:**
   - **(a)** In ShopHunter the **AGENT** finds the winner (dump → open every store → enrich → judge the PRODUCT →
     present winners / borderline / browse). Marina's role is **Founder Review** on what is presented, plus deciding
     how many sessions to run. She does not pick winners by eye out of the raw pool.
   - **(b)** Store Leads never chased scale: we run the **same number of batches per session** as ShopHunter. The huge
     universe is an **ASSET** (it solves the wall we hit when ShopHunter's stores ran out), not a race.
   **The real root cause:** over sessions the RULES duplicated and layered (33 rules, ~30 ideas restated 4–5×), and the
   agent's genuine analysis — actually opening a store and judging the product — was displaced by **ticking checkpoint
   boxes**. The gates measure COVERAGE (250 read, flags «opened», browse≥7), never JUDGMENT — so the dashboard stayed
   green while a real winner was dropped = **Goodhart**. Store Leads' core must be **IDENTICAL to ShopHunter's**; only
   (i) data acquisition differs (more stores) and (ii) a few parts we genuinely strengthened (enricher, reports, guard).
2. **Archaeology of failures.** Each failure spawned a NEW gate instead of restoring the simple practice:
   S5→RULE 25/26 · S6→RULE 27 · S7→RULE 29 (`sl_open_flags` — where "open" silently became "curl") · b3/b4→RULE 31/32/33.
   33 rules accreted. The machinery built to PREVENT winner-loss CAUSED it (gate passed on curl+card → genuine live-open faded).
3. **Duplication / cloning.** ~30 distinct ideas restated 4–5× across op-rules/workflow/discovery-funnel/learnings/CREED
   (e.g. "open every flag" = RULE 23 + 29 + §1a + CREED; "read all no gut-top-N" = RULE 6 + 21 + CREED + funnel). So the
   SOUL is invisible and gates give false comfort. **Live proof (S16):** agent almost ADDED a line to RULE 29 that
   already exists verbatim in RULE 23. Adding more = worse.
4. **Misleading / contradicting rules (found in the S16 contradiction scan):**
   - **OPEN:** RULE 23 = "live-open EVERY needs_live + unreachable BY HAND" vs RULE 29 = "`sl_open_flags`... opens each...
     the tool ENFORCES RULE 23" — but the tool only CURLS. So "open by hand" silently became "tool curled + fill verdict."
   - **AUTONOMY (self-contradiction):** workflow line 9 + README = "human-in-loop, NOT autonomous (not earned)" vs workflow
     line 234 + RULE 33 = "EARNED in-session autonomy for ANALYSIS... supersedes the NOT-autonomous line." The doc argues
     with itself. RULE 33's autonomous-batches is itself scale-machinery that drove quality decay → **rebuild resolves to
     human-in-loop** (matches ShopHunter + Marina watching every batch now).
5. **Stale data-acquisition docs.** The OLD pipeline (API `bq` dump via scrapers, paginated, quota-limited) is RETIRED —
   we now have the whole universe as a downloaded CSV. But `discovery-funnel.md` Stage 0 + `interface-guide.md` still
   describe the retired dump as current. **Symptom (S16 start):** the agent hunted the CSV on Marina's Desktop when
   it's on VPS+repo — the data-acquisition step has no clear pointer (AUDIT-1).

## FILE INVENTORY + VERDICT (lines as of S16)
| File | Lines | Verdict |
|---|---|---|
| `op-rules.md` | 369 | **REWRITE from scratch** → ≤~1 page, ~10 distinct rules (re-distill the 33, each once). Keep CREED at top. |
| `workflow.md` | 302 | **TRIM hard** — collapse the 3 checkpoint shapes + 5 gate refs into one thin funnel; point to op-rules, don't re-state. |
| `learnings.md` | 246 | TRIM — archive S13b HANDOFF (RULE 18 overdue), collapse old session blocks; keep active learnings + HANDOFF. |
| `discovery-funnel.md` | 135 | **FIX Stage 0** — mark API/`bq` dump RETIRED, point to `csv-export.md`; keep Stage 1–3 (still current). |
| `interface-guide.md` | 96 | **ARCHIVE most** — API/bq/dump mechanics superseded by CSV. Keep only what CSV-slice still uses. |
| `subagent-spec.md` | 136 | KEEP — enricher contract, still current (this is a STRONG part). |
| `prescale-hardening-plan.md` | 68 | **ARCHIVE** — its Q1–Q5 were resolved S6 (banner says so). |
| `csv-export.md` | 91 | KEEP + ELEVATE — this is the CURRENT data-acquisition method; surface it as the entry point. |
| founder-feedback / keep-list / niche-track-record / capabilities / README / hypotheses / reference | — | **KEEP ALL** — this is the real experience/calibration. Don't touch. |

> No single file exceeds the ~2000-line read limit (largest = op-rules 369), so each is readable — the problem is
> AGGREGATE bloat (~1709-line mandatory-load) + duplication, not one unreadable file. Flag if any file approaches ~1000+.

## THE STAGED REBUILD (next session — Marina approves each step)
Walk the pipeline end-to-end, and at EACH step ask: what did we do before · what now · where in other depts (ShopHunter
base) · where do we LOSE the thread · what did we make genuinely STRONGER. Restore the base; keep the real upgrades.
1. **Data acquisition** (enter SL → get data). Archive the retired dump/scraper experience. Pin the CURRENT method:
   the captured CSV universe (Shopify 2.89M + Woo 4.26M) — **WHERE it lives** (VPS `logs/storeleads/exports/` + Desktop;
   NOT in git). Add a DATA-INVENTORY pointer so no session hunts for it again (AUDIT-1).
2. **Selection / segmentation / strategy.** How we pick a niche + slice the CSV; categories; the strategy we've moved
   through (niche-store-first-at-scale). Write the strategy once, clearly; archive outdated strategy notes.
3. **Prep before analysis (enrichment).** The scraper/enricher (`sl_enrich4`, subagent-spec). How before/now/other depts;
   what we made STRONGER than ShopHunter (likely a lot here). Fix it clearly; could run the enricher in background to
   produce a clean reference report for this part.
4. **Analysis.** Walk ONE batch on the CURRENT docs; compare to the ShopHunter base (their funnel + SH-8 safeguard);
   design the human-approval points; find where the thread breaks. **This is where we became stronger than ShopHunter**
   (gates/checkpoints on HOW we analyse stores) — keep the genuine strength, cut the duplication. **The single real
   ShopHunter advantage we add = COVERAGE (whole Shopify universe) + the cross-winner guard + the honest question.**
5. **Declutter pass.** With the base clear, go rule-by-rule: needed / duplicate / misleading → keep one, archive rest.
   THEN re-run batches b1→b4 to verify the clean base finds winners (this is where the work gets maximally good).

## RULES (interim, until next session)
- **No new rules. No more gates.** If a discipline seems missing, FIRST grep — it's probably already written (cloning).
- Keep the SOUL practice alive by hand: read all · open every unreachable + every genuine candidate LIVE · judge the
  product · browse · checkpoint-before-Notion · honest zero ok. (CREED.)
- Batches paused until the base is rebuilt (don't keep digging on a tangled base).
