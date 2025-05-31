def build_spiral(n):
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down
    x, y = n // 2, n // 2  # Start at center of the matrix
    num = 1                # Start filling with 1
    step = 1               # How many steps to take in current leg

    while num <= n * n:
        for d in range(4):  # Right, Up, Left, Down
            dx, dy = directions[d]
            for _ in range(step):
                if num > n * n:
                    break
                spiral[x][y] = num
                x += dx
                y += dy
                num += 1
            if d == 1 or d == 3:
                step += 1  # Increase step after Up and Down
    return spiral

def print_spiral(grid):
    for row in grid:
        print(" ".join(f"{num:3}" for num in row))

n = 5  # Must be odd!


# (Insert your spiral generation code here)

print_spiral(build_spiral(n))