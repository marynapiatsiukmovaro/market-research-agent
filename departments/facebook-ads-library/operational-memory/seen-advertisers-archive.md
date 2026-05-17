# SEEN ADVERTISERS — ARCHIVE

Historical log of advertisers from sessions beyond the 20-session active window.

**Agent rule:** Do NOT load this file during scout sessions — never required for discovery.
**Scraper rule:** Scraper does NOT use this file. Only `seen-advertisers.md` (active, last 20 sessions) is used.
**Purpose:** Preserved for historical reference and audit only.

Format: same as seen-advertisers.md — domain | reason_skipped | date_seen

---

## How entries get here

At STEP 8 (end of session), agent counts `## Session` headers in seen-advertisers.md.
If count > 20 → oldest session block (header + all entries) is moved here (appended below).
Rotation repeats until ≤ 20 sessions remain in active file.
See op-rules.md RULE 13 for full protocol.

---

<!-- Archived session blocks will be appended below by the agent at rotation time -->
