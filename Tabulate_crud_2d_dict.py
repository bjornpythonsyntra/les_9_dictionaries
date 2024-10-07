from tabulate import tabulate

# Dezelfde data in een dictionary
data = {
    1: {"naam": "Jan Peeters", "leeftijd": 28, "woonplaats": "Hasselt"},
    2: {"naam": "Anke Jansen", "leeftijd": 34, "woonplaats": "Genk"},
    3: {"naam": "Tom Willems", "leeftijd": 22, "woonplaats": "Maasmechelen"},
    4: {"naam": "Sara Dubois", "leeftijd": 29, "woonplaats": "Sint-Truiden"},
    5: {"naam": "Pieter Martens", "leeftijd": 45, "woonplaats": "Tongeren"},
    6: {"naam": "Liesbeth Verhoeven", "leeftijd": 31, "woonplaats": "Bilzen"}
}


# Functie om nieuwe gegevens toe te voegen op basis van gebruikersinput
def voeg_nieuwe_rij_toe(data):
    # Vraag de gebruiker om input voor naam, leeftijd en woonplaats
    naam = input("Voer de naam in: ")
    leeftijd = int(input("Voer de leeftijd in: "))
    woonplaats = input("Voer de woonplaats in: ")

    # Bepaal het volgende ID (het laatste ID + 1)
    nieuw_id = max(data.keys()) + 1

    # Voeg de nieuwe gegevens toe aan de dictionary
    data[nieuw_id] = {"naam": naam, "leeftijd": leeftijd, "woonplaats": woonplaats}


# Functie om een rij te verwijderen op basis van ID
def verwijder_rij_op_id(data):
    try:
        # Vraag de gebruiker om het ID dat verwijderd moet worden
        id_verwijderen = int(input("Voer het ID in van de persoon die je wilt verwijderen: "))

        # Controleer of het ID in de dictionary zit
        if id_verwijderen in data:
            del data[id_verwijderen]  # Verwijder de rij
            print(f"Rij met ID {id_verwijderen} succesvol verwijderd.")
        else:
            print(f"ID {id_verwijderen} bestaat niet in de data.")

    except ValueError:
        print("Ongeldige invoer! Voer een geldig ID-nummer in.")


# Functie om de dictionary in tabelvorm te tonen
def toon_data_in_tabel(data):
    data_list = []
    for key, info in data.items():
        row = [key]  # Voeg de ID toe
        for k, v in info.items():
            row.append(v)
        data_list.append(row)

    # Toon de data in een tabel
    headers = ["ID", "Naam", "Leeftijd", "Woonplaats"]
    print(tabulate(data_list, headers=headers, tablefmt="grid"))


# Toon de huidige data
print("Huidige data:")
toon_data_in_tabel(data)

# Vraag de gebruiker of hij een rij wil toevoegen of verwijderen
actie = input("\nWil je een rij toevoegen of verwijderen? (toevoegen/verwijderen): ").strip().lower()

if actie == 'toevoegen':
    voeg_nieuwe_rij_toe(data)
elif actie == 'verwijderen':
    verwijder_rij_op_id(data)
else:
    print("Ongeldige keuze!")

# Toon de bijgewerkte data
print("\nBijgewerkte data:")
toon_data_in_tabel(data)
