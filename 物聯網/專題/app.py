from flask import Flask, request, jsonify, g
import sqlite3
import datetime
import random
import calendar
app = Flask(__name__)
fake=True

if fake:
    app.config['DATABASE'] = 'fake.db'
else:
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

# update data from esp32 or ardo 
@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.get_json()  # 接收來自 ESP32 的 JSON 資料
    device = data['device']
    current = data['current']
    work=data['work']
    db,cursor=get_db()
    # fake time
    if not fake:
        timee=datetime.datetime.now()
    else:
        timee = datetime.datetime(2024,  # 隨機年份從2010到2024
                          random.randint(1, 12),       # 隨機月份
                          random.randint(1, 28),       # 隨機日期（簡化到28日以內）
                          random.randint(0, 23),       # 隨機小時
                          random.randint(0, 59),       # 隨機分鐘
                          random.randint(0, 59))       # 隨機秒
    cursor.execute("INSERT INTO sensor_data (device, current,work,tim1) VALUES (?, ?,?,?)", (device, current,work,timee))
    db.commit()
    return "sucess"

#getrange
@app.route('/getrange', methods=['POST'])
def getrange():
    data = request.get_json()
    selected_unit = data.get('date')  # 從前端獲取選擇的時間跨度
    db, cursor = get_db()

    # 獲取當前日期
    current_date = datetime.datetime.now().date()

    if selected_unit == 'day':
        # 如果選擇的是日，則從資料庫中取出當天的資料
        cursor.execute("SELECT * FROM sensor_data WHERE DATE(tim1) = ?", (current_date,))
    elif selected_unit == 'week':
        # 如果選擇的是週，則從資料庫中取出本週的資料
        # 本週的第一天是星期一
        start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
        end_of_week = start_of_week + datetime.timedelta(days=6)
        cursor.execute("SELECT * FROM sensor_data WHERE DATE(tim1) BETWEEN ? AND ?", (start_of_week, end_of_week))
    elif selected_unit == 'month':
        # 如果選擇的是月，則從資料庫中取出當月的資料
        start_of_month = current_date.replace(day=1)
        end_of_month = start_of_month + datetime.timedelta(days=calendar.monthrange(current_date.year, current_date.month)[1] - 1)
        cursor.execute("SELECT * FROM sensor_data WHERE DATE(tim1) BETWEEN ? AND ?", (start_of_month, end_of_month))
    elif selected_unit == 'year':
        # 如果選擇的是年，則從資料庫中取出當年的資料
        start_of_year = current_date.replace(month=1, day=1)
        end_of_year = start_of_year.replace(month=12, day=31)
        cursor.execute("SELECT * FROM sensor_data WHERE DATE(tim1) BETWEEN ? AND ?", (start_of_year, end_of_year))
    else:
        # 錯誤的選擇
        return jsonify({'error': 'Invalid unit selected'})

    rows = cursor.fetchall()

    # 將資料轉換為JSON格式返回給前端
    response_data = {
        "pulgin": [row[1] for row in rows],
        "work": [row[3]/3600000 for row in rows],
        "time":[datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S") for row in rows]
    }
    
    if selected_unit=="day":
        lll=len(response_data['pulgin'])
        set_p=set(response_data['pulgin'])
        recall_data = {
        "pulgin": [i for i in set_p],
        "w&t":[{
            "kw/h":[0]*24,
            "h":[i for i in range(24)],
            "trueday":[""]*24
        } for i in set_p]
        }  
        for i in range(lll):
          for k in range(len(set_p)):
            if   recall_data['pulgin'][k]==response_data['pulgin'][i]:
                wat=recall_data['w&t'][k]
                for tim in range(24):
                    if response_data['time'][i].hour==tim:
                        wat['kw/h'][tim]+=response_data['work'][i]
                        wat['trueday'][tim]=response_data['time'][i].strftime("%Y-%m-%d %H")
    elif selected_unit=="week":
        lll=len(response_data['pulgin'])
        set_p=set(response_data['pulgin'])
        recall_data = {
        "pulgin": [i for i in set_p],
        "w&t":[{
            "kw/h":[0]*7,
            "h":[i for i in range(7)],
            "trueday":[""]*7
        } for i in set_p]
        }  
        for i in range(lll):
          for k in range(len(set_p)):
            if   recall_data['pulgin'][k]==response_data['pulgin'][i]:
                wat=recall_data['w&t'][k]
                for tim in range(7):
                    if response_data['time'][i].weekday()==tim:
                        wat['kw/h'][tim]+=response_data['work'][i]
                        wat['trueday'][tim]=response_data['time'][i].strftime("%Y-%m-%d")
    elif selected_unit=="month":
        current_date = datetime.datetime.now()
        # 獲取當前月份的年份和月份
        year = current_date.year
        month = current_date.month
        # 使用calendar模組的monthrange函式獲取當前月份的天數
        days_in_month = calendar.monthrange(year, month)[1]
        lll=len(response_data['pulgin'])
        set_p=set(response_data['pulgin'])
        recall_data = {
        "pulgin": [i for i in set_p],
        "w&t":[{
            "kw/h":[0]*days_in_month,
            "h":[i for i in range(days_in_month)],
            "trueday":[""]*days_in_month
        } for i in set_p]
        }  
        for i in range(lll):
            for k in range(len(set_p)):
                if   recall_data['pulgin'][k]==response_data['pulgin'][i]:
                    wat=recall_data['w&t'][k]
                    for tim in range(days_in_month):
                        if response_data['time'][i].day==tim+1:
                            wat['kw/h'][tim]+=response_data['work'][i]
                            wat['trueday'][tim]=response_data['time'][i].strftime("%Y-%m-%d")
    elif selected_unit=="year":
        lll=len(response_data['pulgin'])
        set_p=set(response_data['pulgin'])
        recall_data = {
        "pulgin": [i for i in set_p],
        "w&t":[{
            "kw/h":[0]*12,
            "h":[i for i in range(12)],
            "trueday":[""]*12
        } for i in set_p]
        }  
        for i in range(lll):
            for k in range(len(set_p)):
                if   recall_data['pulgin'][k]==response_data['pulgin'][i]:
                    wat=recall_data['w&t'][k]
                    for tim in range(12):
                        if response_data['time'][i].month==tim+1:
                            wat['kw/h'][tim]+=response_data['work'][i]
                            wat['trueday'][tim]=response_data['time'][i].strftime("%Y-%m")
    
    return jsonify(recall_data)

#get 插座
@app.route('/get_device', methods=['POST'])
def get_device():
    db, cursor = get_db()
    cursor.execute("SELECT device FROM sensor_data")
    rows = cursor.fetchall()
    # 將資料轉換成集合，再轉換成清單
    devices = list(set(row[0] for row in rows))
    
    db.close()
    return jsonify(devices)

#getpay
@app.route('/getpay', methods=['POST'])
def getpay():
    db, cursor = get_db()
    current_date=datetime.datetime.now()
   # 如果選擇的是月，則從資料庫中取出當月的資料
    start_of_month = current_date.replace(day=1)
    end_of_month = start_of_month + datetime.timedelta(days=calendar.monthrange(current_date.year, current_date.month)[1] - 1)
    cursor.execute("SELECT * FROM sensor_data WHERE DATE(tim1) BETWEEN ? AND ?", (start_of_month, end_of_month))    
    rows = cursor.fetchall()
    response_data = {
        "pulgin": [row[1] for row in rows],
        "work": [row[3]/3600000 for row in rows],
        "time":[datetime.datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S") for row in rows]
    }
    # 將資料轉換成集合，再轉換成清單
    current_date = datetime.datetime.now()
    # 獲取當前月份的年份和月份
    year = current_date.year
    month = current_date.month
    # 使用calendar模組的monthrange函式獲取當前月份的天數
    days_in_month = calendar.monthrange(year, month)[1]
    lll=len(response_data['pulgin'])
    set_p=set(response_data['pulgin'])
    recall_data = {
    "pulgin": [i for i in set_p],
    "w&t":[{
        "kw/h":[0]*days_in_month,
        "h":[i for i in range(days_in_month)],
        "trueday":[""]*days_in_month
    } for i in set_p]
    }  
    for i in range(lll):
        for k in range(len(set_p)):
            if   recall_data['pulgin'][k]==response_data['pulgin'][i]:
                wat=recall_data['w&t'][k]
                for tim in range(days_in_month):
                    if response_data['time'][i].day==tim+1:
                        wat['kw/h'][tim]+=response_data['work'][i]
                        wat['trueday'][tim]=response_data['time'][i].strftime("%Y-%m-%d")
    sum=0
    for k in range(len(set_p)):
        wat=recall_data['w&t'][k]
        for tim in range(days_in_month):
            sum+=wat['kw/h'][tim]
    sum*=5.5
    db.close()
    return jsonify(sum)
#asd
@app.route('/get_range_data', methods=['POST'])
def get_range_data():
    data = request.get_json()  # 接收來自 ESP32 的 JSON 資料
    end = data['end']
    start = data['start']
    db,cursor=get_db()
    pass
    db.commit()
    return ""

#asd
@app.route('/getnowdata', methods=['GET'])
def getnowdata():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1")
    data=cursor.fetchone()
    print(data)
    return jsonify(data)


@app.route('/')
def index():
    return app.send_static_file('index.html')



# @app.route('/')
# def index():
#     return app.send_static_file('tyr.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
