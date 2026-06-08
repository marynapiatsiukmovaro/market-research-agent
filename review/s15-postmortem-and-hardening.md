# S15 POST-MORTEM + SYSTEM-HARDENING AGENDA (2026-06-08)

> **Status:** OPEN. This is the agenda for the next session (system hardening, NOT batches).
> Marina-initiated after S15 revealed the analysis system runs on **discipline, not system** — a
> blocker for scaling. b1–b8 results are NOT trusted and NOT recorded (see "Redo state").

---

## 1. What happened (S15, Home & Garden, visits 1k–10k, Shopify-Active full-universe slice)
Ran b1–b8 (2000 stores). Reported **1 winner (CouchConsole 74) + 2 borderline**, declared the niche
structurally weak, and floated a **pivot** — a self-invented conclusion. Marina caught that several
stores matched **already-validated Notion winners** and were dumped to `browse` (or dropped entirely),
not scored:
- **The Wriggler** (b5, anti-roll changing mat, ~$43) — DROPPED entirely (not even browse). Direct
  convergence with **Yogorgeous Anti-Roll Mat (Watchlist)** + same pain as **WriggleBum (Consider)**.
- **Rockit** (b7, rockitsleep.com, $59.95) — the brand store of Marina's **Nursery Rockit (Consider)** — buried in browse as "convergence".
- **SnoofyBee** (b7, Playtime changing pad, $38) — diaper-change cluster — browse only.

In the autonomous block b3–b8 the agent **opened ZERO links by hand** (relied on card-read + the
`sl_open_flags` HTTP fetch), did its own live-WebFetch only in b1/b2. The consolidated report also dropped browse links.

## 2. Root cause — measured, not asserted (this is the important part)
Marina's hypothesis (docs overloaded → discipline diluted) is **confirmed by data:**
- **Mandatory-load = 2252 lines** (op-rules alone 356).
- **Attention skew ≈ 41 : 4.** op-rules mentions gate/contract/PASS-line/"don't-truncate" machinery
  **41×**; the SOUL rule **"evaluate PRODUCTS not categories" (product-first) appears ~4× across ALL
  core + op-rules** (0× in mindset / mandatory-filters / winner-detection / identity).
- → The system **trained attention onto gate+contract compliance and away from product-first judgment.**
  Under context pressure (8 batches) the weakly-represented discipline (open links, judge the product,
  borderline-not-category) fell out of working memory first.

**Goodhart's law, mechanically:** the system made **"gate PASS + contract-complete" the measured target**
(heavily enforced, machine-STOPs). The **actual objective — find winners by judging products — is barely
encoded and NOT gated.** So the agent optimized the measurable proxy; real quality decayed **while every
dashboard stayed green.** That is exactly why the system is **not scale-ready**: at scale, discipline-
dependent quality collapses faster (more batches, more fatigue) while the metrics keep lying green.

**The specific hole:** `sl_analysis_gate` checks COVERAGE + STRUCTURE (every flag has a verdict string,
browse≥7, all sections present, PASS line pasted). It is **happy even when a real candidate is dismissed
by category** ("off-model: baby") or when the agent live-opened nothing. Judgment quality is ungated.

## 3. Fix directions (proposals — Tier-2, to discuss + harden the folder)
- **A. Doc diet + invert salience.** A short **ANALYSIS CREED (5–7 lines) at the very TOP**, above all
  gate machinery: *evaluate PRODUCTS not categories · adjacent/cross-niche is normal · open links EVERY
  batch · real-pain or cross-niche-match → borderline minimum, never browse-dismiss · honest-zero is fine
  but never invent a pivot.* Trim the oversized RULE-31 anti-truncation prose (symptom of over-engineering
  the wrong thing).
- **B. Gate the JUDGMENT, not only coverage:**
  - gate STOP if the agent live-opened **< N candidate stores/batch** (hero+price logged) — makes
    "open links every batch" structural, not disciplinary;
  - **auto cross-reference** each batch against the known-winner-type list (founder-feedback / reported-
    products) → any match MUST get an explicit score, cannot be silently browsed (prevents the Rockit/
    Wriggler miss by system);
  - verdict reason must be **product-level** (price / wow / COGS / saturation) — a bare category label
    ("off-model: baby") is rejected.
- **C. Cap batches/session** at a level where context never degrades judgment (6 = ~50% context per
  Marina = OK; the failure was quality, not count — but keep a hard ceiling).
- **D. Remove the pivot-narrative invitation** from the session prompt (the S13 "flag weak niche early"
  heuristic is what licensed the premature pivot).
- **E. Cross-department audit (Marina, + her side audit):** review core/ docs and how discipline is built
  in FB / ShopHunter departments; bring the Store Leads folder into clean, scale-ready shape.

## 4. Redo state (DO NOT lose this)
- **b1–b8 analysis = UNTRUSTED.** Re-analyze Home & Garden from b1 with the corrected process.
- **`sl_mark_processed` NOT run** — b1–b8 stores remain un-processed so they can be re-pulled. Reservoirs
  `hg_b1..b12_enriched.json` intact on VPS; data is fine (only the READING/JUDGMENT was bad).
- **Notion: nothing written.** Provisional finds to re-verify in the redo (NOT yet cards):
  CouchConsole 74 · The Wriggler ~60 · SnoofyBee ~58 · Ez Faux Decor 60 · YARDLOCK 63 · Rockit (=existing Consider, confirmed live in H&G).
- New tool kept: `scripts/sl_subniche_profile.py` (observation-only sub-niche classifier — showed the H&G
  whole-category dump is ~98% off-model-for-impulse sub-niches, appliance/gadget only ~1.9%; the weak raw
  yield is a SUB-NICHE-MIX artifact, NOT an H&G-category verdict — Marina's hypothesis confirmed).
