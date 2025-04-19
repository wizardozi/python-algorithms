import heapq, math
def k_closest(points, k):
    return heapq.nsmallest(k, points, key=lambda p: math.hypot(p[0], p[1]))

points = [[3, 3], [5, -1], [-2, 4], [0, 0], [1, 1]]
k = 3
print(k_closest(points, k))