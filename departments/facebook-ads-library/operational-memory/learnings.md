# SESSION LEARNINGS

**Active temporary guidance — read at session start, before scanning anything.**

These are working hypotheses and tactical discoveries from recent sessions.
They are NOT core rules. They do not override core/.
Items here expire after 7 sessions or after Marina promotes/rejects them via review/promotion-queue.md.

Agent may APPEND new entries. Agent must NEVER edit or delete existing entries.
Marina promotes or rejects items manually via `review/promotion-queue.md`.

---

## ⚡ КРИТИЧЕСКИЕ ОПЕРАЦИОННЫЕ ПРАВИЛА (читать первыми — всегда)

> Эти правила были учтены в предыдущих сессиях, но потерялись из-за размера файла.
> Вынесены сюда для гарантированного попадания в первый read.

### ОП-1: fb_session.json — ПРАВИЛЬНЫЙ путь
Файл сессии находится ТОЛЬКО по этому пути: `/opt/market-research-agent/cookies/fb_session.json`
НЕ `/root/fb_session.json` и НЕ `/tmp/fb_session.json`.
Проверка: `ls /opt/market-research-agent/cookies/fb_session.json`

### ОП-2: Candidate list — НЕ выводить в чат полностью
После скрапинга полный список ВСЕГДА сохранять в файл на VPS: `/tmp/{keyword}_candidates.txt`
В чат выводить ТОЛЬКО топ-15-20 наиболее перспективных.
Сообщить путь: "Full list saved: /tmp/xyz_candidates.txt (N candidates)"
**Источник:** Session 10/11, Marina явно подтвердила — вывод 229 кандидатов = ~8-10% контекста за один блок.

### ОП-3: --sort=recent — статус
С работающей fb_session.json флаг --sort=recent НЕ вызывает login wall (подтверждено Session 8 Part 2 + Session 13).
НО: скрапер часто fallback-ается на impressions sort по умолчанию даже с флагом. Проверять URL в scraped data.
По умолчанию: запускать БЕЗ --sort (impressions = proven winners) если нет явной причины иначе.

### ОП-4: Три обязательных условия перед запуском скрапера
1. VPS подключён: `ssh root@5.78.217.133 "echo OK"` → OK
2. fb_session.json существует: `/opt/market-research-agent/cookies/fb_session.json` → EXISTS
3. Скрапер использует window.scrollBy: `grep "window.scrollBy" skills/facebook_scraper.py` → найдено
Без любого из трёх → 28 ads вместо 500+. ОСТАНОВИТЬСЯ и исправить.

### ОП-5: Параллельная верификация кандидатов
При verification stage делать 3-4 WebFetch ПАРАЛЛЕЛЬНО в одном response block.
Ускорение ~30-40%. НЕ делать последовательно.

### ОП-6: Дропшип-бренд = сигнал спроса, НЕ причина reject
Несколько доменов продают один продукт → это validation, не red flag.
Фильтровать по ПРОДУКТУ (цена, механизм, COGS), не по типу продавца.

---

## Current Focus

**Sessions 1+: Facebook Ads Library as primary discovery source (ongoing)**

- **Primary:** Facebook Ads Library (via VPS scraper) — all broad discovery here
- **Secondary:** Amazon, TikTok, AliExpress — for verification, or when a very strong external signal appears naturally; do not actively expand into other source systems yet
- **Why:** deepening Facebook Ads Library methodology — finding the right keywords, reading ad signals, calibrating entry windows — before diversifying sources

This focus applies until Marina says otherwise.

---

## Active Learnings

### [2026-05-15] Session 7 — Home/Kitchen: Structurally Weak for DTC FB Model
**Type:** Pattern
**Severity:** HIGH (prevents wasted sessions in retail-dominated categories)
**Confidence:** HIGH (confirmed across all 3 subcategories in one session)
**Evidence count:** 15+ brands checked, 3 subcategories explored
**Observation:** Home/Kitchen вертикаль показала структурное сопротивление DTC FB модели по трём причинам: (1) Retail-first ДНК — кухонные категории исторически идут через big box (Walmart, Target, Home Depot), не через DTC Facebook; (2) Amazon commodity trap — большинство продуктов либо <$35, либо Amazon-native без DTC play; (3) FoodSaver-эффект — legacy retail brands блокируют DTC innovation в потребительском сознании.
Конкретные паттерны: Spin scrubber = Amazon-native (45% ASINs в $20-50, 126 конкурирующих брендов); Food sealer = FoodSaver доминирует retail; Self-wringing mop = O-Cedar retail giant, 0 DTC FB advertisers.
Единственный частичный кандидат: Dovety ($59.99, FB confirmed) — но запущен 2023 (B0C ASIN), не проходит freshness filter.
**Applies to:** Home/Kitchen keyword selection — проверяй структуру канала перед входом в вертикаль
**Expires after:** Session 14

### [2026-05-15] Session 7 — КРИТИЧНО: Новый алгоритм поиска (Marina's insight)
**Type:** Tactical
**Severity:** CRITICAL (меняет фундаментальный подход к discovery)
**Confidence:** HIGH (Marina явно подтвердила как правильный направление)
**Evidence count:** Прямой фидбек от Марины, Session 7
**Observation:** Старый алгоритм (product hypothesis → deep dive) ограничен кругозором агента — можно найти только то, что уже можно представить. Марина предложила кардинально другой подход:

НОВЫЙ АЛГОРИТМ — Keyword-First Deep Scan:
1. Выбрать нишу (например, Kids)
2. Определить 20 широких ключевых слов для этой ниши
3. Открыть FB Ads Library → фильтр: English, Active ads, Jan 1 2026 – текущая дата, сортировка по убыванию (новые сначала)
4. Один раунд = 1-2 ключевых слова, анализировать 200-500 объявлений на каждое
5. Быстрый фильтр (5-10 сек на объявление) → keep/reject
6. Детальный анализ только тех, кто прошёл mandatory filters
7. Повторить для следующего ключевого слова

ПОЧЕМУ ЭТО ЛУЧШЕ: Система сама показывает, что рынок тестирует прямо сейчас — обнаруживаются продукты, которые нельзя было предсказать заранее. Именно здесь живут winners.

КЛЮЧЕВОЕ ТРЕБОВАНИЕ: Этот алгоритм требует прямого доступа к FB Ads Library (VPS scraper). WebSearch = Tier 3 сигналы, недостаточны для полноценного выполнения.

Сессионная структура: 5-15 сессий на одну нишу. Глубина важнее ширины.
**Applies to:** Все будущие scout сессии — это новый baseline алгоритм
**Expires after:** Session 20 или до замены новым подтверждённым алгоритмом

### [2026-05-15] Session 7 — Мёртвые ключевые слова: Home/Kitchen
**Type:** Warning
**Severity:** HIGH
**Confidence:** HIGH (подтверждено в сессии)
**Evidence count:** 3 субкатегории, 15+ брендов
**Observation:** Следующие ключевики для Home/Kitchen дают retail brands, Amazon-native commodity, или ценовой пол — не использовать:
- "self wringing mop" / "spin mop" → O-Cedar retail dominance, 0 DTC FB advertisers
- "handheld vacuum sealer" / "food sealer" → FoodSaver retail giant, 0 fresh DTC FB advertisers
- "home organizer" → (уже был в Session 4) Amazon affiliate spam
Spin scrubber = возможен при наличии свежего 2025-2026 DTC бренда, но требует VPS верификации.
**Applies to:** Home/Kitchen keyword selection
**Expires after:** Session 14

---

### [2026-05-15] Session 8 — Keywords: Broad = Noise, Specific = Signal
**Type:** Pattern
**Severity:** HIGH (влияет на keyword selection strategy)
**Confidence:** HIGH (6 keywords протестировано)
**Evidence count:** 6 keywords, два broad (baby, baby sleep) vs четыре specific
**Observation:** Keyword формула для Kids/Baby вертикали:
❌ ШУМНЫЕ (1 слово или common word): "baby", "baby sleep" → 80%+ noise (apps, pharma, FMCG giants, unrelated)
✅ ЧИСТЫЕ (2 слова, category-defining): "baby carrier", "nursing pillow", "stroller" → прямые DTC advertisers
Практическое правило: использовать 2-3 слова, описывающих конкретную продуктовую категорию.
**Applies to:** Kids vertical keyword selection
**Expires after:** Session 15

### [2026-05-15] Session 8 — Kids Vertical: Категорийная Карта (первичная)
**Type:** Signal
**Severity:** MEDIUM (первые данные, требуют подтверждения)
**Confidence:** MEDIUM (1 сессия, ~150 ads)
**Evidence count:** 6 keywords, 5 категорий проанализированы
**Observation:** Первичная карта Kids/Baby вертикали после Session 8:

ОТКРЫТЫЕ НИШИ (активные DTC, < saturated):
- Baby ring sling / soft carrier: Bambora ($59, 13+ ads, bamboraco.com) → OPEN entry window
- Stroller attachment/seat для 2го ребёнка: Hoppie ($79, 1 player) → VERY EARLY entry

