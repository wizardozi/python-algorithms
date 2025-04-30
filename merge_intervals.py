from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged



print(merge([[1,3],[2,6],[8,10],[15,18]]))       # [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                      # [[1,5]]
print(merge([[1,4],[0,2],[3,5]]))                # [[0,5]]
print(merge([[1,4],[5,6]]))                      # [[1,4],[5,6]]
print(merge([[1,10],[2,3],[4,5],[6,7]]))         # [[1,10]]