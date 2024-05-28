from flask import Flask, request, jsonify, g
import sqlite3
import datetime
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
    timee=datetime.datetime.now()
    cursor.execute("INSERT INTO sensor_data (temperature, humidity,tim1) VALUES (?, ?,?)", (temperature, humidity,timee))
    db.commit()
    
    print(f"溫度：{temperature}，濕度：{humidity}time {timee}")
    return '資料已收到'

@app.route('/get_data', methods=['GET'])
def get_data():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()
    if data:
        temperature, humidity,timee = data[1], data[2],data[3]
        print(temperature,humidity,timee)
        return jsonify({'temperature': temperature, 'humidity': humidity,"timee":timee})
    else:
        return jsonify({'error': 'No data available'})
        
# new 
@app.route('/get_range_data', methods=['GET'])
def get_range_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    db, cursor = get_db()
    try:
        cursor.execute("SELECT * FROM sensor_data WHERE tim1 BETWEEN ? AND ?", (start_time, end_time))
        data = cursor.fetchall()
        if data:
            temperature_data = []
            humidity_data = []
            time_data = []
            print(data)
            for row in data:
                temperature_data.append(row[1])
                humidity_data.append(row[2])
                time_data.append(row[3])
            print(temperature_data,humidity_data,time_data)
            return jsonify({'temperature': temperature_data, 'humidity': humidity_data, 'time': time_data})
        else:
            return jsonify({'error': 'No data available for the specified time range'})
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
        

@app.route('/')
def index():
    return app.send_static_file('hw.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
