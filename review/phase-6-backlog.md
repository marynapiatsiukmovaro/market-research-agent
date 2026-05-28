# Phase 6 Backlog — Deferred Cleanup Items

**Created:** 2026-05-28 (end of pre-dept#3 cleanup session)
**Status:** Open — decisions deferred to dept #3 (Dropship.io) preparation phase
**Why this file exists:** Items intentionally NOT done during Phase 1-5 cleanup. Future agents should consult this BEFORE proposing changes to listed files — to avoid re-discovering the same trade-offs.

## Context

Phase 1-5 cleanup completed 2026-05-28 (9 commits on `origin/main`). Phase 6 was explicitly skipped per Marina's principle: "clarity > token saving" + "don't touch what isn't operationally broken."

Items below were identified as legacy / orphan / optional BUT consciously left alone. **They are NOT bugs — they are deferred decisions.**

---

## Deferred items

### 1. `prompts/` folder — operationally dead

**State (grep verified 2026-05-28):** 3 files, 0 live references in active code.

| File | Lines | Status |
|---|---|---|
| `prompts/find-products.md` | 44 | Pre-multi-dept legacy, FB-shaped. Still has stale "find 5" (line 3) cap after Edit #2 (line 39) fixed «2–5» |
| `prompts/daily-report.md` | 16 | Pre-multi-dept legacy. Still has «2–5» cap (line 9) |
| `prompts/validate-product.md` | 17 | Updated to 4-tier Founder Review in Phase 1-5 (profilactic), but still unread |

**Why kept:** `CLAUDE.md` routes "Find Products" → `departments/{dept}/workflow.md` directly. Marina writes session prompts in chat, doesn't read from `prompts/` (see memory: `feedback_no_prompt_files.md`). Folder is reference-only.

**Decision when reopening:**
- (A) Archive whole folder to `archive/legacy-prompts/`
- (B) Redesign under Layer A/B convention (department-agnostic prompts that route to `departments/{dept}/workflow.md`)
- (C) Delete

### 2. `core/` — 4 orphan files

**State (grep verified 2026-05-28):** Not in CLAUDE.md Layer A mandatory load. 0 active references.

| File | Size | Status |
|---|---|---|
| `core/rejection-rules.md` | 7 lines | Pointer stub to `mandatory-filters.md` |
| `core/agent-rules.md` | 3713 bytes | Duplicates `operating-rules.md` + `identity.md`. Contains stale «2–5 cap» at line 35 |
| `core/autonomy.md` | 602 bytes | General SHOULD / SHOULD NOT — absorbed into `identity.md` + `mindset.md` |
| `core/token-efficiency.md` | 529 bytes | Overlaps with `identity.md` Scout Mode. 1 ref from `departments/shophunter/README.md:28` |

**Why kept:** Marina's principle "core/ scoring/filter/mandatory-filter logic: not modified." Phase 6 explicitly skipped.

**Decision when reopening:**
- (A) Archive to `archive/core-legacy/`
- (B) Delete (after confirming no live refs)
- (C) Consolidate into existing core files
- If kept as-is: fix internal staleness (e.g., «2–5» in `agent-rules.md:35`)

### 3. `scripts/` — versioned pairs unclear + flat structure

**Versioned pairs (which is canonical?):**
- `sh_cat_dump.py` + `sh_cat_dump_v2.py`
- `sh_proxy_diag.py` + `sh_proxy_diag2.py`
- `sh_collections_recon.py` + `sh_collections_recon2.py`
- `sh_collection_add.py` + `sh_collection_add_test.py`

**Structure issue:** 28/30 scripts are SH-specific (`sh_*`, `ap_*`). 2 are FB or shared. No dept subfolders. CLAUDE.md already notes "scripts/ → dept-specific scripts move under departments/{dept}/ over time."

**Decision when reopening:**
- Resolve versioned pairs — delete the older OR rename to clarify which is canonical
- Adopt `scripts/{dept}/` convention OR explicit prefix convention (`sh_`, `fb_`, `dr_`, `wh_`, `sl_`) during dept #3 setup

### 4. ShopHunter — no `op-rules.md`

**State:** `departments/shophunter/operational-memory/` lacks `op-rules.md`. FB has one as a major file. `README.md` explicitly notes "(op-rules: not yet created)".

**Why kept:** Marina's principle "let it mature naturally — FB got op-rules after ~7 sessions, SH will produce its own when needed."

**Decision when reopening:** Do NOT force-backfill before dept #3. If dept #3 (Dropship.io) cloning surfaces friction, decide then.

---

## Items NOT in backlog (intentional — don't propose changing these)

- `core/operating-rules.md:2` FB-specific breadcrumb — **by design** (FB is the operational reference for new depts per Marina). STATUS comment added in Phase 5 makes intent explicit.
- `archive/sources-overview-capability-map.md` Minea verdict note — intentional historical breadcrumb.
- `shared/founder-taste.md` — Tier-2 strong doc, never auto-edit.
- `departments/{dept}/operational-memory/founder-feedback.md` per-dept — Marina's explicit design (do not propose consolidating).
- Live Notion DB historical cards — never modify retroactively.

---

## When to reopen this backlog

When preparing infrastructure for **dept #3 (Dropship.io)**. Resolve items 1-3 as part of `_TEMPLATE/` design discussion — what goes into the template determines what's redundant in current departments.

Item 4 (SH `op-rules.md`) — resolve naturally during dept #3 cloning **if** friction emerges, not preemptively.

---

## Related artifacts

- Phase 1-5 completion record: `archive/audits/audit-2026-05-28-post-cleanup.md` (full audit report)
- Architectural decisions in force: see Marina's `.claude/memory/project_system_cleanup_phases.md` summary
