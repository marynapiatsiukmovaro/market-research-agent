# Post-Cleanup Audit — 2026-05-28

**Цель аудита:** Сверить состояние проекта `market-research-agent` со снапшотом исходного аудита (`market-research-agent_audit.pdf`, 2026-05-27). Подтвердить, что предыдущая чистка не сломала систему, и найти оставшиеся мелкие нестыковки — без перестройки архитектуры.

**Главный вывод:** Работа предыдущей сессии — большой шаг вперёд. Архитектура стала чище, кросс-ссылки в порядке, два департамента (FB + ShopHunter) корректно изолированы. Найдено ~5 точечных мест, которые стоит подровнять перед добавлением третьего департамента. Ничего критичного, никакой переделки.

---

## ✅ Что было сделано хорошо (подтверждено)

1. **CLAUDE.md разделён на Layer A / Layer B.** Чёткий contract: что грузить всегда, что — только для активного департамента. Это масштабируется на любое количество новых департаментов.
2. **`founder-taste.md` поднят из FB в `shared/`** — теперь компания-уровень. Все старые ссылки (`departments/facebook-ads-library/operational-memory/founder-taste.md`) убраны. Чисто.
3. **Стратегия больше не зашита в CLAUDE.md.** Теперь — единственный источник `departments/{dept}/hypotheses/_active.md`. Это убирает риск «забыл обновить CLAUDE при смене гипотезы».
4. **ShopHunter оформлен как полноценный департамент:** есть `workflow.md`, `capabilities.md`, `methods/`, `operational-memory/learnings.md` + `founder-feedback.md` + `handoffs-archive.md`, `hypotheses/_active.md`.
5. **RULE-15 (Memory File Growth Discipline)** в `core/session-health-rules.md` — отличная превентивная политика для роста файлов памяти. Особенно важно с появлением SH.
6. **README.md обновлён под текущую архитектуру** — структура папок, описание двух департаментов, ссылки на нужные файлы.
7. **`shared/sources-overview.md` стал каналонезависимым** — корректно говорит, что приоритет источников определяется в `workflow.md` департамента.
8. **`core/winner-detection.md` помечен как «Strategic reference»** с явным указанием на FB+SH как primary discovery. Старый алгоритм сохранён как историческая справка.
9. **Архивные пути убраны из активных файлов** — `review/audit-2026-05-15.md` → `archive/`, `shared/telegram-report.md` → `archive/`. В non-archive файлах ссылок на старые пути нет.

---

## 🔧 Что осталось подровнять (по приоритету)

### Priority 1 — Реальные противоречия (стоит починить)

#### 1.1 Устаревший кап «2–5 продуктов» в 4 файлах

Канон в CLAUDE.md / README.md / `core/identity.md`: «Minimum 2, **no upper limit** — report all 65+». Но 4 файла всё ещё несут старую формулировку «2–5»:

| Файл | Строка | Что написано сейчас |
|------|-------|---------------------|
| `core/agent-rules.md` | 35 | «Target **2–5** products per session — quality over quota, never force weak products to fill 5» |
| `departments/facebook-ads-library/workflow.md` | 7 | «Output: **2–5** best products in Scout Mode format» |
| `prompts/find-products.md` | 39 | «For each qualifying product (**2–5** expected)» |
| `prompts/daily-report.md` | 9 | «All qualifying products (**2–5**) with scores» |

**Особо коварный кейс:** `departments/facebook-ads-library/workflow.md` сам себе противоречит — строка 7 говорит «2–5», строка 80 (STEP 5) уже правильно говорит «Include ALL products scoring 65+. No upper limit». Любой агент, прочитавший шапку, может остановиться на 5.

**Правка:** заменить «2–5» на «Minimum 2, no upper limit — all 65+» в этих четырёх местах. Минута работы.

---

#### 1.2 `prompts/` устарели по архитектуре

