from typing import List
def findMatrix(nums: List[int]) -> List[List[int]]:
    freq = [0] * (len(nums) + 1)
    matrix = []
    for n in nums:
        if freq[n] >= len(matrix):
            matrix.append([])
        matrix[freq[n]].append(n)
        freq[n] += 1
    return matrix




nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
print(findMatrix(nums)) 

    