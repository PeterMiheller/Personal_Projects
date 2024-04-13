from functools import reduce


class Identifizierbar():
    def __init__(self, id: int):
        self.id = id


class Gericht(Identifizierbar):
    def __init__(self, id: int, portionsgröße: str, preis: int):
        Identifizierbar.__init__(self, id)
        self.portionsgröße = portionsgröße
        self.preis = preis


class Gekochtergericht(Gericht):
    def __init__(self, id: int, portionsgröße: str, preis: int, name: str, zubereitungszeit: int):
        Gericht.__init__(self, id, portionsgröße, preis)
        self.name = name
        self.zubereitungszeit = zubereitungszeit

    def __str__(self):
        return f'{self.name} mit: ID:{self.id} Portionsgröße:{self.portionsgröße}, Preis:{self.preis}, Zubereitungszeit:{self.zubereitungszeit}'

    def __eq__(self, other):
        return (self.id == other.id and self.portionsgröße == other.portionsgröße and self.preis == other.preis
                and self.name == other.name and self.zubereitungszeit == other.zubereitungszeit)


class Getränk(Gericht):
    def __init__(self, id: int, portionsgröße: str, preis: int, name: str, alkoholgehalt: str):
        Gericht.__init__(self, id, portionsgröße, preis)
        self.name = name
        self.alkoholgehalt = alkoholgehalt

    def __str__(self):
        return f'{self.name} mit: ID:{self.id} Größe:{self.portionsgröße}, Preis:{self.preis}, Alkoholgehalt:{self.alkoholgehalt}'

    def __eq__(self, other):
        return (self.id == other.id and self.portionsgröße == other.portionsgröße and self.preis == other.preis
                and self.name == other.name and self.alkoholgehalt == other.alkoholgehalt)


class Kunde(Identifizierbar):
    def __init__(self, id: int, name: str, adresse: str):
        Identifizierbar.__init__(self, id)
        self.name = name
        self.adresse = adresse

    def __repr__(self):
        return f'Id:{self.id}, Name:{self.name}, Adresse:{self.adresse}'

    def __eq__(self, other):
        return self.id == other[0].id and self.name == other[0].name and self.adresse == other[0].adresse


class Bestellung(Identifizierbar):
    def __init__(self, id: int, kunden_id: int, gerichts_id: list, getränk_id: list):
        Identifizierbar.__init__(self, id)
        self.kunden_id = kunden_id
        self.gerichts_id = gerichts_id
        self.getränk_id = getränk_id
        self.gesamtkosten = 0


    def calculate_total_cost(self, gerichte, getränke):
        gericht_kosten = [gericht.price for gericht in gerichte if gericht.id in self.gerichts_id_liste]
        getränk_kosten = [getränk.price for getränk in getränke if getränk.id in self.getränk_id_liste]
        self.gesamtkosten = sum(gericht_kosten) + sum(getränk_kosten)

    def generate_bill(self, gerichte, getränke, kunden):
        customer_name = ""
        customer_address = ""

        for customer in kunden:
            if customer.id == self.kunden_id:
                customer_name = self.kunde.name
                customer_address = self.kunde.address
                break

        ordered_dishes = [gericht for gericht in gerichte if gericht.id in self.gerichts_id_liste]
        ordered_drinks = [getränk for getränk in getränke if getränk.id in self.getränk_id_liste]

        rechnung = f'===== Rechnung =====\nKunde: {customer_name}\nAdresse: {customer_address}\nBestellte Gerichte: \n'
        for gericht in ordered_dishes:
            rechnung += f"{gericht.id}: {gericht.portionsgröße} - {gericht.preis}\n"
        rechnung += "\nBestellte Getränke:\n"
        for getränk in ordered_drinks:
            rechnung += f"{getränk.id}: {getränk.portionsgröße} - {getränk.preis}\n"
        rechnung += f'\nGesamtkosten:{self.gesamtkosten}\n'
        return rechnung

    def __str__(self):
        return f'BestellungsID: {self.id}, KundenID: {self.kunden_id}, GerichtsID: {self.gerichts_id}, GetränksId: {self.getränk_id}'
