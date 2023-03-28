from jour02.job00.Personne import Personne
from jour02.job01.Livre import Livre


class Auteur(Personne):

    def __init__(self, nom: str, prenom: str):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def lister_oeuvre(self):
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrit_un_livre(self, titre: str):
        self.oeuvre.append(Livre(titre, self))
