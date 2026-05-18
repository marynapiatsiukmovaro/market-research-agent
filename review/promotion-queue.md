# PROPOSED CORE UPDATES

**Marina reviews this file and decides. Agent only adds items — never promotes automatically.**

Items here are candidates for promotion into core documents.
They come from departments/facebook-ads-library/operational-memory/learnings.md when a pattern is confirmed across multiple sessions.

Agent may APPEND new items. Agent must NEVER self-promote items into core files.
Marina sets each item to: **Promote → Wait → Reject**

---

## Pending Review

---

### RULE 7 — fast_filter.py: добавить технический пайплайн в op-rules.md
**Observation:** RULE 7 в op-rules.md требует "только top 15-20 в чат" — но не указывает КАК это сделать технически. Нет ссылки на конкретный скрипт, нет команды. В Session 15 fast_filter.py упал с ошибкой regex → агент сделал fallback и вывел 238 рекламодателей напрямую в чат (40-50% контекста потрачено зря). Постоянный скрипт `skills/fast_filter.py` теперь задеплоен на VPS.
**Why it matters:** Без конкретного скрипта правило не работает при первой же ошибке. Правило есть → реализации не было → контекст горит. Фикс: добавить в RULE 7 конкретный пайплайн и ссылку на скрипт.
**Proposed addition to RULE 7:**
```
Standard pipeline (run on VPS after every scrape):
  python3 skills/fast_filter.py /tmp/{keyword}_results.json --top=20
Output: top 20 candidates printed to chat; full list saved to /tmp/{keyword}_results_candidates.txt
Script location: /opt/market-research-agent/skills/fast_filter.py
If fast_filter.py fails: fix the script on VPS — do NOT dump raw advertiser list to chat.
```
**Affected file(s):** `departments/facebook-ads-library/operational-memory/op-rules.md` → RULE 7
**Confidence:** High (failure observed Session 15, root cause clear, fix tested)
**Recommendation:** Promote
**Added:** 2026-05-18, Session 15
**Source learnings:** Session 15 retrospective — RULE 7 implementation gap

---

## How to Add a New Item

Append to Pending Review using this format:

```
### [Short name]
**Observation:** what was consistently found across sessions
**Why it matters:** impact on product selection, scoring, or filtering
**Affected file(s):** which core file would change (brain/ / criteria/ / config/ / memory/)
**Confidence:** High / Medium / Low
**Recommendation:** Promote / Wait / Reject
**Added:** [YYYY-MM-DD], Session [N]
**Source learnings:** operational-memory/learnings.md entries [list dates]
```


---

## Decided

| Date | Item | Decision | Notes |
|------|------|----------|-------|
| 2026-05-17 | Output format — no product card in chat | ✅ Promoted | Implemented in core/identity.md — chat = Score + 1-2 lines + Recommendation only |
| 2026-05-17 | Pivot communication + round reporting | ✅ Promoted | Implemented in workflow.md STEP 1 — round announcement + pivot format added |
| 2026-05-17 | Keyword-First Discovery Algorithm | ✅ Promoted | Already in workflow.md STEP 1 + CLAUDE.md strategy — no additional change needed |
| 2026-05-17 | Pet vertical AOV ceiling $79→$120 | ✅ Promoted (expanded) | Resolved as universal rule: $100–170 = score normally with Margin cap 5/10. Updated mandatory-filters.md + scoring-system.md + op-rules.md RULE 12. Applies to ALL categories, not just Pet. |
