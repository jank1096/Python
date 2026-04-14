import re

products   = [" t-shirt_RED_m ", "HOODIE_blue_l", " socken_GREEN_s ", "JACKE_black_xl"]
prices_raw = ["Preis: 19.99 EUR", "Price: 29.50 USD", "Kosten: 5.00 EUR", "Price: 89.00 EUR"]


#1: Bereinigen
sauber = [(p.strip().lower(), r) for p, r in zip(products, prices_raw)]
print("Bereinigte Produkte:")
for produkt, preis_raw in sauber:
    print(f"  {produkt} | {preis_raw}")


#2: Regex Extrahieren
def extrahiere_preis(preis_raw: str) -> float:
    treffer = re.search(r"\d+\.\d+", preis_raw)
    if treffer:
        return float(treffer.group())
    return 0.0                          


#3: Match Case
def kategorisiere(produkt: str) -> str:
    typ = produkt.split("_")[0]    
    match typ:
        case "t-shirt" | "hoodie":
            return "Oberteil"
        case "socken":
            return "Accessoires"
        case _:         
            return "Sonstiges"


#4: Dict. Comprehesnsion
katalog = {
    produkt: extrahiere_preis(preis_raw)
    for produkt, preis_raw in sauber
}

print("\nFinaler Katalog:")
for produkt, preis in katalog.items():
    kategorie = kategorisiere(produkt)
    print(f"  {produkt:<20} {preis:.2f} € | Kategorie: {kategorie}")



#5: WHILE-LOOP
print("PREISABFRAGE:")
print("Produktnamen eingeben oder 'exit' zum Beenden:")

while True:
    eingabe = input("Produkt: ").strip().lower()
    if eingabe == "exit":
        break                 

    if eingabe in katalog:
        preis = katalog[eingabe]
        print(f"  {eingabe} kostet {preis:.2f} €")
    else:
        print(f"  '{eingabe}' nicht gefunden.")
        print(f"  Verfügbare Produkte: {list(katalog.keys())}")
