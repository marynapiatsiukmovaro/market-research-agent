# MIGRATION v2 — HANDOFF FOR CLAUDE CODE

> **Read this entire document before doing anything.**
>
> This is an architectural reorganization of an already-working operational
> system. **Nothing is being created from scratch.** Existing files contain
> live intelligence built over 9+ scout sessions and must be preserved exactly
> as they are. The work is **moves and renames only.**
>
> Execute one phase at a time. After each phase: show the diff, list any
> warnings, and **STOP** for Marina's approval before moving to the next phase.

---

## MIGRATION LAWS (apply to every phase until validation passes)

These five laws are non-negotiable. If you find yourself about to break one of
them — stop and ask Marina.

1. **No deletion.** No file is deleted, period. Not now, not at the end of
   this migration. Cleanup of legacy folders is a separate decision Marina
   makes later, not part of this work.

2. **No radical rewrite.** No file's content is rewritten or "improved" during
   migration. Move + rename only. Wording stays exactly as it is, even if you
   notice it's outdated or duplicated elsewhere. Deduplication is a future
   task, not this one.

3. **Preservation-first.** Every move uses `git mv` (or equivalent) so file
   history is preserved. Content is byte-identical before and after the move.

4. **Archive-first.** Old folders (`brain/`, `criteria/`, `workflows/`,
   `memory/`, `config/`, `skills/`) **stay in place** with `.gitkeep` files
   after their contents are moved out. They are not removed during this
   migration.

5. **Reversible.** Until Phase 5 validation passes, the entire migration must
   be revertable with a single `git reset --hard <pre-migration-commit>`. Do
   not squash, do not force-push, do not delete the pre-migration branch.

---

## TARGET STRUCTURE

```
market-research-agent/
│
├── CLAUDE.md                          ← stays in root (updated in Phase 4)
├── README.md                          ← stays in root
├── SYSTEM_ARCHITECTURE_SNAPSHOT.md    ← stays in root (historical snapshot)
├── .env / .env.example / .gitignore   ← stays
├── run_scout.sh                       ← stays (legacy entry point — not touched)
│
├── core/                              ← COMPANY (changes rarely)
│   ├── identity.md                    ← from brain/system.md
│   ├── mindset.md                     ← from brain/mindset.md
│   ├── autonomy.md                    ← from brain/autonomy-rules.md
│   ├── token-efficiency.md            ← from brain/token-efficiency.md
│   ├── winner-detection.md            ← from brain/winner-detection-algorithm.md
│   ├── mandatory-filters.md           ← from criteria/mandatory-filters.md
│   ├── scoring-system.md              ← from criteria/scoring-system.md
│   ├── product-requirements.md        ← from criteria/product-requirements.md
│   ├── rejection-rules.md             ← from criteria/rejection-rules.md
│   ├── agent-rules.md                 ← from config/agent-rules.md
│   ├── operating-rules.md             ← from memory/agent-operating-rules.md
│   ├── session-health-rules.md        ← from config/session-health-rules.md
│   └── founder.md                     ← from memory/founder-goals.md
│
├── departments/
│   └── facebook-ads-library/
│       ├── README.md                  [ONLY new file in entire migration]
│       ├── workflow.md                ← from workflows/daily-scout.md
│       ├── pre-flight.md              ← from config/vps-connection.md
│       ├── methods/
│       │   ├── keyword-scan.md        ← from skills/fb-ads-keyword-scan.md
│       │   └── facebook_scraper.py    ← from skills/facebook_scraper.py
│       ├── operational-memory/
│       │   ├── learnings.md           ← from memory/session-learnings.md
│       │   ├── seen-advertisers.md    ← from memory/seen-advertisers.md
│       │   ├── founder-taste.md       ← from memory/founder-taste.md
│       │   └── founder-feedback.md    ← from memory/founder-feedback.md
│       └── current-context/
│           └── kids-niche.md          ← from memory/kids-vertical-hypothesis.md
│
├── shared/                            ← channel-agnostic resources
│   ├── notion-schema.md               ← from config/notion-config.md
│   ├── notion-workflow.md             ← from workflows/notion-update.md
│   ├── product-validation.md          ← from workflows/product-validation.md
│   ├── telegram-report.md             ← from workflows/telegram-report.md
│   ├── sources-overview.md            ← merged from config/sources.md
│   │                                       + config/sources-capability-map.md
│   ├── reported-products.md           ← from memory/reported-products.md
│   ├── rejected-products.md           ← from memory/rejected-products.md
│   ├── successful-patterns.md         ← from memory/successful-patterns.md
│   ├── failed-patterns.md             ← from memory/failed-patterns.md
│   └── skills/
│       ├── wow-factor.md              ← from skills/wow-factor-analysis.md
│       ├── ugc.md                     ← from skills/ugc-analysis.md
│       ├── trend.md                   ← from skills/trend-analysis.md
│       ├── sourcing.md                ← from skills/sourcing-analysis.md
│       ├── shophunter.md              ← from skills/shophunter-analysis.md
│       ├── paid-traffic-analysis.md   ← from skills/paid-traffic-analysis.md
│       └── product-discovery.md       ← from skills/product-discovery.md
│
├── review/
│   └── promotion-queue.md             ← from memory/proposed-core-updates.md
│
├── prompts/                           ← untouched
├── outputs/                           ← untouched
├── research/                          ← untouched
│
└── archive/                           ← created in Phase 3, holds old handoffs
```

