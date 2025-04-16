
lists = [[1, 2, 2, 3, 4], [2, 3, 5], [2, 3, 6, 7]]




def find_intersect_pythonic(lists):
    result = []
    for list in lists:
        new_set = set(list)
        
    return 

def find_intersect_loop(lists):
    
    intersection =[]
    
    for item in lists[0]:
        if item not in intersection:
            intersection.append(item)

    for row in lists:
        for item in row:
            if item in intersection and item not in row:
                intersection.remove(item)

    print(intersection)
    return intersection


# print("pythonic intersection")
# print(find_intersect_pythonic(list1, list2))
print("loop based intersection")
print(find_intersect_loop(lists))
