import pygame
import sys

pygame.init()

# 设置窗口的宽度和高度
width, height = 500, 500

# 创建窗口
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Creating a Color Block")

# 定义颜色（RGB格式）
RED = (255, 0, 0)



position=[
            [[20,20],[140,20],[260,20],[380,20]],
            [[20,140],[140,140],[260,140],[380,140]],
            [[20,260],[140,260],[260,260],[380,260]],
            [[20,380],[140,380],[260,380],[380,380]]    
        ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清空窗口
    window.fill((255, 255, 255))

    # 绘制色块
    for i in range(4):
        for j in range(4):
            now=position[i][j]
            block_rect = pygame.Rect(now[0], now[1], 100, 100)
            pygame.draw.rect(window, (0,0,0), block_rect)

    # 更新显示
    pygame.display.flip()
