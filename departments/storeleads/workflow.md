# Store Leads — Department Workflow (session entry point)

Thin entry point. The full procedure lives in `methods/`. Store-first discovery at scale via
storeleads.app. **SYSTEM-BUILD / in development — human-in-loop, NOT autonomous (not earned).**

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

## 2. Mode & checkpoints (STANDING)
- **Human-in-loop — NOT autonomous** (not earned). Work autonomously through dump→funnel→deep-score,
  then deliver the checkpoint and **WAIT for Marina's explicit OK before ANY Notion write.**
- Checkpoint = winners 65+ / borderline 55–64 / patterns / browse-pool (curated UNIQUE genuine-product
  links). Every link clickable. Convergence/revenue earns at most Watchlist, never auto-Consider.

## 3. End-of-session Learning Protocol
1. After Marina's OK: save reported (65+) to Notion (`shared/notion-workflow.md`, Source = "Store Leads")
   + `shared/reported-products.md`; rejects → `shared/rejected-products.md`.
2. Append tactical learnings to `operational-memory/learnings.md` (with expiry); archive expired (RULE-15).
3. Log any founder decision on a SPECIFIC product → `operational-memory/founder-feedback.md` (Tier-1 fact).
4. Update the **HANDOFF** block at the top of `learnings.md` for the next session.
5. **Tier-2 guard (FB RULE 14):** any system-changing generalization (new taste/filter/veto rule,
   closing a category, a pivot, promotion into core/shared) is PROPOSED via `review/promotion-queue.md`,
   never self-written. Never edit `core/` or `shared/founder-taste.md` autonomously.
