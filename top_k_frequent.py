import heapq
from collections import Counter

def top_k_frequent(nums, k):
    # this is a heap algorithm.
    return  [result[0] for result in heapq.nlargest(k, Counter(nums).items(), key=lambda item: item[1])]





nums = [1]
k = 1
print(top_k_frequent(nums, k))
# Output: [1,2]
nums = [4,4,6,6,7,7]
k = 2
# Expected: Any 2 of [4,6,7]
print(top_k_frequent(nums, k))
nums = [-1,-1,-2,-2,-3]
k = 2
# print(Expected: [-1, -2]
print(top_k_frequent(nums, k))
nums = [9,9,9,1,2,3]
k = 1
# Expected: [9]
print(top_k_frequent(nums, k))