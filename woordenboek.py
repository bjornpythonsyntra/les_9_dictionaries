woordenboek = {
    "apple": "appel",
    "book": "boek",
    "cat": "kat",
    "dog": "hond",
    "house": "huis",
    "water": "water",
    "sun": "zon",
    "tree": "boom",
    "car": "auto",
    "chair": "stoel"
}
zoek_woord = input("geef je woord")
if zoek_woord in woordenboek:
    print(woordenboek[zoek_woord])
else:
    print("woord niet in woordenboek")

for k,v in woordenboek.items():
    print(k,v)
