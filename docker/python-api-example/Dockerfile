# Базовый образ - легковесный Python
FROM python:3.12-slim

# Метаданные
LABEL maintainer="ruslan"
LABEL description="Simple Flask API example"

# Рабочая директория внутри контейнера
WORKDIR /app

# Сначала копируем только requirements (для кэширования слоёв)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app.py .

# Переменные окружения
ENV ENVIRONMENT=production
ENV PORT=5000

# Документируем порт (не открывает, только документация)
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]
