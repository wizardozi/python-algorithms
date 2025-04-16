def longest_zigzag(nums: list[int]) -> int:
    result = []
    i,j = 0, 1
    
    while j < len(nums) and i < j:
        if zigzag(result, nums[i], nums[j]):
            result.append(nums[i])            
            i += 1
            j += 1

    return len(result)

def zigzag(compare, a, b):    
    if a != b:
        if a < b and compare[-1] < a:
            return True
        elif a > b and compare[-1] > a:
            return True
    else:
        return False

    


print(longest_zigzag([1, 3, 2, 4, 3, 5]))      # Output: 6
print(longest_zigzag([1, 2, 3, 4, 5]))         # Output: 2
print(longest_zigzag([9, 4, 2, 10, 7, 8, 8, 1, 9]))  # Output: 5
