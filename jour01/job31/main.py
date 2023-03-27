word = input("Entrez votre mot : ")
n = len(word)

letters = list(word)

i = n - 1
while i > 0 and letters[i-1] >= letters[i]:
    i -= 1

else:
    j = n - 1
    while letters[j] <= letters[i-1]:
        j -= 1
    letters[i-1], letters[j] = letters[j], letters[i-1]

    letters[i:] = letters[i:][::-1]

    nouveau_mot = ''.join(letters)
    print("Le nouveau mot est : ", nouveau_mot)

