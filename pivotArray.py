def pivotArray(nums, pivot):
    smaller = []
    equal = []
    larger = []
    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            larger.append(num)
        else:
            equal.append(num)
    return smaller + equal + larger
