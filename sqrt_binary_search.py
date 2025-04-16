def my_sqrt(x: int) -> int:
    left, right = 0, x

    # looking for a number which muliplied by itself is the target x
    while left <= right:
        mid = left + (right - left)//2
        if mid*mid == x: # if mid^2 is equal to x return mid
            return mid
        elif mid*mid < x: # if mid^2 is less than target search right half
            left = mid + 1
        else: # else search left half
            right = mid -1
    return right

print(my_sqrt(10))