`prompts/find-products.md` написан под одно-департаментный мир (FB-only). Сейчас два департамента, и CLAUDE.md правильно говорит: «Follow your active department's `workflow.md`. The department is stated in the session prompt; if unstated, ask which one.»

Но сам `find-products.md`:
- Не спрашивает о департаменте,
- Зашивает FB-логику («Scan 15–20 candidates from primary sources»),
- Несёт устаревший кап (см. 1.1),
- Дублирует то, что уже есть в `workflow.md`.

**Правка-минимум:** добавить в шапку `find-products.md` строчку: «Specify department (`facebook-ads-library` или `shophunter`). Then run that department's `workflow.md` per CLAUDE.md.» — и убрать FB-зашитые шаги, оставив только общую логику + ссылку.

То же для `daily-report.md` — формат выхода вроде универсальный, но «2–5» надо убрать.

---

### Priority 2 — Мёртвые / сиротские файлы в `core/`

После переезда логики в Layer A/B многие core-файлы стали орфанами — на них нигде нет ссылок и в обязательный load они не входят:

| Файл | Длина | Где упоминается | Что внутри |
|------|-------|------------------|------------|
| `core/rejection-rules.md` | 7 строк | **0 ссылок** | заглушка-указатель на mandatory-filters.md |
| `core/agent-rules.md` | 58 строк | **0 ссылок** | дублирует логику operating-rules + identity |
| `core/autonomy.md` | 19 строк | **0 ссылок** | общие «SHOULD / SHOULD NOT» — поглощено identity.md и mindset.md |
| `core/token-efficiency.md` | 18 строк | 1 ссылка (SH README) | overlaps с identity.md (Scout Mode) |

**Рекомендация:** для каждого — два варианта на выбор:
- **(a) Архивировать:** перенести в `archive/core-legacy/` с одной строкой-указателем, чтобы grep всё ещё работал по истории. Не удалять физически — будут видны как фон, но не путать агента.
- **(b) Слить** ценные пункты в активный файл (например, уникальная фраза из autonomy.md «Your scope: product discovery and early-stage validation only» → в `identity.md`), потом архивировать.

`core/rejection-rules.md` — однозначно (a) или просто удалить, это пустой указатель.

⚠️ **Перед действием:** проверь, что VPS-скрипты или внешние агенты не читают эти файлы по жёсткому пути. Если читают — переименование сломает.

---

### Priority 3 — Каталог `scripts/` — кандидат на разнос по департаментам

CLAUDE.md File Map уже честно говорит: «dept-specific scripts move under departments/{dept}/ over time». Сейчас перекос очевидный:

- **28 из 30 скриптов — ShopHunter** (`sh_*`, `sh4_*`, `sh5_*`, `sl_*`, `ap_*`, `build_enrich*`, `build_tracked*`, `set_shophunter*`)
- **1 — FB** (`update_fb_session.py`)
- **2 — общие** (`md_to_pdf.py`, `prep_next_dumps.sh`)

**Дополнительные точки уборки внутри scripts/:**

*Возможные дубли / версионные варианты (стоит выяснить, какая версия живая):*
- `sh_cat_dump.py` + `sh_cat_dump_v2.py`
- `sh_collection_add.py` + `sh_collection_add_test.py`
- `sh_collections_recon.py` + `sh_collections_recon2.py`
- `sh_proxy_diag.py` + `sh_proxy_diag2.py`

*Скрипты с нулём ссылок в репо (возможно мёртвые — но могут вызываться с VPS-стороны):*
- `scripts/build_enrich_input.py`
- `scripts/build_tracked_docs.py`
- `scripts/sh_iface_recon.py`
- `scripts/sl_iface_shots.py`

