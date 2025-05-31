from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    directions = [(1,0), [-1,0], [0,1], [0,-1]]
    d = 0
    # while d <= len(directions):
    #     for row in matrix:
    #         for item in row:
    #             pass
    print(d + directions[0])

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix)) # Output: [1,2,3,6,9,8,7,4,5]


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix)) # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
