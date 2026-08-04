# AGENTS.md — AI Learning Project

@../SHARED_RULES.md

## VPS Codex Routing
- Для операций на VPS, OpenClaw, Gurra, Hermes, systemd/logs/patch/update/deploy сценариев по умолчанию использовать схему: локальный Codex = оркестратор, VPS Codex = исполнитель.
- Сначала запускать read-only статус: `C:\Users\Ruslan\gurra\scripts\codex-vps-run.ps1 -Status`.
- Для анализа, проверок, логов и долгих задач делегировать на VPS через `C:\Users\Ruslan\gurra\scripts\codex-vps-run.ps1`; для долгих задач использовать `-Detach -Name ...`.
- Локально оставлять GUI/browser/screenshots/Telegram UX/Windows-specific проверки и финальную координацию.
- Не читать и не печатать токены/credentials. Если VPS Codex упёрся в auth, просить интерактивно выполнить `C:\Users\Ruslan\gurra\scripts\codex-vps-run.ps1 -Login`.

## Контекст проекта
- Практическое изучение AI/ML с Java-backend перспективой
- Объяснения на русском, с Java/Spring аналогиями где уместно
- Фокус на практике, а не теории

## Правила
- Для вопросов по библиотекам, API, настройке окружения и генерации кода использовать Context7, когда нужны свежие или версионные доки.
- `notebooks/` — эксперименты и обучение
- `docs/` — роадмапы и заметки
- `data/` — датасеты, не удалять/перезаписывать без спроса
- При создании ноутбуков: `%matplotlib inline` в первую ячейку
- Анализ/гайд ≠ редактирование файлов — жди явную команду
- Windows-инструкции для локального setup по умолчанию

## Продуктовая спецификация

- `docs/product-spec/` — каноническое описание текущего наблюдаемого поведения; отдельные возможности ведутся как capability.
- Material delta требует явного approval до реализации. После реализации собрать проверяемое evidence и выполнить fold-forward: обновить capability как цельное описание актуального состояния.
- Beads хранит identity, priority и dependency graph работы, а Spec Kitty — требования, решения, критерии приёмки и lifecycle рабочих пакетов.
- Не включать в product spec secrets, credentials, `.env`, содержимое datasets или персональные сведения.

<!-- spec-kitty:orientation -->
**Spec Kitty v3.2.5** — project: unknown (healthy)

Two usage patterns:
- **Full mission** (spec → plan → tasks → implement → review → merge):
  trigger: "spec out", "create a mission", "write a spec", "plan this"
  → run `/spec-kitty.specify`
- **Lightweight dispatch** (ad-hoc fix, question, or advice — no mission created):
  trigger: "hey spec kitty", "use spec kitty to", "spec kitty <anything>"
  → **ALWAYS run `spec-kitty dispatch "<request verbatim>"` — do NOT answer directly.**
  If you know the right profile, pass it to skip routing:
  `spec-kitty dispatch "<request verbatim>" --profile <profile-id>`
  Reason: `spec-kitty dispatch` loads governance context, routes the request,
  and opens the Op. Skipping it produces ungoverned, untracked responses.
  After finishing the work, close the Op with the command printed in the capsule
  (`spec-kitty profile-invocation complete --invocation-id <id> --outcome <done|failed|abandoned>`).
<!-- /spec-kitty:orientation -->
