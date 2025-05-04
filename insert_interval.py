from typing import List

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[Lisint[int]]:
        
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if last[0] <= new_interval[0] and :
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


intervals = [[1,3],[6,9]]
new_interval = [2,5]
print(insert(intervals, new_interval))
# Expected: [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print(insert(intervals, new_interval))
# Expected: [[1,2],[3,10],[12,16]]

intervals = [[5,7],[8,10]]
new_interval = [1,3]
print(insert(intervals, new_interval))
# Expected: [[1,3],[5,7],[8,10]]

intervals = [[1,2],[3,4]]
new_interval = [5,7]
print(insert(intervals, new_interval))
# Expected: [[1,2],[3,4],[5,7]]

intervals = [[2,3],[5,7],[8,10]]
new_interval = [1,12]
print(insert(intervals, new_interval))
# Expected: [[1,12]]

intervals = []
new_interval = [4,8]
print(insert(intervals, new_interval))
# Expected: [[4,8]]