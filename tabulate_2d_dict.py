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

# Lege 2D-lijst maken
data_list = []

# Eerste for-lus om de dictionary keys (ID's) te doorlopen
for key, info in data.items():
    row = [key]  # Voeg de key (ID) toe aan de rij
    # Tweede for-lus om de naam, leeftijd en woonplaats toe te voegen
    for k, v in info.items():
        row.append(v)
    data_list.append(row)

# Gebruik tabulate om de data mooi weer te geven
headers = ["ID", "Naam", "Leeftijd", "Woonplaats"]
print(tabulate(data_list, headers=headers, tablefmt="pretty-grid"))
