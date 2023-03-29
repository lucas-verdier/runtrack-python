import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import string

with open('data.txt') as f:
    list_letter: list = []
    text = f.read().translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    for letter in text:
        if letter in text:
            list_letter.append(letter)

list_letter.sort()
plt.title("Nombre d'itération de lettres")
plt.hist(list_letter, color='blue', density=True, bins=26, range=(0, 26), edgecolor='white', align='left')
plt.ylabel("Pourcentage de lettres")
plt.xlabel("Lettres")
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
