"""
Простой API на Flask для демонстрации Docker.
"""
from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Привет из Docker контейнера!",
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": os.environ.get('HOSTNAME', 'unknown')
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/info')
def info():
    return jsonify({
        "python_version": os.popen('python --version').read().strip(),
        "environment": os.environ.get('ENVIRONMENT', 'development'),
        "container": True
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
