import pygame
import numpy as np
from method import grid as gd
from method.keyboard import kbmanager
from screeninfo import get_monitors
import keyboard as kb
import random
monitors = get_monitors()
# Initialize Pygame
pygame.init()
  
# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = monitors[1].width-100,monitors[1].height-100
CELL_SIZE = 5
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH// CELL_SIZE, SCREEN_HEIGHT//CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid with random cell states
grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))


clock = pygame.time.Clock()
running = True

clock.tick_busy_loop(60)
density=0
font = pygame.font.Font(None, 36)
k1b= kbmanager()
while running:
    clock.tick_busy_loop(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    density=0
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            
            if grid[x, y] == 1:
                density+=1
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    density/=(GRID_HEIGHT*GRID_WIDTH)
    
    
    pygame.display.flip()

    grid = gd.update_grid(grid)

pygame.quit()

