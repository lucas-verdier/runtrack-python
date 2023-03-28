class Livre:

    def __init__(self, titre: str, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)
