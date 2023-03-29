import string

user_input = int(input("Renseigner un nombre entier : "))
count: int = 0

with open('data.txt') as f:
    text = f.read()
    text_list = text.split()
    for word in text_list:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if len(word) == user_input:
            count += 1

print(f"Il y a {count} mots qui ont une longueur de {user_input}")
