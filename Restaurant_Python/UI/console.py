from Controller.logik import Controller
from Repo.repository import *
from Modelle.bestellungs_modelle import *
import datetime


class Console:
    def __init__(self):

        self.repo = None
        self.controller = None

    def menu(self):
        return """
        1- Neue Bestellung registrieren
        2- Speisekarte verwalten
        3- Kundenliste verwalten
        4- Bestellungsliste zeigen
        0- Exit   
        """

    def run(self):
        while True:
            print(self.menu())
            opt = int(input('Opt='))
            if opt == 1:
                opt1 = int(input('1.Neue Kunde\n2.Aus der Kundenliste Kunde auswählen\n'))
                if opt1 == 1:
                    self.repo = CustomerRepo()
                    self.controller = Controller(self.repo)
                    id = int(input('ID: '))
                    name = input('Name:')
                    adresse = input('Adresse: ')
                    self.controller.repo.add(Kunde(id, name, adresse))
                    print('Kunde erfolgreich eingefügt. Bitte machen Sie jetzt die Bestellung')
                if opt1 == 2:
                    search_query = input("Geben Sie einen Teil des Namens oder der Adresse des Kunden ein: ")
                    self.repo = CustomerRepo()
                    self.controller = Controller(self.repo)

                    found_customers = self.controller.repo.find_customer(search_query)

                    kunden_id = None
                    kunde_bill = None
                    if found_customers:
                        print("Gefundene Kunden:")
                        for customer in found_customers:
                            print(f"ID: {customer.id}, Name: {customer.name}, Adresse: {customer.adresse}")
                            kunden_id = customer.id
                            kunde_bill = customer
                    else:
                        print("Keine Kunden gefunden.")
                        self.run()
                    bestellungs_id = int(input('ID der Bestellung:'))

                    self.repo = CookedDishRepo()
                    self.controller = Controller(self.repo)
                    speisen = self.controller.repo.load()
                    for line in speisen:
                        for gericht in line:
                            print(gericht)
                    selected_dish = input('Was haben sie gawählt zum essen:')
                    found_dish = self.controller.repo.find_dish(selected_dish)

                    gerichts_id = None
                    dish_bill = None
                    if found_dish:
                        print("Gefundenes Gericht:")
                        for dish in found_dish:
                            print(f"ID: {dish.id}, Name: {dish.name}, Preis: {dish.preis}")
                            gerichts_id = dish.id
                            dish_bill = dish
                    else:
                        print("Nicht gefunden.")
                    # self.repo = OrderRepo('orders.data')
                    # self.controller = Controller(self.repo)
                    # self.controller.repo.add(found_dish)
                    self.repo = DrinkRepo()
                    self.controller = Controller(self.repo)
                    selected_drink = input('Was haben sie gawählt zum trinken:')
                    found_drink = self.controller.repo.find_drink(selected_drink)

                    getränk_id = None
                    drink_bill = None
                    if found_drink:
                        print("Gefundenes Getränk:")
                        for drink in found_drink:
                            print(f"ID: {drink.id}, Name: {drink.name}, Preis: {drink.preis}")
                            getränk_id = drink.id
                            drink_bill = drink
                    else:
                        print("Nicht gefunden.")
                    self.repo = OrderRepo('orders.data')
                    self.controller = Controller(self.repo)
                    #self.controller.repo.add(found_drink)
                    neue_bestellung = Bestellung(bestellungs_id, kunden_id, gerichts_id, getränk_id)
                    self.controller.repo.add(neue_bestellung)
                    bill = self.controller.repo.generate_bill(dish_bill, drink_bill, kunde_bill)
                    print(bill)
                    ora_actuala = datetime.datetime.now().time()
                    ziua_actuala = datetime.date.today()
                    print(f'Bestellung wurde erfolgrein um {ora_actuala} Uhr hingefügt')
                    print(f'Die voraussichtliche Lieferdatum ist {ziua_actuala}')
            if opt == 2:
                choice = int(input('Was möchen Sie machen:\n1.Gericht oder Getränk hinzufügen\n'
                                   '2.Speisekarte anzeigen\n3.Speisekarte aktualisieren\n4.Gericht löschen\n'))
                if choice == 1:
                    choice = int(input('Was möchen Sie hinzufügen?:\n1.Gericht \n2.Getränk\n'))
                    if choice == 1:
                        self.repo = CookedDishRepo()
                        self.controller = Controller(self.repo)
                        name = input('Name:')
                        portionsgröße = input('Portionsgröße in Gramm: ')
                        preis = int(input('Preis in Euro: '))
                        zubereitungszeit = int(input('Zubereitungszeit in Minuten: '))
                        id = int(input('ID: '))
                        self.controller.add_neues_gericht(id, portionsgröße, preis, name, zubereitungszeit)
                        print('Speise wurde erfolgrein hingefügt')
                    if choice == 2:
                        self.repo = DrinkRepo()
                        self.controller = Controller(self.repo)
                        name = input('Name:')
                        preis = int(input('Preis in Euro: '))
                        portionsgröße = input('Größe in Liter: ')
                        alkoholgehalt = int(input('Alkoholgehalt in %: '))
                        id = int(input('ID: '))
                        self.controller.add_neues_getränk(id, portionsgröße, preis, name, alkoholgehalt)
                        print('Speise wurde erfolgrein hingefügt')
                if choice == 2:
                    self.repo = CookedDishRepo()
                    self.controller = Controller(self.repo)
                    speisen = self.controller.repo.load()
                    for line in speisen:
                        for gericht in line:
                            print(gericht)

                if choice == 3:
                    opt3 = int(input('Was möchten Sie aktualisieren?:\n1.Gericht\n2.Getränk\n'))
                    if opt3 == 1:

                        self.repo = CookedDishRepo()
                        self.controller = Controller(self.repo)
                        selected_dish = input('Welches Gericht möchten Sie aktualisieren:')
                        found_dishes = self.controller.repo.find_dish(selected_dish)
                        speise_actualizat = None
                        if found_dishes:
                            print("Gefundenes Gericht:")
                            for dish in found_dishes:
                                print(f"ID: {dish.id}, Name: {dish.name}, Preis: {dish.preis} ")
                                speise_actualizat = [dish]
                        else:
                            print("Keines Gericht gefunden.")
                            self.run()

                        new_name = input('Neue Name:')
                        new_id = input('Neues id:')
                        new_portionsgröße = input('Neue Portionsgröße:')
                        new_preis = input('Neues Preis:')
                        new_time = input('Neue Zubereitungszeit: ')
                        print('Getränk wurde aktualisiert')
                        self.controller.repo.aktualisieren_dish(new_id, new_portionsgröße, new_preis, new_name,
                                                                new_time,
                                                                speise_actualizat)

                    if opt3 == 2:
                        drink_actualizat = None
                        found_drink = None
                        self.repo = DrinkRepo()
                        self.controller = Controller(self.repo)
                        selected_drink = input('Welches Getränk möchten Sie aktualisieren:')
                        found_drink = self.controller.repo.find_drink(selected_drink)

                        if found_drink:
                            print("Gefundenes Getränk:")
                            for drink in found_drink:
                                print(f"ID: {drink.id}, Name: {drink.name}, Preis: {drink.preis} ")
                                drink_actualizat = [drink]
                        else:
                            print("Keines Getränk gefunden.")
                            self.run()

                        new_name = input('Neue Name:')
                        new_id = input('Neues id:')
                        new_portionsgröße = input('Neue Portionsgröße:')
                        new_preis = input('Neues Preis:')
                        new_alkoholgehalt = input('Neues Alkoholgehalt: ')
                        print('Getränk wurde aktualisiert')
                        self.controller.repo.aktualisieren_drink(new_id, new_portionsgröße, new_preis, new_name,
                                                                 new_alkoholgehalt, drink_actualizat)

                if choice == 4:
                    opt4 = int(input('Was möchten Sie löschen?:\n1.Gericht\n2.Getränk\n'))
                    if opt4 == 1:
                        self.repo = CookedDishRepo()
                        self.controller = Controller(self.repo)
                        selected_dish_delete = input('Welches Gericht möchten Sie löschen:')
                        found_dish = self.controller.repo.find_dish(selected_dish_delete)

                        if found_dish:
                            print("Gefundenes Gericht:")
                            for dish in found_dish:
                                print(
                                    f"ID: {dish.id}, Name: {dish.name}, Preis: {dish.preis} wurde erfolgreich gelöscht")
                            self.controller.repo.delete(found_dish)
                        else:
                            print('Kein Gericht gefunden')
                    if opt4 == 2:
                        self.repo = DrinkRepo()
                        self.controller = Controller(self.repo)
                        selected_drink_delete = input('Welches Getränk möchten Sie löschen:')
                        found_drink = self.controller.repo.find_drink(selected_drink_delete)

                        if found_drink:
                            print("Gefundenes Getränk:")
                            self.controller.repo.delete(found_drink)
                            for drink in found_drink:
                                print(
                                    f"ID: {drink.id}, Name: {drink.name}, Preis: {drink.preis} wurde erfolgreich gelöscht")

                        else:
                            print('Kein Getränk gefunden')
            if opt == 3:
                self.repo = CustomerRepo()
                self.controller = Controller(self.repo)
                choice = int(input('Was möchen Sie machen:\n1.Kunde hinzufügen\n'
                                   '2.Kundeliste anzeigen\n3.Kundeliste aktualisieren\n4.Kunde löschen\n'))

                if choice == 1:
                    id = int(input('ID: '))
                    name = input('Name:')
                    adresse = input('Adresse: ')
                    self.controller.repo.add(Kunde(id, name, adresse))
                    # self.controller.add_neue_kunde(id,name,adresse)
                    print('Kunde wurde erfolgrein hingefügt')
                if choice == 2:
                    try:
                        # kunden=self.controller.anzeigen_kunden()
                        # for kunde in kunden:
                        #     print(kunde)

                        kunden = self.controller.repo.load()
                        # for line in kunden:
                        #     print(*kunden)
                        # print(kunden)
                        # print('')
                        for line in kunden:
                            for kunde in line:
                                print(kunde)
                    except FileNotFoundError:
                        print("Bitte zuerst Kunde hinfugen")
                        self.run()

                if choice == 3:
                    try:
                        kunde_actualizat = None
                        nume_actualizat = input('Wen möchten Sie aktualisieren?: ')
                        found_customers = self.controller.repo.find_customer(nume_actualizat)
                        if found_customers:
                            print("Gefundene Kunden:")
                            for customer in found_customers:
                                print(f"ID: {customer.id}, Name: {customer.name}, Adresse: {customer.adresse}\n")
                                kunde_actualizat = customer
                        else:
                            print("Keine Kunden gefunden.")
                            self.run()

                        new_id = input('Neues id:')
                        new_name = input('Neue Name:')
                        new_adress = input('Neue Adresse:')
                        self.controller.repo.aktualisieren(new_name, new_id, new_adress, kunde_actualizat)
                    except FileNotFoundError:
                        print("Bitte zuerst Kunde hinfugen")
                if choice == 4:
                    try:
                        nume_de_sters = input("Geben Sie einen Teil des Namens oder der Adresse des Kunden ein: ")
                        found_customers = self.controller.repo.find_customer(nume_de_sters)
                        if found_customers:
                            print("Gefundene Kunden:")
                            for customer in found_customers:
                                print(
                                    f"ID: {customer.id}, Name: {customer.name}, Adresse: {customer.adresse} wurde erfolgreich gelöscht\n")
                            self.controller.repo.delete(found_customers)
                        else:
                            print("Keine Kunden gefunden.")
                            self.run()
                    except FileNotFoundError:
                        print("Bitte zuerst Kunde hinfugen")

            if opt == 4:
                try:
                    self.repo = OrderRepo('orders.data')
                    self.controller = Controller(self.repo)
                    orders = self.controller.repo.load()
                    for line in orders:
                        for order in line:
                            print(order)
                except FileNotFoundError:
                    print("Bitte zuerst Bestellung hinfügen")
                    self.run()

            if opt == 0:
                break