ЗАКРЫТЫЕ / НЕРЕАЛИСТИЧНЫЕ (legacy or price):
- Baby monitor: Owlet ($100+), Nanit (legacy brands dominate)
- Smart baby bed/bassinet: Cradlewise $1000 → too expensive
- Premium stroller: Doona, UPPAbaby ($300-800) → luxury retail
- Nursing pillow: Boppy→Walmart, retail-dominant category

СРЕДНЯЯ ЗОНА (требуют доп. сессий):
- Diaper bag / mom bag: Emmafy, MINA BAIE, Tactical Baby Gear — активны, но цены не проверены
- Pregnancy pillow: babybub $49-75 — multi-product brand, слабый сигнал
- Nursing arm pillow: CozyArm (no domain found), multiple 2026 campaigns — нужна проверка

СЛЕДУЮЩИЕ KEYWORDS (не изучены):
- "pregnancy pillow" → проверить цены и валидацию
- "postpartum" → recovery products
- "baby wrap" → может дать другие sling brands
- "diaper bag" → проверить price range для Emmafy/MINA BAIE
- "toddler" → дошкольный возраст, другие категории

**Applies to:** Kids vertical — следующие сессии
**Expires after:** Session 15

### [2026-05-15] Session 8 — Bambora: Валидатор Baby Sling Carrier Категории
**Type:** Signal
**Severity:** HIGH (конкретный market signal с ценой и ad count)
**Confidence:** HIGH (found across 2 keywords, 13+ ad units confirmed)
**Evidence count:** "baby carrier" + "stroller" keywords, bamboraco.com verified
**Observation:** Bambora (bamboraco.com) — активный DTC FB advertiser для baby ring sling carrier. $59 retail, множество цветовых вариантов, accessory upsells. 13+ ad units across multiple campaigns starting Nov 2025. Trustpilot: mixed reviews (quality/fulfillment complaints) → white-label с лучшим контролем качества может конкурировать. WildBird ($69+ ring sling) ушёл в Target retail → DTC ниша частично освобождается. Bambora = Category Validator (как KittySpout для cat fountain).
**Applies to:** Baby carrier / sling sub-category для будущих сессий
**Expires after:** Session 15

### [2026-05-15] Session 8 (Part 2) — РЕШЕНО: FB Login + JS Scroll = 500+ ads/keyword
**Type:** Tactical
**Severity:** CRITICAL (полностью меняет capacity скрапера)
**Confidence:** HIGH (подтверждено живым тестом: 561 карточка по "baby carrier")
**Evidence count:** 1 тест, результат: 561 raw ads → 74 unique advertisers
**Observation:** Два исправления в facebook_scraper.py разблокировали полный доступ:
1. SCROLL FIX: `page.mouse.wheel()` НЕ тригерил FB lazy-load. Замена на `page.evaluate('window.scrollBy(0, N)')` — мгновенный результат: 28 → 174 карточек за 10 скроллов.
2. LIMIT FIX: Убран `[:25]` hard cap в parse_ad_cards (строка ~299). Без него парсятся все карточки.
3. SESSION: fb_session.json сохранён на VPS навсегда. Scraper автозагружает при каждом старте.
БЫЛО: 28 ads/keyword. СТАЛО: 500+ ads/keyword (target 500, тест дал 561).
Инкрементальный парсинг (каждые 5 scroll-шагов → парсинг → деdup по Library ID) решает virtual DOM recycling.
**Applies to:** Все будущие VPS scraper сессии
**Expires after:** Session 20 или до изменения архитектуры скрапера

### [2026-05-15] Session 8 (Part 2) — КРИТИЧНО: Три обязательных условия для работы скрапера
**Type:** Warning
**Severity:** CRITICAL (без любого из трёх — агент работает вхолостую)
**Confidence:** HIGH (подтверждено болезненным опытом Sessions 1-8)
**Evidence count:** Весь путь Sessions 1-8
**Observation:** Три условия, без которых запускать скрапер бессмысленно:
1. VPS ОБЯЗАТЕЛЕН: без VPS FB Ads Library недоступна (WebSearch = Tier 3, шум).
   Проверка: `ssh -i ~/.ssh/market_research_vps root@5.78.217.133 "echo OK"` — должно вернуть OK.
2. СЕССИЯ ОБЯЗАТЕЛЬНА: без fb_session.json лимит = 28 ads/keyword (бесполезно).
   Проверка: `ls /opt/market-research-agent/cookies/fb_session.json` — должен существовать.
   Если сессия истекла (FB разлогинит через несколько недель/месяцев): экспортировать куки снова через DevTools → Network → cookie header.
3. JS SCROLL ОБЯЗАТЕЛЕН: без window.scrollBy FB lazy-load не тригерится.
   Проверка: grep в скрапере должен содержать `window.scrollBy`, НЕ `mouse.wheel`.
   Если скрапер даёт < 50 ads в --deep режиме → это ошибка, не норма.
**Applies to:** КАЖДАЯ сессия перед запуском
**Expires after:** Never — это постоянное правило (кандидат в core rules)

### [2026-05-15] Session 8 (Part 2) — Оптимальная глубина сканирования: 400-600 ads/keyword
**Type:** Tactical
**Severity:** HIGH (определяет архитектуру всех будущих сессий)
**Confidence:** HIGH (подтверждено эмпирически: 576 raw ads → 78 unique advertisers)
**Evidence count:** 2 keywords: baby carrier (561 ads, 74 advertisers), baby monitor (576 ads, 78 advertisers)
**Observation:** Закон убывающей отдачи для FB Ads Library depth:
- 576 raw ads → 78 unique advertisers (ratio ~7.4 ads/advertiser)
- После 500 ads те же рекламодатели появляются повторно в новых вариантах объявлений
- 1 keyword × 1000 ads ≈ 100-110 unique advertisers
- 2 keywords × 500 ads ≈ 150-160 unique advertisers + 2 ниши покрыты
ВЫВОД: Масштабировать через breadth (больше keywords), НЕ через depth (глубже 600).
УСТАНОВЛЕННЫЙ СТАНДАРТ: target = 500, hard cap = 600. Это не произвольная пара — скрапер проверяет total >= target только ПОСЛЕ батча (~50-90 новых ads), поэтому естественно останавливается на 500-580. Результат 576 в тесте — норма, не превышение. Выше 600 = diminishing returns + detection risk растёт.
**Applies to:** Все будущие VPS scraper сессии — keyword planning
**Expires after:** Session 20

### [2026-05-15] Session 8 (Part 2) — Risk Map: глубина сканирования vs FB detection
**Type:** Warning
**Severity:** HIGH (защита от потери сессии)
**Confidence:** MEDIUM (логический анализ + паттерны anti-bot; требует эмпирической проверки)
**Evidence count:** Архитектурный анализ + наблюдения из сессий
**Observation:** Уровни риска при увеличении depth:
- 400-600 ads: LOW — "heavy researcher" поведение, реалистично для живого пользователя
- 600-800 ads: LOW-MEDIUM — приемлемо при human-like delays
- 800-1000 ads: MEDIUM — FB anomaly detection фиксирует сессию; human-like delays критичны
- 1000-2000 ads: HIGH — реален hidden throttling (те же результаты, меньше diversity)
- 2000-3000 ads: VERY HIGH — CAPTCHA при следующем логине, soft session ban
HIDDEN THROTTLING: FB не выдаёт ошибку — просто повторяет те же объявления по кругу. Детектируется по резкому падению `new_count` в batch logs (инкрементальный парсер уже логирует это).
Если пойти на 1000+: сначала проверить на отдельном keyword, смотреть на new_count в batch 10-20.
**Applies to:** Все VPS scraper runs с deep режимом
**Expires after:** Session 20 или до эмпирического stress test

### [2026-05-15] Session 8 (Part 2) — Нерелевантные категории в результатах: post-filter нужен
**Type:** Warning
**Severity:** MEDIUM (влияет на качество research signal)
**Confidence:** HIGH (подтверждено на baby monitor: фармацевтика, услуги, случайные бренды)
**Evidence count:** baby monitor run: NUBEQA (онко-препарат), KESIMPTA (MS-препарат), Bethany Monaco Smith (романтика), Effortless Touch Miami (медспа)
**Observation:** FB keyword matching поверхностное — "baby monitor" даёт фармацевтические "monitor"-препараты, медицинские бренды, lifestyle content. Это норма для keyword search, не баг скрапера. Но загрязняет выдачу. Нужен ручной или автоматический post-filter перед анализом. Быстрый ручной фильтр: пропустить если domain содержит медицинский disclaimer или ad copy содержит "prescription", "mg", "FDA". Или фильтровать на уровне исследования по category relevance.
**Applies to:** Kids/Baby vertical keyword runs + любые keywords с dual-meaning терминами
**Expires after:** Session 15 или до реализации авто-фильтра

---

### [2026-05-15] Session 9 — КРИТИЧНО: FB Session истекает между сессиями — обязательный re-export

