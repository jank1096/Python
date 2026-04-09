# ============================================================
#  DAS FORMEL-1-RENNANALYSE-TOOL
#  Themen: Listen, Dictionaries, Funktionen, Schleifen, Sets
# ============================================================


# ==========================
#  DIE DATEN
# ==========================

# Eine Liste die 3 Dictionaries enthält — jedes Dictionary = ein Rennen
# Jedes Rennen hat einen "ort" (String) und "zeiten" (Liste mit Zahlen)
races = [
    {"ort": "Monaco", "zeiten": [75.2, 74.8, 76.1, 74.5, 82.0]},
    {"ort": "Spa",    "zeiten": [104.2, 103.5, 105.0, 120.1]},
    {"ort": "Monza",  "zeiten": [80.5, 79.8, 79.2, 81.0]}
]


# ==========================
#  FUNKTION 1: RENNEN ANALYSIEREN
# ==========================

# Die Funktion bekommt EIN Rennen-Dictionary übergeben (z.B. races[0])
def analysiere_rennen(rennen_dict):

    # Wir holen uns den Ort und die Zeiten aus dem Dictionary
    ort    = rennen_dict["ort"]       # → z.B. "Monaco"
    zeiten = rennen_dict["zeiten"]    # → z.B. [75.2, 74.8, 76.1, 74.5, 82.0]

    # sum() addiert alle Zahlen in der Liste
    # len() zählt wie viele Zahlen drin sind
    # → zusammen ergibt das den Durchschnitt
    durchschnitt = sum(zeiten) / len(zeiten)

    # min() findet die kleinste Zahl in der Liste → beste Runde
    # max() findet die größte Zahl in der Liste → schlechteste Runde
    beste   = min(zeiten)
    schlechteste = max(zeiten)

    # Differenz zwischen bester und schlechtester Runde
    differenz = schlechteste - beste

    # Überschrift ausgeben — ort wird in den f-String eingefügt
    print(f"--- ANALYSE: {ort.upper()} ---")

    # Durchschnitt ausgeben — :.2f = immer 2 Nachkommastellen
    print(f"Durchschnitt:       {durchschnitt:.2f}s")

    # Beste und schlechteste Runde ausgeben
    print(f"Beste Runde:        {beste:.2f}s")
    print(f"Schlechteste Runde: {schlechteste:.2f}s")

    # ==========================
    #  AUSREISSER-CHECK
    # ==========================

    # enumerate() gibt uns Index UND Wert gleichzeitig
    # i = Rundennummer (0, 1, 2 ...), zeit = die eigentliche Zeit
    for i, zeit in enumerate(zeiten):

        # Wenn die Runde mehr als 10% langsamer ist als der Durchschnitt
        # durchschnitt * 1.10 = Durchschnitt + 10%
        if zeit > durchschnitt * 1.10:

            # i+1 weil enumerate bei 0 anfängt, Runden aber bei 1
            print(f"⚠️  Runde {i+1} ({zeit}s) - BOXENSTOPP ODER FEHLER")

    # Differenz ausgeben
    print(f"Differenz Best/Worst: {differenz:.2f}s")

    # Trennlinie am Ende
    print("-" * 25 + "\n")


# ==========================
#  FUNKTION 2: GLOBALES RANKING
# ==========================

# Die Funktion bekommt die komplette races-Liste
def orte_extrahieren(races_liste):

    # Wir starten mit einem leeren Set
    # Set = keine Duplikate → perfekt falls ein Ort doppelt vorkommt
    orte = set()

    # Wir gehen jedes Rennen in der Liste durch
    for rennen in races_liste:

        # .add() fügt den Ort zum Set hinzu
        # Falls der Ort schon drin ist → passiert einfach nichts
        orte.add(rennen["ort"])

    # len() zählt wie viele verschiedene Orte im Set sind
    anzahl = len(orte)

    print(f"Dieses Jahr haben wir an {anzahl} verschiedenen Orten trainiert.")
    print(f"Orte: {orte}\n")

    # Das Set zurückgeben falls wir es woanders brauchen
    return orte


# ==========================
#  AUSFÜHRUNG
# ==========================

# Wir gehen jedes Rennen in der Liste durch und analysieren es
# rennen = jeweils ein Dictionary aus der Liste
for rennen in races:
    analysiere_rennen(rennen)   # Funktion aufrufen mit dem aktuellen Rennen

# Orte extrahieren und ausgeben
orte_extrahieren(races)
