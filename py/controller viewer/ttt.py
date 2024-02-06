import pygame as pg
import sys

# 初始化 Pygame
pg.init()

# 設定視窗大小
window_size = (400, 400)

# 創建視窗
screen = pg.display.set_mode(window_size)
pg.display.set_caption("方向鍵示例")

# 定義顏色
white = (255, 255, 255)

# 定義方向鍵的寬度和高度
key_width = 100  # 短邊在內
key_height = 50

# 定義方向鍵的位置
up_key_rect = pg.Rect((window_size[0] - key_width) // 2, (window_size[1] - key_height) // 2 - key_height // 2, key_width, key_height)
down_key_rect = pg.Rect((window_size[0] - key_width) // 2, (window_size[1] - key_height) // 2 + key_height // 2, key_width, key_height)
left_key_rect = pg.Rect((window_size[0] - key_width) // 2 - key_width // 2, (window_size[1] - key_width) // 2, key_width, key_height)
right_key_rect = pg.Rect((window_size[0] - key_width) // 2 + key_width // 2, (window_size[1] - key_width) // 2, key_width, key_height)

# 主迴圈
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # 清空畫面
    screen.fill(white)

    # 繪製方向鍵
    pg.draw.rect(screen, (0, 0, 0), up_key_rect)
    pg.draw.rect(screen, (0, 0, 0), down_key_rect)
    pg.draw.rect(screen, (0, 0, 0), left_key_rect)
    pg.draw.rect(screen, (0, 0, 0), right_key_rect)

    # 更新畫面
    pg.display.flip()

# 退出 Pygame
pg.quit()
sys.exit()