**Type:** Warning
**Severity:** CRITICAL (без этого весь сеанс = 19-32 ads вместо 500+)
**Confidence:** HIGH (подтверждено боевым опытом Session 9)
**Evidence count:** Session expired between Session 8 Part 2 (09:12) и Session 9 (11:00) — тот же день
**Observation:** FB session cookie истекает быстро (может быть несколько часов). Это НЕ зависит от того, работал ли VPS — просто FB invalidates cookie. Признак истечения: python3 /tmp/check_session.py → "SESSION EXPIRED: Shows login page" вместо "SESSION OK: Logged in".

**Процесс обновления session (Marina выполняет):**
1. Открыть Chrome → зайти на facebook.com (убедиться, что залогинена как Mikhail Piatsiuk)
2. DevTools → Network tab → любой запрос к facebook.com → Headers → Request Headers → Cookie → скопировать полную строку (начинается с "datr=...")
3. Передать агенту строку cookies
4. Агент создаёт /tmp/fb_session.json из строки и заливает на VPS через SCP:
   `scp -i ~/.ssh/market_research_vps /tmp/fb_session.json root@5.78.217.133:/opt/market-research-agent/cookies/fb_session.json`
5. Проверить: `python3 /tmp/check_session.py` → "SESSION OK: Logged in"

**Обязательные ключевые cookies в строке (если нет любого — сессия не работает):**
- c_user (user ID)
- xs (session token)
- fr (Flash cookie)
- datr (device auth)
- sb (browser session)

**Когда давать cookies:** в начале каждой новой сессии, если прошло более 2-3 часов с момента последнего успешного run. Просто дай агенту строку из DevTools Network вкладки.

**Applies to:** КАЖДЫЙ SESSION START — проверка обязательна
**Expires after:** Never — постоянное правило (кандидат в core rules)

---

### [2026-05-15] Session 9 — Почему НЕ нужно идти глубже 600 объявлений

**Type:** Tactical
**Severity:** HIGH (предотвращает потерю сессии и трату времени)
**Confidence:** HIGH (подтверждено Session 8 Part 2 + Session 9 эмпирически)
**Evidence count:** "baby" keyword: остановился на 349 (FB исчерпал уникальный контент); "baby carrier" Session 8: 561 ads достаточно
**Observation:** Два разных сценария:

**Сценарий А: Широкий keyword (baby, kids) при impressions sort**
→ FB исчерпывает уникальных рекламодателей до 500. "baby" = 349 unique advertisers max (natural stop).
→ Идти дальше = те же advertisers повторяются. Бессмысленно и по времени, и по сигналу.

**Сценарий Б: Специфический keyword (baby carrier, stroller) при impressions sort**
→ FB может дать 500-580 unique advertisers. Scraper сам останавливается при target=500.
→ Выше 600 = detection risk (anti-bot) + hidden throttling (повторяющийся контент).

**Правило: 500 = target, 600 = hard cap. Никогда не увеличивать.**
Масштабировать через больше keywords, НЕ через глубже на одном keyword.

**Applies to:** Все VPS scraper сессии
**Expires after:** Session 20

---

### [2026-05-15] Session 9 — "baby" keyword при impressions sort = доминируют big brands (≠ DTC signal)

