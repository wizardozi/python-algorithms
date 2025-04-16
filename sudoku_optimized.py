def read_sudoku(filename):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            row = list(map(int, line.split()))
            grid.append(row)
        return grid

sudoku = read_sudoku('sudoku.txt')

from itertools import product

# Helper function to print the grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to find the empty cell with the fewest possibilities
def find_min_options(grid, possibilities):
    min_options = 10  # No cell can have more than 9 possibilities
    min_cell = None
    for r, c in product(range(9), repeat=2):
        if grid[r][c] == 0:
            num_options = len(possibilities[r][c])
            if num_options < min_options:
                min_options = num_options
                min_cell = (r, c)
    return min_cell

# Function to initialize possibilities for each cell
def initialize_possibilities(grid):
    possibilities = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
    for r, c in product(range(9), repeat=2):
        if grid[r][c] != 0:
            possibilities[r][c] = set()
    return possibilities

# Function to update possibilities after placing a number
def update_possibilities(grid, possibilities, row, col, num):
    for k in range(9):
        possibilities[row][k].discard(num)
        possibilities[k][col].discard(num)
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r, c in product(range(start_row, start_row + 3), range(start_col, start_col + 3)):
        possibilities[r][c].discard(num)

# Backtracking function with optimizations
def solve_sudoku(grid):
    # Initialize possibilities
    possibilities = initialize_possibilities(grid)

    # Propagate initial numbers to reduce search space
    for r, c in product(range(9), repeat=2):
        if grid[r][c] != 0:
            update_possibilities(grid, possibilities, r, c, grid[r][c])

    def backtrack(possibilities):
        cell = find_min_options(grid, possibilities)
        if not cell:
            return True  # No empty cells left, puzzle solved
        
        row, col = cell
        # Try each possible number in the cell
        for num in list(possibilities[row][col]):
            # Place the number and propagate changes
            grid[row][col] = num
            saved_possibilities = [row.copy() for row in possibilities]
            update_possibilities(grid, possibilities, row, col, num)

            # Recursively solve the rest
            if backtrack(possibilities):
                return True
            
            # Backtrack
            grid[row][col] = 0
            possibilities = saved_possibilities  # Restore previous state

        return False

    # Start solving
    if backtrack(possibilities):
        print('---------------------------')
        print('Solved Sudoku')
        print('---------------------------')
        print_grid(grid)
    else:
        print("No solution exists")

solve_sudoku(sudoku)
