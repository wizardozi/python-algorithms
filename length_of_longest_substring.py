def length_of_longest_substring(s: str) -> int:
    temp = [] 
    result = 1 # start 1 since shortest substring >= 1
    # have two pointers so that one can iterate through the string
    # the other one can hang back and move up once the substring is broken
    # how do you count a substring? 
        # i think a nested loop that that has a dynamic start position
        # top loop just goes through the whole string
            # inside loop starts at the index of the top loop since that one is always starting at a new character
            # inside loop counts unique chars
            # breaks out when it sees a char thats already been counted
        
    # once a substring is counted 
        # check if the temp count is bigger than result count
        # if temp > result: result = temp
    for i, char in enumerate(s):        
        j = i
        if len(temp) > result:
            result = len(temp)
            temp = []
        while j < len(s):
            if s[j] in temp:
                break
            else:
                temp.append(s[j])    
    return max(len(temp), result)

s = "abcabcbb"
print(length_of_longest_substring(s)) # The answer is "abc", with the length of 3.
s = "bbbbb"
print(length_of_longest_substring(s)) # The answer is "b", with the length of 1.
s = "pwwkew"
print(length_of_longest_substring(s)) # The answer is "wke", with the length of 3.

