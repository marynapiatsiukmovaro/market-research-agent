#!/usr/bin/env python3
"""
build_rules_by_file.py — op-rules distributed BY DESTINATION FILE.
Per file: ② МОЯ ВЕРСИЯ = verdict + the ACTUAL TEXT to paste into that file (copy-paste,
verbatim from op-rules by line range — NOT a pointer/name). ③ ПРАВКА МАРИНЫ.
Where the text must be written from live code, we say so honestly (no fake text).
Output: review/s22-rules-by-file.md -> md2html.py -> HTML.
"""
SRC = "departments/storeleads/operational-memory/op-rules.md"

# (file, desc, verdict, [(a,b) ranges pasted verbatim as insert-text], [manual lines], task_note_or_None)
DEST = [
 ("history/lessons.md", "Хроника — «почему система такая». НЕ грузится. Уже собрана (ступень 4).",
  "провенанс + разборы поломок; заново не формулирую, эти блоки уже лежат в history/lessons.md.",
  [("RULE 25 · блок S18",287,301),("RULE 29 · истории",358,368),("RULE 4a · история S2",92,98)],
  [], None),

 ("methods/card-contract.md", "Контракт карточки — что робот отдаёт (задание скрипту).",
  "блоки op-rules описывают МЁРТВУЮ карточку v4.2 — не переносить; файл пишется по живому коду (_TEST).",
  [], [], "готового текста НЕТ — это задача: снять контракт с _TEST-скриптов. «28 полей» выкинуть."),

 ("methods/pipeline.md", "Механика прогона — команды, пороги, шаблоны.",
  "весь технический прогон RULE 30 → сюда, КРОМЕ «batched-tier» (L390–397, удаляю — спорит с волной 1+9).",
  [("RULE 30 без batched-tier · часть 1",370,389),("RULE 30 без batched-tier · часть 2",398,418)],
  ["Плюс числа-пороги из RULE 26: reach≥90 · ≥1top≥97 · descConf≥99 · in_range≥99 · cur_null=0."], None),

 ("methods/scripts.md", "Реестр действующих скриптов. Имена — только здесь.",
  "реестр собрать по факту (VPS); сейчас имена в правилах врут (TEST↔канон, долг №1).",
  [], [], "готового текста НЕТ — это задача: сверить с кодом. Форма записи: `имя · что делает · жив/мёртв`."),

 ("workflow.md", "Форма процесса и чекпойнта.",
  "сюда — только ФОРМА чекпойнта (содержание не дублирую; «Checkpoint shape» = дубль RULE 31/32/33).",
  [("«Checkpoint shape»",469,476)], [], None),

 ("founder-feedback.md", "Формат решений Марины. 🔴 Красная линия — сам файл не трогаем.",
  "формат заметок из RULE 17 → дословно в шапку founder-feedback.",
  [("RULE 17 · формат заметок + approval-блок",181,200)], [], None),

 ("where-things-live.md", "Пути и команды — без меняющихся цифр.",
  "собрать пути и команды.",
  [], ["Перед любым запуском на VPS: `ps aux | grep claude` (credit-guard).",
       "Прокси: health-check перед прогоном (`sh_proxy_check`).",
       "VPS-коннект (host · ключ · база) + где лежат processed_domains · keep-list · резервуары."], None),

 ("peculiarities.md ⭐ новый", "Частные случаи: симптом → что это скорее всего → что делать.",
  "создать файл; формат по этапам.",
  [], ["reach упал ниже нормы → скорее всего products.json выключен, магазин ЖИВ → открыть руками, не перезапускать.",
       "SSH оборвался посреди прогона → энрич выжил под nohup → ждать sentinel, не перезапускать.",
       "при обвале reach → сначала прогнать прежнюю версию скрапера на тех же данных, потом гипотеза (S21)."], None),

 ("⛔ УДАЛИТЬ · git помнит", "Мёртвое и дубли — не переносим никуда.",
  "удалить, откат через git.",
  [], [], "не вставляется никуда. На удаление: RULE 5 (мёртв) · «batched-tier» (L390–397) · «(This is a habit…)» (L97–98) · «Checkpoint shape» (дубль). Шапку op-rules сжать до 2 строк."),
]


