import re 

email = input('Enter and email address: ')

before_symbol = re.findall('^(.*?)@', email)
for word in before_symbol:
    print(word)