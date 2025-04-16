# The quick brown fox jumps over the lazy dog and the quick blue hare.

sentence = input('Enter a sentence: ').lower().split()
words_dict = {}

for word in sentence:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

# Formatted output
for word, count in words_dict.items():
    print(f"{word}: {count}")