# ОБЩАЯ КАРТА — весь op-rules по порядку → куда идёт каждый кусок
MASTER = [
 ("RULE 0","L3–11","сначала проверь","Правило **П1**"),
 ("RULE 0b","L15–43","неудобство = дефект","Правило **П3**"),
 ("CREED","L47–57","душа","**CREED**"),
 ("шапка","L60–68","provenance / порядок загрузки","**удалить** (provenance → хроника)"),
 ("RULE 1","L74–77","funnel transparency","Правило **П2**"),
 ("RULE 2","L79–81","не менять score молча","Правило **П2**"),
 ("RULE 3","L83–86","«не найдено» ≠ «нет»","Правило **П2**"),
 ("RULE 4","L88–89","verify before asserting","Правило **П1**"),
 ("RULE 4a","L91–98","при поломке замедлиться","Правило **П1**"),
 ("RULE 5","L104–106","conservative cut","**удалить** (мёртв, отменён 24)"),
 ("RULE 6","L108–112","читать всё; тир = сортировка","Правило **П4**"),
 ("RULE 7","L114–118","подтвердить героя+цену live","Правило **П5**"),
 ("RULE 8","L120–123","browse каждый батч","Правило **П8**"),
 ("RULE 9","L128–130","дропшип/бренд ≠ reject","Правило **П9**"),
 ("RULE 10","L132–135","high-ticket / bulky вниз","Правило **П9**"),
 ("RULE 11","L137–140","honest low-yield валиден","Правило **П9**"),
 ("RULE 12","L142–146","Founder Review — отдельный слой","Правило **П9**"),
 ("RULE 13","L152–155","тяжёлое на VPS; no parallel claude","Правило **П10**"),
 ("RULE 14","L157–159","прокси-дисциплина","Правило **П10**"),
 ("RULE 15","L161–163","креды не в чат/git","Правило **П10**"),
 ("RULE 16","L169–173","Tier-1 / Tier-2","Правило **П13**"),
 ("RULE 17","L175–200","конец сессии + формат","Правило **П12** · формат → `founder-feedback.md`"),
 ("RULE 19","L202–208","mark processed","Правило **П12**"),
 ("RULE 18","L210–213","гигиена памяти","Правило **П12**"),
 ("RULE 20","L217–225","master-record + keep-list","Правило **П12** · поля → `methods/card-contract.md`"),
 ("RULE 21","L227–232","качество > токенов","**CREED** (п.9)"),
 ("RULE 22","L234–238","самопроверка энричера","`methods/card-contract.md`"),
 ("RULE 23","L240–259","открыть каждый флаг ⚠","Правило **П5** (⚠ развилка)"),
 ("RULE 24","L261–270","анализировать всё; не фильтровать","Правило **П4**"),
 ("RULE 25","L272–301","полная карточка + паритет","Правило **П6** · разбор S18 → `history/lessons.md`"),
 ("RULE 26","L303–324","QA-gate перед анализом","Правило **П6** · пороги → `methods/pipeline.md`"),
 ("RULE 27","L325–334","анализ доказан файлами","Правило **П7**"),
 ("RULE 28","L336–351","browse + floor-not-ceiling","Правило **П8** · floor → **CREED** (п.8)"),
 ("RULE 29","L353–368","curl ≠ заход","Правило **П5** · истории → `history/lessons.md`"),
 ("RULE 30","L370–418","волна сборки 1+9","Правило **П11** · механика → `methods/pipeline.md` · batched-tier(L390–397) → **удалить**"),
 ("RULE 31","L420–438","контракт чекпойнта","Правило **П7**"),
 ("RULE 32","L440–450","browse floor = 7","Правило **П8**"),
 ("RULE 33","L452–467","human-in-loop","Правило **П11** · история S15 → `history/lessons.md`"),
 ("Checkpoint shape","L469–476","форма чекпойнта","`workflow.md` (форма) · как дубль → **удалить**"),
]


def blk(lines,a,b): return "".join(lines[a-1:b]).rstrip("\n")

def main():
    lines=open(SRC,encoding="utf-8").readlines()
    o=["# S22 — РАЗБРОС op-rules ПО ФАЙЛАМ: вердикт + САМ ТЕКСТ для вставки\n",
       "> Один файл-приёмник → **вердикт** (что делаем) + **сам текст, готовый к copy-paste** (дословно из op-rules, "
       "не ссылка) + **③ твоя правка**. Где текст надо писать по живому коду — так и сказано, выдуманного текста нет.\n",
       f"> Собрано `scripts/build_rules_by_file.py` из `{SRC}`.\n\n---\n"]
    # ОБЩАЯ КАРТА сверху
    o.append("\n## 🗺️ ОБЩАЯ КАРТА — весь op-rules по порядку → куда идёт\n")
    o.append("Одним взглядом видно, что уходит в ПРАВИЛА, а что разбивается по файлам.\n\n")
    o.append("| op-rules | строки | что это | → куда |\n|---|---|---|---|\n")
    for lab,ln,what,dest in MASTER:
        o.append(f"| {lab} | {ln} | {what} | {dest} |\n")
    o.append("\n---\n")
    for fname,desc,verdict,ranges,manual,task in DEST:
        o.append(f"\n## → `{fname}`\n*{desc}*\n")
        o.append(f"\n**② МОЯ ВЕРСИЯ (агент).** Вердикт: {verdict}\n")
        if task:
            o.append(f"\n**Текст для вставки:** — {task}\n")
        else:
            o.append(f"\n**Текст для вставки в `{fname}` (copy-paste, дословно):**\n")
            for lab,a,b in ranges:
                o.append(f"\n> ⸻ {lab} (op-rules L{a}–{b}) ⸻\n>\n")
                for ln in blk(lines,a,b).split("\n"): o.append("> "+ln+"\n")
            for m in manual:
                o.append(f">\n> {m}\n")
        o.append("\n**③ ПРАВКА МАРИНЫ:**\n> _(вычеркни / оставь / добавь)_\n\n---\n")
    open("review/s22-rules-by-file.md","w",encoding="utf-8").write("".join(o))
    print(f"OK → review/s22-rules-by-file.md ({len(''.join(o))} chars, {len(DEST)} файлов)")

if __name__=="__main__": main()
