def first_unique_char(s):
    seen = {}
    for c in s:
            seen[c] = seen.get(c, 0) + 1
    for c in s:
        if seen[c] == 1:
            return c
    return None

# Test cases
print(first_unique_char("leetcode"))     # 'l'
print(first_unique_char("aabbcc"))       # None
print(first_unique_char("aabbcce"))      # 'e'
print(first_unique_char(""))             # None
print(first_unique_char("abcabcddx"))    # 'x'

def first_unique_index(s):
    seen = {}
    for c in s:
            seen[c] = seen.get(c, 0) + 1
    for i, c in enumerate(s):
        if seen[c] == 1:
            return i
    return -1

print(first_unique_index("leetcode"))       # → 0   ('l')
print(first_unique_index("aabbcc"))         # → -1
print(first_unique_index("aabbcce"))        # → 6   ('e')
print(first_unique_index(""))               # → -1
print(first_unique_index("abcabcddx"))      # → 8   ('x')