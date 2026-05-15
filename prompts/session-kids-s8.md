# SESSION 8 — KIDS VERTICAL — KEYWORD-FIRST DEEP SCAN

## Context
Первая сессия нового алгоритма: **Keyword-First Deep Scan**.
Вертикаль: **Kids** (baby / toddler / infant / newborn / mom).
Цель: дать рынку самому показать, что тестируется прямо сейчас.
НЕ начинать с product hypothesis — начинать с keyword → 300-500 ads → fast filter.

---

## ШАГ 0 — VPS (ПЕРВОЕ ДЕЙСТВИЕ, ОБЯЗАТЕЛЬНО)

```bash
ssh -i ~/.ssh/market_research_vps root@5.78.217.133
```

После подключения — обязательные 4 проверки (все должны пройти):

```bash
# 1. Нет параллельных процессов
ps aux | grep claude | grep -v grep     # если есть — сообщить Марине, НЕ запускать
ps aux | grep facebook_scraper | grep -v grep   # то же самое

# 2. FB сессия существует (без неё лимит 28 ads — бесполезно)
ls -la /opt/market-research-agent/cookies/fb_session.json

# 3. Скрапер использует JS scroll (не mouse.wheel)
grep 'window.scrollBy' /opt/market-research-agent/skills/facebook_scraper.py

# 4. Scraper файл на месте
ls /opt/market-research-agent/skills/facebook_scraper.py

cd /opt/market-research-agent/
```

Если любая из 4 проверок не прошла → сообщить Марине точную ошибку. НЕ продолжать. НЕ заменять WebSearch-ом.

---

## ШАГ 1 — Load Files (до любой работы)

Прочитать в порядке:
1. `brain/system.md`
2. `brain/mindset.md`
3. `criteria/mandatory-filters.md`
4. `criteria/scoring-system.md`
5. `memory/reported-products.md` — антидубликат-проверка
6. `memory/rejected-products.md` — паттерны провала, пропускать быстрее
7. `memory/founder-taste.md`
8. `memory/founder-feedback.md`
9. `memory/founder-goals.md`
10. `memory/session-learnings.md` — может содержать overrides для текущей сессии
11. `memory/seen-advertisers.md` — передаётся в `--seen` флаг scraper'у
12. `memory/kids-vertical-hypothesis.md` — план вертикали Kids на 10-20 сессий
13. `config/vps-connection.md` — параметры подключения и команды

---

## ШАГ 2 — Keyword план на эту сессию

Приоритет Session 8 (первая сессия Kids):

| Раунд | Keyword | Sort | Цель |
|-------|---------|------|------|
| Round 1 | `baby` | Most recent | Свежие entrants 2026 — кто запустился недавно |
| Round 2 | `baby` | Impressions: high to low | Proven winners — кто уже масштабировался |
| Round 3 (если остаётся контекст) | `toddler` | Most recent | Второй ★★★ keyword |

**Правило:** 1 keyword × 2 sorts (300-500 ads каждый) >> 2 keywords × 200 ads.
Глубина важнее ширины.

---

## ШАГ 3 — Round 1: baby / Sort A (Most recent)

### Команда на VPS:

```bash
cd /opt/market-research-agent/

nohup python3 skills/facebook_scraper.py \
  --deep \
  --sort=recent \
  --since=2026-01-01 \
  --seen=memory/seen-advertisers.md \
  --output=/tmp/r1_baby_recent.json \
  "baby" \
  > logs/fb_s8_r1_baby_recent.log 2>&1 &

echo "Round 1 PID: $!"
```

Мониторинг прогресса:
```bash
tail -f logs/fb_s8_r1_baby_recent.log
# ключевые строки для мониторинга: [SCROLL] Batch N/60: +X new → Y unique ads
```

Когда завершится — читать JSON (не stdout лог):
```bash
# Метаданные запуска (сколько собрано, время, keyword)
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 \
  "python3 -c \"import json; d=json.load(open('$(ls -t /opt/market-research-agent/logs/facebook_ads_*.json | head -1)')); print('META:', d['meta'])\""

# Полный список рекламодателей
ssh -i ~/.ssh/market_research_vps root@5.78.217.133 \
  "cat \$(ls -t /opt/market-research-agent/logs/facebook_ads_*.json | head -1)"
```

