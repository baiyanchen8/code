import pygame
import sys
import numpy as np
import random
import time
import rainbow as rn  # 引入虹色模組

# 初始化 Pygame
pygame.init()

# 設定視窗大小
width, height = 1800, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('連桿運動')

# 控制 FPS 的 clock
clock = pygame.time.Clock()
min_fps = 30  # 設定最低 FPS

n = 5
# 設定初始條件
L = np.zeros(n)  # 各根桿的長度
k = 90

kk = [199, 133, 97, 47, 37]
L[0] = 199
for i in range(1, n):
    L[i] = L[i - 1] - random.randint(20, 30)

# 初始角度
theta = np.zeros(n)  # 各根桿的初始角度

for i in range(n):
    theta[i] = 0.0

# 初始角速度
omega = np.zeros(n)

# 重力加速度
g = np.zeros(n)  # 各根桿的重力加速度

g[0] = 5
for i in range(1, n):
    g[i] = g[i - 1] * (random.randint(1, 100) / 10)

# 每針幾秒
dt = 0.4

# 初始化位置
x, y = np.zeros(n), np.zeros(n)

# 初始化端點軌跡
trajectory = []

# color
rainbow_colors = rn.getrainbow()  # 取得虹色模組的顏色
line_color = (0, 250, 0)  # 連桿的顏色
trace_color = (250, 250, 250)  # 軌跡的顏色
node_color = (250, 0, 0)  # 節點的顏色

# 運動模擬
line_on = True  # 是否顯示連桿
with_node = False  # 是否顯示節點
running = True
screen_fill = True  # 是否填充視窗背景色
rainbow = True  # 是否使用虹色軌跡
p1 = False
trade = 1000
row = 4000
s = row
while running:
    s += 1
    if s == row:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 計算每根桿的角度
    for i in range(n):
        theta[i] += 0.5 * (-g[i] / L[i]) * dt * dt
        if i == 0:
            x[i], y[i] = width / 2 + L[i] * np.sin(theta[i]), height / 2 - L[i] * np.cos(theta[i])
        else:
            x[i], y[i] = x[i - 1] + L[i] * np.sin(theta[i]), y[i - 1] - L[i] * np.cos(theta[i])

    # 儲存端點軌跡
    trajectory.append((x[n - 1], y[n - 1]))
    if trade > 0:
        while len(trajectory) > trade:
            trajectory.pop(0)

    # 畫連桿
    if screen_fill:
        screen.fill((0, 0, 0))  # 設定背景色為白色
    for i in range(0, n):
        if line_on:
            if i == 0:
                pygame.draw.line(screen, line_color, (width / 2, height / 2), (x[0], y[0]), 2)
            else:
                pygame.draw.line(screen, line_color, (x[i - 1], y[i - 1]), (x[i], y[i]), 2)
        if with_node:
            if i > 0:
                pygame.draw.circle(screen, node_color, (int(x[i - 1]), int(y[i - 1])), 2)

    # 畫端點軌跡
    if True:
        if len(trajectory) >= 2:
            if rainbow:
                # 使用彩虹色
                rainbow_idx = 0
                for i in range(len(trajectory) - 1):
                    pygame.draw.line(screen, rainbow_colors[rainbow_idx], trajectory[i], trajectory[i + 1], 1)
                    rainbow_idx = (rainbow_idx + 1) % len(rainbow_colors)
                for i in range(2):
                    a = rainbow_colors.pop(0)
                    rainbow_colors.append(a)
            else:
                pygame.draw.lines(screen, trace_color, False, trajectory, 1)

    # 更新視窗
    pygame.display.flip()
    p1 = False

# 退出 Pygame
pygame.quit()



print("L ",L)
print("theta ",theta)
print("g ",g)
print("trade ",trade)