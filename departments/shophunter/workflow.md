# ShopHunter — Department Workflow (session entry point)

This is the entry point for any ShopHunter session. It is intentionally **thin** — the full
discovery procedure lives in `methods/`. This file gives the load order, the standing
mode/checkpoint discipline, and the end-of-session protocol. It does NOT duplicate the funnel.

---

## 0. Before you start
- Confirm this is a **ShopHunter** session (store-first discovery). Operate only inside this department —
  never apply FB scraper/cookie/scroll/keyword assumptions here.
- Load the ALWAYS files (core/ + shared/, incl. `shared/founder-taste.md`) + this department's
  `operational-memory/learnings.md` and `operational-memory/founder-feedback.md`.
  *(No `op-rules.md` yet — ShopHunter's rules still live in `methods/discovery-funnel.md` as a living doc.)*
- Read the **HANDOFF → NEXT SESSION** block at the top of `operational-memory/learnings.md` — it carries current state.
- Current research directions: see `hypotheses/` (`storeleads-breadth-source`, `collection-newest-first-monitor`).

## 1. Run the discovery funnel
Follow **`methods/discovery-funnel.md`** end-to-end (Stages 0–6: dump → hero → conservative cut →
enrich → deep-score → report). Supporting method docs:
- `methods/interface-guide.md` — how to drive the ShopHunter UI (Playwright + proxy on VPS).
- `methods/subagent-spec.md` — the Stage-2 enricher sub-agent spec.

Heavy lifting stays on the VPS; only finalists enter chat (FB RULE 7). Verify ALL above the
objective bar, never top-N by gut (FB RULE 8).

## 2. Mode & checkpoints (STANDING)
- **Human-in-loop — NOT autonomous.** ShopHunter has not earned autonomous mode (FB earned it at S30).
- **Checkpoint BEFORE Notion.** Work autonomously through dump → funnel → deep-score, then deliver the
  intermediate checkpoint and WAIT for Marina's explicit OK before ANY Notion write.
- Full reporting protocol (clickable links, mandatory browse-pool, lead with WOW/taste not Tier label) →
  `methods/discovery-funnel.md`.

## 3. End-of-session Learning Protocol (this department's "STEP 8")
Run every session before closing:
1. Save each reported product (65+, **after Marina's OK**) to Notion (`shared/notion-workflow.md`) +
   `shared/reported-products.md`; rejects → `shared/rejected-products.md`.
2. Seed the tracked-shop Collection (Collection-seeding rule in `methods/discovery-funnel.md`).
3. Append new tactical learnings to `operational-memory/learnings.md` (with expiry); archive expired entries.
4. Log any founder decision on a SPECIFIC product to `operational-memory/founder-feedback.md` (Tier-1 fact only).
5. Update the **HANDOFF → NEXT SESSION** block at the top of `learnings.md` so the next session resumes cleanly.
6. **Tier-2 guard (FB RULE 14):** any system-changing generalization — a new taste/filter/veto rule, closing a
   category, a pivot, or any promotion into `core/` or `shared/` — is PROPOSED via `review/promotion-queue.md`,
   never self-written. `shared/founder-taste.md` is a company-wide strong document: never edit it autonomously.
