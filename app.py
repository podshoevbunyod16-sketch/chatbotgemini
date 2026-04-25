from flask import Flask, render_template, request, jsonify
import datetime
import random

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Пример API-эндпоинта (для демонстрации работы с сервером)
@app.route('/api/time')
def get_time():
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return jsonify({"time": now, "status": "ok"})

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'Гость')
    return jsonify({"message": f"Привет, {name}! Рады видеть вас на нашем сайте."})

# Здоровье для Render
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)