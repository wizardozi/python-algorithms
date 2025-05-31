def sum(n):
    if n == 1:    
        print(f'{n} = ', end='')
        return 1
    else:
        print(f'{n} + ', end='')
        return n + sum(n - 1)



def factorial(n):
    if n == 1:    
        print(f'{n} = ', end='')
        return 1
    else:
        print(f'{n} x ', end='')
        return n * factorial(n - 1)

print(factorial(6))