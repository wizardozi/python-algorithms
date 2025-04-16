def is_palindrome(s):    
    clean_s = ''.join(char for char in s.lower() if char.isalpha())
    i,j = 0, len(clean_s) - 1
    while i < j:
        if clean_s[i] != clean_s[j]:
            return False
        i += 1
        j -= 1

    return True

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("RaceCar"))                         # True
print(is_palindrome("hello!"))                          # False
print(is_palindrome(""))                                # True
print(is_palindrome("Able was I ere I saw Elba"))       # True