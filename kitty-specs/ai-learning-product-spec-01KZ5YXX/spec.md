# Русская продуктовая спецификация AI Learning

## Цель

Создать в `ai-learning` короткую repository-owned product spec, которая
описывает подтверждённое текущее поведение проекта, а не историю обучения или
будущие планы. Первой возможностью зафиксировать существующий учебный маршрут
по production RAG из `notebooks/10_production_rag/`.

## Исходное состояние

- В репозитории нет `docs/product-spec/`.
- `README.md` описывает модули 01–08 как завершённые, а 09–10 как находящиеся
  в работе.
- В `notebooks/10_production_rag/` отслеживаются четыре последовательных
  ноутбука: chunking, embeddings/vector stores, retrieval/reranking и
  generation/evaluation.
- Repo-local `AGENTS.md` требует русские объяснения, запрещает перезаписывать
  `data/` без согласования и отделяет анализ от редактирования.

## Функциональные требования

| ID | Требование |
| --- | --- |
| FR-001 | Создать русский индекс `docs/product-spec/`, каталог возможностей и переиспользуемый шаблон capability. |
| FR-002 | Описать current-state capability «Учебный маршрут production RAG» только по отслеживаемым README и notebook evidence. |
| FR-003 | Явно различать наличие учебного материала, статус модуля в README и фактический запуск notebook; не утверждать непроверенное выполнение. |
| FR-004 | Зафиксировать delta → approval → evidence → fold-forward цикл и связь с отдельным Bead. |
| FR-005 | Не менять notebooks, datasets, Docker examples, Python-код, `.env`, runtime или legacy-документы. |
| FR-006 | До merge пройти link/content/allowed-path checks и независимый `luna_worker` review. |

## Наблюдаемое поведение первой возможности

Пользователь начинает с модуля chunking и последовательно переходит к
embeddings/vector stores, retrieval/reranking и generation/evaluation. Каждый
следующий notebook явно опирается на предыдущие части. Спецификация описывает
эту навигацию, назначение этапов, пререквизиты и границы доказанности, но не
копирует содержимое notebook и не объявляет весь модуль 10 завершённым.

## Критерии приёмки

- Все человекочитаемые заголовки и пояснения product spec написаны по-русски;
  точные пути, команды, названия библиотек и метрик не переводятся.
- Каталог содержит рабочую относительную ссылку на capability.
- Capability ссылается на четыре существующих notebook и согласуется со
  статусом `README.md`.
- Проверка подтверждает, что diff реализации ограничен `docs/product-spec/`,
  коротким governance-разделом `AGENTS.md` и стандартными mission/tooling
  artifacts.
- Независимый reviewer может отличить «файл существует» от «notebook был
  воспроизводимо выполнен».

## Не входит в scope

- Запуск или изменение notebook, установка зависимостей и пересчёт outputs.
- Чтение `.env`, API keys, datasets или персональных сведений roadmap.
- Объявление production RAG готовым сервисом.
- Перевод всего `README.md` или учебных материалов.
- Изменение Docker examples, Python-кода или GitHub publication.

## Решения

- Каноническое текущее состояние живёт в `docs/product-spec/`; notebooks и
  `README.md` остаются источниками evidence.
- Начальная capability называется `production-rag-learning-path`.
- Beads хранит identity/priority/dependencies; требования и критерии остаются в
  этой mission и product spec.
- Любая потребность изменить учебный код или выполнить внешние API-вызовы —
  material delta и требует нового согласования.
