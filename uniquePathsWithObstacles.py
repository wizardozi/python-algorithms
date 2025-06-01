from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    grid = obstacleGrid
    memo = {}
    deltas = [(0, 1), (1, 0)]

    rows, cols = len(grid), len(grid)
    def dfs(x, y):
        if x >= rows or y >= cols or grid[x][y] == 1:
            return 0
        if (x, y) == (rows - 1, cols - 1):
            return 1
        if (x, y) in memo:
            return memo[(x, y)]
        total_paths = 0
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            total_paths += dfs(nx, ny)

        memo[(x , y)] = total_paths
        return total_paths
    return dfs(0, 0)



obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid))