def two_sum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1    
    while i < j:
        if  numbers[i] + numbers[j] == target:            
            return [i + 1, j + 1]
        elif numbers[i] + numbers[j] < target:
            i+= 1
        else:
            j-= 1
    return []
numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))

numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9
print(two_sum(numbers, target))



    
