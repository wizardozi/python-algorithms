anagrams =  ["listen", "silent", "enlist", "rat", "tar", "art"]
group_anagrams = {}

for word in anagrams:
    word_sorted = ''.join(sorted(word))        
    if word_sorted in group_anagrams:
        group_anagrams[word_sorted].append(word)
    else:
        group_anagrams[word_sorted] = [word]
    
grouped_anagrams = list(group_anagrams.values())    
print(anagrams) 
print(grouped_anagrams)   

