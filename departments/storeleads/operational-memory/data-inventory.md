# Store Leads — DATA INVENTORY (где что лежит) — read at session start

> **Зачем (Marina, S17 2026-06-29):** один канонический указатель «где всё лежит», чтобы ни одна сессия
> больше не искала данные наугад (на старте S16 агент пошёл искать CSV на Desktop, не зная где они).
> Закрывает AUDIT-1 + AUDIT-2. Это карта, а не метод — метод выгрузки см. `methods/csv-export.md`.

---

## 🔌 VPS-подключение
- Host: `root@5.78.217.133` · Key: `~/.ssh/market_research_vps` · Base: `/opt/market-research-agent`
- **Credit-guard (Marina, обязательно):** перед любым запуском `ps aux | grep claude` на VPS. НИКОГДА
  параллельный `claude`. На VPS бегает только Playwright/скрипты; `claude` — только на Маке (RULE 13).
- Сессия StoreLeads: passwordless (email + 6-значный код). Аккаунт `babbystorecom@gmail.com`.
  Ре-логин: `scripts/sl_email_login.py` (живёт неделями; восстановить свежим кодом). Проверка: `sl_check_login.py`.

## 🗂️ Юниверс-вселенная (текущий источник данных) — НЕ в git (слишком большие)
Два CSV, **захвачены 2026-06-08 на Pro-плане, 162 колонки**, лежат в ДВУХ местах байт-в-байт:
- **VPS:** `logs/storeleads/exports/` (+ `.sentinel` + backup-логи)
- **Desktop:** `~/Desktop/StoreLeads_Exports/`

| Файл | Платформа | Строк (магазинов) | Размер |
|---|---|---|---|
| `storeleads_shopify_active_2026-06-08.csv` | Shopify Active | **2,890,820** | 6.14 GB |
| `storeleads_woocommerce_all_2026-06-08.csv` | WooCommerce | **4,255,809** | 4.98 GB |

> **Pro auto-renew ВЫКЛ (Marina S17) — Pro-окно закрывается 2026-06-29 (сегодня); после этого переэкспорт
> невозможен без повторного включения Pro. Эти файлы = постоянный актив (снимок). Текущий анализ Pro НЕ требует
> (работает по CSV + session-enrich).** WooCommerce — 2-й независимый юниверс; его карточки нужен НЕ-Shopify
> энрич-путь (`/products.json` там нет) — оценить перед использованием.

### ✅ Проверка полноты выгрузки (S17, 2026-06-29) — выгрузка честная
Сверка живого StoreLeads с нашим снимком (ожидаемый недельный дрейф базы, не потеря):

| Срез | Живой StoreLeads | Снимок 2026-06-08 | Дрейф |
|---|---|---|---|
| Shopify + Active (весь) | 2,867,778 | 2,890,820 | −0.8% |
| Home & Garden → Home Improvement | 33,410 | 32,967 | −1.3% |

Инструменты сверки: `scripts/sl_filter_count.py` (живой счётчик по фильтру `bq`), `scripts/sl_csv_check.py` (счётчик по CSV).
Замечено: **категория** фильтруется на сервере (`bq cat match`), **визиты** — на стороне клиента (из данных).

## 🛢️ Энрич-резервуары (готовые Stage-2 файлы для анализа) — на VPS
`logs/storeleads/niches/<niche>/`:
- `home-and-garden/` — `hg_b1..b22_enriched.json` (**5,500 магазинов**, полоса 1k–10k) + `_table.html`; у `b1` есть `_crossref/_opens/_scores.jsonl`
- `toys-and-hobbies/` — `th_1k10k_full.json` (срез 7,639) + `th_1k10k_s1_b1..b3_enriched.json` (**750 магазинов**, полоса 1k–10k, построены S17; ещё ~28 чанков в срезе)
- `pets-and-animals/` — Dogs/Cats прошлых сессий

**Итого соэнричено (enriched_index): 27,749 магазинов.** `processed` (проанализировано) = 19,604 — **enriched ≠ processed**, это инвариант: сборка не помечает processed, только анализ.

## 📒 Состояние (single source of truth — на VPS, зеркало в репо)
`logs/storeleads/` на VPS:
- `processed_domains.json` — мастер-запись проанализированных магазинов (RULE 19/20). **Зеркало в репо:** `operational-memory/processed_domains.json`.
- `master_domains.json` — кросс-нишевый dedup (RULE 19).
- `enriched_index.json` — что уже соэнричено (decoupled build, RULE 30).
- `_visits_map.json` — карта визитов.
- `operational-memory/keep-list.md` (в репо) — strong/borderline магазины для будущего newest-first монитора (RULE 20).

## 🛠️ Скрипты выгрузки
- **Текущий:** `scripts/sl_export_run.py` — CSV-экспорт всей вселенной (Pro). Метод → `methods/csv-export.md`.
- **RETIRED (сохранено):** `scripts/sl_dump*.py` — старый постраничный API-дамп через `/json/auth/domains` (упирался в квоту HTTP 402 на Premium). Не использовать; оставлено «вдруг вернёмся».
- Сверка/верификация: `sl_filter_count.py`, `sl_csv_check.py`. Селекторы батчей: `sl_select_all.py` (RULE 24), `sl_select_build.py` (decoupled build).
