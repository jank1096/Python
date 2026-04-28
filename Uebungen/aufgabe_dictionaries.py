# ============================================================
# AUFGABE: Kontaktbuch
# Konzepte: Dictionaries, verschachtelte Dicts, Schleifen, Methoden
# ============================================================


# ============================================================
# SCHRITT 1: Kontaktbuch erstellen
# ============================================================

kontaktbuch = {
    "jan": {
        "name":     "Jan Koch",
        "telefon":  "0211-123456",
        "email":    "jan@mail.de",
        "alter":    20,
    },
    "anna": {
        "name":     "Anna Müller",
        "telefon":  "0211-654321",
        "email":    "anna@mail.de",
        "alter":    24,
    },
    "tom": {
        "name":     "Tom Weber",
        "telefon":  "0211-999888",
        "email":    "tom@mail.de",
        "alter":    19,
    },
}

print(f"Kontakte gespeichert: {len(kontaktbuch)}")


# ============================================================
# SCHRITT 2: Kontakt abrufen
# ============================================================

print("\n--- Kontakt abrufen ---")

# Sicherer Zugriff mit .get() — kein Fehler wenn nicht vorhanden
def kontakt_anzeigen(kuerzel):
    kontakt = kontaktbuch.get(kuerzel)

    if kontakt is None:
        print(f"'{kuerzel}' nicht gefunden.")
        return

    print(f"Name:    {kontakt['name']}")
    print(f"Telefon: {kontakt['telefon']}")
    print(f"E-Mail:  {kontakt['email']}")

kontakt_anzeigen("jan")
kontakt_anzeigen("xyz")     # nicht vorhanden → Fehlermeldung


# ============================================================
# SCHRITT 3: Kontakt hinzufügen & bearbeiten
# ============================================================

print("\n--- Kontakt hinzufügen ---")

kontaktbuch["sara"] = {
    "name":     "Sara Becker",
    "telefon":  "0211-777666",
    "email":    "sara@mail.de",
    "alter":    22,
}
print(f"Sara hinzugefügt. Jetzt {len(kontaktbuch)} Kontakte.")

# Telefonnummer aktualisieren
kontaktbuch["jan"]["telefon"] = "0211-000111"
print(f"Jans neue Nummer: {kontaktbuch['jan']['telefon']}")

# Mit update() mehrere Felder auf einmal ändern
kontaktbuch["anna"].update({"alter": 25, "email": "anna.neu@mail.de"})
print(f"Anna aktualisiert: {kontaktbuch['anna']}")


# ============================================================
# SCHRITT 4: Kontaktbuch durchsuchen
# ============================================================

print("\n--- Alle Kontakte ---")

for kuerzel, daten in kontaktbuch.items():
    print(f"[{kuerzel}] {daten['name']} | {daten['telefon']}")


# ============================================================
# SCHRITT 5: Filtern nach Kriterien
# ============================================================

print("\n--- Unter 23 Jahre ---")

for kuerzel, daten in kontaktbuch.items():
    if daten["alter"] < 23:
        print(f"  {daten['name']} ({daten['alter']} Jahre)")


# ============================================================
# SCHRITT 6: Kontakt löschen
# ============================================================

print("\n--- Kontakt löschen ---")

entfernt = kontaktbuch.pop("tom", None)     # None = kein Fehler wenn nicht vorhanden

if entfernt:
    print(f"'{entfernt['name']}' wurde gelöscht.")

print(f"Verbleibende Kontakte: {list(kontaktbuch.keys())}")


# ============================================================
# BONUS: Kontaktbuch nach Alter sortieren
# ============================================================

print("\n--- Sortiert nach Alter ---")

sortiert = sorted(kontaktbuch.items(), key=lambda x: x[1]["alter"])

for kuerzel, daten in sortiert:
    print(f"  {daten['name']}: {daten['alter']} Jahre")
