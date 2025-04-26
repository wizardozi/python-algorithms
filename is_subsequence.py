def is_subsequence(s: str, t: str) -> bool:
    '''
    Given two strings s and t, return True if s is a subsequence of t.
    A subsequence is formed by deleting zero or more characters without changing the order.
    '''
    s_pointer, t_pointer = 0, 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        t_pointer += 1

    return s_pointer == len(s)


print(is_subsequence("abc", "ahbgdc"))     # True
print(is_subsequence("axc", "ahbgdc"))     # False
print(is_subsequence("", "ahbgdc"))        # True  (empty string is always a subsequence)
print(is_subsequence("abc", ""))           # False
print(is_subsequence("aaa", "aabbaaa"))    # True
print(is_subsequence("aaa", "aabbaa"))     # True
