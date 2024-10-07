persoon = {"naam":"Bert","leeftijd":25}
persoon2 = {"naam":"Bart","leeftijd":28}

persoon["plaats"] = "Genk"
print(len(persoon))
print(persoon.items())

for k,v in persoon2.items():
    print(k,v)

