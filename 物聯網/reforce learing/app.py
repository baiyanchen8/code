from flask import Flask, request, jsonify, send_file
import numpy as np
import os

app = Flask(__name__)

# 定义迷宫的大小和起点终点
MAP_SIZE = (5, 5)
START = (0, 0)
END = (MAP_SIZE[0] - 1, MAP_SIZE[1] - 1)

# 初始化迷宫地图和价值表
maze = np.zeros(MAP_SIZE)
values = np.zeros(MAP_SIZE)

# 定义动作集合（上、下、左、右）
ACTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 进行一次价值迭代算法的训练
def train_value_iteration(maze, values, start, end):
    gamma = 0.9
    epsilon = 0.01
    max_iterations = 1000

    for _ in range(max_iterations):
        delta = 0
        for i in range(MAP_SIZE[0]):
            for j in range(MAP_SIZE[1]):
                if (i, j) == end:
                    continue
                v = values[i, j]
                max_value = float("-inf")
                for action in ACTIONS:
                    ni, nj = i + action[0], j + action[1]
                    if ni >= 0 and ni < MAP_SIZE[0] and nj >= 0 and nj < MAP_SIZE[1]:
                        if maze[ni, nj] == 0:
                            max_value = max(max_value, values[ni, nj])
                values[i, j] = max_value * gamma
                if (i, j) == start:
                    values[i, j] = 1
                delta = max(delta, abs(v - values[i, j]))
        if delta < epsilon:
            break

# 计算路径的评分（与最短路径的差异）
def calculate_score(path):
    # 计算路径与最短路径的差异，并返回评分
    # 这里简单地使用路径长度作为评分
    shortest_path_length = abs(END[0] - START[0]) + abs(END[1] - START[1])
    path_length = len(path)
    score = shortest_path_length - path_length
    return score

# 保存路径记录
def save_path_record(path):
    with open('path_records.txt', 'a') as f:
        f.write(str(path) + '\n')

# 处理前端发送的地图数据并进行训练，并返回最佳路径
@app.route('/saveMapData', methods=['POST'])
def save_map_data():
    global maze, values
    

    # 获取前端发送的地图数据
    re= request.json
    map_data=re["mapData"]
    
    block=re["block"]
    maze = np.array((int(block),int(block)))
    for i in range(int(block)):
        for j in range(int(block)):
            if map_data=="start":
                START=(i,j)
            if map_data=="end":
                END=(i,j)
            if map_data=="start":
                START=(i,j)
            

    # 更新迷宫地图
    maze = np.array(map_data)

    # 进行 100 次价值迭代算法的训练
    best_path = []
    best_score = float("-inf")
    for _ in range(100):
        # 重新初始化价值表
        values = np.zeros(MAP_SIZE)

        # 进行价值迭代算法的训练
        train_value_iteration(maze, values, START, END)

        # 计算当前路径
        current_path = [START]
        current_position = START
        while current_position != END:
            max_value = float("-inf")
            next_position = None
            for action in ACTIONS:
                ni, nj = current_position[0] + action[0], current_position[1] + action[1]
                if ni >= 0 and ni < MAP_SIZE[0] and nj >= 0 and nj < MAP_SIZE[1]:
                    if values[ni, nj] > max_value:
                        max_value = values[ni, nj]
                        next_position = (ni, nj)
            if next_position is not None:
                current_path.append(next_position)
                current_position = next_position
            else:
                break  # 如果没有可行的下一步移动，则结束路径搜索

            current_path.append(next_position)
            current_position = next_position

        # 计算路径评分
        current_score = calculate_score(current_path)

        # 更新最佳路径和最佳评分
        if current_score > best_score:
            best_path = current_path
            best_score = current_score

    # 保存最佳路径记录
    save_path_record(best_path)

    return jsonify({'best_path': best_path})
@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    static_dir = os.path.join(root_dir, 'template')
    return send_file(os.path.join(static_dir, filename))
if __name__ == '__main__':
    app.run(debug=True)
