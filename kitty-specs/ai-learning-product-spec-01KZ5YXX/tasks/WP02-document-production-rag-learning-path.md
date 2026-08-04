---
work_package_id: WP02
title: Описать учебный маршрут production RAG
dependencies:
- WP01
requirement_refs:
- FR-002
- FR-003
- FR-005
- FR-006
tracker_refs:
- ops-h53.2
planning_base_branch: codex/ai-learning-product-spec
merge_target_branch: codex/ai-learning-product-spec
branch_strategy: Planning artifacts for this mission were generated on codex/ai-learning-product-spec. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into codex/ai-learning-product-spec unless the human explicitly redirects the landing branch.
subtasks:
- T004
phase: Phase 2 - Current-state capability
assignee: codex
agent: "codex:gpt-5.6-luna:reviewer-renata:reviewer"
history: []
agent_profile: implementer
authoritative_surface: docs/product-spec/capabilities/
create_intent:
- docs/product-spec/capabilities/README.md
- docs/product-spec/capabilities/production-rag-learning-path.md
execution_mode: code_change
owned_files:
- docs/product-spec/capabilities/README.md
- docs/product-spec/capabilities/production-rag-learning-path.md
tags:
- product-spec
- production-rag
- evidence
shell_pid: "4040088"
---

## Цель

Создать каталог возможностей и описать существующий маршрут chunking →
embeddings/vector stores → retrieval/reranking → generation/evaluation.

## Обязательная работа

1. Создать каталог с относительной ссылкой на capability.
2. Сверить claims с README и четырьмя versioned notebook.
3. Зафиксировать назначение, порядок, пререквизиты и границы доказанности.
4. Явно отделить file existence и README status от execution evidence.
5. Не копировать notebook content и не объявлять модуль 10 завершённым.

## Ограничения

- Notebook остаются read-only; не запускать и не менять outputs.
- Не устанавливать зависимости и не вызывать внешние API.
- Не читать `.env`, datasets или roadmap personal details.

## Проверка

- Все четыре относительные evidence-ссылки существуют.
- Capability не содержит неподтверждённых execution/production claims.
- `git diff --check` и language assertions проходят.

## Критерии завершения

- [ ] T004 выполнена.
- [ ] FR-002/FR-003 покрыты доказуемыми current-state assertions.
- [ ] Independent reviewer подтвердил evidence boundary.

## Журнал работы <!-- ## Activity Log -->

- 2026-08-04T08:44:31Z — codex — Запланировано; зависит от WP01 и approval baseline.
- 2026-08-04T09:29:57Z – codex:gpt-5:implementer-ivan:implementer – shell_pid=4040088 – Assigned agent via action command
- 2026-08-04T09:32:44Z – codex:gpt-5:implementer-ivan:implementer – shell_pid=4040088 – Ready for review: documented four-stage production RAG learning path with explicit README/file/execution evidence boundaries
- 2026-08-04T09:34:51Z – codex:gpt-5.6-luna:reviewer-renata:reviewer – shell_pid=4040088 – Started review via action command
- 2026-08-04T09:36:26Z – user – shell_pid=4040088 – Review passed: WP02 commit owns only catalog and capability; four notebook links/order, README in-progress status, absent verified execution evidence, Russian text, frozen/privacy boundaries, and git checks all pass