**Legacy folders that stay in place with `.gitkeep` after their contents move:**
`brain/`, `criteria/`, `workflows/`, `memory/`, `config/`, `skills/`.

---

## PHASES

Each phase ends with a **STOP** for Marina's review. Do not chain phases.

### PHASE 0 — Pre-migration safety

Before touching anything:

1. Confirm you are on a clean working tree:
   ```bash
   cd /Users/marinapetuk/Desktop/АГЕНТЫ/market-research-agent
   git status
   ```
   If there are uncommitted changes — stop, ask Marina what to do with them.

2. Create a safety branch from current state:
   ```bash
   git checkout -b pre-migration-v2-backup
   git checkout main   # or whichever branch is the working one
   git checkout -b migration-v2
   ```
   This guarantees the pre-migration state is preserved as a named branch.

3. Confirm to Marina: "Safety branch `pre-migration-v2-backup` created.
   Working on `migration-v2`. Ready for Phase 1."

**STOP — wait for Marina's OK before Phase 1.**

---

### PHASE 1 — Create folder structure only

**Goal:** create empty folders. No file is moved. No new file is created
(except `.gitkeep` markers so git tracks the empty folders).

```bash
cd /Users/marinapetuk/Desktop/АГЕНТЫ/market-research-agent

mkdir -p core
mkdir -p departments/facebook-ads-library/methods
mkdir -p departments/facebook-ads-library/operational-memory
mkdir -p departments/facebook-ads-library/current-context
mkdir -p shared/skills
mkdir -p review
mkdir -p archive

touch core/.gitkeep
touch departments/facebook-ads-library/.gitkeep
touch departments/facebook-ads-library/methods/.gitkeep
touch departments/facebook-ads-library/operational-memory/.gitkeep
touch departments/facebook-ads-library/current-context/.gitkeep
touch shared/.gitkeep
touch shared/skills/.gitkeep
touch review/.gitkeep
touch archive/.gitkeep
```

Verify:
```bash
find core departments shared review archive -type d
```

Commit:
```bash
git add core departments shared review archive
git commit -m "Phase 1: create new architecture folders (empty)"
```

**Report to Marina:** list of new folders created, confirm no existing file
was touched, no existing folder was modified. Show `git status` and
`git diff --stat HEAD~1`.

**STOP — wait for Marina's OK before Phase 2.**

---

### PHASE 2 — Move core/ files (13 files)

**Goal:** move 13 files into `core/` using `git mv`. Content unchanged.
Old folders (`brain/`, parts of `criteria/`, `config/`, `memory/`) keep their
remaining contents and their `.gitkeep` if they end up empty.

Commands (run them one block at a time; after each block, run `git status`
to verify the move was clean):

