from flask import Flask, render_template, g, jsonify,send_file
import sqlite3
import os
app = Flask(__name__)

DATABASE = 'data.db'

# connect to "mydatabase.db"
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('data.db')
        g.cursor = g.db.cursor()
    return g.db, g.cursor

# close_db when teardown Flask's application context
def close_db(db):
    if db in g:
        g.db.close()

@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    static_dir = os.path.join(root_dir, 'template')
    return send_file(os.path.join(static_dir, filename))


# API 路由: 取得指定地區的溫度資料
@app.route('/temperature/<location>')
def temperature(location):
    db,cursor =get_db() 
    cursor.execute("SELECT date, max_temp, min_temp FROM temperature WHERE location=?", (location,))
    data = cursor.fetchall()
    result = [{'date': row[0], 'max_temp': row[1], 'min_temp': row[2]} for row in data]
    print(result)
    close_db(db)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
