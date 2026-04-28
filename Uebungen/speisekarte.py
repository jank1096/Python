# ============================================================
# AUFGABE: Die smarte Restaurant-Speisekarte
# Konzepte: Funktionen, Tuple, Liste, for-Schleife, if/and
# ============================================================


def gericht_hinzufuegen(speisekarte, name, kategorie, preis):
    # 1. Drei Werte → ein Tuple packen
    neues_gericht = (name, kategorie, preis)

    # 2. Tuple ans Ende der Liste anhängen
    speisekarte.append(neues_gericht)

    print(f"Neu auf der Karte: {name}")


def gerichte_filtern(speisekarte, wunsch_kategorie, max_preis):
    print(f"\n--- Suche: {wunsch_kategorie} für maximal {max_preis} € ---")

    # Durch jedes Gericht (= Tuple) in der Liste gehen
    for gericht in speisekarte:

        # Werte aus dem Tuple per Index auslesen
        name = gericht[0]       # Index 0 = Name
        kategorie = gericht[1]  # Index 1 = Kategorie
        preis = gericht[2]      # Index 2 = Preis

        # Beide Bedingungen müssen gleichzeitig erfüllt sein:
        # → Kategorie stimmt überein UND Preis ist im Budget
        if kategorie == wunsch_kategorie and preis <= max_preis:
            print(f"- {name}: {preis} €")


# ============================================================
# TESTLÄUFE
# ============================================================

# Startliste mit 3 Gerichten
meine_speisekarte = [
    ("Cheeseburger", "Fleisch", 12.00),
    ("Gemüsesuppe", "Vegan", 6.50),
    ("Pizza Margherita", "Vegetarisch", 9.00),
]

# 1. Zwei neue Gerichte hinzufügen
gericht_hinzufuegen(meine_speisekarte, "Currywurst", "Fleisch", 7.50)
gericht_hinzufuegen(meine_speisekarte, "Salat Mista", "Vegan", 5.00)

# 2. Kunde sucht vegane Gerichte bis 7.00 €
gerichte_filtern(meine_speisekarte, "Vegan", 7.00)

# 3. Kunde sucht Fleisch-Gerichte bis 10.00 €
gerichte_filtern(meine_speisekarte, "Fleisch", 10.00)