**Рекомендация:** не трогать сейчас руками — но при следующей ShopHunter-сессии Марина может попросить агента отметить в `methods/discovery-funnel.md`, какие скрипты он сейчас реально вызывает. После этого:
1. SH-скрипты → `departments/shophunter/scripts/`
2. FB-скрипты → `departments/facebook-ads-library/scripts/`
3. Generic → остаются в `scripts/` (или в новой `tools/`)
4. Сиротские «v2 / _test / _recon2» — после подтверждения, что они не нужны, → `archive/scripts-legacy/`

⚠️ Это **не сейчас**. Это пункт «когда дойдут руки» — никакого срочного риска.

---

### Priority 4 — Будущее имя архива для rejected-products

`core/session-health-rules.md` строка 81 говорит, что при ротации `shared/rejected-products.md` файл должен перетекать в `archive/rejected-products-archive.md`. Сейчас в архиве есть только `archive/rejected-products-pre-S21-archive.md` (исторический срез).

**Это не баг сейчас** — просто когда триггер первой ротации сработает, агенту нужно либо создать `rejected-products-archive.md` (как указано в правиле), либо аккуратно дополнить существующий pre-S21 архив. Лучше — заранее зафиксировать в `op-rules` SH или FB одну строчку, чтобы выбор имени не делался импровизированно.

---

## 📌 Сводный чек-лист правок (когда будешь готова)

Минимальный пакет — то, что стоит сделать в одну короткую сессию:

- [ ] Убрать «2–5» из `core/agent-rules.md:35`
- [ ] Убрать «2–5» из `departments/facebook-ads-library/workflow.md:7`
- [ ] Убрать «2–5» из `prompts/find-products.md:39`
- [ ] Убрать «2–5» из `prompts/daily-report.md:9`
- [ ] Обновить `prompts/find-products.md` под Layer A/B — «укажи департамент, иди в его workflow.md»
- [ ] Решить судьбу 4 сиротских core-файлов (архивировать / слить / оставить)

Опционально — на потом:
- [ ] Разнести `scripts/` по департаментам
- [ ] Зафиксировать имя файла будущего архива rejected-products

---

## 🟢 Что НЕ ТРОГАТЬ

Эти места выглядят странновато, но это «фича», а не «баг»:

- **`emotional-trigger-scan.md` в `core/research-framework.md`** — помечено как «future example», т.е. это иллюстрация будущей гипотезы. Удалять не нужно.
- **`memory/kids-vertical-patterns.md` в `kids-vertical.md`** — внутри архивированной гипотезы, исторический след. Не трогать.
- **`project_keyword_audit_system.md` в `learnings.md`** — упомянут в исторической таблице «S10–S11». След прошлого, не активный путь.
- **«2–5 lines max» в `learnings.md`** — это про размер заметок-наблюдений, не про количество продуктов. Не путать с капом «2–5 продуктов».
- **Все ссылки на «Broad Horizontal Discovery» вне `archive/`** — либо в архивированных гипотезах, либо как пример «temporary research direction». Корректно.
- **`outputs/daily-reports/` 5 файлов** — нормальная глубина для regular workflow. Будут периодически смахиваться в `archive/daily-reports/` по RULE-15.

---

## 📐 Микро-наблюдение про масштабирование

Когда будешь добавлять третий департамент (Instagram / TikTok Ads / Amazon), архитектура уже почти готова. Понадобится только:
1. Скопировать структуру `departments/{template}/` (workflow.md + operational-memory/ + hypotheses/_active.md + methods/).
2. Если департамент использует уникальный signal-тип, добавить пункт в `shared/sources-overview.md` «Department primary surfaces».
3. Добавить enum-значение в `core/identity.md` «Discovery Type» (сейчас FB / SH / Amazon / TikTok / Trend / Problem-solving / Viral / Founder).
4. Если в Notion есть field «Source», убедиться, что в `shared/notion-schema.md` enum синхронизирован.

CLAUDE.md трогать не нужно — Layer B уже параметризован через `{dept}`.

---

**Итог:** база подготовлена к масштабированию. Все правки выше — косметика поверх крепкого фундамента.
