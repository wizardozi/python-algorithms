with open("words.txt", "r") as file:
    content = file.read()

import re
clean_content = re.sub(r'[^\w\s]', '', content)

word_dict = {}
for word in clean_content.split():
    word = word.lower()
    word_dict[word] = word_dict.get(word, 0) + 1

with open("word_count.txt", "w") as output:
    for word in sorted(word_dict):
        output.write(f"{word}: {word_dict[word]}\n")

