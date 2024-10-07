persoon = {"naam":"Bert","leeftijd":25,"stad":"Genk"}
persoon2 = {"naam":"Bart","leeftijd":28}
persoon3 = {"naam":"Bartje","leeftijd":20}
persoon3["naam"] = "Piet"
persoon3.update({"naam":"Bartjee","functie":"Developer","getrouwd":"Ja"})
lijst_personen = [persoon,persoon2,persoon3]
#headers uit de keys halen van persoon
for header in persoon.keys():
    print(header,end="\t")
print("") # nieuwe regel
#elke persoon in de lijst doorlopen
for pers in lijst_personen:
    #elke waarde in pers uitlezen
    for item in pers.values():
       print(item,end="\t")
    print("")

