def collatz_steps(n: int) -> int:        
    steps = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1        
        steps.append(n)
    return len(steps)


def longest_collatz(n):
    longest_sequence = 0
    longest_number = 0
    for i in range(2, n):
        current = collatz_steps(i)
        if longest_sequence < current:
            longest_sequence = current
            longest_number = i
    print(f'Longest Sequence is: {longest_sequence} from the number: {longest_number}')
    return longest_sequence

def collatz_memoization(n):
    memo = {1:0}
    steps = 0
    
    def compute_steps(k):
        if k not in memo:
            if k % 2 == 0:
                memo[k] = 1 +  compute_steps(k // 2)
            else:
                memo[k] = 1 + compute_steps(3 * k + 1)
        return memo[k]
    longest_sequence = 0
    for i in range(2, n):
        steps = compute_steps(i)
        if steps > longest_sequence:
            longest_sequence = steps
    return longest_sequence

n = int(input('Enter a number: '))
print(collatz_memoization(n))
# print(collatz_steps(n))
