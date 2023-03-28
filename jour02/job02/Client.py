from jour02.job00.Personne import Personne
from jour02.job01.Livre import Livre

class Client(Personne):
    collection: Livre = {}

    def __init__(self, nom: str, prenom: str):
        super().__init__(nom, prenom)

    def inventaire(self):
        return self.collection
