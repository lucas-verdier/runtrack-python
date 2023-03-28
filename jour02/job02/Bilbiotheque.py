from jour02.job01.Auteur import Auteur
from jour02.job02.Client import Client
from jour02.job01.Livre import Livre


class Bilbiotheque:

    def __init__(self, nom: str, catalogue: dict = { Livre: int }):
        self.nom = nom
        self.catalogue = catalogue

    def acheter_livre(self, auteur: Auteur, nom_livre: Livre, quantite: int):
        if nom_livre in auteur.oeuvre:
            self.catalogue[nom_livre] += quantite

    def inventaire(self):
        for livre in self.catalogue:
            print("___________________________________")
            print("Livre :", livre.titre)
            print("quantité :", self.catalogue[livre])

    def louer(self, client: Client, titre_livre: str):
        if self.catalogue[titre_livre] > 0:
            client.collection[titre_livre] = 1
            self.catalogue[titre_livre] -= 1

    def rendre_livres(self, client):
        for livre in client.collection:
            self.catalogue[livre] += 1
        client.collection = {}


auteur1 = Auteur("Ecrivain", "Jean")
auteur2 = Auteur("Palmade", "Pierre")
auteur1.ecrit_un_livre("LIVRE 1")
auteur1.ecrit_un_livre("LIVRE 2")
auteur2.ecrit_un_livre("Soirée entre amis")

book_shop = Bilbiotheque("Alcazar", {auteur1.oeuvre[0]: 5, auteur1.oeuvre[1]: 3, auteur2.oeuvre[0]: 55})

book_shop.acheter_livre(auteur1, auteur1.oeuvre[1], 7)

client1 = Client("Pigeon", "Timothé")
book_shop.louer(client1, auteur2.oeuvre[0])
book_shop.louer(client1, auteur1.oeuvre[1])
book_shop.rendre_livres(client1)

book_shop.inventaire()
