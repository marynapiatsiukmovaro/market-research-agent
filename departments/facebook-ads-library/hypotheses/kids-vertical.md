# KIDS VERTICAL — MULTI-SESSION HYPOTHESIS

**Created:** 2026-05-15, Session 7 (Marina's direct instruction)
**Status:** ARCHIVED — superseded by Broad Horizontal Discovery (Session 15, 2026-05-17)
**Algorithm:** Keyword-First Deep Scan (VPS + FB Ads Library)
**Archive note:** Keyword verdicts preserved in keyword-map.md. Reported products in shared/reported-products.md. Reactivate only on Marina's explicit instruction.

---

## Гипотеза

Стандартный подход (product hypothesis → search) ограничен кругозором агента и Марины.
Выигрышные продукты — это НЕОЧЕВИДНЫЕ продукты, которые нельзя было предсказать.

**Решение:** Дать рынку самому показать, что тестируется прямо сейчас.
Инструмент: FB Ads Library — прямой доступ через VPS scraper.
Метод: Перебор ключевых слов вглубь (200-500+ объявлений на keyword).

**Прогноз:** За 10-20 сессий по нише Kids сформируется:
- Карта активных DTC категорий в Kids
- Паттерны успешных продуктов (ценовые, визуальные, триггерные)
- Список winners, которые невозможно было найти без глубокого сканирования

---

## Вертикаль: KIDS

**Почему Kids:**
- Родительские триггеры — сильнейшие (страх, безопасность, развитие, любовь)
- Ценовой диапазон $39-99 реалистичен (родители платят больше за детей)
- DTC FB реклама активна: много брендов запускается через Facebook/Instagram
- Белый лейбл доступен: большинство детских аксессуаров → generic sourcing из Китая
- Множество под-аудиторий: новорождённые, toddler, дошкольники, школьники, беременные

---

## 20 Ключевых Слов (в приоритетном порядке)

| # | Keyword | Ожидаемый тип продуктов | Приоритет | Verified Status (S8–S9) |
|---|---------|------------------------|-----------|------------------------|
| 1 | baby | всё для младенцев — широкий вход | ★★★ | ❌ Last resort (349 ads, 0 reportable — big brand noise) |
| 2 | kids | школьный возраст, игрушки, гаджеты | ★★★ | ❌ Dead (53 ads, scroll stall, FMCG-dominated) |
| 3 | toddler | 1-3 года, развитие, безопасность | ★★★ | ❌ Replace (327 ads, 0 reportable — use specific product keywords) |
| 4 | infant | новорождённые 0-12 мес | ★★ | — Not tested |
| 5 | newborn | первые недели | ★★ | — Not tested |
| 6 | mom | продукты через маму (не ребёнка) | ★★ | ⚠️ Weak (tested via "mom life": 375 ads, UGC/affiliate-heavy, 0 reportable) |
| 7 | nursery | комната ребёнка, декор, безопасность | ★★ | — Not tested |
| 8 | stroller | коляски, аксессуары к коляскам | ★★ | ⚠️ Partial (S8: signal found — Hoppie score 65; retry with full session) |
| 9 | baby monitor | наблюдение за ребёнком | ★★ | ❌ Dead (S8: legacy tech brands — Owlet, Nanit dominate) |
| 10 | potty | приучение к горшку | ★ | ⚠️ Price floor (S9 via "toddler": 3 DTC brands active, but $7–37 — below $39) |
| 11 | teething | прорезывание зубов | ★ | — Not tested |
| 12 | feeding | кормление, бутылочки, слюнявчики | ★★ | — Not tested |
| 13 | breastfeeding | молокоотсосы, подушки, аксессуары | ★★ | — Not tested |
| 14 | sleep baby | сон ребёнка, пеленание, белый шум | ★★★ | ⚠️ Narrow (267 ads, 2 borderline at 66–67 — retry as "baby swaddle" or "sleep sack") |
| 15 | bath baby | купание, термометры, ванночки | ★ | — Not tested |
| 16 | baby carrier | слинги, эрго-рюкзаки | ★★ | ✅ Best signal (S8: Bambora score 73, 561 ads — use again) |
| 17 | diaper | подгузники, аксессуары | ★ | — Not tested |
| 18 | learning toy | развивающие игрушки, Монтессори | ★★ | ⚠️ Weak (S9 via "Montessori toy": 81 ads, dropship/established — use specific: "busy board") |
| 19 | pregnancy | до рождения, для беременных | ★★ | — Not tested |
| 20 | child safety | защита дома, розетки, углы | ★ | ❌ Dead (S9: 327 ads, 60% local services, regulatory space) |

---

## FB Ads Library — Параметры Сканирования

**Фиксированные фильтры (не менять):**
- Language: English
- Status: Active (активные объявления)
- Date range: January 1, 2026 → [текущая дата]
- Country: United States

**Сортировка — тестировать обе в каждой сессии:**
- Sort A: **Newest first** (по убыванию даты запуска) → ловит свежих entrants
- Sort B: **Most active / longest running** → ловит proven winners

**Глубина сканирования (подтверждено Session 8 Part 2):**
- Стандарт: target 500, реальный диапазон 500–580 raw ads/keyword (hard cap 600)
- После дедупликации по рекламодателю: 150–200+ unique advertisers/keyword
- Скрапер сам останавливается после первого batch, пересёкшего 500 (overshoot нормален)
- Масштабировать через breadth (больше keywords), НЕ через depth (выше 600 — detection risk)

---

## Структура Одной Сессии

### Раунд 1: Keyword X → Sort A (Newest)
- Сканировать 300-500 объявлений
- Fast filter (5-10 сек/объявление): pass / reject
- Логировать: brand domain, price signal, visual hook, reject reason

### Раунд 2: Keyword X → Sort B (Longest Active)
- Сканировать 300-500 объявлений
- Fast filter
- Сравнить с Round 1: что появляется в обоих? → Strong signal

### Раунд 3 (если остаётся контекст): Keyword Y → Sort A
- Новое ключевое слово по той же схеме

### Конец сессии:
- Суммировать: какие категории/продукты появились?
- Паттерны: что повторяется?
- Candidates для глубокого анализа (score 65+)
- Обновить memory

---

## Что Фиксировать После Каждой Сессии

В `departments/facebook-ads-library/operational-memory/learnings.md`:
- Какие ключевые слова дали больше viable candidates?
- Какие категории появляются чаще всего?
- Какие продукты прошли mandatory filter?
- Новые паттерны (ценовые, визуальные, аудиторные)
- Сколько объявлений реалистично за раунд и за сессию

В `departments/facebook-ads-library/operational-memory/kids-vertical-patterns.md` (создать после Session 8):
- Emerging categories in Kids
- Price clusters ($39-49, $50-69, $70-99)
- Top hooks/triggers observed
- Keywords ranked by signal quality

---

## Ожидаемый Результат через 10 Сессий

- Карта активных DTC категорий в Kids (по keyword)
- 5-15 reported products с confirmed FB ads
- Понимание entry windows (saturated vs open)
- Список неочевидных winners, которые невозможно было предсказать
- Паттерная база для Kids vertical

---

## Важные Ограничения

1. **VPS обязателен + 5 обязательных проверок перед каждым запуском:**
   ```bash
   # Проверка 1: VPS доступен
   ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "echo OK"
   
   # Проверка 2: fb_session.json существует
   ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "ls /opt/market-research-agent/cookies/fb_session.json"
   
   # Проверка 3: скрапер использует window.scrollBy (не mouse.wheel)
   ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "grep 'window.scrollBy' /opt/market-research-agent/skills/facebook_scraper.py"
   
   # Проверка 4: нет уже запущенного scraper процесса
   ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "ps aux | grep facebook_scraper | grep -v grep"
   
   # Проверка 5 (КРИТИЧНО — добавлена Session 9): сессия ещё действительна
   ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "python3 /tmp/check_session.py"
   # Должно вернуть: "SESSION OK: Logged in" + имя Mikhail Piatsiuk
   # Если "SESSION EXPIRED" → нужно обновить cookies (см. ниже)
   ```
   Если любая из пяти не прошла → остановиться, не продолжать.
   **Без действующей сессии = 19-32 ads/keyword (бесполезно). Без fb_session.json = то же самое.**

   **Если Проверка 5 показала SESSION EXPIRED — процесс обновления cookies:**
   1. Marina открывает Chrome → facebook.com → убеждается, что залогинена как Mikhail Piatsiuk
   2. DevTools (F12) → Network tab → нажать любой запрос к facebook.com → Headers → Request Headers → Cookie → скопировать всю строку (начинается с "datr=...")
   3. Передать строку агенту
   4. Агент создаёт fb_session.json и загружает на VPS:
      `scp -i ~/.ssh/market_research_vps /tmp/fb_session.json root@5.78.217.133:/opt/market-research-agent/cookies/fb_session.json`
   5. Повторить Проверку 5 → SESSION OK → можно запускать

2. **Обязательно проверять freshness** — ideal 2026, acceptable 2025, old = 2024+
3. **Mandatory filters применять ДО scoring** — не тратить время на нежизнеспособные
4. **Максимум 3 active candidates за раз** — не накапливать "maybe" пул без checkpoint
5. **Honest zero-product раунд приемлем** — не форсировать. Качество > квота.
6. **Price >$100 = НЕ автоматический reject** — смотреть mandatory-filters.md: если есть strong social proof (Shark Tank, 10K+ reviews, viral) → score продукт с ценовым штрафом. Reject только если score < 65.
