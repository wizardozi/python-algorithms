def defangIPaddr(address: str) -> str:
    result = []
    for char in address:
        if char == '.':
            result.append('[.]')
            continue
        result.append(char)
    return ''.join(result)

address = '1.1.1.1'

print(defangIPaddr(address))