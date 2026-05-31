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
`Date · Product · Score · Marina's reason (her words — the "сок", 2–3 words) · Signal to keep (calibration)`.
So Marina explains once; the agent distils. *(Marina's exact phrasing-principle table → to be pasted in and baked here.)*

### RULE 18 — Memory hygiene (RULE-15 of core/session-health-rules)
Keep only the **2 most recent HANDOFF blocks** in `learnings.md`; move older ones to `handoffs-archive.md`. Archive
expired learnings (never delete — move to Expired). Dedup. Keep the mandatory-load footprint lean.

---

## Checkpoint shape (every batch, before any Notion write)
Winners (65+) · Borderline (55–64, flag for founder call) · Watchlist-signal · Browse-pool (unique) · Patterns ·
the full funnel breakdown (RULE 1). Every link = a clickable markdown hyperlink. Then **STOP and wait for Marina's OK
before writing to Notion.**
