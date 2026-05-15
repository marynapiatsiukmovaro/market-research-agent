# FB ADS LIBRARY — KEYWORD SCAN SCRIPT

**Tool:** VPS + Facebook Ads Library (direct browser/scraper access)
**Created:** 2026-05-15
**Purpose:** Keyword-First Deep Scan алгоритм — Marina's method

---

## ОБЯЗАТЕЛЬНО ПЕРЕД ЗАПУСКОМ

1. Убедиться, что работаешь на VPS (не локально)
2. Проверить: scraper/browser запущен, FB Ads Library доступна
3. Прочитать `memory/reported-products.md` — дубли не искать
4. Прочитать `memory/rejected-products.md` — пропускать похожие паттерны

---

## ПАРАМЕТРЫ ЗАПУСКА

```
URL: https://www.facebook.com/ads/library/

Filters:
  - Ad category: All ads
  - Country: United States
  - Language: English
  - Status: Active
  - Date range: Start date FROM January 1, 2026 TO [today]

Search: [keyword]

Sort A run: Sort by "Newest" (сначала новые — свежие entrants)
Sort B run: Sort by "Most active" or longest running (proven winners)
```

---

## АЛГОРИТМ СКАНИРОВАНИЯ

### ШАГ 1 — FAST FILTER (5-10 сек на объявление)

Для каждого объявления быстро проверить:

```
REJECT немедленно если:
□ Цена визуально < $30 (слишком дёшево)
□ Цена > $120 (выше потолка)
□ Продукт — одежда, еда, подписка
□ Бренд очевидно legacy (Amazon, Walmart, Target)
□ Это услуга, не физический продукт
□ Уже в reported-products.md или rejected-products.md
□ Нет visual hook (скучное изображение)

KEEP если:
□ Физический продукт $30-120
□ Есть wow-element или визуальная трансформация
□ Свежий бренд (домен не узнаваем)
□ Эмоциональный триггер очевиден
```

Логировать: domain | price signal | first seen | keep/reject | reject reason

### ШАГ 2 — CHECKPOINT после 100 объявлений

- Сколько прошло fast filter из 100? (цель: 10-20%)
- Есть ли emerging patterns? (повторяющиеся категории?)
- Продолжать или сменить keyword?

### ШАГ 3 — ОБЯЗАТЕЛЬНЫЕ ФИЛЬТРЫ (для KEEP кандидатов)

Применить `criteria/mandatory-filters.md` ко всем прошедшим fast filter:

```
FILTER GROUP A (самые быстрые):
□ Результат визуально верифицируем за 30 сек?
□ < 100 активных конкурентных объявлений?
□ Generic / white-label (не branded proprietary)?

FILTER GROUP B (если прошли A):
□ Ценность понятна за 3 секунды?
□ Эмоциональный триггер?
□ Масштабируемая аудитория?
□ Можно источник из Китая?
□ 3+ creative angles?
□ Есть competitor ad activity ИЛИ organic momentum?
```

### ШАГ 4 — SCORING (только для прошедших все фильтры)

Применить `criteria/scoring-system.md`.
Минимальный порог для репорта: 65/100.

### ШАГ 5 — FIND REAL LINKS

Для каждого кандидата 65+:
- Ad Link: прямая ссылка на объявление в FB Ads Library
- Store Link: DTC сайт бренда (verify не broken, не scam)
- Если не найдено → "Not found", НЕ придумывать URL

---

## CAPACITY ESTIMATION (обновить после Session 8)

| Metric | Estimate | Confirmed |
|--------|----------|-----------|
| Fast filter speed | 5-10 sec/ad | TBD Session 8 |
| Ads per round (realistic) | 300-500 | TBD |
| Ads per session (2 rounds) | 600-1000 | TBD |
| Pass rate (fast filter) | ~10-15% | TBD |
| Candidates for scoring | 30-75 per session | TBD |
| Reported products (65+) | 2-8 per session | TBD |

**Обновить эту таблицу после Session 8 с реальными данными.**

---

## OUTPUT FORMAT (после каждого раунда)

```
ROUND [N] CHECKPOINT
Keyword: [X] | Sort: [A/B] | Scanned: [N] ads
Passed fast filter: [N] ([%])
Categories observed: [list]
Notable candidates: [list with domain + price + hook in 1 line each]
Patterns: [что повторялось?]
```

---

## ОШИБКИ КОТОРЫЕ ЗАПРЕЩЕНЫ

❌ WebSearch вместо прямого FB Ads Library — недопустимо
❌ Инвентировать URLs если не нашёл — лучше "Not found"
❌ Форсировать продукт если сигнал слабый — честный нулевой раунд ок
❌ Суммировать Tier 3 сигналы в Tier 2 вывод — анти-галлюцинация правило
❌ Продолжать раунд если 70%+ результатов — услуги/аппы/аффилиаты
