def read_sudoku(filename):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            # Split each line into numbers and convert to integers
            row = list(map(int, line.split()))
            grid.append(row)
        return grid

sudoku = read_sudoku('sudoku.txt')
for row in sudoku:
    print(row)


def is_valid(num, row, col, grid):
    # Check if the number already exists in the specified row        
    if num in grid[row]:
        return False
    # Check if the number already exists in the same column
    for i in range(len(grid)):
        if grid[i][col] == num:
            return False
    return True
    
def find_empty(grid):
    empty = 0    
    for index1, row in enumerate(grid):
        for index2, cell in enumerate(row):
            if cell == empty:
                location = [index1, index2]
                return location
     

def solve_sudoku(grid):
    # Base case: Check if the puzzle is complete
    location = find_empty(grid)
    if not location:
        
        # No empty spots left, solution found
        for row in grid:
            print(row)
        return True

    row, col = location
    
    for num in range(1, 10):
        if is_valid(num, row, col, grid):
            grid[row][col] = num  # Place the number
            # Recursively attempt to solve the rest of the grid
            if solve_sudoku(grid):                
                return True
            # Backtrack: Undo the move if not successful
            grid[row][col] = 0

    # If no number works, backtrack
    return False

print('---------------------------')
print('Solved Sudoku')
print('---------------------------') 

solve_sudoku(sudoku)
    
    