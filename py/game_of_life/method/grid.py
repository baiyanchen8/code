import pygame
import numpy as np
# Function to update the grid based on Game of Life rules
def update_grid(grid):
    new_grid = grid.copy()
    GRID_WIDTH =len(grid)
    GRID_HEIGHT = len(grid[1])
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            neighbors = [
                grid[(x - 1) % GRID_WIDTH, (y - 1) % GRID_HEIGHT],
                grid[(x) % GRID_WIDTH, (y - 1) % GRID_HEIGHT],
                grid[(x + 1) % GRID_WIDTH, (y - 1) % GRID_HEIGHT],
                grid[(x - 1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                grid[(x + 1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                grid[(x - 1) % GRID_WIDTH, (y + 1) % GRID_HEIGHT],
                grid[(x) % GRID_WIDTH, (y + 1) % GRID_HEIGHT],
                grid[(x + 1) % GRID_WIDTH, (y + 1) % GRID_HEIGHT],
            ]
            live_neighbors = sum(neighbors)
            if grid[x, y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if live_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid