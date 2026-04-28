# ============================================================
# AUFGABE: Notenrechner
# Konzepte: Funktionen, Parameter, return, Standardwerte, *args
# ============================================================
#
# Ziel: Ein Programm das Noten verwaltet und auswertet.
# Jede Aufgabe ist eine eigene Funktion — kein doppelter Code!
# ============================================================


# ============================================================
# SCHRITT 1: Einzelne Note bewerten
# ============================================================

def note_bewerten(note):
    """Gibt die Bezeichnung für eine Note zurück."""
    if note == 1:
        return "Sehr gut"
    elif note == 2:
        return "Gut"
    elif note == 3:
        return "Befriedigend"
    elif note == 4:
        return "Ausreichend"
    elif note == 5:
        return "Mangelhaft"
    elif note == 6:
        return "Ungenügend"
    else:
        return "Ungültige Note"

print(note_bewerten(1))     # → Sehr gut
print(note_bewerten(4))     # → Ausreichend
print(note_bewerten(7))     # → Ungültige Note


# ============================================================
# SCHRITT 2: Durchschnitt aus beliebig vielen Noten
# ============================================================

def durchschnitt(*noten):
    """Berechnet den Notendurchschnitt. Gibt None zurück wenn keine Noten übergeben."""
    if not noten:       # leeres Tuple → keine Noten
        return None

    return sum(noten) / len(noten)

print(f"\nDurchschnitt: {durchschnitt(1, 2, 3, 2, 1):.2f}")    # → 1.80
print(f"Durchschnitt: {durchschnitt(3):.2f}")                  # → 3.00
print(f"Keine Noten:  {durchschnitt()}")                        # → None


# ============================================================
# SCHRITT 3: Notenliste analysieren
# ============================================================

def analyse(noten, name="Schüler"):
    """Analysiert eine Notenliste und gibt eine Zusammenfassung aus."""
    if not noten:
        print(f"{name}: Keine Noten vorhanden.")
        return

    schnitt = sum(noten) / len(noten)

    print(f"\n--- {name} ---")
    print(f"Noten:        {noten}")
    print(f"Anzahl:       {len(noten)}")
    print(f"Beste Note:   {min(noten)}")
    print(f"Schlechteste: {max(noten)}")
    print(f"Durchschnitt: {schnitt:.2f} ({note_bewerten(round(schnitt))})")

    # Bestanden wenn Durchschnitt ≤ 4.0
    bestanden = schnitt <= 4.0
    print(f"Status:       {'Bestanden' if bestanden else 'Nicht bestanden'}")

analyse([1, 2, 1, 3, 2], "Jan")
analyse([3, 4, 5, 4, 3], "Anna")
analyse([], "Tom")


# ============================================================
# SCHRITT 4: Note verbessern (Standardwert)
# ============================================================

def note_verbessern(note, schritte=1):
    """Verbessert eine Note um eine bestimmte Anzahl Schritte (Standard: 1)."""
    neue_note = note - schritte     # kleinere Zahl = bessere Note

    if neue_note < 1:
        print(f"Note {note} kann nicht weiter verbessert werden.")
        return 1

    print(f"Note {note} → {neue_note} ({note_bewerten(neue_note)})")
    return neue_note

print()
note_verbessern(3)          # → 3 → 2
note_verbessern(3, 2)       # → 3 → 1
note_verbessern(1)          # → kann nicht weiter verbessert werden


# ============================================================
# SCHRITT 5: Klasse mit mehreren Schülern auswerten
# ============================================================

def klassen_auswertung(klasse):
    """
    Wertet ein Dictionary mit Schüler-Noten aus.

    Parameter:
        klasse (dict): {"Name": [noten...], ...}
    """
    print("\n=== Klassenauswertung ===")

    alle_schnitte = []

    for name, noten in klasse.items():
        schnitt = sum(noten) / len(noten)
        alle_schnitte.append((name, schnitt))
        print(f"  {name}: {schnitt:.2f}")

    # Klassenbester
    bester = min(alle_schnitte, key=lambda x: x[1])
    klassen_schnitt = sum(s for _, s in alle_schnitte) / len(alle_schnitte)

    print(f"\nKlassenbester:   {bester[0]} ({bester[1]:.2f})")
    print(f"Klassenschnitt:  {klassen_schnitt:.2f}")


meine_klasse = {
    "Jan":  [1, 2, 1, 2, 1],
    "Anna": [2, 3, 2, 3, 2],
    "Tom":  [3, 4, 3, 4, 3],
    "Sara": [1, 1, 2, 1, 1],
}

klassen_auswertung(meine_klasse)
