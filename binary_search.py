def binary_search(arr: list[int], target: int) -> int:
    # Initialize Pointers:
    left, right = 0, len(arr) - 1 #left and right are set to the start and end of the array
    
    # Binary Search Loop:
    while left <= right: # Continues as long as left is less than or equal to right.                
        mid = left + (right - left)//2 # Calculates mid correctly to avoid integer overflow.
        # Comparison Logic:        
        if arr[mid] == target: # If the middle element matches the target, returns mid.
            return mid
        
        elif arr[mid] < target: # If the middle element is less than the target, move the left pointer to mid + 1.
            left = mid + 1        
        else:
            right = mid - 1 # If greater, move the right pointer to mid - 1.
    # Return -1 if Not Found:    
    return -1 # After the loop, if no match was found, returns -1.
print(binary_search([-1, 0, 3, 5, 9, 12], 9))  # Expected: 4
print(binary_search([-1, 0, 3, 5, 9, 12], 2))  # Expected: -1
print(binary_search([1, 2, 3, 4, 5], 1))  # Expected: 0
print(binary_search([1, 2, 3, 4, 5], 5))  # Expected: 4
print(binary_search([], 10))  # Expected: -1
