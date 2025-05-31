def convert_to_base(n: int, base: int) -> str:
    converted = ''
    while n > 0:
        remainder = n % base
        converted += str(remainder)
        n = n // base            
    return converted
print(convert_to_base(115, 2))
