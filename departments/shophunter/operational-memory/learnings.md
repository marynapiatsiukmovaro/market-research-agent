# ShopHunter — Session Learnings

Short-lived tactical discoveries from recent sessions. Read at session start.
Does NOT contain permanent rules (those go to `op-rules.md` once it exists) or
company-level logic (that stays in `core/`).

Discipline mirrors the FB department: append new entries with an expiry; archive
expired entries; never delete — move to the Expired section. A pattern confirmed
across 3 sessions OR explicitly approved by Marina may be promoted to a permanent
rule via `review/promotion-queue.md`.

---

## Active Learnings

### [2026-05-24] Session SH-1 — Explore Shops search needs the BARE DOMAIN, not the full product URL
**Type:** Tactical / Warning
**Severity:** MEDIUM
**Confidence:** HIGH (confirmed live with renpho.com)
**Observation:** In Explore → Shops, the "Search Shops" box matches a store by its
domain/handle, NOT a full product path. Searching `renpho.com/collections/eye-massager`
did NOT surface the store; stripping to `renpho.com` returned the shop (id 8346304597).
Rule: when taking a Store Link from our records/Notion, strip it to the bare domain
(everything up to the first slash after .com) before searching.
The shop page then exposes: store revenue (Day/Week/Month + trend), **Store Creation Date**,
**SKU count**, **tracked-by-N-users**, **Competitor Analysis** (rival stores + their revenue +
top products), and a **"View on Facebook Ads Archive"** link (built-in FB cross-reference).
**Applies to:** every Explore Shops lookup that starts from a known store link
**Expires after:** Never → promote to `op-rules.md` when that file is created (permanent operational fact)

---

## Expired / Promoted

_Empty._

---

## How to add a learning

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW / MEDIUM / HIGH / CRITICAL
**Confidence:** LOW (1 case) / MEDIUM (2–3) / HIGH (multiple or founder-confirmed)
**Observation:** what was found (2–5 lines)
**Applies to:** [store type / category / discovery path]
**Expires after:** Session [N+7]   (use "Never" → promote to op-rules.md instead)
```
