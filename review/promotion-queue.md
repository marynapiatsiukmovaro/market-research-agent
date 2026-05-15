# PROPOSED CORE UPDATES

**Marina reviews this file and decides. Agent only adds items — never promotes automatically.**

Items here are candidates for promotion into core documents.
They come from session-learnings.md when a pattern is confirmed across multiple sessions.

Agent may APPEND new items. Agent must NEVER self-promote items into core files.
Marina sets each item to: **Promote → Wait → Reject**

---

## Pending Review

### [Output format — no product card in chat]
**Observation:** Агент пишет полный product card (8+ строк) в чат — это дублирует Notion и тратит токены впустую. Марина явно указала: детали в чат не нужны.
**Why it matters:** Экономит 30-40% токенов на отчёт. Чат остаётся чистым и оперативным.
**Affected file(s):** brain/system.md (Output Format section)
**Confidence:** High — прямой фидбек от Марины, Session 4
**Recommendation:** Promote
**Rule to add:** "В чате — только: Score + 1-2 строки почему + Recommendation. Полный product card → сразу в Notion, не в чат."
**Added:** 2026-05-14, Session 4
**Source learnings:** Прямой фидбек Марины в конце Session 4

### [Pivot communication + round reporting]
**Observation:** Марина явно подтвердила ценность: (1) сообщать о смене курса ("pivot") в процессе работы, (2) описывать план каждого раунда до его запуска с ожиданием OK. Это позволяет менять направление до того, как раунд потрачен впустую.
**Why it matters:** Даёт Марине контроль над стратегией в реальном времени без ожидания конца сессии.
**Affected file(s):** workflows/daily-scout.md (round protocol)
**Confidence:** High — прямой фидбек от Марины, Session 4
**Recommendation:** Promote
**Rule to add:** "Перед каждым раундом — объяви keyword paths и логику. Если меняешь вертикаль или стратегию — назови это pivot и объясни почему."
**Added:** 2026-05-14, Session 4
**Source learnings:** Прямой фидбек Марины в конце Session 4

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
**Source learnings:** session-learnings.md entries [list dates]
```

### [Pet vertical AOV ceiling — не жёсткий $79]
**Observation:** В Pet Tech вертикали Marina явно допускает AOV до ~$120 при исключительных условиях: сильный visual demo, высокая эмоциональная привязанность к питомцу, premium DTC positioning, Meta economics viable. Pet owners tolerate higher AOV than most verticals.
**Why it matters:** Текущий mandatory-filters.md говорит "over $100 = requires strong social proof, not suitable for cold traffic MVP" — это слишком жёстко для Pet Tech где $79-120 = working range.
**Affected file(s):** criteria/mandatory-filters.md (price ceiling rule) + criteria/scoring-system.md (Margin Potential calibration)
**Confidence:** High — прямой фидбек от Марины, Session 5
**Recommendation:** Promote (с уточнением: "в Pet vertical, с явным обоснованием")
**Added:** 2026-05-14, Session 5
**Source learnings:** session-learnings.md "[2026-05-14] Session 5 — Pet Tech Price Ceiling Relaxation"

### [Новый алгоритм discovery: Keyword-First Deep Scan]
**Observation:** Текущий алгоритм (product hypothesis → поиск) ограничен кругозором агента. Marina предложила принципиально другой подход: выбрать нишу → определить 20 ключевых слов → FB Ads Library с фильтром (English, Active, Jan 2026–now, sort by newest) → 200-500 объявлений на keyword → быстрый фильтр → детальный анализ выживших. Это позволяет находить продукты, которые нельзя было предсказать заранее.
**Why it matters:** Фундаментально меняет step 1 и step 2 в daily-scout.md. Без этого изменения агент ищет в пространстве своего кругозора, а не в пространстве рынка.
**Affected file(s):** workflows/daily-scout.md (STEP 1 — Scan Sources), config/sources.md
**Confidence:** High — прямой фидбек от Марины, Session 7, подтверждён неудачей противоположного подхода
**Recommendation:** Promote — после проверки в 1-2 сессиях с VPS scraper
**Added:** 2026-05-15, Session 7
**Source learnings:** session-learnings.md "[2026-05-15] Session 7 — КРИТИЧНО: Новый алгоритм поиска"

---

## Decided

| Date | Item | Decision | Notes |
|------|------|----------|-------|
| — | — | — | *Empty — no decisions yet* |
