from typing import List

# def length_of_LIS(nums: List[int]) -> int:
#     if len(nums) == 1:
#         return 1
#     result = 0
#     for i in range(len(nums)):
#         temp = [nums[i]] 
#         for j in range(i + 1, len(nums)):            
#             if temp[-1] < nums[j]: 
#                 temp.append(nums[j])
#         result = max(result, len(temp))

#     return result

def length_of_LIS(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1
    tails = []    
    for num in nums:
        if not tails or num > tails[-1]:
            tails.append(num)
        else: 
            left, right = 0, len(tails) - 1
            temp = len(tails)
            while left <= right:
                mid = left + (right - left) // 2
                if tails[mid] >= num:
                    temp = mid
                    right = mid - 1
                else:
                    left = mid + 1
            tails[temp] = num
    return len(tails)

print(length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Expected output: 4
print(length_of_LIS([1, 2, 3, 4, 5]))
# Expected output: 5
print(length_of_LIS([5, 4, 3, 2, 1]))
# Expected output: 1
print(length_of_LIS([2, 2, 2, 2, 2]))
# Expected output: 1
print(length_of_LIS([-1, 3, 4, 5, 2, 2, 2, 2]))
# Expected output: 4
print(length_of_LIS([7]))
# Expected output: 1

import random
random.seed(42)
large_input = [random.randint(-10000, 10000) for _ in range(2500)]
print(length_of_LIS(large_input))
# Expected output: Varies (should finish quickly)