### Fast Filter (5-10 сек на объявление)

**REJECT немедленно если:**
- Цена явно < $30 или > $120
- Одежда, еда, подписка
- Бренд очевидно legacy (Amazon, Walmart, Carter's, Graco, Chicco, Owlet, Nanit, Boppy)
- Услуга, не физический продукт
- Уже в `reported-products.md` или `rejected-products.md`
- Нет visual hook (скучное изображение без wow-элемента)
- Аффилиат (comment-for-link паттерн)
- `started_running` = 2023 или раньше → слишком established (исключение: если active_ads_count ≥ 5 → category validator, не для входа)

**KEEP для дальнейшего анализа если:**
- Физический продукт $30-120
- Свежий бренд (домен не узнаваем)
- `started_running` = 2026 → fresh entrant, приоритет
- `started_running` = 2025 + `active_ads_count` ≥ 2 → проверен временем
- Wow-элемент или визуальная трансформация
- Эмоциональный триггер очевиден (страх, безопасность, развитие ребёнка)

**Примечание по keyword "baby":** ожидать 50-70% noise (фарма, FMCG, приложения, legacy retail). Это нормально для широкого keyword — задача fast filter именно в том, чтобы это вычистить быстро.

Логировать: `domain | price signal | first seen date | keep/reject | reject reason`

### Round 1 Checkpoint (после обработки всех результатов)

Отчитаться Марине:
```
ROUND 1 CHECKPOINT
Keyword: baby | Sort: Most recent | Raw ads collected: [N] | Unique advertisers: [N]
Passed fast filter: [N] ([%])
Categories observed: [list — что рекламируется в Kids прямо сейчас]
Notable candidates: [domain | started: MMM YYYY | active_ads: N | price | hook]
Patterns: [что повторяется?]
→ Готов к Round 2? [да/нет + причина]
```

Ожидаемые цифры: 500-580 raw ads → 150-200 unique advertisers → 20-40% noise (фарма, legacy, услуги) → 80-120 чистых рекламодателей для fast filter.

---

## ШАГ 4 — Round 2: baby / Sort B (Impressions: high to low)

После OK от Марины на Round 2.

### Команда на VPS:

```bash
nohup python3 skills/facebook_scraper.py \
  --deep \
  --sort=impressions \
  --since=2026-01-01 \
  --seen=memory/seen-advertisers.md \
  --output=/tmp/r2_baby_impressions.json \
  "baby" \
  > logs/fb_s8_r2_baby_impressions.log 2>&1 &

echo "Round 2 PID: $!"
```

### После Round 2 — сравнить с Round 1:

Что появляется в **обоих** раундах (и по новизне, и по импрессиям)?
→ **Strong double signal** — приоритет для обязательных фильтров.

Что только в Round 1 (новое, ещё без импрессий)?
→ Early entrant — риск выше, но может быть opportunity window.

Что только в Round 2 (impressions, но не новое)?
→ Established players — полезны для понимания saturation, не для входа.

---

## ШАГ 5 — Round 3: toddler / Sort A (если остаётся контекст)

После OK от Марины.

```bash
nohup python3 skills/facebook_scraper.py \
  --deep \
  --sort=recent \
  --since=2026-01-01 \
  --seen=memory/seen-advertisers.md \
  --output=/tmp/r3_toddler_recent.json \
  "toddler" \
  > logs/fb_s8_r3_toddler_recent.log 2>&1 &

echo "Round 3 PID: $!"
```

---

## ШАГ 6 — Обязательные фильтры (для KEEP кандидатов)

Применить `criteria/mandatory-filters.md` ко всем прошедшим fast filter.

### Filter Group A (самые быстрые):
- Результат визуально верифицируем за 30 сек?
- < 100 активных конкурентных объявлений?
- Generic / white-label (не branded proprietary)?

### Filter Group B (если прошли A):
- Ценность понятна за 3 секунды?
- Эмоциональный триггер?
- Масштабируемая аудитория?
- Можно источник из Китая?
- 3+ creative angles?
- Есть competitor ad activity ИЛИ organic momentum?

---

## ШАГ 7 — Scoring

Применить `criteria/scoring-system.md` только для прошедших все обязательные фильтры.
Минимальный порог для репорта: **65/100**.
Score 85+ → deep analysis автоматически.

Kids-специфичные бонусы при оценке:
- **+5** если продукт адресует safety/security триггер у родителей
- **+5** если очевидна визуальная демонстрация (видео-дружелюбный продукт)
- **+3** если аудитория охватывает 2+ sub-сегмента Kids (newborn + toddler, mom + baby)

---

## ШАГ 8 — Психологические механизмы (накапливать по сессиям)

Для каждого найденного продукта отметить доминирующий механизм:
- **Страх / безопасность** — "мой ребёнок в безопасности"
- **Развитие** — "мой ребёнок развивается лучше"
- **Convenience** — "это делает мою жизнь родителя легче"
- **Guilt reduction** — "я хороший родитель даже когда занят"
- **Health** — "это полезно для здоровья ребёнка"
- **Bonding** — "это сближает меня с ребёнком"

Продукты, активирующие 2+ механизма одновременно → более высокий potential.

---

## Output Format (обязательный)

### В чате — ТОЛЬКО короткий:
```
[Product Name] | Score XX | [Worth Testing / Needs Verification / Skip]
→ [1-2 строки: почему интересно + главный риск]
```

Полный product card → только в Notion (не в чате).

### В Notion — для каждого продукта 65+:
Заполнить по `config/notion-config.md`.
Язык: русский.
Founder Notes / Founder Review: оставить пустым — Marina заполняет вручную.

---

## Pivot Rules

### Менять keyword если:
- 80%+ результатов — услуги, аффилиаты, нерелевантный контент
- Все активные рекламодатели — legacy brands (Carter's, Graco, Gerber)
- 0 продуктов в $30-120 после полного скана

### Объявлять pivot явно:
`PIVOT — [причина] — [новый keyword]`
Не менять курс молча.

---

## Session Health — Self-Monitor

Сообщить Марине если:
- 3+ раунда дают 0 кандидатов после fast filter
- 80%+ объявлений — аффилиаты или legacy
- Контекст заканчивается — краткое резюме + вопрос как продолжать
- Sort button не найден или labels изменились → screenshot + alert

---

## ШАГ 9 — End of Session (обязательный протокол)

Запустить полный Learning Protocol (`workflows/daily-scout.md` STEP 8):

1. Обновить `memory/seen-advertisers.md` — добавить все просмотренные домены
2. Обновить `memory/reported-products.md` — добавить продукты 65+
3. Обновить `memory/rejected-products.md` — добавить заметные rejections + паттерны
4. Дописать в `memory/session-learnings.md`:
   - Какие категории Kids появлялись чаще всего
   - Какие keywords дали больше viable candidates
   - Паттерны (ценовые, визуальные, эмоциональные механизмы)
   - Сколько объявлений реалистично за раунд (обновить capacity table)
5. Дописать в `memory/kids-vertical-patterns.md` (создать если нет):
   - Emerging categories в Kids
   - Price clusters ($30-49, $50-69, $70-99, $100-120)
   - Top hooks/triggers observed
   - Keywords ranked by signal quality
6. Сохранить все продукты 65+ в Notion
7. Git commit всех изменений memory файлов

Git commit message format:
```
Scout session 8: Kids vertical — [N] products reported ([keyword list])
```

---

## Forbidden Errors

❌ WebSearch вместо VPS + FB Ads Library — недопустимо
❌ Запускать без pre-run safety check (ps aux)
❌ Изобретать URLs если не нашёл — писать "Not found"
❌ Форсировать продукт если сигнал слабый — честный нулевой раунд ок
❌ Суммировать Tier 3 сигналы (WebSearch) в Tier 2 вывод
❌ Менять курс без явного объявления PIVOT
❌ Редактировать brain/, criteria/, config/ файлы во время scout сессии
