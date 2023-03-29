import re
count: int = 0
with open('data.txt') as f:
    text = f.read()
    text_list = text.split()
    print("Mots au total:", len(text_list))
    regex = r'^[a-zA-Z0-9_\-]+$'
    for word in text_list:
        if re.search(regex, word):
            count += 1

print("Mots sans caractères spéciaux:", count)
