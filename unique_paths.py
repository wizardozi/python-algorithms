import math
def uniquePaths(m: int, n: int) -> int:        
    numer = math.factorial(m + n - 2)
    denom = math.factorial(m - 1) * math.factorial(n - 1)
    return numer // denom