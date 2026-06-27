# S16 — Session Progress Snapshot (intermediate, mid-session 2026-06-27)

> **Purpose (Marina, S16):** freeze where this session started, what we did, the findings, and the agent's
> concerns — so that as we run batches we don't lose this thread. NOT final; a running snapshot. Persistent
> (survives compact). Pairs with `s16-folder-audit-notes.md` (audit worklist) + learnings.md S16 HANDOFF.

## Where the session started
- Dept **Store Leads**, mode **🔬 ANALYSIS**, niche **Home & Garden (visits 1k–10k, Shopify-Active slice)**.
- Goal: **rebuild the analysis system** after S15 failed (Goodhart — green gates, lost winners). Re-analyze H&G
  from b1 on the corrected system. Reservoirs `hg_b1..b22_enriched` ready on VPS.
- Pre-compact S16: b1–b3 done → CouchConsole 73 → Notion (+3 founder-raised). Post-compact: continue.

## What we did this session (in order)
1. Read ALL docs (core + shared + full Store Leads dept + ShopHunter for cross-reference).
2. **b4** — read 250, opened 58 flags, gate PASS → **0 winners**. BUT did it **thin** (curl seed + card-judgment,
   almost no genuine live-opens).
3. **Marina caught the under-opening** → traced it: the genuine LIVE-open (WebFetch + look) atrophied, displaced
   by tooling (`sl_open_flags` curl seed since S7) + the projection — same Goodhart as S15. Restored from ShopHunter's
   SH-8 description-confidence gate. (Full trace: learnings.md S16 + audit-notes AUDIT-5.)
4. Simplified the per-batch checkpoint: **1 honest rotating question (Marina's voice)** + dropped the duplicated
   gate-numbers; removed the word "схитрил" (wrong tone — imperfect work = system not built, not bad faith).
5. **b5** — read 250, opened 58 flags, **+ 11 genuine live WebFetch in chat** → **2 winners + 2 borderline**
   (The Wriggler 68 = THE S15 MISS, caught by guard + live-open; OtterSpace blackout 66; LuvLink 63; ChickCozy 63).
   **Direct proof: b4 (no live-opens) = 0; b5 (live-opens) = 2 winners.**

## Key finding
**The live-open is what finds winners** in a heavy niche — not reading the card, not the proxy A/B/C tier
(whall was A75→browse; winners sat in A54/A62). The tooling had quietly made "open" = a cheap curl, so the
real open faded under load. Restored as practice on b5.

## Agent's concerns (open — for the deep audit)
1. **Live-open + loss-audit still rest on DISCIPLINE, not the machine.** The gate enforces "every flag opened" but
   does NOT require a min genuine live-open count, nor a fixed loss-audit sample. A tired future session could
   relapse to card-only (exactly the b4 relapse). → AUDIT-5: make the gate require live-opens for in-range
   single-product-DT consumer candidates (by product_class+price+store_type, like the device-flag) + a fixed
   loss-audit size.
2. **Open-count scales with genuine candidates, not a fixed number** (Nursery ~90, heavy H&G ~11). Risk = the agent
   UNDER-marks a genuine candidate and card-dismisses it. Interim check = the loss-audit; system fix = #1.
3. **ABC tier counts must ALWAYS be in the checkpoint** (it's the workflow standard; the agent dropped it in the b5
   checkpoint — corrected). Marina cross-checks against the ABC split.

## Clarified this session — the OPEN principle + funnel numbers (capture so it's not re-litigated)
**Two DIFFERENT actions (the agent confused them in the b5 checkpoint — fixed):**
- **"flags opened" (the robot's set)** = `sl_open_flags` does a LIGHT CURL (status·title·prices) to confirm alive +
  seed a verdict line. This is a SEED, **not** a genuine open. For off-model bulk among flags, curl-title + the full
  card is enough to verdict.
- **"live WebFetch" (the genuine open)** = the agent actually opens the site and looks (hero/price/wow). Done across
  ALL 250 by PRODUCT criteria, not by tier letter.

**Which stores get a genuine live WebFetch (criteria — any tier A/B/C):**
1. EVERY unreachable (always — no card exists; curl-title can hide a winner → S16 proof: claymore $64.95).
2. EVERY guard hit (known winner-type).
3. EVERY genuine white-label single-product-DT consumer candidate (physical, ~$39–100, possible wow/pain, NOT
   furniture/decor/food/plants/trade/catalog/luxury/branded-premium-above-range).
4. EVERY thin/mismatched-desc store that looks like a genuine physical product (the ShopHunter SH-8 gate).
**Card-judged (no open):** the off-model bulk (full card = 3 products + desc + price + image is definitive).
**Open-count is NOT fixed** — it scales with how many genuine candidates the niche has (Nursery ~90; heavy H&G ~11).
Residual risk = under-marking a genuine candidate → the loss-audit (spot-open card-judged off-model) is the interim
check; the SYSTEM fix (machine-require it) = AUDIT-5.

**Funnel numbers reconcile like this (must always be in the checkpoint — ABC counts included):**
`250 = A + B + C (proxy revenue-tier, NOT quality)` · `reach = N reachable + M unreachable` · `flags = needs_live +
unreachable` · `live WebFetch = the genuine opens, by tier`. (b5: 250 = A45·B27·C154 · reach 232 +18 unreach · 58 flags
· 11 live opens A5/B2/C4.)

## Plan from here (Marina-agreed)
- **Re-run b1–b4 this session** with the restored live-open discipline (b4 first — its read is in context; then b1–b3
  fresh, compact between if needed). They were done on the thin approach → may hide winners like The Wriggler did.
- Hold Notion (The Wriggler 68 + OtterSpace 66) until Marina's OK; mark b1–b5 processed at clean session close.
- Deep folder/core/cross-dept audit = its OWN dedicated session (AUDIT-1..5 + s15-postmortem A–E).
