# Server Conventions — VPS file hygiene (ALL departments)

> Cross-department "house rules" for the shared VPS (`/opt/market-research-agent`).
> Marina-approved 2026-06-06 (S10). Deliberately LIGHT — minimal rules, maximum freedom.
> Every department working on this server follows these. Other projects (e.g. the launch
> department) read the copy at the VPS root: `/opt/market-research-agent/SERVER-CONVENTIONS.md`.

## The rules

1. **One department, one folder** under `logs/`. Each department keeps its own folder tidy;
   never dump into the shared root, never touch another department's folder.

2. **⛔ Deletion needs Marina's approval — always.** Never `rm` directly on the server.
   To remove anything: **move it** (`mv`) to `logs/_trash/YYYY-MM-DD/`. The trash is a safety
   net (recoverable). **Emptying the trash (permanent delete) happens only with Marina's OK.**
   This is the ONE hard rule. (Born from S10: a working file was overwritten with no recovery.)

3. **Hygiene by size-trigger only.** Only review a folder for cleanup when it has grown large
   (≈2–3 GB+). Otherwise leave it alone — do NOT prescribe what a department must/​must not store,
   do not restrict, do not "optimize" unprompted. What a department keeps is its own business.
   (Disk is large — 75 GB, ~10% used — so there is no space pressure; the trash can safely hold
   removed files as a backup.)

4. **VPS data has NO backup.** `logs/` and `cookies/` live only on the server (gitignored). So in
   ANY unexpected situation, **STOP and ask** — never overwrite or delete a working file to "fix"
   things fast. A new/edited dump or script writes to a TEST name first, never over a live file.

5. **Memory & rules are safe.** `core/ · departments/ · shared/` are markdown in git (versioned,
   backed up) — the "brain." Data cleanup never touches them. Notion is fully independent of the
   VPS too — file cleanup/moves never affect the Notion tracker.

## Trash mechanics
- `logs/_trash/README.md` states the rule on the server itself.
- Move to delete: `mv <path> logs/_trash/$(date +%F)/`.
- Restore: `mv logs/_trash/<date>/<file> <original-path>`.
- Purge (permanent): only on Marina's explicit OK, e.g. `rm -rf logs/_trash/<date>`.

## Target folder grouping (aspirational — not a forced migration)
New departments are created already grouped: discovery departments (`storeleads`, `shophunter`,
`facebook-ads`) conceptually under "product discovery"; the launch department separate. Existing
working folders are NOT physically moved (script paths hardcode `logs/<dept>/…` — a move would
break them for no real gain; they are already organized siblings). Group new things, don't churn old.
