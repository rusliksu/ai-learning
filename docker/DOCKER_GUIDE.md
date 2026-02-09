# Docker - Шпаргалка

## Что такое Docker?

Docker - это платформа для контейнеризации приложений.
Контейнер = изолированная среда с приложением и всеми зависимостями.

**Аналогия для Java-разработчика:**
- JAR файл содержит код + библиотеки
- Docker контейнер содержит код + библиотеки + ОС + окружение

## Основные понятия

| Термин | Описание | Аналогия |
|--------|----------|----------|
| **Image** | Шаблон/образ контейнера | Класс в Java |
| **Container** | Запущенный экземпляр образа | Объект (new Class()) |
| **Dockerfile** | Инструкция для сборки образа | Исходный код |
| **Registry** | Хранилище образов (Docker Hub) | Maven Central |
| **Volume** | Постоянное хранилище данных | Внешняя БД |

## Основные команды

### Работа с образами

```bash
# Скачать образ
docker pull nginx

# Список образов
docker images

# Удалить образ
docker rmi nginx

# Собрать образ из Dockerfile
docker build -t myapp:1.0 .
```

### Работа с контейнерами

```bash
# Запустить контейнер
docker run nginx

# Запустить в фоне (-d) с портом (-p)
docker run -d -p 8080:80 nginx

# Список запущенных контейнеров
docker ps

# Все контейнеры (включая остановленные)
docker ps -a

# Остановить контейнер
docker stop <container_id>

# Удалить контейнер
docker rm <container_id>

# Зайти внутрь контейнера
docker exec -it <container_id> bash

# Логи контейнера
docker logs <container_id>
```

### Флаги запуска

| Флаг | Описание | Пример |
|------|----------|--------|
| `-d` | Detached (в фоне) | `docker run -d nginx` |
| `-p` | Port mapping | `-p 8080:80` (хост:контейнер) |
| `-v` | Volume (данные) | `-v /host/path:/container/path` |
| `-e` | Environment var | `-e MYSQL_ROOT_PASSWORD=123` |
| `--name` | Имя контейнера | `--name myapp` |
| `--rm` | Удалить после остановки | `docker run --rm nginx` |
| `-it` | Интерактивный режим | `docker exec -it container bash` |

## Dockerfile - основы

```dockerfile
# Базовый образ
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Копирование файлов
COPY requirements.txt .

# Выполнение команд (при сборке)
RUN pip install -r requirements.txt

# Копирование кода
COPY . .

# Порт (документация)
EXPOSE 8000

# Команда запуска
CMD ["python", "app.py"]
```

## Docker Compose

Для запуска нескольких контейнеров вместе.

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
# Запустить все сервисы
docker-compose up -d

# Остановить
docker-compose down

# Логи
docker-compose logs -f

# Пересобрать
docker-compose up -d --build
```

## Практические примеры

### 1. Запуск PostgreSQL

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=mypassword \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
```

### 2. Запуск Redis

```bash
docker run -d --name redis -p 6379:6379 redis:alpine
```

### 3. Запуск Python приложения

```bash
docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  python:3.12 python script.py
```

## Полезные команды

```bash
# Очистить неиспользуемые данные
docker system prune -a

# Статистика ресурсов
docker stats

# Информация о контейнере
docker inspect <container_id>

# Копировать файл из/в контейнер
docker cp file.txt container:/path/
docker cp container:/path/file.txt .
```

## Связь с Java/Spring Boot

```dockerfile
# Dockerfile для Spring Boot
FROM eclipse-temurin:21-jdk-alpine
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## Ресурсы

- [Docker Hub](https://hub.docker.com/) - образы
- [Docker Docs](https://docs.docker.com/) - документация
- [Play with Docker](https://labs.play-with-docker.com/) - онлайн песочница
