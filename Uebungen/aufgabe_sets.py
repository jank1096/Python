# ============================================================
# AUFGABE: Kursteilnehmer-Verwaltung
# Konzepte: Sets, Mengenoperationen, Duplikate entfernen
# ============================================================
#
# Szenario: Zwei Kurse (Python und Web) — wer ist wo angemeldet?
# ============================================================


# ============================================================
# SCHRITT 1: Kurslisten bereinigen (Duplikate entfernen)
# ============================================================

# Rohdaten — können doppelte Einträge enthalten
python_kurs_roh = ["Anna", "Jan", "Tom", "Anna", "Sara", "Jan", "Mike"]
web_kurs_roh    = ["Sara", "Mike", "Lisa", "Tom", "Sara", "Felix", "Mike"]

# Set → entfernt Duplikate automatisch
python_kurs = set(python_kurs_roh)
web_kurs    = set(web_kurs_roh)

print("--- Kursteilnehmer ---")
print(f"Python-Kurs ({len(python_kurs)} Personen): {python_kurs}")
print(f"Web-Kurs    ({len(web_kurs)} Personen): {web_kurs}")


# ============================================================
# SCHRITT 2: Mengenoperationen
# ============================================================

print("\n--- Auswertungen ---")

# Wer ist in BEIDEN Kursen? (Schnittmenge)
beide_kurse = python_kurs & web_kurs
print(f"In beiden Kursen:       {beide_kurse}")

# Alle Teilnehmer zusammen (Vereinigung)
alle = python_kurs | web_kurs
print(f"Alle Teilnehmer:        {alle}")

# Nur im Python-Kurs (nicht im Web-Kurs)
nur_python = python_kurs - web_kurs
print(f"Nur Python-Kurs:        {nur_python}")

# Nur im Web-Kurs
nur_web = web_kurs - python_kurs
print(f"Nur Web-Kurs:           {nur_web}")

# In einem Kurs, aber nicht in beiden
genau_ein_kurs = python_kurs ^ web_kurs
print(f"Genau ein Kurs:         {genau_ein_kurs}")


# ============================================================
# SCHRITT 3: Neuen Teilnehmer hinzufügen
# ============================================================

print("\n--- Anmeldungen ---")

python_kurs.add("Lea")
print(f"Lea angemeldet: {python_kurs}")

python_kurs.add("Anna")     # Anna ist schon drin → passiert nichts
print(f"Anna nochmal (kein Duplikat): {python_kurs}")

# Abmeldung
python_kurs.discard("Tom")      # Tom abmelden (kein Fehler wenn nicht vorhanden)
print(f"Tom abgemeldet: {python_kurs}")


# ============================================================
# SCHRITT 4: Prüfen ob jemand angemeldet ist
# ============================================================

print("\n--- Anmelde-Check ---")

zu_pruefen = ["Anna", "Felix", "Max", "Sara"]

for name in zu_pruefen:
    python = name in python_kurs
    web    = name in web_kurs

    if python and web:
        status = "beide Kurse"
    elif python:
        status = "nur Python"
    elif web:
        status = "nur Web"
    else:
        status = "nicht angemeldet"

    print(f"  {name}: {status}")


# ============================================================
# SCHRITT 5: Teilmenge prüfen
# ============================================================

print("\n--- Teilmengen ---")

vip_gruppe = {"Anna", "Sara"}       # kleine Gruppe

# Sind alle VIPs im Python-Kurs?
print(f"Alle VIPs im Python-Kurs: {vip_gruppe.issubset(python_kurs)}")

# Haben Python- und Web-Kurs nichts gemeinsam?
print(f"Keine Überschneidungen:   {python_kurs.isdisjoint(web_kurs)}")
