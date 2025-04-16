def find_peak(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check the direction of the peak
        if arr[mid] < arr[mid + 1]:
            # Move right if the right side is higher
            left = mid + 1
        else:
            # Move left if the left side is higher or equal
            right = mid

    # After the loop, left and right will converge to the peak element
    return left
