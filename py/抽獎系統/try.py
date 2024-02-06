import pygame
import webbrowser
import sys

pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame 中打開 URL")

def open_url(url):
    webbrowser.open(url)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_url("https://chat.openai.com/c/3d2206fc-666a-4332-acde-43fa9b40aa4c")
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 在此插入你想要打開的URL
                
                pygame.quit()
                sys.exit()

    pygame.display.flip()

pygame.quit()
