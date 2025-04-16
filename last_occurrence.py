def last_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left +(right - left)//2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

print(last_occurrence([1, 2, 2, 2, 3, 4, 5], 2))  # Expected: 3
print(last_occurrence([1, 2, 3, 4, 5], 6))  # Expected: -1
print(last_occurrence([1, 2, 3, 4, 5], 3))  # Expected: 2
print(last_occurrence([1, 1, 2, 3], 1))  # Expected: 1
print(last_occurrence([1, 2, 3, 3, 3], 3))  # Expected: 4
