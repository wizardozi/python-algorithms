from typing import List

def getSneakyNumbers(nums: List[int]) -> List[int]:
    result = []
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i, j in count.items():
        print(i, j)
        if j > 1:
            result.append(i)
    return result

nums = [0,3,2,1,3,2]
print(getSneakyNumbers(nums))

