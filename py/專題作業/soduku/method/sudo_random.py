import random

def generate_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    return grid

def fill_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid_move(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def is_valid_move(grid, row, col, num):
    # Check row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def sudoku_return():
    sudoku = generate_sudoku()
    return sudoku
