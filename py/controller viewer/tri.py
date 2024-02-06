import pygame
import sys

# 初始化 Pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
# 載入圖片
image = pygame.image.load("pic/lb.png").convert_alpha()

# 取得圖片的大小
width, height = image.get_size()

# 創建一個新的 Surface，大小與原圖相同
new_image = pygame.Surface((width, height), pygame.SRCALPHA)

# 將非透明部分換成黑色
image.fill((0, 0, 0, 255))

# 初始化畫面
screen.fill((250,250,250))

# 繪製新圖片到畫面上
screen.blit(image, (0, 0))

# 更新畫面
pygame.display.flip()

# 主迴圈等待關閉視窗事件
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 退出 Pygame
pygame.quit()
sys.exit()
