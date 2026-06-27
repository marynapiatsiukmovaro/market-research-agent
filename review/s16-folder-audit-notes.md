# S16 — Folder Audit Notes (running list, fix during the deliberate audit pass)

> **Purpose (Marina, S16 2026-06-27):** a single running page where the agent logs everything that
> needs editing / cleaning / relinking in the Store Leads folder, AS it's noticed during work — so the
> later deliberate folder-audit has a ready worklist instead of re-discovering. Folder "fullness" /
> clutter may itself be degrading work quality (the S15 doc-overload root cause), so this also tracks
> stale/duplicate docs to archive. **Nothing here is acted on without Marina's OK (Tier-2 = proposal-first).**
> Add freely; mark each item OPEN / DONE / DEFERRED.

---

## Findings

### AUDIT-1 — Universe CSV (11 GB) has no top-level pointer · OPEN
**What:** the two universe CSVs (Shopify-Active 5.7G + WooCommerce 4.6G = ~11 GB) live on **VPS**
`logs/storeleads/exports/` (backup) + **Desktop** `~/Desktop/StoreLeads_Exports/` (origin). They are NOT
in git (too big — correct). The only in-repo pointer is buried in `methods/csv-export.md` ("where they live").
**Why it matters:** this is our most valuable, hard-to-re-create asset. The agent (me, S16) failed to find it
quickly and wrongly looked on Marina's Desktop — the pointer should not require reading a method doc.
**Fix idea:** add a prominent **DATA INVENTORY** block to `departments/storeleads/README.md` (or a dedicated
`operational-memory/data-inventory.md`) listing: universe CSVs (path/size/date/row-counts), enriched reservoirs
on VPS, processed_domains mirror, keep-list — the canonical "where everything is" map. Surface it in the session
load order so it's read at start.

