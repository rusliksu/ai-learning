"""
Flask API с PostgreSQL и Redis.
Демонстрация Docker Compose.
"""
from flask import Flask, jsonify, request
import psycopg2
import redis
import os
import json

app = Flask(__name__)

# Подключения (Docker Compose создаёт DNS по имени сервиса)
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user:password@db:5432/mydb')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379')

def get_db():
    """Подключение к PostgreSQL."""
    return psycopg2.connect(DATABASE_URL)

def get_redis():
    """Подключение к Redis."""
    return redis.from_url(REDIS_URL)

@app.route('/')
def home():
    return jsonify({
        "service": "API с Docker Compose",
        "endpoints": ["/", "/health", "/db/test", "/cache/set", "/cache/get", "/visits"]
    })

@app.route('/health')
def health():
    """Проверка здоровья всех сервисов."""
    status = {"api": "ok"}

    # Проверка PostgreSQL
    try:
        conn = get_db()
        conn.close()
        status["postgres"] = "ok"
    except Exception as e:
        status["postgres"] = f"error: {str(e)}"

    # Проверка Redis
    try:
        r = get_redis()
        r.ping()
        status["redis"] = "ok"
    except Exception as e:
        status["redis"] = f"error: {str(e)}"

    return jsonify(status)

@app.route('/db/test')
def db_test():
    """Тест PostgreSQL - создание таблицы и запись."""
    try:
        conn = get_db()
        cur = conn.cursor()

        # Создаём таблицу если не существует
        cur.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                text TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Вставляем запись
        cur.execute("INSERT INTO messages (text) VALUES (%s) RETURNING id", ("Hello from Docker!",))
        msg_id = cur.fetchone()[0]

        # Читаем все записи
        cur.execute("SELECT COUNT(*) FROM messages")
        count = cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            "status": "ok",
            "inserted_id": msg_id,
            "total_messages": count
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cache/set', methods=['POST'])
def cache_set():
    """Сохранить значение в Redis."""
    data = request.get_json() or {}
    key = data.get('key', 'test')
    value = data.get('value', 'hello')

    try:
        r = get_redis()
        r.set(key, value, ex=300)  # TTL 5 минут
        return jsonify({"status": "ok", "key": key, "value": value})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cache/get/<key>')
def cache_get(key):
    """Получить значение из Redis."""
    try:
        r = get_redis()
        value = r.get(key)
        if value:
            return jsonify({"key": key, "value": value.decode()})
        return jsonify({"key": key, "value": None, "message": "Key not found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/visits')
def visits():
    """Счётчик посещений (Redis INCR)."""
    try:
        r = get_redis()
        count = r.incr('visit_counter')
        return jsonify({"visits": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
