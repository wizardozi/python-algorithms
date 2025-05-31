from typing import List
import math

def sieve(n: int) -> List[int]:
    A = [True for i in range(2, n)]

    for i in range(math.floor(math.sqrt(n))):
        if A[i] is True:
            j = i*i
            while j < n:
                A[j] = False
                j += i
    primes = []
    for i, value in enumerate(A):
        if value:
            primes.append(i)

    return primes
    


print(sieve(30))

