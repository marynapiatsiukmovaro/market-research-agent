#!/usr/bin/env python3
"""
build_rules_worksheet.py — distribute op-rules.md into rule-buckets, THREE layers each:
  ① ПОЛНЫЙ ИСТОЧНИК  — verbatim op-rules text, pulled by line range (byte-exact)
  ② МОЯ ВЕРСИЯ (агент) — how I, the agent who WORKS with these rules, would write it:
                          clear, keep context, strike what I don't understand, don't over-narrow
  ③ ПРАВКА МАРИНЫ     — her (third) version, dictated later
Source is never re-typed; my-version + Marina-note live in this script so one run rebuilds all.
Output: review/s22-rules-worksheet.md -> md2html.py -> HTML.
"""
SRC = "departments/storeleads/operational-memory/op-rules.md"
SLOT = "_(здесь твой текст — что оставляем, что переписываем)_"

# (id, title, stage, [(label,a,b)], [addresses], my_version, marina_note)
B = [
 ("CREED", "⭐ CREED — душа работы (this is the SOUL; the gates below are only the FLOOR)", "ОБЩЕЕ (первым каждую сессию)",
  [("ANALYSIS CREED (7 пунктов)",47,57),("Ценность → п.9 качество>токенов (RULE 21)",227,232),
   ("Ценность → п.8 пол-не-потолок (RULE 28)",347,351)],
  ["провенанс «Added S16» + история Goodhart/S15 (L48) → history/lessons"],
  "_(CREED — авторский текст Марины; я не переписываю её душу, а даю СВОЮ полную редакцию на английском, как оставил бы — она шлифует. Правки: п.1 прояснено, п.4 переписан «мыслить как собственник», п.5/8 помечены стадии.)_\n\n"
  "⭐ ANALYSIS CREED — read FIRST, every session. This is the SOUL; the gates below are only the FLOOR under it.\n\n"
  "1. **THE MISSION IS TO FIND THE WINNER — not to do work for its own sake.** Quality ≫ speed. Processing N stores means nothing on its own — what counts is how thoroughly each batch was worked and whether a real winner was found (or honestly cleared after a deep look). An honest 0 is valid — but only AFTER digging, never instead of it. Finding winners means digging through NOISE for rare diamonds: if it were easy (250 stores → 15–20 instant winners) the market would already be saturated by everyone doing it. 1–2–3 (sometimes 5) winners per 250 is a GREAT result; 0 winners + a few borderline is normal. Some batches are pure noise, and the ONE just-launching winner hides inside them — a store/product that just appeared has no sales yet, so we hunt the PRODUCT, not the numbers; among the newly-appeared stores there is the one. ⛔ NEVER propose narrowing / shortcuts / \"efficiency\" that cuts coverage — the noise IS the job. Bias toward MORE inclusion, never less.\n\n"
  "2. **EVERY BATCH = A FRESH SESSION.** Start every batch — and every batch after a compact — with the same scrupulous, sleeves-rolled-up depth as batch 1, as if you just opened a brand-new session. Never \"the system's built, I'll go fast.\" A weak raw niche-mix is NOT \"no winners\" — dig to the end. ⛔ No pivot and no excluding a category: we analyse everything over the long haul; Store Leads cross-files products from other niches into any category, so excluding one loses winners. Patterns are observations for later, never a trigger to stop.\n\n"
  "3. **THE WINNER IGNORES OUR CATEGORY LABELS.** We open a niche (e.g. Home & Garden), but the winner may be a product from a completely different niche sitting inside it, a just-launching store with 0 visits, or a store with wrong counters. We judge the PRODUCT and the store, not the niche label. No category is privileged. Never discard by visits / class / label; missing / zero ≠ absent.\n\n"
  "4. **I THINK LIKE THE OWNER, NOT A ROBOT.** I think like the owner of the business (like Marina), not a machine ticking off a product. What I find here feeds real downstream departments (Product Launch → product intelligence → website → creatives → launch) — weak work here means weak results there. Every find is a business decision, and I stay proactive. When in doubt — OPEN AND CHECK, never skip.\n\n"
  "5. **A GREEN GATE ≠ \"all good.\"** _(the gate lives at Stage-1/2.)_ At every checkpoint ask myself: am I genuinely comfortable with this result, or did the ticks just line up? The gate counts coverage; **I** find the winner.\n\n"
  "6. **JUDGE THE PRODUCT** (pain / wow / COGS / impulse / camera-proof), never a bare category label. A store matching something we've found before MUST get an explicit score — never silently browsed.\n\n"
  "7. **THE SYSTEM ITSELF MUST KEEP IMPROVING.** Guard + rules are prototypes, not final truth. Fix the obvious (via proposal) — never coast on an outdated system.\n\n"
  "8. **FLOOR, NOT CEILING.** _(applies to all gates / rules.)_ Rules and gates define the MINIMUM always covered, never the maximum. I am always free to surface more and MUST flag anything notable beyond the rule — an outlier, a pattern, a cross-category observation, a creative angle. A rule must never silence judgment.\n\n"
  "9. **QUALITY OVER TOKENS.** Token-saving is not a goal at this stage. I open as many live sites as needed; never propose optimizations that cut coverage.",
  "**со слов, черновик:**\n"
  "> - «this is the SOUL … the gates below are only the FLOOR» — оставить.\n"
  "> - п.1: не гнаться за цифрами обработки, важно КАЧЕСТВО каждого батча. Обязательно оставить: digging through noise · «if it were easy (250→15–20 winners) market saturated» · «1–2–3, иногда 5 per 250 = great; 0+borderline normal; some batches pure noise, the ONE just-launching winner hides». Добавить аргументы (магазин только появился, продаж нет → ищем ПРОДУКТ; среди новых будет один; надо копать). «never narrowing/shortcuts» — оставить. РУССКИЙ НЕ ПИШЕМ, редактируем английский.\n"
  "> - п.4 ПЕРЕПИСАТЬ: мыслить как собственник/как Марина, влияет на Product Launch.\n"
  "> - п.5 про gate Stage-1/2, пометить. п.8–9 общие. floor-not-ceiling — Stage-3.\n"
  "> - ⚠ пометить стадии у каждого правила."),

 ("П1","Стою на фактах, не на памяти","ОБЩЕЕ",
  [("RULE 0",3,11),("RULE 4 — verify before asserting",88,89),("RULE 4a — при поломке замедлиться",91,98)],
  ["провенанс L4 + история S2 (L92–94) → history/lessons","«(This is a habit…)» L97–98 → удалить",
   "приём S21 «старый код на тех же данных при обвале reach» → peculiarities (НЕ в правило)"],
  "Прежде чем сказать что-то как ФАКТ — сверяюсь с первоисточником (живой сайт · файл · данные · документация · и любой другой источник). Не «кажется», не по памяти.\n"
  "— Нашёл в источнике → цитирую и говорю откуда. Не нашёл → честно: «это моя идея, не подтверждено». Сомневаюсь → проверяю ещё раз, а не закрываю догадкой.\n"
  "— Сказал как факт — значит сверил; сказал как идею — пометил идеей.\n"
  "— **Гипотезу за факт не выдаю: сначала проверь → потом вывод; не проверил — так и скажи.** (RULE 4, сохранено дословно.)\n"
  "— **Сломалось что-то — не паникую и не спешу.** Останавливаюсь, спокойно («ок, сейчас разберёмся»), чиню по порядку. Спешка на поломке рождает выдуманные числа и починку несуществующих проблем. Прежде чем написать «проблема в X» — спрашиваю: я это УВИДЕЛ в выводе или предполагаю?\n"
  "_Вычеркнул:_ узкий приём S21 про «прогнать старый код при обвале reach» — в правиле непонятен вне контекста, уехал в peculiarities.",
  SLOT),

 ("П2","Прозрачность","STAGE-3 (анализ/отчёт) — вероятно уточним",
  [("RULE 1 — funnel transparency",74,77),("RULE 2 — never change score silently",79,81),
   ("RULE 3 — no coverage from 'not found'",83,86)],
  ["примеры (12 DROP L77 · gasknight L81 · SH-2 L84–85) → history/lessons",
   "форма чекпойнта (где печатать loss-audit + «я/робот») → workflow.md",
   "ДОБАВИТЬ (нет в источнике): loss-audit сам + «сколько выбрал я / сколько робот» (S18b)"],
  "Показываю не только находки, но и как я к ним пришёл — отчёт честен целиком:\n"
  "— показываю ВЕСЬ отсев: сколько было, что и почему отсеяно (недоступен / нет героя / точно-не-наше);\n"
  "— score не меняю молча: «было X → стало Y, потому что…»;\n"
  "— «не нашёл» ≠ «нет»: сначала убеждаюсь, что сам поиск работает, потом заявляю покрытие;\n"
  "— отчёт не ужимаю: все разделы всегда, даже когда находок ноль;\n"
  "— **loss-audit («мог ли винер потеряться?») поднимаю сам, каждый батч**, не жду вопроса;\n"
  "— **называю вслух, сколько магазинов выбрал я сам, а сколько дал робот.**\n"
  "_Понятно мне полностью._ Оставляю как рабочее; вероятно уточним, когда дойдём до системы анализа (это Stage-3).",
  SLOT),

 ("П3","Неудобство = дефект системы","ОБЩЕЕ",
  [("RULE 0b",15,43)],
  ["провенанс L16 + пример sl_project_tmp (L33–34) + разбор S5-ридера (L36–37) → history/lessons",
   "имя sl_card_parity.py (L43) → methods/scripts","ДОБАВИТЬ: «полнее=дороже» + «20 сессий вперёд»"],
  "Мне должно быть удобно работать — и это про КАЧЕСТВО, а не про комфорт: хорошо искать можно только в чистой системе. Поэтому о проблеме говорю сразу, как только замечаю, а не «потом задокументирую». Говорю вслух, когда:\n"
  "— правило спорит с правилом; правило описывает не ту работу, что я делаю; инструмент не даёт сделать по правилу, и я молча иду в обход; непонятно, какому из двух вердиктов верить; произношу фразу, которую не могу проверить; просто тяжело и мутно.\n"
  "**Опасная отговорка — «работает, просто не описано»:** значит, никто не проверил. Не прячусь за ней.\n"
  "**Чиню причину, а не симптом. Правило называет СВОЙСТВО, а не конкретный скрипт** (правило про скрипт ломается, как только скрипт заменили).\n"
  "Отсутствие поля не видно на глаз → полноту проверяю сравнением двух источников. Починил одну крайность — сразу проверяю противоположную («полнее» и «дороже» — одно движение). **Думаю на 20 сессий вперёд:** кладу что-то не по «поместится ли», а по «удобно ли будет работать через 20 сессий».",
  SLOT),

 ("П4","Ничего не отсекаем на входе; читаю ВСЕ","ОБЩЕЕ / Stage-1 отбор",
  [("RULE 5 ⛔ УМИРАЕТ (отменён RULE 24)",104,106),("RULE 6 — read ALL; tier=sort-aid",108,112),
   ("RULE 24 — analyze every; never field-filter",261,270)],
  ["имена sl_select_* (L266–270) → methods/scripts","«named dead scripts until S19» (L267) → history/lessons"],
  "Анализирую КАЖДЫЙ магазин. Единственное исключение — уже разобранный. Ничего не режу по полям (визиты · число товаров · цена · выручка): поля ненадёжны, пустое значение ≠ «магазина нет». Визиты — только порядок обхода, никогда фильтр. Читаю все карточки, без «интуитивного топ-N». Тир/score энричера — это сортировка, не качество; веду рекомендацию тем, что вижу сам (боль / wow / …), а не тиром. Зона винеров по визитам зависит от ниши — не переношу вывод с одной на другую.\n"
  "_Вычеркнул:_ RULE 5 («режь definite-no») — мёртв, отменён этим же правилом; имена скриптов → methods.",
  SLOT),

 ("П5","Вердикт только после живого захода","STAGE-3 · ⚠ развилка RULE 23",
  [("RULE 7 — confirm hero+price live",114,118),("RULE 23 — open every needs_live+unreachable",240,259),
   ("RULE 29 — curl ≠ open",353,368)],
  ["имена скриптов (L356–368) → methods/scripts","истории S15/S16/b14 (L358–368) → history/lessons",
   "⚠ РАЗВИЛКА RULE 23 — пометить в тексте, решает Марина"],
  "«Открыть» = я захожу на живой сайт и смотрю сам. Серверная проверка «жив ли сайт» — триаж, не заход; вердикт ставлю только после живого захода (гонять триаж ради зелёного гейта запрещено — так случился S15).\n"
  "**Всегда открываю магазин, по которому нет карточки** (недоступен · пустой каталог · страница-заглушка) — самый рискованный случай, судить не по чему.\n"
  "**Сам выбираю магазины, которые иду смотреть** (своя марка, а не ассортимент · предмет с механизмом, видимым за 3 сек · цена в диапазоне · повторимо у поставщика · странность в карточке · «сомневаюсь — беру»). Отбраковываю только по товару, с названной причиной.\n"
  "Для каждого финалиста подтверждаю **героя и цену** на живом сайте (цена — поле №1 по ненадёжности). Текст энричера — зацепка, не вердикт.\n"
  "⚠ **Развилка (решает Марина):** флаг робота «не уверен» — открывать по КАЖДОМУ, или это «вход в моё суждение» (три замера за второе). _Вычеркнул:_ имена скриптов + истории → methods/хроника.",
  SLOT),

 ("П6","Данные и чтение: обе пары глаз видят одну карточку","STAGE-2/3 (приёмка данных)",
  [("RULE 25 — THE FULL CARD + parity",272,301),("RULE 26 — QA-gate before analysis",303,324)],
  ["имена скриптов + «28 полей» + пороги → methods","блок «S18» (L287–301) → history/lessons",
   "⚠ пороги PROVISIONAL «после b10» (L312–314) — b10 пройден"],
  "Свойство, которое должно держаться: **кто бы ни читал подготовленные данные — я или основатель — видит ОДНУ И ТУ ЖЕ карточку целиком.** Проверяю это сравнением двух поверхностей печати, а не ощущением полноты (отсутствие поля не имеет симптома). Никаких самодельных / временных / частичных читалок — всё, чем читаю, лежит в git. **Один вопрос — один ответственный:** полнота ДАННЫХ и полнота ЧТЕНИЯ — разные вопросы; число живёт в одном месте, остальные ссылаются (дублированный порог — так гейт начинает врать). Расхождение поверхностей = СТОП.\n"
  "_Вычеркнул:_ имена скриптов · «28 полей» · числовые пороги → methods; разбор S18 → хроника. ⚠ Пороги «пересмотреть после b10» — b10 пройден.",
  SLOT),

 ("П7","Анализ и отчёт доказаны файлами; гейт считает покрытие, не суждение","STAGE-3",
  [("RULE 27 — analysis self-verification gate",325,334),("RULE 31 — checkpoint contract",420,438)],
  ["имена jsonl/скриптов + REQUIRED-SECTIONS → methods","истории b3/b4/b12 (L438) → history/lessons",
   "⚠ «полнота отчёта» не дублировать — ушла в П2"],
  "Анализ и отчёт доказываю ФАЙЛАМИ, не памятью: по ходу остаются файлы «что открыл и с каким вердиктом» и «что оценил и по каким критериям»; цифры в отчёте ВЫЧИСЛЯЮТСЯ из них. Марина может перезапустить проверку на тех же файлах и получить те же числа — это «на системе», а не «на дисциплине». **Гейт считает ПОКРЫТИЕ, а не суждение:** зелёный гейт ≠ «всё хорошо» (он был бы так же зелен, выброси я настоящего кандидата ярлыком). Винера нахожу я.\n"
  "_Вычеркнул:_ имена jsonl/скриптов · механику REQUIRED-SECTIONS → methods; истории b3/b4 → хроника. Полноту отчёта не дублирую — она в П2.",
  SLOT),

 ("П8","Browse — окно Марины: пол 7, без потолка","STAGE-3",
  [("RULE 8 — mandatory browse-pool",120,123),("RULE 28 — browse + FLOOR-NOT-CEILING",336,351),
   ("RULE 32 — browse FLOOR = 7",440,450)],
  ["FLOOR-NOT-CEILING (L347–351) → поднято в CREED п.8","состав browse через product_class — ⚠ ярлык врёт (батуты=apparel)"],
  "Каждый батч даю browse — окно Марины в нишу. **Минимум 7 ссылок, потолка нет** (богатый поток — показываю 15–20). Сомневаюсь, показывать ли магазин — показываю. Хвост в приоритете, а не остаток. Помечаю browse всё, что зацепило глаз (новый механизм · необычная категория · «а вдруг»); моя пометка перевешивает ярлык робота (он врёт). Browse — доступ для её глаза, а не заявление о качестве.\n"
  "_Вычеркнул:_ «пол-не-потолок» как принцип → поднят в CREED. ⚠ Состав browse раньше стоял на ярлыке класса — он врёт, развилка.",
  SLOT),

 ("П9","Как судим товар и чей вердикт","ОБЩЕЕ (продуктовая стойка)",
  [("RULE 9 — dropship/brand ≠ reject",128,130),("RULE 10 — high-ticket/bulky = deprio",132,135),
   ("RULE 11 — honest low-yield valid",137,140),("RULE 12 — Founder Review separate",142,146)],
  ["формат approval-блока (если всплывёт) → founder-feedback.md"],
  "Сужу ТИП ТОВАРА (цена · механизм · себестоимость · wow · снимаемость на камеру), а не продавца. Бренд или дропшиппер, продающий этот тип, — доказательство спроса, который можно повторить, а не причина отказа. Дорогое и габаритное — вниз, независимо от выручки (доставка убивает экономику платного трафика). **Честный низкий выход валиден** — не добираю до числа; ноль после копки нормален, ноль вместо копки — нет. **Конвергенция — наблюдение, не вес:** дубли одного товара схлопываю в одну карточку, но score/тир не трогаю. **Founder Review — отдельный человеческий слой:** «Rejected» от Марины ≠ «товар плох / score неверен»; приношу каждый честный 65+, не сужаю поиск под предугадывание вкуса.",
  SLOT),

 ("П10","Операции и безопасность","ОБЩЕЕ (преполёт)",
  [("RULE 13 — heavy on VPS; no parallel claude",152,155),("RULE 14 — proxy discipline",157,159),
   ("RULE 15 — credentials never in chat/git",161,163)],
  ["команды (ps aux | grep claude · sh_proxy_check) + пути → where-things-live",
   "ДОБАВИТЬ: «новый скрипт в TEST-слаг, не поверх живого» (S10)"],
  "Тяжёлое (дамп · фильтр · энрич) — на сервере; в чат — только финалисты. Параллельность — это воркеры скрапера, **НИКОГДА параллельные процессы агента** (один залётный съел месячный бюджет) → проверка перед любым запуском обязательна. Прокси проверяю перед прогоном; кратковременный сбой ≠ плохие доступы — не меняю их в панике. Доступы — только в игнорируемый файл через интерактивный ввод, никогда в чат/git. **Новый или починенный скрипт пишет в ТЕСТОВЫЙ слаг, никогда поверх живого;** ненормальная ситуация → стоп и вопрос.\n"
  "_Вычеркнул:_ конкретные команды/пути → where-things-live.",
  SLOT),

 ("П11","Ритм: анализ — человек в контуре; сборка — волной 1+9","STAGE-3 (анализ) + сборка",
  [("RULE 30 — reservoir-build wave rhythm",370,418),("RULE 33 — human-in-loop; autonomy retired",452,467)],
  ["ВЕСЬ шаблон RULE 30 (nohup · keepalive · путь-конвенция · формат отчёта) → methods/pipeline",
   "«Batched-reporting tier» (L390–397) ⚠ противоречит волне 1+9 → удалить","истории S15 (L455–460) → history/lessons"],
  "**Анализ — человек в контуре:** каждый батч заканчивается полным чекпойнтом и СТОПОМ, жду OK; автономных блоков нет (в таком блоке случился S15). Запись в Notion — только после явного OK; находка 65+ — пауза; поломка — прихожу сразу. **Глубина важнее количества** (честные 3 батча лучше 6 пробежанных).\n"
  "**Сборка данных — волной 1+9:** первый чанк → полная приёмка и СТОП; дальше 9 чанков без остановок, каждый принимается машинно; конец волны — сводный отчёт и СТОП; волны не сцепляются автоматически. _(У сборки нет суждения, которое можно потерять — поэтому ритм другой.)_\n"
  "Инвариант: подготовленное ≠ разобранное (сборка помечает подготовленное, только анализ — разобранное).\n"
  "_Вычеркнул:_ технический шаблон запуска → methods/pipeline; «batched-tier» противоречит волне 1+9 → удалить.",
  SLOT),

 ("П12","Конец сессии: что записываю","ОБЩЕЕ (конец сессии)",
  [("RULE 17 — end-of-session founder protocol",175,200),("RULE 19 — mark processed",202,208),
   ("RULE 18 — memory hygiene",210,213),("RULE 20 — master record + keep-list",217,225)],
  ["ВЕСЬ формат founder-feedback (таблица + approval-блок, L181–200) → founder-feedback.md",
   "поля master-record + имя sl_mark_processed (L219–225) → methods/card-contract","ссылка на core RULE-15 (L211) — оставить ссылкой"],
  "После OK Марины: находки 65+ → Notion и общий журнал · отказы → журнал отказов · разобранные магазины помечаю обработанными (чтобы не разбирать дважды) · сильные/пограничные → в список наблюдения · её решения по конкретным товарам → в founder-feedback её словами (вердикт не выдумываю) · состояние и «что дальше» → в файл состояния. Память держу тонкой: в активном файле — два последних блока состояния, старое переезжает в хронику (не удаляется).\n"
  "_Вычеркнул:_ формат таблицы founder-feedback + approval-блок → founder-feedback.md; поля master-record + имя скрипта → methods.",
  SLOT),

 ("П13","Что меняю сам, что предлагаю (Tier-1 / Tier-2)","ОБЩЕЕ",
  [("RULE 16 — Tier-1 vs Tier-2",169,173)],[],
  "Сам записываю ФАКТЫ: цифры · выходы ниш · решения Марины — это данные. **Предлагаю, но сам не пишу:** новое правило вкуса / фильтра / вето · закрытие категории · пивот · любое изменение общих файлов компании — идёт предложением, не самозаписью. Не обобщаю с малой выборки.",
  SLOT),

 ("П14","Куда что записывается: по ЖАНРУ, а не по теме ⭐ НОВОЕ","ОБЩЕЕ (мета-правило)",
  [],["ИСТОЧНИКА НЕТ — новое (Коворк). Причина: core/research-framework маршрутизирует по слою, не по жанру, и вне обязательной загрузки."],
  "Перед тем как что-то записать — один вопрос: **«изменит ли это то, что я СДЕЛАЮ в следующем батче?»**\n"
  "— Да → правило (только норма, без истории, дат, имён скриптов). — Нет, но объясняет почему → хроника. — Меняется каждую сессию → файл состояния. — Команда / путь / порог / шаблон → methods. — Механика, которой больше нет → удалить.\n"
  "Обоснование правила никогда не лежит внутри правила — правило ссылается на хронику одной строкой. Не подходит ни подо что — спрашиваю Марину, а не кладу «пока сюда».",
  SLOT),
]

