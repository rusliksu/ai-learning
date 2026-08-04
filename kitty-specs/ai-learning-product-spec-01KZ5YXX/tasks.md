# Рабочие пакеты: product spec AI Learning

## Контракт веток

- Planning/target branch: `codex/ai-learning-product-spec`
- Mission branch: `kitty/mission-ai-learning-product-spec-01KZ5YXX`
- Integration target после acceptance: repository `master` через отдельный gate
- Tracker identity: central Bead `ops-h53.2`

## Индекс подзадач

| ID | Описание | WP | Статус |
| --- | --- | --- | --- |
| T001 | Получить explicit approval target spec/plan/tasks baseline | WP01 | [D] |
| T002 | Создать русский canonical root | WP01 | [D] |
| T003 | Добавить reusable current-state capability template | WP01 | [D] |
| T004 | Создать capability catalog и описать production RAG learning path | WP02 | [D] |
| T005 | Добавить delta/fold-forward/Beads gate в `AGENTS.md` | WP03 | [ ] |
| T006 | Выполнить checks, independent review, accept и delivery handoff | WP03 | [ ] |

## WP01 — Канонический product-spec contract

**Prompt**: `tasks/WP01-establish-product-spec-contract.md`
**Приоритет**: P1
**Цель**: создать discoverable русский current-state contract и template.
**Зависимости**: нет

## WP02 — Учебный маршрут production RAG

**Prompt**: `tasks/WP02-document-production-rag-learning-path.md`
**Приоритет**: P1
**Цель**: доказуемо описать существующую последовательность четырёх notebook.
**Зависимости**: WP01

## WP03 — Governance, проверка и приёмка

**Prompt**: `tasks/WP03-govern-and-accept.md`
**Приоритет**: P1
**Цель**: закрепить fold-forward и завершить target-specific gates.
**Зависимости**: WP01, WP02
