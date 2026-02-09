# Python API образ
FROM python:3.12-slim

WORKDIR /app

# Зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Код
COPY app.py .

ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]
