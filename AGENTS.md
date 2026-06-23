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
