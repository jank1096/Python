races = [
    {"ort": "Monaco", "zeiten": [75.2, 74.8, 76.1, 74.5, 82.0]},
    {"ort": "Spa",    "zeiten": [104.2, 103.5, 105.0, 120.1]},
    {"ort": "Monza",  "zeiten": [80.5, 79.8, 79.2, 81.0]}
]

#1: RENNEN ANALYSIEREN
def analysiere_rennen(rennen_dict):
    ort    = rennen_dict["ort"]
    zeiten = rennen_dict["zeiten"]
    durchschnitt = sum(zeiten) / len(zeiten)
    beste   = min(zeiten)
    schlechteste = max(zeiten)
    differenz = schlechteste - beste

    print(f"ANALYSE: {ort.upper()} ---")
    print(f"Durchschnitt:       {durchschnitt:.2f}s")
    print(f"Beste Runde:        {beste:.2f}s")
    print(f"Schlechteste Runde: {schlechteste:.2f}s")

    for i, zeit in enumerate(zeiten):
        if zeit > durchschnitt * 1.10:
            print(f"Runde {i+1} ({zeit}s) - BOXENSTOPP ODER FEHLER")
    print(f"Differenz Best/Worst: {differenz:.2f}s")
    print("-" * 25 + "\n")

#2: GLOBALES RANKING
def orte_extrahieren(races_liste):
    orte = set()

    for rennen in races_liste:
        orte.add(rennen["ort"])
    anzahl = len(orte)

    print(f"Dieses Jahr haben wir an {anzahl} verschiedenen Orten trainiert.")
    print(f"Orte: {orte}\n")
    return orte

# run
for rennen in races:
    analysiere_rennen(rennen)
orte_extrahieren(races)
