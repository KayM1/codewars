import random
from pathlib import Path

class Program:
    def __init__(self, naam):
        self.naam = naam
        self.cursussen = [] # Lijst voor meerdere cursussen
    
    def voeg_cursus_toe(self, cursus):
        self.cursussen.append(cursus)

class Cursus:
    def __init__(self, titel):
        self.titel = titel
        self.leereenheden = [] # Lijst voor meerdere leereenheden

    def voeg_leereenheid_toe(self, leereenheid):
        self.leereenheden.append(leereenheid)

class Leereenheid:
    def __init__(self, naam, cursus):
        self.naam = naam
        self.cursus = cursus # verwijzing naar de cursus
        self.vragen = [] # Lijst voor meerdere vragen

    def voeg_vraag_toe(self, vraag):
        self.vragen.append(vraag)

class Vraag:
    def __init__(self, tekst, leereenheid):
        self.tekst = tekst
        self.leereenheid = leereenheid

# Functie om tekstbestanden te lezen en de data te structureren
def lees_cursus_bestand(bestandsnaam):
    # Maak een cursus object aan op basis van de bestandsnaam
    cursus_titel = bestandsnaam.stem
    cursus = Cursus(cursus_titel)
    leereenheid = None
    with open(bestandsnaam, 'r') as f:
        for regel in f:
            regel = regel.strip()
            if regel.startswith("Leereenheid:"):
                # voeg de vorige leereenheid toe aan de cursus
                if leereenheid:
                    cursus.voeg_leereenheid_toe(leereenheid)
                # maak een nieuwe leereeneheid met verwijzing naar cursus
                leereenheid_naam = regel.replace("Leereenheid: ", "")
                leereenheid = Leereenheid(leereenheid_naam, cursus)
            elif regel.startswith("Vraag:"):
                # voeg vraag toe aan de huidige leereenheid
                if leereenheid:
                    vraag = Vraag(regel.replace("Vraag: ", ""), leereenheid)
                    leereenheid.voeg_vraag_toe(vraag)
        # Voeg de laatste leereenheid toe aan de cursus
        if leereenheid:
            cursus.voeg_leereenheid_toe(leereenheid)
    return cursus

# Willekeurige vraag kiezen
def kies_willekeurige_vraag(leereenheden):
    alle_vragen = []
    for leereenheid in leereenheden:
        alle_vragen.extend(leereenheid.vragen)
    if alle_vragen:
        return random.choice(alle_vragen)
    return None

# Functie om gebruiker te laten kiezen
def geef_cursus_keuze(cursussen):
    print("Kies een cursus:")
    for i, cursus in enumerate(cursussen):
        print(f"{i + 1}. {cursus.titel}")
    keuze = int(input("Cursus nummer: ")) - 1
    return cursussen[keuze]

def geef_leereenheid_keuze(cursus):
    print(f"Kies een leereenheid in {cursus.titel} (of alle leereenheden):")
    for i, leereenheid in enumerate(cursus.leereenheden):
        print(f"{i + 1}. {leereenheid.naam}")
    print(f"{len(cursus.leereenheden) + 1}. Alle leereenheden")
    keuze = int(input("Leereenheid nummer: ")) - 1
    if keuze == len(cursus.leereenheden):
        return cursus.leereenheden  # Alle leereenheden
    return [cursus.leereenheden[keuze]]

# Functie om automatisch alle .txt bestanden in te lezen
def lees_alle_cursusbestanden(map_pad):
    cursus_bestanden = Path(map_pad).glob("*.txt")
    cursussen = []
    for cursus_bestand in cursus_bestanden:
        cursus = lees_cursus_bestand(cursus_bestand)
        if cursus:
            cursussen.append(cursus)
    return cursussen

# Main programma
def main():
    # Programma en cursussen aanmaken
    program = Program("Informatica")
    ### cursus_bestanden = ["cursus.txt"]  # Vervang met echte bestandsnamen
    map_pad = "cursussen"
    program.cursussen = lees_alle_cursusbestanden(map_pad)

    # Gebruiker keuzes laten maken
    gekozen_cursus = geef_cursus_keuze(program.cursussen)
    gekozen_leereenheden = geef_leereenheid_keuze(gekozen_cursus)

    # Willekeurige vraag geven
    vraag = kies_willekeurige_vraag(gekozen_leereenheden)
    if vraag:
        print(f"Willekeurige vraag: {vraag.tekst} (Leereenheid: {vraag.leereenheid.naam})")
    else:
        print("Geen vragen beschikbaar.")

if __name__ == "__main__":
    main()

