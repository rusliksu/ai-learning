# План: русская product spec для AI Learning

**Ветка**: `codex/ai-learning-product-spec`
**Дата**: 2026-08-04
**Спецификация**: `kitty-specs/ai-learning-product-spec-01KZ5YXX/spec.md`

## Краткое решение

Добавить общий русский contract `docs/product-spec/` и одну current-state
capability `production-rag-learning-path.md`. Утверждения выводятся только из
`README.md` и четырёх versioned notebook модуля 10. Notebook, data, Docker и
Python surfaces остаются read-only evidence.

## Технический контекст

**Language/Version**: Markdown/UTF-8; evidence notebooks используют Python 3.12
**Primary Dependencies**: Git, Spec Kitty 3.2.5, Beads 1.1.2, Jupyter notebook format
**Storage**: Git-tracked Markdown и mission artifacts
**Testing**: `git diff --check`, allowed-path check, относительные Markdown links,
content assertions, независимый `luna_worker` review
**Target Platform**: Git repository; инструкции пользователя по умолчанию Windows
**Project Type**: documentation/governance mission
**Performance Goals**: не применимо
**Constraints**: русский human-facing слой; без запуска notebook/API, чтения
`.env`/datasets и изменения учебного кода
**Scale/Scope**: один contract, один template, одна начальная capability, 3 WP

## Проверка правил проекта

- Русская проза и literal technical identifiers сохранены.
- Current-state claims отделены от статуса «в работе» и от execution evidence.
- Изменения ограничены documentation/governance и project-local tooling.
- Независимый review обязателен до acceptance.

Charter gate пройден для draft baseline; повторная проверка обязательна перед
реализацией.

## Структура результата

```text
docs/product-spec/
├── README.md
├── capabilities/
│   ├── README.md
│   └── production-rag-learning-path.md
└── templates/
    └── capability-spec.md

kitty-specs/ai-learning-product-spec-01KZ5YXX/
├── spec.md
├── plan.md
├── tasks.md
└── tasks/
```

Короткий раздел в `AGENTS.md` связывает существенные изменения с delta,
approval, evidence и fold-forward, не дублируя полную спецификацию.

## Порядок реализации

1. Создать русский корневой индекс и шаблон без capability claims.
2. На основе read-only evidence создать каталог и описать последовательность
   четырёх production RAG notebook с границами доказанности.
3. Добавить короткое governance-правило, проверить links/language/scope.
4. Для каждого WP выполнить независимый review; затем accept, merge,
   post-merge review и retrospective.

## Проверки и безопасность

- Allowed product paths: `docs/product-spec/**` и короткое дополнение
  `AGENTS.md`; standard `.kittify/`, `.beads/`, `kitty-specs/`, `.gitignore`,
  `.gitattributes`, `.claudeignore` относятся к mission tooling.
- Frozen paths: `notebooks/**`, `data/**`, `docker/**`, существующие `docs/**`,
  `README.md`, `.env*`, Python files.
- Не выполнять notebook и не устанавливать зависимости.
- Не читать `.env`, datasets или roadmap personal details.

## Карта аспектов реализации

### IC-01 — Общий contract

- **Назначение**: задать индекс, шаблон и правила current-state/fold-forward.
- **Требования**: FR-001, FR-004, FR-005.
- **Поверхности**: `docs/product-spec/README.md`, template.
- **Зависимости**: нет.
- **Риск**: англоязычный шаблон или избыточный процесс.

### IC-02 — Production RAG learning path

- **Назначение**: описать существующую последовательность notebook без ложного
  заявления о завершении или воспроизводимом выполнении.
- **Требования**: FR-002, FR-003, FR-005.
- **Поверхности**: catalog и одна capability; README/notebooks только evidence.
- **Зависимости**: IC-01.
- **Риск**: смешение file existence, README status и execution evidence.

### IC-03 — Governance и приёмка

- **Назначение**: закрепить русский fold-forward и независимые gates.
- **Требования**: FR-004, FR-006.
- **Поверхности**: `AGENTS.md`, mission review artifacts.
- **Зависимости**: IC-01, IC-02.
- **Риск**: выход в учебный код или datasets.

## Учёт сложности

Нарушений charter нет.
