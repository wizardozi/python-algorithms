nums = [2, 7, 11, 15]
print('Numbers: '+ str(nums))

target = 18
print('Target number: '+ str(target))

diff = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in diff:
        print(f"Indices: {diff[complement]}, {index}")
        print(f"Numbers: {nums[diff[complement]]}, {num}")
        break
    diff[num] = index
    

        
