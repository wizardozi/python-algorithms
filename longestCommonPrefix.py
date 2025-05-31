def longestCommonPrefix(strs):
    prefix = ""
    if len(strs) == 1:
        return strs[0]
    
    end_loop = False
    s = sorted(strs, key=len)
    for i in range(len(s[0])):
        if end_loop:
            break
        c1 = s[0][i]
        c2 = ''
        for j in range(1, len(s)):
            c2 = s[j][i]            
            if c1 != c2:
                end_loop = True
                break
        if c1 == c2:
            prefix += c1
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))

strs = ["a"]
print(longestCommonPrefix(strs))

strs = ["cir","car"]
print(longestCommonPrefix(strs))

strs = ["aa","aa"]
print(longestCommonPrefix(strs))