from Modelle.bestellungs_modelle import *


class Controller:
    def __init__(self, repo):
        self.repo = repo

    def suchen(self):
        pass

    # def kunden_löschen(self,nume_de_sters):
    #     kunden=self.repo.load()
    #     sterge_kunden=list(filter(lambda kunde: kunde.nume == nume_de_sters, kunden))
    #     for kunde in sterge_kunden:
    #         self.repo.delete(kunde)

    # def add_neue_kunde(self, id, name,adresse):
    #     neue_kunde=Kunde(id,name,adresse)
    #     self.repo.add(neue_kunde)

    # def anzeigen_kunden(self):
    #     self.repo.load()
    #     # for kunde in self.repo.kunden:
    #     #     print(kunde)
    #     return [kunde for kunde in self.repo.kunden]

    def add_neues_gericht(self, id, portionsgröße, preis, name, zubereitungszeit):
        neues_gericht = Gekochtergericht(id, portionsgröße, preis, name, zubereitungszeit)
        self.repo.add(neues_gericht)

    # def speisekarte_anzeigen(self):
    #     self.repo.load()
    #     return [speise for speise in self.repo.gericht]

    def add_neues_getränk(self, portionsgröße, preis, name, alkoholgehalt, id):
        neues_getränk = Getränk(portionsgröße, preis, name, alkoholgehalt, id)
        self.repo.add(neues_getränk)
