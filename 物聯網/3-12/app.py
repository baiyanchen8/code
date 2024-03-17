from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'mydatabase.db'

# 建立資料庫連接
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.cursor = g.db.cursor()
    return g.db, g.cursor

# 在應用程式關閉時關閉資料庫連接
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.get_json()  # 接收來自 ESP32 的 JSON 資料
    temperature = data['temperature']
    humidity = data['humidity']
    if temperature==0 and humidity ==0:
        return
    # 將資料插入資料表
    db, cursor = get_db()
    cursor.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
    db.commit()
    
    print(f"溫度：{temperature}，濕度：{humidity}")
    return '資料已收到'

@app.route('/get_data', methods=['GET'])
def get_data():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()
    if data:
        temperature, humidity = data[1], data[2]
        return jsonify({'temperature': temperature, 'humidity': humidity})
    else:
        return jsonify({'error': 'No data available'})

@app.route('/')
def index():
    return app.send_static_file('hw.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
