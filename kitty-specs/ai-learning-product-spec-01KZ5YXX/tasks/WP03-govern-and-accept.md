---
work_package_id: WP03
title: Закрепить governance и провести приёмку
dependencies:
- WP01
- WP02
requirement_refs:
- FR-004
- FR-005
- FR-006
tracker_refs:
- ops-h53.2
planning_base_branch: codex/ai-learning-product-spec
merge_target_branch: codex/ai-learning-product-spec
branch_strategy: Planning artifacts for this mission were generated on codex/ai-learning-product-spec. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into codex/ai-learning-product-spec unless the human explicitly redirects the landing branch.
subtasks:
- T005
- T006
phase: Phase 3 - Governance and acceptance
assignee: codex
agent: codex
history: []
agent_profile: implementer
authoritative_surface: AGENTS.md
execution_mode: code_change
owned_files:
- AGENTS.md
tags:
- governance
- acceptance
- luna-worker
---

## Цель

Закрепить обновление product spec после принятого изменения и завершить
независимые delivery gates.

## Обязательная работа

1. Добавить короткий русский раздел в `AGENTS.md` о capability/delta/approval,
   evidence/fold-forward и роли Beads.
2. Проверить allowed paths, links, язык, frozen surfaces и privacy boundary.
3. Провести отдельный `luna_worker` review каждого WP, accept, merge,
   post-merge review и retrospective.

## Ограничения

- Не менять scope/claims WP02 без material delta.
- Не менять notebooks, data, Docker, Python, README или существующие docs.
- Не публиковать GitHub без отдельной проверки remote history.

## Проверка

- Catalog link, созданный в WP02, проходит.
- Frozen surfaces не изменены.
- Все review/accept/merge artifacts сохранены.

## Критерии завершения

- [ ] T005–T006 выполнены.
- [ ] FR-004–FR-006 покрыты.
- [ ] Mission принята, слита и post-merge review завершён.

## Журнал работы

- 2026-08-04T08:44:31Z — codex — Запланировано; зависит от WP01 и WP02.
