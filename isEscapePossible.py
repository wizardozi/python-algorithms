import sys
sys.setrecursionlimit(100000)
from typing import List

def isEscapePossible(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    MAX = 10**6
    LIMIT = 20000
    blocked = set(map(tuple, blocked))
    memo = {}
    deltas = [
            (-1, 0),
        (0, -1), (0, 1),
            (1, 0)
            ]
    def dfs(x, y, target, visited):
        # reached target
        if (x, y) == tuple(target):
            return True
        if len(visited) >= LIMIT:
            return True
        if (x, y) in blocked or (x, y) in visited:
            return False
        # out of bounds or position is blocked or already visited
        if  x < 0 or x >= MAX or y < 0 or y >= MAX:
            return False
        visited.add((x, y))
        for dx, dy in deltas:
            if dfs(x + dx, y + dy, target, visited):
                return True
        return False
    return dfs(*source, target, set()) and dfs(*target, source, set())

blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]
print(isEscapePossible(blocked, source, target))

blocked = []
source = [0,0]
target = [999999,999999]
print(isEscapePossible(blocked, source, target))

