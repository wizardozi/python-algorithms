def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    p1, p2 = 0, 0
    result = []
    nums1.sort()
    nums2.sort()
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            if not result or result[-1] != nums1[p1]:
                result.append(nums1[p1])
            p1 += 1
            p2 += 1
            
            
    return result

nums1 = [1, 2, 2, 3]
nums2 = [2, 2]
print(intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
