# Agents DTO Mapper Fix — пакет фиксов 06.03.2026

## Задача: LEGALBPM-3107 / LEGALBPM-16917

## Основной фикс: AgentDTO + AgentDTOMapper

### Проблема
Спека обновления агента требует поля `processorsLimit` и `processorsIterLimit`.
UseCase уже сеттил эти значения в entity, но DTO их не содержал, а MapStruct маппер явно игнорировал оба поля (`@Mapping(target = "...", ignore = true)`).
Результат: фронт получал `null` по трём ключам, обновление не применялось.

### Симптомы
- Фронт жаловался на отсутствие 3 полей в ответе API `/api/kc-agents/cp/agents`
- PATCH агента не обновлял лимиты процессоров — значения всегда `null`

### Фикс
1. **AgentDTO** — добавлены поля `processorsLimit` (Integer) и `processorsIterLimit` (Integer)
2. **AgentDTOMapper** — убраны `@Mapping(target = "processorsLimit", ignore = true)` и аналогичный для `processorsIterLimit`

### Что остаётся ignore
- `allocateRanges` — внутренний флаг, не в спеке обновления
- `processors` — дочерние entity, не редактируются через DTO
- `createDateTime`, `updateDateTime`, `updateOperator` — auto-generated поля

---

## Сопутствующие фиксы (06.03.2026)

### FramesPresets — lazy-loading filters/sorting

**Проблема:** `findPersonalAndOwnerLessByFrameID` использовал обычный Spring Data запрос без EntityGraph.
Коллекции `filters` и `sorting` оставались ленивыми прокси.
`HibernateConditionHelper.isInitialized` возвращал `false` → MapStruct пропускал поля → `null` в DTO.

**Фикс:** паттерн «сначала ID, потом EntityGraph». Метод сначала получает ID через репозиторий, затем загружает полные entity через `findAllByIdsWithDynamicGraph(ids, ATTRS_FULL)`. Тот же подход, что в `CriteriaQueryHelper`.

**SonarQube S6809:** `this::findAllByIdsWithDependencies` обходит Spring AOP прокси — `@Transactional` не сработает через `this`. Безопасно: вызов всегда внутри уже открытой `@Transactional(readOnly = true)` транзакции (REQUIRED propagation). Подавляется через `@SuppressWarnings("java:S6809")` с комментарием.

### FramesPresets — фикс теста

**Проблема:** `testFindPersonalAndOwnerLessByFrameID` проверял прямое делегирование в репозиторий.
После фикса метод дополнительно вызывает `findAllByIdsWithDynamicGraph` через EntityManager. EntityManager не был замокан в старом тесте → NPE.

**Фикс:** тест обновлён — моки EntityManager/TypedQuery/EntityGraph, verify на `createEntityGraph` и `setHint("jakarta.persistence.fetchgraph", ...)`. Добавлен edge case: пустой результат из репо → `verifyNoInteractions(entityManager)`.

### PochtaConversionIntegrationTest — NPE в setUp

**Проблема:** поле `pdfPassthroughConverter` не инициализировалось в `@BeforeAll`. `List.of()` не принимает `null` → NPE при создании `ConvertPochtaFileToPdfUseCaseImpl`.

**Фикс:** добавлена инициализация `pdfPassthroughConverter = new PochtaPdfToPdfConverter(pdfVersionService)` перед созданием `convertUseCase`.

### Верификация дефекта

Создан HTTP-сценарий проверки (IntelliJ HTTP Client):
1. **Список дел** (`POST /cases/entries`) — `comments` и `claims` должны быть `null` (не загружаются в списке)
2. **Карточка дела** (`GET /cases/{id}`) — `comments` и `claims` должны быть не `null` (загружаются через ATTRS_FULL)
3. **Пресеты фрейма** (`GET /frames/{id}?type=DYNAMIC_DATA_LIST`) — `filters` и `sorting` не `null`

---

## Контекст: agents-manager

Сервис управления агентами (scheduler). Развёрнут на DEV отдельным подом.
API: `POST /api/kc-agents/cp/agents` (список), `PATCH /api/kc-agents/cp/agents/{id}` (обновление).
gRPC зависимости: RBAC, OrgStructure, DSS, CP Administration, Casework, Jurisdiction.
Подробнее: [Deployment Guide](../infrastructure/LegalBPM_DSS_AgentsManager_Deployment_Guide_26_02_26.md).

## Тестирование
- Unit-тесты адаптеров с моками EntityManager (MockitoExtension)
- Интеграционный тест конвертации (PochtaConversion) на H2
- HTTP-сценарий верификации дефекта на DEV-стенде
- Проверка SonarQube: S6809 подавлен с обоснованием

## Урок
MapStruct `ignore = true` — опасная дефолтная привычка. Если добавил поле в entity, проверь маппер: `ignore` не выбросит ошибку компиляции, просто молча вернёт `null`.