### AUDIT-2 — VPS connection details not pinned centrally · OPEN
**What:** host `root@5.78.217.133`, key `~/.ssh/market_research_vps`, base `/opt/market-research-agent`. To find
these I had to grep `scripts/sl_email_login.py` + `README.md`. Already flagged as a gap in S13b learnings ("pin
VPS connection (key path/host)").
**Fix idea:** put a one-line CONNECTION block in the same DATA INVENTORY / department README (host · key · base path).

### AUDIT-3 — Doc overload + attention skew (the S15 root cause) · OPEN (Tier-2, big)
**What:** mandatory-load ≈ 2252 lines; op-rules attention skew ≈ 41:4 (gate/contract machinery vs product-first
SOUL). Captured fully in `review/s15-postmortem-and-hardening.md` + promotion-queue [2026-06-08] S15 (proposals A–E).
**Fix idea (deferred to the deliberate audit):** ANALYSIS CREED (5–7 lines) at the TOP of op-rules/workflow;
trim oversized RULE-31 anti-truncation prose; gate the JUDGMENT not only coverage. **Do NOT touch core/ without OK.**

### AUDIT-4 — Stale / resolved docs to archive · OPEN
**What:** candidates that may be adding clutter:
- `operational-memory/prescale-hardening-plan.md` — its Q1–Q5 were RESOLVED in S6 (banner at top says so); could move to archive.
- S13b HANDOFF archival was DEFERRED from S15 (RULE 18 — keep only 2 newest in learnings).
**Fix idea:** during the audit, archive resolved-agenda docs to `archive/` or `handoffs-archive.md`; keep mandatory-load lean.

---

### GUARD v0.1 — `scripts/sl_winner_crossref.py` — tuning backlog (refine on b2) · OPEN
**Built S16** (Marina-approved). Core = cross-category catch: flags any store whose product TYPE matches a
known winner-type from ANY niche, forcing an explicit score (never browse-only). **CATEGORY-NEUTRAL by design
(Marina S16 correction): no category is privileged — the registry has more nursery entries only because that's
the niche mined most; that is NOT a hint about where winners live.** Validated on b1 → correctly caught eu.boba +
babymoov + hydroslife/ezfauxdecor/mihigh sitting inside H&G.
**Tuning items (b1–b3):**
- **Missed CouchConsole** (our own winner): brand token is concatenated ("couchconsole") so the spaced
  keyword "couch console" didn't match + empty descs. Fix: ADD domain-with-separators-stripped + space-stripped
  matching (this makes the net WIDER — good).
- **keep-list domain-catch didn't load on VPS** — the repo path has Cyrillic ("АГЕНТЫ") which broke the scp
  sync of keep-list.md; the script's domain-catch fell back to empty. Fix the sync (or load from VPS mirror).
- v0.2 candidate: wire the crossref worklist INTO `sl_analysis_gate.py` so it HARD-STOPs if a flagged store
  has no explicit score (currently advisory-print only). Decide after more batches.
- ⛔ **DO NOT narrow the "sleep sack/sleeping bag" keyword** (Marina S16): the 1–2 false-positives/batch are the
  DESIRED cost of an inclusive safety net, not a defect. The guard stays inclusive (bias toward MORE catches).
  My earlier "tighten the keyword" instinct was wrong — coverage/inclusion over noise-reduction, always.

### AUDIT-5 — GENUINE live-open atrophied (tooling displaced it) · OPEN (Tier-2, important)
**What (Marina caught on b4, S16):** the genuine LIVE-open (WebFetch the actual store, look at hero/wow/price) eroded into a
light server curl (`sl_open_flags` = title+price) + card-judgment. I stopped opening the B/C/tail stores I find interesting — in
S3/S4 I opened ~90 live per session. **Where it eroded:** S7 `sl_open_flags` (RULE 29) made the gate satisfiable by a curl seed +
card; S13b projection reinforced "judge from the card." Same Goodhart as S15 — system stopped REQUIRING the real open.
**From ShopHunter (where it was structural):** Stage-2 "open ALL, no name-pick" + **SH-8 safeguard #3** = thin/mismatched desc →
WebFetch the LIVE page BEFORE scoring (born from SlotPro 52→66; Marina caught it by question).
**Fix (interim, applied b5):** live description-confidence gate active — thin desc OR any genuine-product store marked across
A/B/C/tail → WebFetch live BEFORE scoring, shown in chat; `sl_open_flags` curl = triage only. Per-batch CONSTANT honest-question
added (workflow §1a). **Audit decision to make:** should `sl_analysis_gate` machine-REQUIRE a min genuine-live-open count/batch
(so coverage can't be satisfied by curl+card)? — Tier-2, gather more batches, decide in the deep audit. Full trace: learnings.md S16.

**⭐ PINPOINTED erosion moment (Marina S16, 2026-06-27): S7 RULE 29.** RULE 29's `sl_open_flags` is described as
"opens each" but it does a CURL (status·title·prices), and "the agent only fills verdict" → the word "open" silently
became "curl-seed," which OVERRODE the older **RULE 23** ("live-open EVERY needs_live + unreachable BY HAND"). On b5
the agent verdicted all **18 unreachable from the curl TITLE alone** — never genuinely opening them. Live-opening them
(Marina's instruction) immediately found **claymoreoutdoor V600+ portable fan $64.95** (genuine candidate the title hid)
→ proves the rule. UNREACHABLE is the highest-risk pile (no card at all → title-judgment is impossible; S1 lost a real
winner here). **PROPOSED op-rules fix (needs Marina OK to edit RULE 23/29):** (a) the curl seed is explicitly a "is-it-alive"
SEED, NOT the open; (b) every UNREACHABLE store MUST be genuinely WebFetched + looked at — always, no exception; (c) its
opens.jsonl verdict must come from a genuine open, not the curl title. This restores RULE 23's intent and stops RULE 29
from eroding it again. **Meta-lesson (Marina): we replaced a working rule instead of improving it — track WHERE/WHEN each
discipline erodes (rule-provenance), don't let tooling silently redefine a verb.**

## How to use
Append a finding the moment it's noticed (don't wait for end-of-session). One block per item:
`### AUDIT-N — title · OPEN/DONE/DEFERRED` + What / Why / Fix idea. Resolve in the deliberate audit pass with Marina.