**Type:** Pattern
**Severity:** HIGH (влияет на ожидания от keyword "baby")
**Confidence:** HIGH (349 ads проанализировано вручную)
**Evidence count:** Round 1 Session 9 = 349 ads, 0 reportable products
**Observation:** Keyword "baby" при FB default sort (impressions high to low) даёт массированный noise:
- ~35% — крупные бренды с бюджетом (Pampers, Graco, Carter's, Huggies, Samsung, NUK, Pottery Barn Kids)
- ~10% — фармацевтика (KEYTRUDA, BOTOX, Mounjaro, RINVOQ и ещё ~15 препаратов)
- ~10% — apps/games (Baby Photo Editor, pregnancy apps, Survivor.io, Dragon City)
- ~20% — food CPG, финансы, услуги, Amazon affiliates, charity
- ~25% — реальные DTC физические продукты, но из них: большинство либо Walmart-distributed, либо established (2021-2023), либо цена вне диапазона

Ни один из кандидатов Session 9 Round 1 не прошёл mandatory filters:
- Obvira teething roller: $25 (ниже ценового пола)
- Dreamland Baby weighted swaddle: $109 (нужна доп. оценка, см. ниже)
- MimiBelt pregnancy belt: Walmart retail
- Blumi Baby swim goggles: Amazon + Walmart, UK brand, established
- Canopy bath tub filter: $89 + subscription + Babylist retail
- Mommy & Me pack & play mattress: Walmart, recall упоминание

**ВЫВОД ДЛЯ БУДУЩИХ СЕССИЙ:** Keyword "baby" при impressions sort — плохой старт для discovery. Работает только при recent sort (показывает свежих advertisers). Специфические keywords (baby carrier, teething, sleep baby, nursing pillow) дают чище сигнал. Использовать "baby" как последний keyword, не первый.

**Applies to:** Kids/Baby vertical keyword ordering
**Expires after:** Session 16

---

### [2026-05-15] Session 9 — ИСПРАВЛЕНИЕ: Price >$100 — НЕ автоматический reject

**Type:** Warning (correction of agent error)
**Severity:** HIGH (агент неправильно применял mandatory filters)
**Confidence:** HIGH (Marina явно указала + подтверждено re-reading mandatory-filters.md)
**Evidence count:** Dreamland Baby ($109) отклонён только по цене без scoring — ошибка агента
**Observation:** Mandatory filter гласит: "Retail price over $100 = requires strong social proof, not suitable for cold traffic MVP". Это УСЛОВНЫЙ фильтр, а не жёсткий reject.

**Правильный процесс для product >$100:**
1. Проверить: есть ли strong social proof? (10K+ reviews, viral TikTok, Shark Tank, mainstream press)
2. Если есть social proof → перейти к scoring, учесть цену как ШТРАФ в scoring (−5 to −10 баллов), но не reject
3. Если нет social proof → reject (cold traffic conversion крайне сложна при $100+ без validation)
4. Результат scoring < 65 при $100+ = reject. Но дать продукту шанс на scoring.

**Пример Dreamland Baby ($109):** Shark Tank brand, dreamlandbabyco.com, weighted swaddle — нужно было score, а не reject сразу. Даже если score < 65 из-за established brand + price, процесс должен был быть полным.

**Applies to:** Все продукты с ценой $100-150 при наличии strong социального proof
**Expires after:** Session 16 или до Marina confirmation

### [2026-05-15] Session 9 — Kids/Baby Sleep: Доминируют Established Brands + Tech

**Type:** Pattern
**Severity:** HIGH (предотвращает растрату раундов на saturated sub-category)
**Confidence:** HIGH (267 ads проанализировано по keyword "sleep baby")
**Evidence count:** Round 3 Session 9 — 267 unique advertisers, 0 reportable
**Observation:** Keyword "sleep baby" показал жёсткую структуру рынка:
- Established brands заняли весь топ: Owlet ($100+, FDA-cleared), Nanit (legacy), SNOO ($1695 smart bassinet), Hatch (sound machine), Dreamland Baby ($109, уже проверен — reject), Nested Bean (since 2015), Love To Dream (since 2007)
- Baby tech ($200-1700): smart bassinets, sleep tracking monitors = выше ceiling и/или subscription
- Adult sleep overlap: ~40% результатов — взрослые матрасы (Casper, Cozy Earth), adult supplements, sleep apps
- Baby sleep apps/courses: Taking Cara Babies, Huckleberry, Tinyhood — не физические продукты
- Weighted products: FDA advisory 2022 → regulatory риск для всей "weighted infant" категории

РАБОЧАЯ НИША: Только swaddles/sleep sacks без weighted claims находятся в рабочем диапазоне. Найдено 2 borderline кандидата (score 66-67): MamaCoco ($44, 656 reviews), Toucan Baby ($44-85, lovey механизм). Оба добавлены в Notion.

РЕКОМЕНДАЦИЯ ДЛЯ БУДУЩИХ СЕССИЙ: Не использовать "sleep baby" — слишком широко. Заменить на: "sleep sack baby", "baby swaddle", "baby white noise machine".

**Applies to:** Kids/Baby vertical — sleep keyword selection
**Expires after:** Session 16

---

### [2026-05-15] Session 9 — Potty Training Category: Demand Validated, Price Floor Issue

**Type:** Pattern
**Severity:** MEDIUM (категория реальна, но цена мешает)
**Confidence:** HIGH (3 независимых DTC бренда с одинаковым hook)
**Evidence count:** UpAiry, Kid Confident, My Carry Potty — из keyword "toddler"
**Observation:** Potty training — реальная боль (родители). Три разных DTC бренда используют ОДИНАКОВЫЙ hook: "7 accidents in 1 day". Подтверждает: боль настоящая, рынок активный.

НО — price floor проблема:
- Training underwear (UpAiry, Kid Confident): $7-15 за штуку → пачка $29-45 → ниже $39 floor
- Portable potty (My Carry Potty): $36.99 individual (ниже $39), $74.97 bundle ✓
- My Carry Potty = UK established brand since ~2014, 1M+ families = не white-label opportunity

ИТОГ: Potty training category существует и активна на FB, НО продукты либо слишком дешёвые, либо established branded. Если найдётся DTC potty training продукт в $49-79 диапазоне → может быть интересно.

KEYWORD ДЛЯ СЛЕДУЮЩЕГО РАУНДА: "potty training" вместо "toddler" — более специфично.

**Applies to:** Kids vertical — potty training sub-category
**Expires after:** Session 16

---

### [2026-05-15] Session 9 — Три Broad Keywords Проверены: Все = Высокий Шум

**Type:** Pattern
**Severity:** HIGH (финальное подтверждение broad keyword стратегии)
**Confidence:** HIGH (3 keywords, 943 ads total)
**Evidence count:** baby (349 ads, 0 reportable), toddler (327 ads, 0 reportable), sleep baby (267 ads, 2 borderline)
**Observation:** Все три broad keyword сессии показали одинаковый паттерн:
- Pass rate: 3-5% (ручной fast filter)
- 0 продуктов с score 65+ из "baby" и "toddler"
- 2 borderline (66-67) из "sleep baby" — и те требуют verification

ПОДТВЕРЖДЁН ЗАКОН: чем уже keyword → тем чище сигнал. Сравнение:
- "baby" (broad): 3% pass rate, 0 reportable
- "sleep baby" (2 слова): 5% pass rate, 2 borderline
- "baby carrier" Session 8 (2 слова, product-specific): 15%+ pass, 1 confirmed (Bambora score 73)

СТРАТЕГИЯ ДЛЯ РАУНДА 4+: только 2-словные product-specific keywords.
Рекомендуемые: "baby carrier", "nursing pillow", "baby monitor" (specific product), "baby wrap", "baby teether".

**Applies to:** Все будущие Kids/Baby keyword runs
**Expires after:** Session 17

---

### [2026-05-15] Session 9 Post-Compact — "kids" keyword = scroll stall + big brand dominance

**Type:** Pattern
**Severity:** HIGH (влияет на ожидания от keyword "kids")
**Confidence:** HIGH (53 ads, fast filter выполнен)
**Evidence count:** Round 4 Session 9 — 53 unique advertisers за 35 сек (vs 327-375 для других keywords)
**Observation:** Keyword "kids" дал аномально мало advertisers (53). Причина: FB lazy-load стоп после batch 5 (59 карточек → 53 unique после dedup). Признак: "[SCROLL] No new cards in 2 consecutive batches". Контент: Bank of America, PediaSure, Hiya Health, Pottery Barn Kids, Guardian Bikes, fairlife, iHerb Spanish — всё крупные бренды. 0 DTC стартапов. Единственный borderline: GetFootStr.com (детские ортопедические стельки $34.99 — ниже floor + branded).

ВЫВОД: "kids" = dead keyword для нашего discovery процесса. FB Ads Library не индексирует широко по "kids" в нашем target (US, Active, English). Заменить на product-specific 2-слова.

**Applies to:** Kids vertical keyword selection — не использовать "kids"
**Expires after:** Session 17

---

### [2026-05-15] Session 9 Post-Compact — "mom life" = UGC/affiliate тяжёлый keyword

**Type:** Pattern
**Severity:** MEDIUM (количество хорошее, но signal слабый)
**Confidence:** HIGH (375 ads analyzed)
**Evidence count:** Round 5 Session 9 — 375 unique advertisers за 91 сек
**Observation:** Keyword "mom life" даёт хорошую плотность (375 advertisers), но структура другая:
- ~30% — UGC creators / affiliate accounts (Amazon "mom finds", Walmart partnership, brand ambassadors)
- ~25% — established FMCG (Pampers, Olay, Dove, Native, Secret, Puffs, Vaseline, fairlife)
- ~15% — services (Teladoc, Connections Academy, Tempo.fit, financial)
- ~15% — pharma/medical
- ~15% — реальные DTC продукты, но mostly established или wrong category

Кандидаты проверены: CocoSeat.com ($44, portable baby seat cover — commoditized, ~62 score), NatPat.com (1M+ customers, Australian brand, reject), MimiBelt.com ($35.99 — ниже floor, branded), Mammabump.com (multi-product, wide range).

ВЫВОД: "mom life" = больше UGC-пространство, чем product-discovery пространство. Работает для категорийного понимания, не для finding winners. Если делать следующий раз — смотреть на domainless ads с конкретными механизмами.

**Applies to:** Kids vertical — "mom life" keyword evaluation
**Expires after:** Session 17

---

### [2026-05-15] Session 9 Post-Compact — "child safety" = service-dominated keyword

**Type:** Pattern
**Severity:** HIGH (предотвращает потрату rounds на service-heavy keyword)
**Confidence:** HIGH (327 ads analyzed)
**Evidence count:** Round 6 Session 9 — 327 unique advertisers за 70 сек
**Observation:** Keyword "child safety" даёт хорошую плотность (327), но структура неподходящая:
- ~60% — local services (D1 Training, swim schools, daycares, martial arts — repeating multiple cities)
- ~15% — pharma/medical (JORNAY PM, SKYTROFA, VOXZOGO, OPZELURA — pediatric drugs)
- ~10% — anti-choking devices (NexBreath, RescueSeal, AirwayClear, Freevair, NovaCare — все reject: патенты/регуляторика)
- ~5% — digital safety apps (Bark, Canopy, MMGuardian — не физические продукты)
- ~10% — прочие (юридические услуги, charity, романтические истории)

Единственный интересный product mechanism: Kaizen Kidz 3-2-1 Swim Pack ($99.99 — патентованная технология, white-label невозможен).
Swim safety как категория: доминируют swim schools + NexBreath anti-choking (reject). SafeHero.us = UK brand (GBP pricing).

ВЫВОД: "child safety" НЕ подходит для product discovery — это service и regulatory space. Избегать.

**Applies to:** Kids vertical keyword selection — не использовать "child safety"
**Expires after:** Session 17

---

### [2026-05-15] Session 9 Post-Compact — Broad Emotional Keywords: Discovery Map (Summary)

**Type:** Pattern
**Severity:** HIGH (итог 6-round strategy из трёх broad keywords)
**Confidence:** HIGH (6 rounds + 1698+ total ads analyzed in Session 9)
**Evidence count:** kids(53), mom life(375), child safety(327) — итог Марининой стратегии

**ИТОГ ЭКСПЕРИМЕНТАЛЬНОЙ СТРАТЕГИИ (Раунды 4-6):**
Marina правильно поставила гипотезу: broad emotional keywords дают discovery map, а не прямых winners. Карта категорий Kids по типам advertisers:

CATEGORY LANDSCAPE INSIGHTS:
1. "kids" → крупные FMCG + retail (PediaSure, Hiya, Guardian Bikes) — покупательская категория ≠ DTC category
2. "mom life" → UGC creator economy + established brands + convenience/lifestyle products
3. "child safety" → service industry (swim schools, daycares) + regulatory/pharma space

ПРОДУКТЫ, КОТОРЫХ НЕТ В BROAD KEYWORDS НО ЕСТЬ В SPECIFIC:
Bambora baby carrier (из "baby carrier") — лучший signal за все 6 rounds.
MamaCoco swaddle, Toucan sleep sack (из "sleep baby") — единственные borderline winners.

ИТОГ ДЛЯ СТРАТЕГИИ: Broad keywords подтвердили category landscape, но НЕ дали winners. Narrow product-specific keywords = путь к winners. Рекомендация: следующие раунды использовать только 2-словные product keywords из ещё неизученного списка.

**Неизученные high-priority keywords для Kids vertical:**
- "baby swaddle" (продолжение sleep сигнала)
- "baby wrap" (альтернативный carrier механизм)
- "learning toy" / "montessori toy" (развивающие)
- "nursing pillow" (Session 8 дал 25 ads — повторить с full session)
- "baby gate" (safety mechanism, конкретный продукт)
- "diaper bag" (bag category, Emmafy ждёт верификации)
- "baby bouncer" / "baby swing" (baby gear sub-category)

**Applies to:** Kids vertical strategy — следующие 3-7 сессий
**Expires after:** Session 18

---

---

### [2026-05-15] Session 9 Post-Compact R7 — "Montessori toy" = medium signal, scroll stall early

**Type:** Pattern
**Severity:** MEDIUM (влияет на ожидания от keyword)
**Confidence:** HIGH (81 unique advertisers проверено)
**Evidence count:** Round 7 — 253 raw → 81 unique, scroll stall batch 5
**Observation:** Keyword "Montessori toy" дал scroll stall уже на batch 5 (253 raw → 81 unique). По сравнению с другими keywords это небольшой пул. Структура:
- Dropship networks: минимум 2 крупные сети (Montessori Fishing Set — 7 доменов; Electric Drill Kit — 3+ домена)
- Marketplace/retail: Etsy, Amazon, Target, IKEA-style stores — ~15%
- Multi-product Montessori stores (не специализированные DTC): MontessoriParadise, MontessoriKidSmart — ~10%
- Established/non-US: LeYaDoll (founded 2018), Toddla.co (Australian AUD), ByCubby (UK "Personalised")
- Suspicious quality: TibaToes (trust 39/100), Minilabbies (fake review claims, shipping from China)
- 0 qualifying DTC candidates

KEY FINDING: Keyword "Montessori toy" = low yield. FB позиционирует Montessori как "attribute" keyword — много generic dropship, мало specialty DTC. Лучше тестировать конкретные продукты: "busy board", "montessori busy book", "wooden stacking toy".

**Applies to:** Kids vertical keyword selection
**Expires after:** Session 18

---

### [2026-05-15] Session 9 Post-Compact R8 — "sensory toy" = взрослый рынок доминирует (60%+)

**Type:** Pattern
**Severity:** HIGH (меняет ожидания от категории "sensory toy")
**Confidence:** HIGH (198 advertisers, 515 raw ads проанализировано)
**Evidence count:** Round 8 — 515 raw → 198 unique advertisers
**Observation:** Keyword "sensory toy" при FB impressions sort показал структуру, неожиданно близкую к взрослому рынку:
- ~45% — adult stress relief (NeeDoh knockoffs, lava flow toys, squishy cubes, fidget spinners) — БОЛЬШИНСТВО
- ~20% — dropship сети для squishies (12 доменов для jelly squishes, 6 для Easter squishy bundle)
- ~15% — baby/toddler sensory (bath toys, stroller toys, teether rattles) — ЦЕЛЕВОЙ сегмент
- ~10% — services (therapy practices, sensory play cafes)
- ~10% — non-US brands (Австралия, Болгария, UK)

DROPSHIP NETWORKS IDENTIFIED (7 кластеров):
1. "Jelly squishes / NeeDoh" — 12 доменов
2. "Easter squishy bundle" — 6 доменов
3. "Stroller hanging sensory toy" — 3 домена (howeveryet, afterdoubt, idealbless)
4. "Interactive Sensory Garden Baby Set" — 2 домена (doneforth, ampleidea)
5. "Interactive Music Plush" — 3 домена (tyiiplus, convergeas, inlikewise)
6. "Kids Phonograph 99 Cards" — 3 домена
7. "Lava Flow Toy" — 3 домена

ЕДИНСТВЕННЫЙ ИНТЕРЕСНЫЙ ПРОДУКТ (недостаточно сигнала): blemory.com/mibbo — musical plush toy $39.95 с механизмом "музыка только при прикосновении". Концепция интересная (screen-time replacement hook), но: sold out, 404 на product page, нет внешних reviews, нет Amazon presence — слишком слабый сигнал.

ВЫВОД: "sensory toy" = не детский keyword. Для baby/toddler sensory нужны: "baby sensory toy", "toddler sensory toy", "infant sensory". Двухслойная проблема: (1) keyword захвачен взрослым рынком; (2) детский сенсорный рынок = dropship + established brands.

**Applies to:** Kids vertical keyword selection
**Expires after:** Session 18

---

### [2026-05-15] Session 9 Full Session — ИТОГ: 10 Keywords Done, Pattern Map

**Type:** Signal
**Severity:** HIGH (стратегический итог 9 sessions в Kids вертикали)
**Confidence:** HIGH (10 keywords analyzed, 3000+ ads total)
**Evidence count:** 10 keywords: baby, toddler, sleep baby, baby carrier, baby monitor, kids, mom life, child safety, Montessori toy, sensory toy

**KIDS VERTICAL — KEYWORD SCORECARD (по 10 проверенным keywords):**

| Keyword | Ads | Yield | Verdict |
|---------|-----|-------|---------|
| baby carrier (S8) | 561 | HIGH — Bambora score 73 | ✅ Use again |
| baby monitor (S8) | 576 | LOW — legacy tech brands | ❌ Dead |
| sleep baby (S9) | 267 | MEDIUM — 2 borderline | ⚠️ Narrow to "sleep sack" |
| baby (S9) | 349 | LOW — big brand noise | ❌ Last resort |
| toddler (S9) | 327 | LOW — 0 reportable | ❌ Replace with specific |
| child safety (S9) | 327 | ZERO — service-dominated | ❌ Dead |
| mom life (S9) | 375 | ZERO — UGC/affiliate | ❌ Dead |
| kids (S9) | 53 | ZERO — scroll stall + FMCG | ❌ Dead |
| Montessori toy (S9) | 81 | ZERO — dropship/established | ❌ Replace with specific |
| sensory toy (S9) | 198 | ZERO — adult market | ❌ Replace with specific |

**РЕКОМЕНДОВАННЫЕ СЛЕДУЮЩИЕ KEYWORDS (в порядке приоритета):**
1. "baby swaddle" — прямое развитие sleep signal (MamaCoco, Toucan Baby validated)
2. "baby bouncer" — конкретный product, активный рынок
3. "diaper bag" — Emmafy, Mina Baie ждут верификации
4. "baby gate" — safety mechanism, specific product
5. "feeding bottle" / "baby bottle" — feeding sub-category
6. "baby wrap" — carrier category, альтернативный механизм к baby carrier
7. "nursing pillow" — Session 8 short test, нужен full run
8. "infant" — 0-12 months focused, more specific than "baby"

**Applies to:** Kids vertical — Session 10+ keyword planning
**Expires after:** Session 20

---

### [2026-05-15] Session 9 — КРИТИЧНО: Дропшип-бренд = сигнал спроса, НЕ причина reject

**Type:** Warning (correction of persistent agent error)
**Severity:** CRITICAL (агент систематически неправильно применял фильтр)
**Confidence:** HIGH (Marina явно указала — она сама дропшиппер)
**Evidence count:** Прямая коррекция от Marina, Session 9, 2026-05-15

**Observation:** Агент ошибочно rejecting-ил продукты на основании того, кто их продаёт (дропшиппер, зарубежный бренд), вместо оценки самого ПРОДУКТА.

**ПРАВИЛЬНАЯ ЛОГИКА:**

Несколько доменов продают ОДИН продукт → это СИГНАЛ СПРОСА, не red flag.
Дропшиппер, который крутит FB рекламу = такая же компания, как у Марины.
Зарубежный бренд (UK, Australia, Canada) продаёт продукт → продукт СУЩЕСТВУЕТ.

**ПРАВИЛЬНЫЙ ФИЛЬТР:**
```
СМОТРИ НА ПРОДУКТ:
✅ Цена в диапазоне $39-99?
✅ COGS реальный (Alibaba/AliExpress)?
✅ Механизм/hook внятный?
✅ White-label возможен (нет патента на концепт)?
✅ US рынок применим?
→ Если всё ДА → Score продукт, как обычно

❌ НЕ фильтровать по:
- "это дропшиппер" → НЕ причина reject
- "это зарубежный бренд" → НЕ причина reject (проверь US applicability)
- "много продавцов продают" → НЕ причина reject (это validation!)
```

**Когда НЕ подходит ПРОДУКТ:**
- Цена розничная ниже $39 → reject по цене
- Commodity настолько глубокая, что дифференциация невозможна
- Патент на КОНЦЕПТ (не механизм) блокирует white-label

**Примеры ошибок, которые нужно исправить:**
- "Stroller Arch Hanging Toy" — отклонил как "dropship сеть". Правильно: проверить цену ($14-30 = ниже floor → reject по ЦЕНЕ)
- "Busy Board" — отклонил как "dropship/established". Правильно: Category Validator score 65
- "Montessori Fishing Set" — отклонил как "dropship". Правильно: проверить цену (DTC $49-59 → в диапазоне, но высокая saturated → score ~58)

**Applies to:** ВСЕ будущие сессии — базовый фильтр логики
**Expires after:** Never — постоянное правило (кандидат в core rules)

---

### [2026-05-16] Session 10 — "screen time" keyword: MEDIUM yield, category map utility

**Type:** Pattern
**Severity:** MEDIUM (влияет на keyword strategy для Screen-Free категории)
**Confidence:** HIGH (313 ads проанализировано)
**Evidence count:** 313 unique advertisers, 2 candidates scored 65+
**Observation:** Keyword "screen time" дал 313 уникальных рекламодателей за 85 секунд. Структура:
- 60%+ — services, apps, pharma, FMCG (Pampers, Google, Walmart, BOTOX)
- ~15% — физические продукты с "screen-free" hook (camera, toys, STEM kits)
- ~25% — другое (религия, финансы, авто, туризм)

YIELD: 2 candidates (77 и 67) из 313 — лучше, чем broad keywords типа "baby" (0/349), но хуже чем product-specific "baby carrier" (1 strong).

ПАТТЕРН: "Screen-free alternative" toy/device category существует и растёт в Kids вертикали. Keyword "screen time" = хороший entry point для поиска этой ниши.

**Applies to:** Kids vertical — screen-free product discovery
**Expires after:** Session 17

---

### [2026-05-16] Session 10 — Camp Snap Camera: Категория "screen-free kids camera" VALIDATED

**Type:** Signal
**Severity:** HIGH (конкретный category signal с мощным ad count)
**Confidence:** HIGH (50+ influencer campaigns verified across Jan–May 2026)
**Evidence count:** 50+ FB ad variants в keyword "camp snap", running Nov 2025 – May 2026
**Observation:** Camp Snap Camera (campsnapcamera.com) = единственный DTC бренд в категории "screen-free digital camera for kids". $69.95 hero price. Работает на FB с November 2025 (6 месяцев). Aggressive influencer/UGC scaling с десятками creator campaigns.

SIGNAL QUALITY: HIGH — 6-месячное scaling = market validation confirmed.
WHITE-LABEL RISK: Camp Snap имеет компаньон-платформу campsnapphoto.com — возможно проприетарная экосистема. Нужна проверка Alibaba на "screen-free point-and-shoot kids camera" (без LCD-экрана на задней панели).

SOURCING HYPOTHESIS: Такие камеры существуют на Alibaba как "retro film digital camera" или "point-and-shoot no screen" — но нужна прямая верификация.

CATEGORY STATUS: "Screen-free kids camera" = новая DTC категория, Camp Snap = pioneer. Конкурировать возможно при наличии white-label источника и дифференцированном позиционировании ($59 vs $69.95, или travel vs camp).

**Applies to:** Kids/Tech vertical — screen-free camera keyword decisions
**Expires after:** Session 17

---

### [2026-05-16] Session 10 — Multi-brand dropship операторы = исследовательский актив

**Type:** Tactical
**Severity:** HIGH (влияет на то, как использовать dropship-операторов в research)
**Confidence:** HIGH (Marina явно подтвердила — она сама делает branding dropshipping)
**Evidence count:** Прямой фидбек от Marina, Session 10; пример: DBO Networks LLC (Wonder Quest, другие бренды)

**Observation:** Когда в FB Ads Library встречается бренд типа Wonder Quest с футером "Operated by DBO Networks LLC" — это не red flag и не сигнал для reject. Это исследовательский актив: такие операторы уже потратили значительный ad spend на product testing. Их активный каталог = список продуктов с доказанным спросом.

**Как использовать:**
1. При виде "Operated by [Company LLC]" → проверить их АКТИВНЫЙ каталог (не только текущий бренд)
2. 404 на продукт = оператор убрал его с теста (не выжил) → нам тоже не нужен
3. Продукт активен 6+ месяцев у оператора → demand validated → кандидат для white-label валидации
4. НЕ тратить время на маркетинговые тактики (таймеры, BOGO, fake reviews) — интересует только ЧТО продают и КАК ДОЛГО
5. НЕ снижать confidence за то что это dropship — Marina тоже dropshipper

**Почему это важно:** DBO Networks и аналоги = бесплатная "pre-validation service". Они уже сделали тест спроса. Если их продукт жив — значит конвертирует.

**Applies to:** Все сессии — отношение к multi-brand dropship операторам
**Expires after:** Session 20 или до Marina override

---

### [2026-05-16] Session 10 — "Screen-free alternative" toy pattern: emerging trend

**Type:** Pattern
**Severity:** MEDIUM (влияет на product angle discovery в Kids вертикали)
**Confidence:** MEDIUM (4 advertisers использовали этот angle в одном keyword scan)
**Evidence count:** Camp Snap, Thoson Kids, BlockBlaster, ArtCreativity — все advertising против screen time
**Observation:** В keyword "screen time" несколько рекламодателей использовали hook "tired of your kid on the tablet?" как главный триггер для своих toy/device продуктов. Это сигнал: "screen-time replacement" angle = очень сильный parental trigger в 2026.

PRODUCTS ЧТО РАБОТАЮТ с этим angle:
- Cameras/devices без экрана (Camp Snap — сильный)
- Magnetic/building toys (Thoson — средний)
- Art/craft kits (TobioShop — слабый)
- STEM exploration kits (Wonder Quest — слабый, dropship)

ВЫВОД: При scoring любого kids toy — проверить можно ли использовать "screen-free" angle. Если да — +2-3 балла к Wow-Effect и Emotional Trigger.

**Applies to:** Kids vertical — all toy/activity products
**Expires after:** Session 17

### [2026-05-16] Session 10 — "learning toy" keyword: LOW yield, слишком широкий атрибут

**Type:** Pattern
**Severity:** HIGH (предотвращает повторный запуск этого keyword)
**Confidence:** HIGH (247 advertisers проверено)
**Evidence count:** 247 unique advertisers, 0 reportable products (0/247)

**Observation:** Keyword "learning toy" дал 247 advertisers за 63 сек, но структура крайне неудобная:
- ~30% — established retail (Scholastic, Target, Amazon, MAGNA-TILES, Stapelstein $119-259)
- ~20% — сервисы (школы, OT-практики, репетиторство)
- ~20% — multi-product dropship stores (Kariney = random gadgets, Broadcasth = clothing store с magnetic car в ad copy — мисматч!)
- ~15% — subscription/tech (ibrick = LEGO-kit subscription, Bondu = AI-плюш с проприетарным чипом)
- ~5% — потенциально интересные физические DTC

ЕДИНСТВЕННЫЙ ВОЗМОЖНЫЙ КОНЦЕПТ: DiyAtive "Little Engineer Toolbox" $62.99 — реальные инструменты (safe drill + 90+ tools + bench). Но: multi-product dropship store, категория children's toy toolset глубоко commoditized на Amazon. Оценочно ~58-62, не репортован.

ПРИЧИНА СЛАБОГО YIELD: "learning toy" = атрибут, не product-category. FB матчит любой ad с "learning" + "toy" — слишком широко. В отличие от "baby carrier" или "screen time" которые дают реальный product-cluster.

DOMAIN MISMATCH ПАТТЕРН: Broadcasth показал в FB ad "Magnetic Transform Engineering Car", но сайт broadcasth.com = clothing store (Jacket/Pants/Skirt/Socks). Это сигнал: domain в FB ad не всегда соответствует реальному сайту продавца. При fast-filter — WebFetch обязателен для подтверждения.

**Applies to:** Kids vertical keyword selection — не использовать "learning toy"
**Expires after:** Session 20

---

### [2026-05-16] Session 10 — Keyword Audit Database: концепция еженедельного мониторинга

**Type:** Tactical
**Severity:** HIGH (стратегическая ценность для долгосрочного research)
**Confidence:** HIGH (Marina явно подтвердила ценность, Session 10)
**Evidence count:** 12 keywords протестировано за Sessions 8-10, паттерны устойчивы

**Observation:** После 12 протестированных keywords формируется устойчивый Keyword Scorecard. Marina предложила идею: построить базу ~50 топ-keywords и делать по ним аудит раз в неделю. Это создаст Market Pulse Monitor — системный способ отслеживать новых FB advertisers без повторного полного сканирования.

ТЕКУЩИЙ SCORECARD (12 keywords):
- ✅ Рабочие: baby carrier (Bambora 73), screen time (Camp Snap 77)
- ❌ Мёртвые: baby monitor, child safety, mom life, kids, learning toy
- ⚠️ Требуют сужения: sleep baby → "sleep sack", Montessori toy → "busy board", sensory toy → "toddler sensory"
- 🔄 Не проверены из priority list: baby swaddle, diaper bag, kids camera, baby bouncer, baby wrap, nursing pillow, baby gate, stem kit

ЦЕННОСТЬ БАЗЫ: раз в неделю прогнать 10-15 рабочих keywords → посмотреть новых advertisers → зафиксировать кто появился/исчез. Экономит часы исследований в долгосроке.

**Applies to:** Session planning — долгосрочная стратегия
**Expires after:** Session 25 или до реализации системы

---

### [2026-05-16] Session 10/11 — "long flight" situation keyword: HIGH noise, LOW physical product yield
**Type:** Pattern
**Severity:** HIGH (влияет на keyword strategy для situation keywords)
**Confidence:** HIGH (314 advertisers проанализировано)
**Evidence count:** 314 unique advertisers, 1 product 65+

**Observation:** Keyword "long flight" = situation/moment keyword. Структура результатов:
- ~65% noise: авиакомпании, кредитные карты, IV-клиники, apps, supplements, драма-контент
- ~20% физические продукты, но большинство или saturated (travel pillows) или ниже ценового пола (компрессионные носки $28-39)
- ~15% реальные physical product кандидаты

Yield сравнение: "long flight" (situation) → 1/314 (0.3%) vs "baby carrier" (product-specific) → 1/74 (1.4%).

**ВЫВОД:** Situation keywords ("long flight", "rainy day") дают меньше прямых product winners, но БОЛЬШЕ category landscape insights. Они показывают КТО рекламирует вокруг момента — это intelligence, а не direct product discovery.

**Правильное использование situation keywords:**
- Смотреть на паттерны КАТЕГОРИЙ, а не конкретные продукты
- Искать unusual/non-obvious products среди шума
- Ожидать меньший yield, чем product-specific keywords
- Компенсировать большим количеством keywords в сессии (2-3 situation vs 1 product)

**Applies to:** Keyword strategy — situation vs. product keywords
**Expires after:** Session 18

---

### [2026-05-16] Session 10/11 — Kids Travel Sleep Nest: открытая DTC ниша
**Type:** Signal
**Severity:** MEDIUM (конкретный category signal)
**Confidence:** MEDIUM (1 DTC advertiser confirmed, Amazon competition verified)
**Evidence count:** 1 FB advertiser (Seat to Sleep), Amazon 5-7 generic brands

**Observation:** Inflatable sleep nest for toddlers on flights = открытая DTC FB ниша в США. Seat to Sleep (seattosleep.co.uk) = единственный DTC FB advertiser в US. Amazon category crowded с generic $15-30 versions (Koala Kloud, Deeteck, Flyaway), но DTC Facebook = открытое пространство. Проблема (дети не могут спать на рейсах) = реальная боль родителей. Визуальный хук сильный (ребёнок спит на самолёте). Reported: score 72.

**Risky part:** Amazon commodity trap — needs premium DTC positioning ($59-69) и strong UGC чтобы оправдать цену.

**Applies to:** Kids vertical — travel/situational products
**Expires after:** Session 18

---

### [2026-05-16] Session 10/11 — Compression socks: активная FB категория, но структурный fail
**Type:** Pattern
**Severity:** HIGH (предотвращает трату времени на эту категорию)
**Confidence:** HIGH (6 брендов подтверждено в одном keyword scan)
**Evidence count:** Everstride, Vixsocks, Crazy Compression, Bright Legs, EverSock, Hushed — все в одном scan

**Observation:** Compression socks = очень активная DTC FB категория. НО: цена $28-39 = на полу или ниже. Everstride ($29-34) = 1M sold, 17,800 reviews = established brand. 6+ брендов одновременно = SATURATED + below floor. Не исследовать снова без ценового сигнала $49+.

**Applies to:** Travel/Health keyword selection
**Expires after:** Session 20

---

### [2026-05-16] Session 10/11 — OPERATIONAL: Parallel verification ускоряет сессию на 30–40%
**Type:** Tactical
**Severity:** MEDIUM (влияет на эффективность verification stage)
**Confidence:** HIGH (Marina confirmed, Session 10/11)
**Evidence count:** Прямой фидбек от Marina

**Observation:** В Session 10/11 верификация кандидатов (WebFetch на домены) делалась последовательно: один домен → ждать → следующий. Правильный подход — параллельно, если контекст позволяет.

**Правило:** При verification stage — делать 3–4 WebFetch параллельно в одном response block.
- Параллельно = ускорение на ~30–40% по времени верификации
- Применять когда: несколько independent кандидатов требуют проверки домена/цены
- НЕ применять когда: результат первого fetch нужен для принятия решения по следующему

**Applies to:** Все verification stages во всех сессиях
**Expires after:** Never — постоянное правило (кандидат в core rules)

---

### [2026-05-16] Session 10/11 — STRUCTURAL: Скрапер не всегда захватывает `started` дату
**Type:** Warning
**Severity:** MEDIUM (structural pipeline limitation)
**Confidence:** HIGH (наблюдалось в Session 10/11: большинство advertisers showed "?" для started)
**Evidence count:** 314 advertisers "long flight" — started date отсутствовал у большинства

**Observation:** Поле `started` (дата начала кампании) — Tier-1 сигнал для Entry Window оценки. Скрапер захватывает его только когда FB явно показывает эту информацию в карточке. Для многих advertisers поле возвращается как "?".

**Это structural limitation текущего pipeline, не баг скрапера.**

**Workaround если start date критичен:**
- Сделать targeted WebFetch на About/brand page рекламодателя → найти founding date или press date
- Или: проверить WHOIS / domain registration date (косвенный сигнал)
- Или: поискать первые reviews по дате (Amazon, Trustpilot)

**Важно:** НЕ превращать в обязательный шаг для каждого advertiser — только когда Entry Window score значимо влияет на решение "report / не report". Например, если продукт на грани 65/70 и freshness = ключевой фактор.

**Applies to:** Все VPS scraper сессии — scoring Entry Window
**Expires after:** До исправления `started` поля в скрапере (либо постоянное если не будет исправлено)

---

### [2026-05-16] Session 10/11 — OPERATIONAL: Candidate list output — НЕ выводить в чат полностью
**Type:** Operational
**Severity:** HIGH (прямо влияет на расход контекста и остаток окна для analysis/feedback)
**Confidence:** HIGH (Marina явно подтвердила, Session 10/11)
**Evidence count:** Session 10/11 "rainy day": 229 кандидатов в чат = ~8-10% контекста за один вывод

**Observation:** Текущий filter script выводил всех кандидатов в чат (229 записей). Это крупный блок текста, который сжигает контекст без необходимости — агент всё равно анализирует только топ-10-15.

**Правило:** При fast filter на candidate list — всегда делать так:
1. Полный список → сохранить в файл на VPS (`/tmp/{keyword}_candidates.json` или `_candidates.txt`)
2. В чат выводить ТОЛЬКО топ shortlist (15-20 наиболее перспективных по сигналам)
3. Сообщить путь к полному файлу: "Full list saved: /tmp/rd_candidates.txt (116 candidates)"
4. Если нужен дополнительный кандидат — прочитать из файла на VPS точечно

**Цель:** снизить расход контекста per keyword session с ~25% до ~15%. Оставить достаточно контекста для: анализа кандидатов, обратной связи Марины, добавления в Notion, финального summary, commit.

**Applies to:** Все sessions с fast filter stage — применять с следующей сессии
**Expires after:** Never — постоянное операционное правило (кандидат в core rules)

---

### [2026-05-16] Session 10/11 — СТРАТЕГИЧЕСКОЕ: Situation keywords = hidden intersection discovery mode
**Type:** Tactical
**Severity:** HIGH (меняет то, КАК интерпретировать situation keyword results)
**Confidence:** HIGH (Marina явно подтвердила, Session 10/11; доказано через Travel Nest discovery)
**Evidence count:** Travel Nest найден через "long flight", а не через "baby product" / "kids toy"

**Observation:** Situation keywords ("long flight", "rainy day", "road trip", "busy toddler", "dinner party") работают принципиально иначе, чем product-specific keywords ("baby carrier", "neck pillow").

**Product-specific keywords:**
→ Прямой path к конкретным продуктам в категории
→ Высокий yield (1-3% advertiser → reportable)
→ Применять для depth сканирования известных категорий

**Situation keywords:**
→ Раскрывают ПЕРЕСЕЧЕНИЯ момента × продукта, которые нельзя предсказать заранее
→ Низкий yield по прямым продуктам (0.3-0.5% ожидаемо) — это НОРМАЛЬНО
→ Высокий noise — это ОЖИДАЕМО
→ Ценность = unusual discoveries и emotional-context intersections

**Travel Nest как proof of concept:**
Kids Travel Sleep Nest не появился бы в keyword "baby product" или "infant toy". Он появился в "long flight" потому что момент боли (ребёнок на самолёте) = intersect Kids × Travel × Sleep. Situation keyword создал контекст, в котором этот нестандартный продукт стал виден.

**Практическое правило для situation keywords:**
- НЕ оценивать сессию по yield (1 из 300 = успех, не провал)
- Смотреть: есть ли среди шума что-то, что НЕ появилось бы в стандартных keywords?
- Искать: unusual category crossovers, new problem framings, non-obvious product applications
- Принять: 65-70% noise = нормально, не менять keyword на середине сессии из-за noise

**Applies to:** Все сессии с situation/moment keywords
**Expires after:** Session 25 или до замены более точным алгоритмом

---

### [2026-05-16] Session 10/11 — "rainy day" keyword: ZERO yield, слабая специфичность
**Type:** Warning
**Severity:** HIGH (предотвращает повторный запуск без новой причины)
**Confidence:** HIGH (370 advertisers проанализировано, 116 filtered, 12+ verified — 0 reportable)
**Evidence count:** 370 advertisers, 0 products ≥65

**Observation:** Keyword "rainy day" дал 370 уникальных advertisers за 66 сек. После двух раундов фильтрации и верификации 12+ кандидатов — 0 reportable products.

Структура результатов:
- ~35% — rain gear (established brands: Hunter Boots, Vessi, Merry People, BaerskinTactical, Rebel Bro)
- ~25% — local services (indoor trampoline parks, kids play centers, art studios, venues)
- ~20% — lifestyle/cozy (candles, blankets — mostly <$30)
- ~10% — established/retail brands (CHANEL, Raycon, KiwiCo, Honeylove, Nugget)
- ~10% — реальные DTC кандидаты, но все ниже 65: Declan's Mining (~57), Pippaloo (~58, fails white-label filter)

**Причина слабого yield:** "rainy day" = generic domestic situation без острой боли. В отличие от "long flight" (конкретный момент + captive audience + физический дискомфорт), "rainy day" = размытое ощущение без buying intent. Не создаёт достаточного контекста для DTC физических продуктов.

**Keyword verdict: ❌ Dead-end для product discovery.** Не повторять без конкретной новой причины (например: если появится сигнал о новой Kids indoor activity category).

**Applies to:** Kids vertical keyword selection — situation keywords
**Expires after:** Session 20

---

### [2026-05-16] Session 10/11 — Честный 0-result = ценный результат, не провал
**Type:** Tactical
**Severity:** MEDIUM (влияет на качество решений по keyword strategy)
**Confidence:** HIGH (Marina явно подтвердила, Session 10/11)
**Evidence count:** "rainy day" scan — 370 ads, 0 reportable, Marina approved as correct decision

**Observation:** Когда keyword даёт 0 reportable products после честного сканирования и верификации — это ценная информация:
1. Keyword можно закрыть и не возвращаться
2. Это освобождает будущие сессии от повторного тестирования
3. Pattern summary по keyword = долгосрочный актив (keyword scorecard)

**Правило:** НЕ форсировать продукт чтобы сессия "не пропала зря". Качественный 0-result лучше одного слабого reportable.
- Если keyword дал шум → честный 0 → зафиксировать в scorecard → двигаться дальше
- Если keyword дал 1-2 borderline кандидата (60-64) → не репортовать → зафиксировать как "weak signal"
- Правило quality over quota: 3 сильных продукта > 5 слабых. 0 с pattern > 1 forced

**Applies to:** Все scout сессии — оценка результатов keyword scan
**Expires after:** Never — постоянное правило (уже частично есть в core, reinforcement)

---

### [2026-05-16] Session 13 — "bored kids" keyword: situation keyword, HIGH noise, LOW physical yield
**Type:** Pattern
**Severity:** MEDIUM
**Confidence:** HIGH (266 advertisers проанализировано)
**Evidence count:** 266 unique advertisers, 1 candidate 70+
**Observation:** Keyword "bored kids" — situation/seasonal keyword. Структура:
- ~35% — local services (martial arts, summer camps, sports academies) — пик в апреле-мае перед летом
- ~20% — digital (apps, streaming, courses)
- ~10% — travel/entertainment venues
- ~6-8% — физические продукты (наш таргет)
- ~25% — прочий шум
Yield: 1 reportable product из 266 (Wonder Quest, score 70). Ожидаемо для situation keyword.
ПАТТЕРН: "bored kids" = calendar keyword — пик активности апрель-май. DTC физические продукты в этом keyword = STEM/exploration toys (screen-free category).
**Applies to:** Kids vertical — situation keyword strategy
**Expires after:** Session 20

### [2026-05-16] Session 13 — Wonder Quest: DBO Networks оператор подтверждён
**Type:** Signal
**Severity:** MEDIUM
**Confidence:** MEDIUM (1 advertiser, Jan 2026, high impressions)
**Evidence count:** Library ID 869115092579954, thewonderquest.net
**Observation:** Wonder Quest 4K Discovery Microscope ($49.99 DTC, ~$15-20 COGS) = single active FB advertiser, started Jan 2026. Operated by DBO Networks LLC (multi-brand dropship operator, уже зафиксирован в Session 10). White-label viable: generic kids digital microscope на Alibaba $12-20. Слабый сигнал (1 ad) vs Camp Snap (50+). Score 70. Ценность: STEM/exploration category signal + sibling cooperation hook.
Reported to Notion: 2026-05-16.
**Applies to:** Kids/STEM exploration category
**Expires after:** Session 20

### [2026-05-16] Session 13 — "keep kids busy" keyword: TOO BROAD, high noise, LOW physical yield
**Type:** Pattern
**Severity:** HIGH (предотвращает повторный запуск без сужения)
**Confidence:** HIGH (362 advertisers проанализировано, 0 reportable)
**Evidence count:** 362 unique advertisers, 1 category signal (score 62)
**Observation:** Keyword "keep kids busy" — ситуационный broad keyword. 362 рекламодателя. Структура:
- ~30% — subscription boxes (Woobles crochet, CrunchLabs), established brands (широкая категория "kids activity")
- ~25% — digital (apps, courses, online camps)
- ~20% — retail (ролевые наборы, настольные игры через Amazon affiliates, etsy)
- ~15% — DTC физические продукты, но большинство несовместимы по цене ($9.99 dragon egg) или established (Hadley Designs, Rouvenor)
- ~10% — другое
YIELD: 0 reportable products. 1 category signal: Magic Playwall by Cherrypick (shopcherrypick.com) — magnetic wall mounted activity board для детей, score 62 (категория интересная, но продукт не прошёл threshold).
ПАТТЕРН: "keep kids busy" = слишком broad → захватывает subscription economy, не DTC физические продукты. Лучше использовать product-specific keywords ("magnetic activity board", "kids building toy", "craft kit kids").
**Applies to:** Kids vertical keyword selection — не использовать "keep kids busy" как primary keyword
**Expires after:** Session 20

---

### [2026-05-16] Session 13 — Magic Playwall by Cherrypick: Category Signal for Magnetic Wall Activities
**Type:** Signal
**Severity:** MEDIUM (category signal, не final product)
**Confidence:** MEDIUM (1 DTC advertiser, store verified)
**Evidence count:** shopcherrypick.com, UGC creator (UGCbyTosin), 1 active FB advertiser, Jan 2026
**Observation:** Cherrypick (shopcherrypick.com) рекламирует Magic Playwall — magnetic wall-mounted activity board для детей. Jan 2026. 1 активное объявление. Продукт: магнитная панель на стену с деревянными деталями. Score 62 — не прошёл порог 65 из-за: (1) только 1 активный рекламодатель, (2) COGS/цена неподтверждены, (3) не verified на Alibaba.
КАТЕГОРИЙНЫЙ СИГНАЛ: "Magnetic wall activity board for kids" = растущая категория. Pinterest / Etsy тренд. Если найдётся второй DTC бренд → категория открывается.
СЛЕДУЮЩИЙ ШАГ (если Marina approves): запустить keyword "magnetic activity board" или "magnetic play board" — проверить есть ли другие DTC advertisers.
Notion: https://www.notion.so/36253ba8196e81bcab5bd8e20a7b81ec
**Applies to:** Kids vertical — wall activity category
**Expires after:** Session 20

---

### [2026-05-16] Session 13 — "screen free" keyword: HIGH app noise (иронично), confirms existing winners
**Type:** Pattern
**Severity:** HIGH (предотвращает повторный запуск как primary discovery keyword)
**Confidence:** HIGH (294 advertisers проанализировано, 0 new reportable)
**Evidence count:** 294 unique advertisers, 0 новых products ≥65
**Observation:** Keyword "screen free" = иронично высокий шум от цифровых продуктов. 294 рекламодателя. Структура:
- ~35% — apps и digital services, которые рекламируют себя как "screen free alternative" (используют термин в copy, но сами являются digital)
- ~25% — established brands (Yoto Player доминирует — появился 4+ раза, разные accounts)
- ~20% — детские физические продукты, но confirmed: Camp Snap (Score 77) + Thoson Kids (Score 67) + Wonder Quest (Score 70) — все уже в reported-products.md
- ~20% — non-kids (взрослые товары, австралийские бренды, ниже price floor)
YIELD: 0 новых reportable products. Keyword работает как VALIDATION keyword — подтверждает уже найденные продукты, но не открывает новые.
ВЫВОД: "screen free" ≠ primary discovery keyword. Использовать только для validation существующих кандидатов или как дополнительный сигнал. Yoto Player = dominant established brand в этом keyword — его присутствие сигнализирует о насыщенности аудитории.
**Applies to:** Kids vertical keyword selection — не использовать как primary discovery keyword
**Expires after:** Session 20

---

## Expired / Promoted

> **Инструкция по архивации:** Записи с "Expires after: Session N" где N ≤ текущей сессии
> переносятся в этот раздел Мариной вручную через review/promotion-queue.md.
> Агент не удаляет записи — только добавляет новые.

> **АРХИВАЦИЯ ВЫПОЛНЕНА (Session 13, 2026-05-16):**
> 18 записей удалены из файла. Марина подтвердила "ок".
> Archive reference: /departments/facebook-ads-library/operational-memory/learnings-archive-queue.md

---

## How to Add a New Learning

Append to Active Learnings using this format:

```
### [YYYY-MM-DD] Session N — [Short Title]
**Type:** Pattern / Warning / Signal / Tactical
**Severity:** LOW (observation) / MEDIUM (repeated pattern) / HIGH (affects scoring or rejection) / CRITICAL (core logic failure)
**Confidence:** LOW (1 weak signal) / MEDIUM (2–3 cases) / HIGH (multiple products or founder-confirmed)
**Evidence count:** N cases / N sessions
**Observation:** what was found
**Applies to:** [keyword category / product type / search method]
**Expires after:** Session [N+7] or earlier if promoted
```

## Correction Format

Do NOT edit old entries. Append a correction block directly below the original entry:

```
[CORRECTION YYYY-MM-DD]
Original learning: [date + title of entry being corrected]
Why it was wrong: [specific reason]
Replacement / updated interpretation: [what is true instead]
Action: Update confidence / Invalidate / Replace with new entry
```

## Promotion Rules

A learning may be added to `review/promotion-queue.md` only if:
- confirmed across **3 sessions**, OR
- **explicitly approved by Marina**

After one session only → stay in departments/facebook-ads-library/operational-memory/learnings.md regardless of signal strength.
Never self-promote into core/ files.
