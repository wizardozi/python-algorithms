
def score_of_String(s):
    result, i, j = 0, 0, 1
    s_list = list(s)
    print(s_list)
    while j < len(s_list):
        result += abs(ord(s_list[i]) - ord(s_list[j]))
        i += 1
        j += 1
    return result
s = 'hello'
print(score_of_String(s))
        
        