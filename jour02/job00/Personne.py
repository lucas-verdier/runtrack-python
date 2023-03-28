class Personne:

    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        print(self.nom)
        print(self.prenom)

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom: str):
        self.prenom = prenom
