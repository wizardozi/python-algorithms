def first_occurrence(arr: list[int], target: int) -> int:    
    result = -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid  # Update result to the current index
            right = mid - 1  # Keep searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  # Move left if mid value is greater
    return result

# Test cases
print(first_occurrence([1, 2, 2, 2, 3, 4, 5], 2))  # Expected: 1
print(first_occurrence([1, 2, 3, 4, 5], 6))        # Expected: -1