```bash
cd /Users/marinapetuk/Desktop/АГЕНТЫ/market-research-agent

# brain/ → core/
git mv brain/system.md                       core/identity.md
git mv brain/mindset.md                      core/mindset.md
git mv brain/autonomy-rules.md               core/autonomy.md
git mv brain/token-efficiency.md             core/token-efficiency.md
git mv brain/winner-detection-algorithm.md   core/winner-detection.md

# criteria/ → core/
git mv criteria/mandatory-filters.md         core/mandatory-filters.md
git mv criteria/scoring-system.md            core/scoring-system.md
git mv criteria/product-requirements.md      core/product-requirements.md
git mv criteria/rejection-rules.md           core/rejection-rules.md

# config/ → core/ (partial — only these two)
git mv config/agent-rules.md                 core/agent-rules.md
git mv config/session-health-rules.md        core/session-health-rules.md

# memory/ → core/ (partial — only these two)
git mv memory/agent-operating-rules.md       core/operating-rules.md
git mv memory/founder-goals.md               core/founder.md
```

Verify the move:
```bash
ls core/
git status
```

Expected: 13 files in `core/`, all marked as renames in `git status`.

Commit:
```bash
git commit -m "Phase 2: move 13 files into core/ (content unchanged)"
```

**Report to Marina:** `git diff --stat HEAD~1` output, list of 13 moves, list
of any old folders now empty (they keep `.gitkeep`, do NOT delete them).

**STOP — wait for Marina's OK before Phase 3.**

---

### PHASE 3 — Move departments/, shared/, review/, archive/ files

**Goal:** move remaining files into their new homes. Create the one new file
(`departments/facebook-ads-library/README.md`). Content of all moved files
unchanged.

#### 3a. departments/facebook-ads-library/

```bash
# workflow + pre-flight
git mv workflows/daily-scout.md              departments/facebook-ads-library/workflow.md
git mv config/vps-connection.md              departments/facebook-ads-library/pre-flight.md

# methods/
git mv skills/fb-ads-keyword-scan.md         departments/facebook-ads-library/methods/keyword-scan.md
git mv skills/facebook_scraper.py            departments/facebook-ads-library/methods/facebook_scraper.py

# operational-memory/
git mv memory/session-learnings.md           departments/facebook-ads-library/operational-memory/learnings.md
git mv memory/seen-advertisers.md            departments/facebook-ads-library/operational-memory/seen-advertisers.md
git mv memory/founder-taste.md               departments/facebook-ads-library/operational-memory/founder-taste.md
git mv memory/founder-feedback.md            departments/facebook-ads-library/operational-memory/founder-feedback.md

# current-context/
git mv memory/kids-vertical-hypothesis.md    departments/facebook-ads-library/current-context/kids-niche.md
```

#### 3b. shared/

```bash
# Notion + workflows
git mv config/notion-config.md               shared/notion-schema.md
git mv workflows/notion-update.md            shared/notion-workflow.md
git mv workflows/product-validation.md       shared/product-validation.md
git mv workflows/telegram-report.md          shared/telegram-report.md

# Product knowledge logs (channel-agnostic)
git mv memory/reported-products.md           shared/reported-products.md
git mv memory/rejected-products.md           shared/rejected-products.md
git mv memory/successful-patterns.md         shared/successful-patterns.md
git mv memory/failed-patterns.md             shared/failed-patterns.md

# Shared skills (channel-agnostic analysis methods)
git mv skills/wow-factor-analysis.md         shared/skills/wow-factor.md
git mv skills/ugc-analysis.md                shared/skills/ugc.md
git mv skills/trend-analysis.md              shared/skills/trend.md
git mv skills/sourcing-analysis.md           shared/skills/sourcing.md
git mv skills/shophunter-analysis.md         shared/skills/shophunter.md
git mv skills/paid-traffic-analysis.md       shared/skills/paid-traffic-analysis.md
git mv skills/product-discovery.md           shared/skills/product-discovery.md
```

#### 3c. shared/sources-overview.md (merge of two files)

This is the **only file in the entire migration that combines two sources**.
Both source files contain non-overlapping content that belongs together. The
merge is a concatenation, not a rewrite.

Steps:
1. First, move one of them to its final name:
   ```bash
   git mv config/sources.md shared/sources-overview.md
   ```
2. Then append the second file's content to it, preserving everything:
   ```bash
   echo "" >> shared/sources-overview.md
   echo "" >> shared/sources-overview.md
   echo "---" >> shared/sources-overview.md
   echo "" >> shared/sources-overview.md
   echo "# CAPABILITY MAP (originally config/sources-capability-map.md)" >> shared/sources-overview.md
   echo "" >> shared/sources-overview.md
   cat config/sources-capability-map.md >> shared/sources-overview.md
   git add shared/sources-overview.md
   ```
