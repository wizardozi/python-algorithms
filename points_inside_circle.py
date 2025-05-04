from typing import List
def countPoints(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    # x,y = points[i][0], points[i][1]
    # h,k = queries[i][0], queries[i][1]
    # r1 = math.sqrt((x - h)**2 + (y - k)**2)
    answers = []
    for c in queries:
        result = 0
        for p in points:
            dx = p[0] - c[0]
            dy = p[1] - c[1]  
            if dx*dx + dy*dy <= c[2]*c[2]:
                result += 1
        answers.append(result)
    return answers



points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(countPoints(points, queries))
# Output: [3,2,2]
points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
print(countPoints(points, queries))
# Output: [2,3,2,4]
        