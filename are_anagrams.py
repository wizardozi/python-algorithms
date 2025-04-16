str1 = input('word 1: ').replace(' ','')
str2 = input('word 2: ').replace(' ','')

def char_count(word):
    char_dict = {}
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict[char] = 1
    return char_count

def are_anagrams(str1, str2):         
    if len(str1) != len(str2):
        return False    
    return char_count(str1) == char_count(str2)

print(are_anagrams(str1, str2))