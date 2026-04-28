# ============================================================
# DICTIONARIES (Wörterbücher)
# Ein Dictionary speichert Daten als SCHLÜSSEL → WERT Paare.
# Statt einem Index (0, 1, 2...) gibst du einen Namen an.
#
# Analogie: Ein echtes Wörterbuch
#   Wort (Schlüssel)  →  Bedeutung (Wert)
#   "Python"          →  "eine Programmiersprache"
#
# Wann Dictionary statt Liste?
#   → Wenn Daten eine Bedeutung/Bezeichnung haben sollen
#   → Wenn du per Name zugreifen willst, nicht per Nummer
#   → z.B. Person, Produkt, Einstellungen, JSON-Daten
# ============================================================


# ============================================================
# 1. DICTIONARY ERSTELLEN
# ============================================================

person = {
    "name":  "Jan",       # Schlüssel: "name"   → Wert: "Jan"
    "alter": 20,          # Schlüssel: "alter"  → Wert: 20
    "stadt": "Düsseldorf" # Schlüssel: "stadt"  → Wert: "Düsseldorf"
}
#           ↑                ↑
#       Schlüssel          Wert
#    (immer ein String    (beliebiger Typ)
#     oder Zahl)

print(person)           # → {'name': 'Jan', 'alter': 20, 'stadt': 'Düsseldorf'}
print(type(person))     # → <class 'dict'>
print(len(person))      # → 3  (Anzahl Schlüssel-Wert-Paare)

# Leeres Dictionary erstellen
leer = {}
leer2 = dict()          # alternative Schreibweise
print(type(leer))       # → <class 'dict'>


# ============================================================
# 2. WERTE ABRUFEN
# ============================================================

# Variante 1: per eckiger Klammer [ ]
print(person["name"])   # → Jan
print(person["alter"])  # → 20
# print(person["xyz"])  → KeyError! Schlüssel existiert nicht

# Variante 2: .get() — sicherer, kein Fehler wenn Schlüssel fehlt
print(person.get("name"))       # → Jan
print(person.get("xyz"))        # → None  (kein Fehler!)
print(person.get("xyz", "???")) # → ???   (eigener Standardwert wenn nicht vorhanden)

# Merkhilfe:
# person["key"]       → Fehler wenn key nicht existiert
# person.get("key")   → None wenn key nicht existiert (sicherer!)


# ============================================================
# 3. WERTE HINZUFÜGEN & ÄNDERN
# ============================================================

# Neuen Schlüssel hinzufügen — einfach zuweisen
person["beruf"] = "Fachinformatiker"
print(person)   # → {..., 'beruf': 'Fachinformatiker'}

# Bestehenden Wert überschreiben — exakt gleiche Syntax!
person["alter"] = 21
print(person["alter"])  # → 21  (war vorher 20)

# update() — mehrere Werte auf einmal hinzufügen/überschreiben
person.update({"stadt": "Berlin", "hobby": "Python"})
print(person)


# ============================================================
# 4. SCHLÜSSEL & WERTE ABRUFEN
# ============================================================

print(person.keys())    # → dict_keys(['name', 'alter', 'stadt', 'beruf', 'hobby'])
                        #   alle Schlüssel

print(person.values())  # → dict_values(['Jan', 21, 'Berlin', 'Fachinformatiker', 'Python'])
                        #   alle Werte

print(person.items())   # → dict_items([('name', 'Jan'), ('alter', 21), ...])
                        #   alle Paare als Tuples

# Prüfen ob ein Schlüssel vorhanden ist:
print("name" in person)     # → True
print("xyz" in person)      # → False


# ============================================================
# 5. WERTE LÖSCHEN
# ============================================================

person2 = {"a": 1, "b": 2, "c": 3, "d": 4}

# pop(key) — entfernt Schlüssel und gibt den Wert zurück
entfernt = person2.pop("b")
print(entfernt)     # → 2
print(person2)      # → {'a': 1, 'c': 3, 'd': 4}

# del — löscht direkt per Schlüssel
del person2["c"]
print(person2)      # → {'a': 1, 'd': 4}

# popitem() — entfernt das ZULETZT hinzugefügte Paar
letztes = person2.popitem()
print(letztes)      # → ('d', 4)  als Tuple
print(person2)      # → {'a': 1}

# clear() — alles löschen
person2.clear()
print(person2)      # → {}


# ============================================================
# 6. SCHLEIFEN ÜBER DICTIONARIES
# ============================================================

auto = {"marke": "BMW", "baujahr": 2020, "farbe": "blau"}

# Variante 1: nur Schlüssel
for key in auto:
    print(key)          # → marke, baujahr, farbe

# Variante 2: nur Werte
for wert in auto.values():
    print(wert)         # → BMW, 2020, blau

# Variante 3: Schlüssel UND Wert — der Python-Weg (items)
for key, wert in auto.items():
    print(f"{key}: {wert}")
    # → marke: BMW
    # → baujahr: 2020
    # → farbe: blau


# ============================================================
# 7. VERSCHACHTELTE DICTIONARIES
# Ein Dictionary kann andere Dictionaries als Wert enthalten
# ============================================================

klasse = {
    "schueler1": {"name": "Jan",   "note": 1},
    "schueler2": {"name": "Anna",  "note": 2},
    "schueler3": {"name": "Tom",   "note": 3},
}
#      ↑                  ↑
#  äußerer Key       inneres Dictionary

# Zugriff: erst äußerer Key, dann innerer Key
print(klasse["schueler1"]["name"])  # → Jan
print(klasse["schueler2"]["note"])  # → 2

# Alle Schüler ausgeben:
for key, schueler in klasse.items():
    print(f"{key}: {schueler['name']} hat Note {schueler['note']}")


# ============================================================
# 8. DICTIONARY MIT LISTE ALS WERT
# Ein Wert kann auch eine Liste sein
# ============================================================

warenkorb = {
    "jan":  ["Apfel", "Brot", "Milch"],
    "anna": ["Käse", "Wasser"],
}

print(warenkorb["jan"])         # → ['Apfel', 'Brot', 'Milch']
print(warenkorb["jan"][0])      # → Apfel  (erstes Element der Liste)

warenkorb["jan"].append("Butter")   # Butter zu Jans Warenkorb hinzufügen
print(warenkorb["jan"])         # → ['Apfel', 'Brot', 'Milch', 'Butter']


# ============================================================
# 9. NÜTZLICHE METHODEN
# ============================================================

d = {"x": 10, "y": 20, "z": 30}

# copy() — echte Kopie erstellen
kopie = d.copy()
kopie["x"] = 99
print(d["x"])       # → 10  (Original unverändert)
print(kopie["x"])   # → 99

# setdefault() — fügt Key hinzu NUR wenn er noch nicht existiert
d.setdefault("x", 0)    # x existiert schon → nichts passiert
d.setdefault("w", 0)    # w existiert nicht → wird mit 0 eingefügt
print(d)            # → {'x': 10, 'y': 20, 'z': 30, 'w': 0}


# ============================================================
# 10. DICTIONARY vs. LISTE vs. SET vs. TUPLE — Wann was?
# ============================================================

# LISTE   → geordnete Sammlung, Duplikate OK
#           noten = [1, 2, 3, 1]

# TUPLE   → geordnet, unveränderlich
#           koordinaten = (48.13, 11.58)

# SET     → keine Duplikate, keine Reihenfolge
#           besucher = {"Jan", "Anna"}

# DICT    → Schlüssel → Wert, benannte Daten
#           person = {"name": "Jan", "alter": 20}
