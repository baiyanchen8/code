import sqlite3
from datetime import datetime, timedelta
import random
# 建立資料庫連接
conn = sqlite3.connect('fake.db')
cursor = conn.cursor()

# 2024-01-05 21:10:54

# 生成日期時間範圍
start_datetime = datetime(2024, 1,1, 0, 0, 0)
end_datetime = datetime(2024, 6, 9, 23, 59, 59)
# 計算總秒數
total_seconds = int((end_datetime - start_datetime).total_seconds())
current=0
# 插入資料
for i in range(0,total_seconds,3600):
    device=random.choice(["插座1","插座2","插座3"])
    current_datetime = start_datetime + timedelta(seconds=i)
    current=random.uniform(0,15)*3600
    if current<0:
        current=0
    work=110*current
    current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO sensor_data (device, current,work,tim1) VALUES (?, ?,?,?)", (device, current,work,current_datetime))
# 提交變更並關閉連接
    conn.commit()
conn.close()
