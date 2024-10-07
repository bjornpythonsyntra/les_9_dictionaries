from tabulate import tabulate

# Dezelfde data in een dictionary
data = {
    #0  1
    1: {"naam": "Jan Peeters", "leeftijd": 28, "woonplaats": "Hasselt"},
    2: {"naam": "Anke Jansen", "leeftijd": 34, "woonplaats": "Genk"},
    3: {"naam": "Tom Willems", "leeftijd": 22, "woonplaats": "Maasmechelen"},
    4: {"naam": "Sara Dubois", "leeftijd": 29, "woonplaats": "Sint-Truiden"},
    5: {"naam": "Pieter Martens", "leeftijd": 45, "woonplaats": "Tongeren"},
    6: {"naam": "Liesbeth Verhoeven", "leeftijd": 31, "woonplaats": "Bilzen"}
}


# Functie om de data op naam te sorteren
def sorteer_op_naam(data):
    # Gebruik sorted() om te sorteren op de waarde van de 'naam'-sleutel
    sorteer = input("op welk veld wil je sorteren")
    gesorteerde_data = dict(sorted(data.items(), key=lambda item: item[1][sorteer]))
    return gesorteerde_data


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

# Vraag de gebruiker of hij/zij de data wil sorteren
actie = input("\nWil je de data sorteren op naam? (ja/nee): ").strip().lower()

# Als de gebruiker wil sorteren, sorteer de data op naam
if actie == 'ja':
    data = sorteer_op_naam(data)

# Toon de (eventueel gesorteerde) data
print("\nData na sortering:")
toon_data_in_tabel(data)
