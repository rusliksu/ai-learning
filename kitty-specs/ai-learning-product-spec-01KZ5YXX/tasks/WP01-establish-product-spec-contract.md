---
work_package_id: WP01
title: Создать канонический product-spec contract
dependencies: []
requirement_refs:
- FR-001
- FR-004
- FR-005
- FR-006
tracker_refs:
- ops-h53.2
planning_base_branch: codex/ai-learning-product-spec
merge_target_branch: codex/ai-learning-product-spec
branch_strategy: Planning artifacts for this mission were generated on codex/ai-learning-product-spec. During /spec-kitty.implement this WP may branch from a dependency-specific base, but completed changes must merge back into codex/ai-learning-product-spec unless the human explicitly redirects the landing branch.
subtasks:
- T001
- T002
- T003
phase: Phase 1 - Canonical contract
assignee: codex
agent: codex
history: []
agent_profile: implementer
authoritative_surface: docs/product-spec/
create_intent:
- docs/product-spec/README.md
- docs/product-spec/templates/capability-spec.md
execution_mode: code_change
owned_files:
- docs/product-spec/README.md
- docs/product-spec/templates/capability-spec.md
tags:
- product-spec
- russian
- privacy-safe
---

## Цель

После explicit approval создать минимальный русский root index и reusable
current-state template.

## Обязательная работа

1. Не начинать implementation до T001.
2. Объявить `docs/product-spec/` source of truth актуального наблюдаемого
   поведения, а README/notebooks — evidence.
3. Описать delta → approval → evidence → fold-forward → accept lifecycle.
4. Сохранить literal technical identifiers без перевода.

## Ограничения

- Не создавать capability WP02 заранее.
- Не менять README, notebooks, data, Docker, Python или существующие docs.
- Не читать `.env`, datasets или персональные сведения roadmap.

## Проверка

- Diff ограничен owned files.
- Required headings, links, русский язык и lifecycle assertions проходят.
- `git diff --check` проходит.

## Критерии завершения

- [ ] T001–T003 выполнены.
- [ ] Contract покрывает FR-001, FR-004–FR-006.
- [ ] Independent reviewer подтвердил русский язык и privacy boundary.

## Журнал работы

- 2026-08-04T08:44:31Z — codex — Draft baseline подготовлен; implementation ожидает отдельного approval.
