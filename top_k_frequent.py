def top_k_frequent(nums, k):
    nums_dict = {}
    for n in nums:
        nums_dict[n] = nums_dict.get(n, 0) + 1
        
    count_list = nums_dict.items()
    for key, value in nums_dict.items():
        count.append(value)
    count.sort(reverse=True)
    i = 0
    result = []
    for i in range(k):        
        for j in nums:
            if count[i] == nums_dict[j] and j not in result:
                result.append(j)                        
    return result





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