3. Then move (not delete) the second file into archive so it's preserved:
   ```bash
   git mv config/sources-capability-map.md archive/sources-capability-map-original.md
   ```

This way both originals are preserved (one as the live file, one as an
archived copy), and `shared/sources-overview.md` contains both contents
concatenated. No content is lost.

#### 3d. review/

```bash
git mv memory/proposed-core-updates.md       review/promotion-queue.md
```

#### 3e. archive/ (move old handoff if it exists)

If `HANDOFF-TO-CLAUDE-CODE.md` still exists in root (Marina mentioned she
removed it, so this may be skipped):
```bash
[ -f HANDOFF-TO-CLAUDE-CODE.md ] && git mv HANDOFF-TO-CLAUDE-CODE.md archive/HANDOFF-TO-CLAUDE-CODE-v1.md
```

#### 3f. Create the ONE new file

`departments/facebook-ads-library/README.md` — a short orientation file for
anyone (including the agent) looking at this department for the first time.
Keep it brief, factual, and link to the actual workflow.

Write this content exactly:

```markdown
# Facebook Ads Library Department

This department handles product discovery through direct Facebook Ads
Library scanning via VPS scraper.

## What this department does
- Keyword-First Deep Scan via FB Ads Library
- 500 ads per keyword (hard cap 600) via `methods/facebook_scraper.py`
- Anti-duplicate dedup via `operational-memory/seen-advertisers.md`
- Founder taste calibration via `operational-memory/founder-taste.md`
  and `operational-memory/founder-feedback.md` (these live inside this
  department while taste is still being calibrated — will move to
  `shared/` once stabilized)

## What this department does NOT do
- TikTok Ads Library (future sibling department)
- Instagram Reels search (future sibling department)
- Amazon scraping, Pinterest, Reddit (out of scope for this department)

## Entry points
- Pre-flight check: `pre-flight.md` (VPS connection, FB session, scraper sanity)
- Full session workflow: `workflow.md`
- Current niche being researched: `current-context/kids-niche.md`

## Rules from core/ that this department must follow
- `core/mandatory-filters.md` — hard rejection logic
- `core/scoring-system.md` — 0–100 scoring
- `core/product-requirements.md` — price tiers and product requirements
- `core/operating-rules.md` — Tier signals, anti-hallucination, pivot rules
- `core/session-health-rules.md` — quality monitoring and self-reporting

## Shared resources this department uses
- `shared/notion-schema.md` — Notion DB structure
- `shared/notion-workflow.md` — how to save findings to Notion
- `shared/reported-products.md` / `shared/rejected-products.md` — product logs
- `shared/skills/*` — analysis methods (wow-factor, UGC, sourcing, etc.)
```

Add it:
```bash
git add departments/facebook-ads-library/README.md
```

#### 3g. Commit Phase 3

```bash
git status
```

Expected: ~28 renames, 1 new file (`README.md`), 1 new file
(`shared/sources-overview.md` shows as new because of the merge — that's
fine), 1 archived file (`archive/sources-capability-map-original.md`).

```bash
git commit -m "Phase 3: move departments/, shared/, review/, archive/ files"
```

**Report to Marina:** `git diff --stat HEAD~1`, total moves count, list of
any old folders that ended up empty (they keep `.gitkeep`, do NOT delete).

**STOP — wait for Marina's OK before Phase 4.**

---

### PHASE 4 — Update CLAUDE.md paths only

**Goal:** update path references in `CLAUDE.md` to point at the new
locations. **Do not change strategy text, do not change rules, do not
remove sections.** Path updates only.

Steps:

1. Archive the current version first:
   ```bash
   cp CLAUDE.md archive/CLAUDE-v1.md
   git add archive/CLAUDE-v1.md
   ```

2. Open `CLAUDE.md` and make these exact path replacements
   (use find/replace, one at a time, and show diff after each):

   | Old path | New path |
   |---|---|
   | `brain/system.md` | `core/identity.md` |
   | `brain/mindset.md` | `core/mindset.md` |
   | `brain/autonomy-rules.md` | `core/autonomy.md` |
   | `brain/token-efficiency.md` | `core/token-efficiency.md` |
   | `brain/winner-detection-algorithm.md` | `core/winner-detection.md` |
   | `criteria/mandatory-filters.md` | `core/mandatory-filters.md` |
   | `criteria/scoring-system.md` | `core/scoring-system.md` |
   | `criteria/product-requirements.md` | `core/product-requirements.md` |
   | `criteria/rejection-rules.md` | `core/rejection-rules.md` |
   | `config/agent-rules.md` | `core/agent-rules.md` |
   | `config/session-health-rules.md` | `core/session-health-rules.md` |
   | `config/sources.md` | `shared/sources-overview.md` |
   | `config/notion-config.md` | `shared/notion-schema.md` |
   | `config/vps-connection.md` | `departments/facebook-ads-library/pre-flight.md` |
   | `memory/agent-operating-rules.md` | `core/operating-rules.md` |
   | `memory/founder-goals.md` | `core/founder.md` |
   | `memory/founder-taste.md` | `departments/facebook-ads-library/operational-memory/founder-taste.md` |
   | `memory/founder-feedback.md` | `departments/facebook-ads-library/operational-memory/founder-feedback.md` |
   | `memory/reported-products.md` | `shared/reported-products.md` |
   | `memory/rejected-products.md` | `shared/rejected-products.md` |
   | `memory/successful-patterns.md` | `shared/successful-patterns.md` |
   | `memory/failed-patterns.md` | `shared/failed-patterns.md` |
   | `memory/session-learnings.md` | `departments/facebook-ads-library/operational-memory/learnings.md` |
   | `memory/seen-advertisers.md` | `departments/facebook-ads-library/operational-memory/seen-advertisers.md` |
   | `memory/proposed-core-updates.md` | `review/promotion-queue.md` |
   | `memory/kids-vertical-hypothesis.md` | `departments/facebook-ads-library/current-context/kids-niche.md` |
   | `workflows/daily-scout.md` | `departments/facebook-ads-library/workflow.md` |
   | `workflows/notion-update.md` | `shared/notion-workflow.md` |
   | `workflows/product-validation.md` | `shared/product-validation.md` |
   | `workflows/telegram-report.md` | `shared/telegram-report.md` |
   | `skills/wow-factor-analysis.md` | `shared/skills/wow-factor.md` |
   | `skills/ugc-analysis.md` | `shared/skills/ugc.md` |
   | `skills/trend-analysis.md` | `shared/skills/trend.md` |
   | `skills/sourcing-analysis.md` | `shared/skills/sourcing.md` |
   | `skills/shophunter-analysis.md` | `shared/skills/shophunter.md` |
   | `skills/paid-traffic-analysis.md` | `shared/skills/paid-traffic-analysis.md` |
   | `skills/product-discovery.md` | `shared/skills/product-discovery.md` |
   | `skills/fb-ads-keyword-scan.md` | `departments/facebook-ads-library/methods/keyword-scan.md` |

3. Update the **File Map** section in CLAUDE.md (lines 57–67) to reflect the
   new structure. Replace the existing file map with:

   ```
   ## File Map
   ```
   ```
   core/         → company-level rules (identity, mindset, filters, scoring, founder, operating rules)
   departments/  → channel-specific operations (currently only facebook-ads-library/)
   shared/       → channel-agnostic resources (Notion, product logs, patterns, analysis skills)
   review/       → promotion queue for moving operational learnings into core
   prompts/      → ready-made session prompts
   outputs/      → generated daily reports
   research/     → research outputs
   archive/      → archived versions and original files
   ```
   ```

4. **Do not modify any other section** of CLAUDE.md in this phase.
   The "Default Behavior", "Category focus", "Key Rules" sections may contain
   outdated strategy text — that is a separate post-migration cleanup. Not now.

5. Commit:
   ```bash
   git add CLAUDE.md archive/CLAUDE-v1.md
   git commit -m "Phase 4: update CLAUDE.md path references to new structure"
   ```

**Report to Marina:** `git diff HEAD~1 -- CLAUDE.md` (full diff), and
confirm: only path strings changed, no rule text was modified.

**STOP — wait for Marina's OK before Phase 5.**

---

### PHASE 5 — Validation: find and fix broken internal links

**Goal:** find every file that references the old path structure and update
those references to the new paths. **Paths only — do not edit surrounding
text, do not improve wording, do not consolidate duplicates.**

Steps:

1. Search for old path references across the new structure:
   ```bash
   cd /Users/marinapetuk/Desktop/АГЕНТЫ/market-research-agent
   grep -rn "brain/" core/ departments/ shared/ review/ 2>/dev/null
   grep -rn "criteria/" core/ departments/ shared/ review/ 2>/dev/null
   grep -rn "workflows/" core/ departments/ shared/ review/ 2>/dev/null
   grep -rn "memory/" core/ departments/ shared/ review/ 2>/dev/null
   grep -rn "config/" core/ departments/ shared/ review/ 2>/dev/null
   grep -rn "skills/" core/ departments/ shared/ review/ 2>/dev/null
   ```

2. For each match, decide:
   - If the match is a **path reference** (something like `see config/notion-config.md`
     or `read memory/founder-taste.md`) → update it to the new path from the
     table in Phase 4.
   - If the match is **historical text** that just happens to contain the
     old path (for example inside `archive/`, inside `SYSTEM_ARCHITECTURE_SNAPSHOT.md`,
     or inside an old `outputs/daily-reports/*.md`) → **leave it alone**.
     Historical documents must remain as-is.

3. **Specifically do not edit:**
   - Anything inside `archive/`
   - `SYSTEM_ARCHITECTURE_SNAPSHOT.md` (point-in-time historical reference)
   - Anything inside `outputs/daily-reports/`
   - `run_scout.sh` (legacy entry point)
   - Anything inside `prompts/`

4. After all path updates are applied, sanity-check the system:
   ```bash
   # Verify every file referenced in core/ exists
   grep -rohn "core/[a-z-]*\.md\|departments/[a-z-/]*\.md\|shared/[a-z-/]*\.md\|review/[a-z-]*\.md" core/ departments/ shared/ review/ | sort -u
   ```
   Check each path exists. Report any that don't.

5. Commit:
   ```bash
   git add -A
   git commit -m "Phase 5: fix broken internal path references in new structure"
   ```

**Report to Marina:** total number of files modified, total number of path
strings updated, list of any paths that could not be resolved.

**STOP — Marina verifies the system is functional. After her OK, migration is
complete.**

---

## WHAT NOT TO DO (mirror of Marina's list)

- Do not delete files.
- Do not clean up legacy folders (`brain/`, `criteria/`, `workflows/`,
  `memory/`, `config/`, `skills/`). They stay in place with `.gitkeep`.
- Do not edit the content of moved files — only their paths.
- Do not touch `outputs/`.
- Do not touch `prompts/`.
- Do not touch `run_scout.sh`.
- Do not perform rule deduplication (that's a separate future task).
- Do not "optimize" or rewrite any document.
- Do not improve wording, fix typos, or consolidate similar text.
- Do not edit `SYSTEM_ARCHITECTURE_SNAPSHOT.md`.
- Do not edit anything inside `archive/`.

---

## ROLLBACK

If anything goes wrong at any phase, the rollback is simple:

```bash
git checkout pre-migration-v2-backup
```

or, to undo just the last phase:

```bash
git reset --hard HEAD~1
```

The `pre-migration-v2-backup` branch is the single source of truth for
the pre-migration state. Do not delete it until Marina explicitly says so,
weeks after the migration is validated and stable.

---

## SUMMARY OF FILE OPERATIONS

| Operation | Count |
|---|---|
| `git mv` operations (move + rename) | 36 |
| New files created | 1 (`departments/facebook-ads-library/README.md`) |
| Files merged | 1 pair → `shared/sources-overview.md` (with original archived) |
| Files archived (preserved copy) | 2 (`archive/CLAUDE-v1.md`, `archive/sources-capability-map-original.md`) |
| Files deleted | **0** |
| Files with content modified | **1** only (`CLAUDE.md` — path references only, in Phase 4) |
| Old folders removed | **0** (all stay with `.gitkeep`) |

---

## AFTER MIGRATION (not part of this work)

Once Marina has validated the migration is stable, she will decide separately
what to do about:
- Rule deduplication (Step 5 from `SYSTEM_ARCHITECTURE_SNAPSHOT.md`)
- Outdated strategy text in `CLAUDE.md` (`Health/Beauty/Fitness` focus,
  `TikTok/Meta` as primary sources)
- Whether to eventually remove empty legacy folders
- Whether to promote `founder-taste.md` and `founder-feedback.md` from the
  FB department into `shared/` once Marina's taste is stable enough

None of those are part of this migration.
