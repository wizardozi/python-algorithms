def search_insert(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left 

# Test case 1: Target is present
print(search_insert([1, 3, 5, 6], 5))  # Expected: 2

# Test case 2: Target is not present, should be inserted in the middle
print(search_insert([1, 3, 5, 6], 2))  # Expected: 1

# Test case 3: Target is greater than all elements
print(search_insert([1, 3, 5, 6], 7))  # Expected: 4

# Test case 4: Target is smaller than all elements
print(search_insert([1, 3, 5, 6], 0))  # Expected: 0
