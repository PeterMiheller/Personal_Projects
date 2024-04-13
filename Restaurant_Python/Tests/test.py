from Repo.repository import *
from Controller.logik import *


class Tests:
    def test_add_cooked_dish(self):
        # Presupunem că avem un Controller și un Repository configurat
        repo = CookedDishRepo()
        controller = Controller(repo)

        # Adăugăm un fel de mâncare nou folosind metoda add_neues_gericht
        controller.add_neues_gericht(1, '250g', 15, 'Nudeln', 30)

        # Verificăm dacă felul de mâncare a fost adăugat corect în repository
        dishes = repo.load()
        new_dish = dishes[-1]  # Luăm ultimul fel de mâncare adăugat
        for el in new_dish:
            # Verificăm dacă atribuțiile noului fel de mâncare corespund valorilor așteptate
            assert el.id == 1
            assert el.portionsgröße == '250g'
            assert el.preis == 15
            assert el.name == 'Nudeln'
            assert el.zubereitungszeit == 30

    def test_find_customer_name(self):
        repo = CustomerRepo()
        controller = Controller(repo)

        controller.repo.add([Kunde(3, "Alice Johnson", "789 Oak Street")])
        search = 'ali'
        customer = controller.repo.find_customer(search)
        for el in customer:
            assert el.id == 3
            assert el.adresse == '789 Oak Street'
            assert el.name == 'Alice Johnson'

    def test_find_customer_adress(self):
        repo = CustomerRepo()
        controller = Controller(repo)

        controller.repo.add([Kunde(5, "Mars Oktavian", "Alserstraße")])
        search = 'als'
        customer = controller.repo.find_customer(search)
        for el in customer:
            assert el.id == 5
            assert el.adresse == 'Alserstraße'
            assert el.name == 'Mars Oktavian'

    def test_aktualisierung(self):
        repo = CustomerRepo()
        controller = Controller(repo)

        controller.repo.add([Kunde(6, "Marina", "Leutasch")])
        search = 'marina'
        customer = controller.repo.find_customer(search)
        new_id = 6
        new_name = 'Octavian'
        new_adress = 'Innsbruck'
        controller.repo.aktualisieren(new_name, new_id, new_adress, customer)
        search2 = 'octa'
        liste = controller.repo.find_customer(search2)
        for el in liste:
            assert el.id == 6
            assert el.adresse == 'Innsbruck'
            assert el.name == 'Octavian'
