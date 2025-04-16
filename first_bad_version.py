# Mock implementation of isBadVersion
bad_version = int(input('Enter a version number: '))

def isBadVersion(version: int) -> bool:
    return version >= bad_version    
    
def first_bad_version(n: int) -> int:    
    # bad verision = n, all n > n are bad
    left, right = 0, n
    while left <= right:
        mid = left + (right - left)//2
        if isBadVersion(mid) == True:  # if version at mid is greater than bad version go left   
            right = mid -1
        else: # else go right
            left = mid + 1
    return left 
number_of_versions = 0
while number_of_versions <= bad_version:
    print("The number of versions must be greater than or equal to the bad version.")
    number_of_versions = int(input('Enter ammount of versions: '))    
        

print(first_bad_version(number_of_versions))

