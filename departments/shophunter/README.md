# ShopHunter Department

Second sourcing department. **Store-first discovery** — starts from stores/products
that already show sales traction, not from keywords. Complementary to, not a
replacement for, the Facebook Ads Library department.

> **Status: MATURE / operational (as of SH-8, 2026-05-26).** The interface is mapped, and the matured
> store-first funnel (dump → parallel hero → conservative cut → sub-agent enricher → main-agent deep-score
> → checkpoint → Notion) has run end-to-end across SH-3→SH-8 (Home & Garden 830, Baby & Toddler 717,
> Arts & Entertainment 823, Toys & Games 788 = all 100% processed). Method = `methods/discovery-funnel.md`
> (incl. Structural safeguards) + `methods/subagent-spec.md` + `methods/interface-guide.md`. The department
> still grows session by session — the same way Facebook Ads Library was built, not designed up front. Still
> human-in-loop (autonomous mode NOT yet earned).

## Why this department exists
FB Ads Library discovery runs keyword → ads → advertisers: lower signal density, more
noise, only a small share of advertisers become strong candidates. That is a limit of
the channel's discovery mechanism, not of the scoring or execution. ShopHunter offers a
different signal — stores/products with existing traction → potentially higher signal
density, a faster path to emerging winners, and store-level intelligence.

## What it inherits (read-only — never modify from a ShopHunter session)
Company-level logic is shared and is NOT recreated here:
- `core/scoring-system.md` — the 100-point system + Marina Veto Checklist
- `core/mandatory-filters.md` — hard rejects (branded, пустышка, price, logistics)
- `core/founder.md` — founder vision + winner definition
- `core/product-requirements.md`, `core/operating-rules.md`, `core/session-health-rules.md`,
  `core/token-efficiency.md`, `core/identity.md`, `core/mindset.md`
- `shared/` — reported/rejected logs, Notion schema + workflow, product validation,
  analysis skills, store/company interpretation (`shared/skills/shophunter.md`)

See `capabilities.md` for the concrete list of what we can already do today.

## Relationship to the Facebook Ads Library department
FB is a **reference for SHAPE, not content.** Study HOW that department matured
(permanent rules vs expiring learnings, founder calibration before scoring,
end-of-session memory, hypothesis management) — do NOT copy its content.
We are building a new operation and are free to reject even good FB practices that
do not fit ShopHunter. Never port FB's scraper / VPS-cookie / scroll-depth / keyword
rules — they do not exist in this channel.

## Access model
- Runs on the shared VPS (same server as FB; connection details in FB `op-rules.md`).
- Auth: ShopHunter login (paid SaaS). Credentials live ONLY on the VPS in a gitignored
  file — never in the repo, never echoed back to chat. A persisted browser profile lets
  most runs skip re-login; re-login from stored credentials is the fallback.
- ShopHunter is a paid tool used by its owner → no ban/block fear; Marina is always reachable.

## Autonomous operation
The destination, not the starting point. FB earned Autonomous Mode at Session 30, after
~29 sessions proved the workflow. ShopHunter earns it the same way: human-in-loop
checkpoints until the workflow is validated. There is intentionally no autonomous-mode
file here yet.

## Entry points
- `capabilities.md` — what we can already do + what ShopHunter offers
- `operational-memory/learnings.md` — session-by-session discoveries (HANDOFF at top — read first)
- `operational-memory/founder-feedback.md` — Marina's Founder Review decisions + calibration
- `methods/discovery-funnel.md` — the matured store-first workflow (dump → hero → conservative cut → enrich → deep-score → report)
- `methods/interface-guide.md` — ShopHunter UI mechanics (collections, membership read, dialogs)
- `methods/subagent-spec.md` — enricher sub-agent spec
