sentence = input('Enter a sentence: ').replace(' ', '')
char_dict = {}

for char in sentence: 
    if char in char_dict:
        char_dict[char] += 1
    else: 
        char_dict[char] = 1



# Formatted output
for char, count in sorted(char_dict.items()):
    print(f"{char}: {count}")