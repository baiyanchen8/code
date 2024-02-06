import pygame
import sys
pygame.init()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_KP1]:
        print("1 key is pressed")