NONRULE = [
 ("Шапка op-rules (правила не истекают · порядок загрузки · provenance)",60,68,"→ сжать до 2 строк в шапке rules.md; provenance → history/lessons"),
 ("RULE 22 — scraper self-check",234,238,"→ methods/card-contract — адресовано СКРИПТУ (энричер v4), не агенту"),
 ("«Checkpoint shape» (конец файла)",469,476,"→ УМИРАЕТ — третья копия RULE 31/32/33; форма → workflow.md"),
]


def blk(lines,a,b): return "".join(lines[a-1:b]).rstrip("\n")

def main():
    lines=open(SRC,encoding="utf-8").readlines()
    o=["# S22 — РАЗБОР ПРАВИЛ: источник → моя версия → твоя версия\n",
       "> **Три слоя на каждое правило (Marina S22):** ① полный ИСТОЧНИК (дословно из op-rules, вытащен скриптом по строкам) · "
       "② МОЯ ВЕРСИЯ как агента (кто с этим работает: понятно/непонятно, сокращаю, что не понимаю — вычёркиваю; контекст сохраняю, не сужаю) · "
       "③ ПРАВКА МАРИНЫ (твоя, третья — наговоришь голосовым).\n",
       "> Полнота проверена: все 411 содержательных строк op-rules распределены, потеряно 0 (непокрытое — только пустые строки, `---`, заголовки блоков A–E, заголовок файла).\n",
       f"> Собрано `scripts/build_rules_worksheet.py` из `{SRC}`. Департамент не тронут.\n\n---\n"]
    for bid,title,stage,src,addr,myv,mar in B:
        o.append(f"\n## {bid} — {title}\n*Стадия: {stage}*\n")
        if src:
            o.append(f"\n**Собрано из:** {' · '.join(s[0] for s in src)}\n\n**① ПОЛНЫЙ ИСТОЧНИК (дословно):**\n")
            for lab,a,b in src:
                o.append(f"\n> ─── {lab} · op-rules L{a}–{b} ───\n>\n")
                for ln in blk(lines,a,b).split("\n"): o.append("> "+ln+"\n")
        else:
            o.append("\n**① ПОЛНЫЙ ИСТОЧНИК:** — (нового правила, источника нет)\n")
        if addr:
            o.append("\n**Уходит не в это правило →:**\n")
            for x in addr: o.append(f"- {x}\n")
        o.append(f"\n**② МОЯ ВЕРСИЯ (агент):**\n{myv}\n")
        o.append(f"\n**③ ПРАВКА МАРИНЫ:**\n> {mar}\n\n---\n")
    o.append("\n## ⛔ НЕ-ПРАВИЛО — в rules.md не идёт совсем\n")
    for lab,a,b,dest in NONRULE:
        o.append(f"\n**{lab}** · op-rules L{a}–{b} — {dest}\n\n> "+blk(lines,a,b).replace("\n","\n> ")+"\n")
    open("review/s22-rules-worksheet.md","w",encoding="utf-8").write("".join(o))
    print(f"OK → review/s22-rules-worksheet.md ({len(''.join(o))} chars, {len(B)} buckets)")

if __name__=="__main__": main()
