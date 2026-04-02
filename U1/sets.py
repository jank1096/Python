# ============================================================
# SETS (Mengen)
# Ein Set ist wie eine Liste — aber mit zwei wichtigen Regeln:
#   1. KEINE Duplikate — jeder Wert kommt nur EINMAL vor
#   2. KEINE Reihenfolge — kein Index, kein s[0]
#
# Wann Set statt Liste?
#   → Wenn du doppelte Werte automatisch loswerden willst
#   → Wenn du prüfen willst ob etwas enthalten ist (viel schneller als Liste!)
#   → Wenn du zwei Gruppen vergleichen willst (Schnittmenge, Unterschied, ...)
# ============================================================


# ============================================================
# 1. SET ERSTELLEN
# ============================================================

s = {1, 2, 3, 4, 5}
#    ↑            ↑
#  geschweifte Klammern — NICHT eckige wie bei Listen!

print(s)            # → {1, 2, 3, 4, 5}  (Reihenfolge kann variieren!)
print(type(s))      # → <class 'set'>
print(len(s))       # → 5

# Leeres Set — ACHTUNG: {} allein erstellt ein Dictionary, nicht ein Set!
leer = set()        # → so erstellt man ein leeres Set
print(type(leer))   # → <class 'set'>

# Set aus einer Liste erstellen
liste = [1, 2, 3, 2, 1, 4]
aus_liste = set(liste)      # doppelte Werte fallen automatisch weg
print(aus_liste)    # → {1, 2, 3, 4}  — 2 und 1 nur noch einmal!


# ============================================================
# 2. DUPLIKATE WERDEN AUTOMATISCH ENTFERNT
# Das ist der häufigste Grund warum man Sets verwendet
# ============================================================

mit_duplikaten = {1, 2, 2, 3, 3, 3, 4}
print(mit_duplikaten)   # → {1, 2, 3, 4}  — Python ignoriert Duplikate einfach

# Klassischer Trick: Liste deduplizieren
emails = ["jan@mail.de", "anna@mail.de", "jan@mail.de", "tom@mail.de"]
eindeutig = list(set(emails))   # Set entfernt Duplikate → zurück in Liste
print(eindeutig)    # → ['anna@mail.de', 'jan@mail.de', 'tom@mail.de']


# ============================================================
# 3. KEIN INDEXZUGRIFF!
# Sets haben keine Reihenfolge — du kannst nicht s[0] schreiben
# ============================================================

s = {10, 20, 30}
# print(s[0])   → TypeError: 'set' object is not subscriptable
#                 Das geht nicht! Kein Index bei Sets.

# Um Elemente zu durchlaufen → for-Schleife:
for element in s:
    print(element)          # Reihenfolge ist nicht garantiert!


# ============================================================
# 4. ELEMENTE HINZUFÜGEN & ENTFERNEN
# ============================================================

farben = {"rot", "blau", "grün"}

# add() — ein Element hinzufügen
farben.add("gelb")
print(farben)           # → {'rot', 'blau', 'grün', 'gelb'}

farben.add("rot")       # "rot" ist schon drin → passiert einfach nichts
print(farben)           # → unverändert

# remove() — Element entfernen (Fehler wenn nicht vorhanden!)
farben.remove("blau")
print(farben)           # → {'rot', 'grün', 'gelb'}
# farben.remove("lila") → KeyError! "lila" existiert nicht

# discard() — Element entfernen (KEIN Fehler wenn nicht vorhanden)
farben.discard("lila")  # lila gibt es nicht → kein Fehler, einfach nichts passiert
farben.discard("rot")   # rot gibt es → wird entfernt
print(farben)           # → {'grün', 'gelb'}

# Merkhilfe:
# remove()  → streng  — Fehler wenn nicht vorhanden
# discard() → sanft   — kein Fehler wenn nicht vorhanden

# pop() — entfernt ein ZUFÄLLIGES Element (da keine Reihenfolge!)
entfernt = farben.pop()
print(entfernt)         # irgendein Element — nicht vorhersagbar!

# clear() — alles löschen
farben.clear()
print(farben)           # → set()


# ============================================================
# 5. SUCHEN MIT "in"
# Sets sind hier VIEL schneller als Listen (bei großen Datenmengen)
# ============================================================

erlaubte_user = {"jan", "anna", "tom", "sara"}

print("jan" in erlaubte_user)       # → True
print("hacker" in erlaubte_user)    # → False
print("hacker" not in erlaubte_user)# → True

# Warum schneller als Liste?
# Liste: Python schaut jeden Eintrag einzeln durch (linear)
# Set:   Python berechnet direkt wo der Wert sein müsste (hash)
# → Bei 1 Million Einträgen ist Set ~1000x schneller!


# ============================================================
# 6. MENGENOPERATIONEN — der eigentliche Superkraft von Sets
# Hier wird verglichen was zwei Gruppen gemeinsam haben oder nicht
# ============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Schnittmenge (&) — was ist in BEIDEN?
print(a & b)            # → {4, 5}
print(a.intersection(b))# → {4, 5}  (dasselbe, andere Schreibweise)

# Vereinigung (|) — alles zusammen (ohne Duplikate)
print(a | b)            # → {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))       # → {1, 2, 3, 4, 5, 6, 7, 8}

# Differenz (-) — was ist in A aber NICHT in B?
print(a - b)            # → {1, 2, 3}  (nur in a)
print(b - a)            # → {6, 7, 8}  (nur in b)
print(a.difference(b))  # → {1, 2, 3}  (dasselbe, andere Schreibweise)

# Symmetrische Differenz (^) — was ist in EINEM aber nicht in BEIDEN?
print(a ^ b)                        # → {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))    # → {1, 2, 3, 6, 7, 8}


# ============================================================
# 7. TEILMENGE & OBERMENGE
# ============================================================

klein = {1, 2, 3}
gross = {1, 2, 3, 4, 5}

# issubset() — ist klein komplett in gross enthalten?
print(klein.issubset(gross))    # → True   (alle von klein sind in gross)
print(gross.issubset(klein))    # → False  (nicht alle von gross sind in klein)

# issuperset() — enthält gross alles aus klein?
print(gross.issuperset(klein))  # → True
print(klein.issuperset(gross))  # → False

# isdisjoint() — haben sie gar nichts gemeinsam?
x = {1, 2, 3}
y = {7, 8, 9}
z = {3, 4, 5}
print(x.isdisjoint(y))  # → True   (keine gemeinsamen Elemente)
print(x.isdisjoint(z))  # → False  (3 ist in beiden!)


# ============================================================
# 8. FROZENSET — unveränderliches Set (wie Tuple für Listen)
# Kann nicht verändert werden — kein add(), remove() etc.
# Nützlich als Dictionary-Key oder wenn Unveränderlichkeit gewünscht
# ============================================================

fs = frozenset({1, 2, 3, 4})
print(fs)               # → frozenset({1, 2, 3, 4})
# fs.add(5)             → AttributeError: frozenset hat kein add()


# ============================================================
# 9. SET vs. LISTE vs. TUPLE — Wann was?
# ============================================================

# LISTE  → Reihenfolge wichtig, Duplikate erlaubt, veränderlich
#          einkauf = ["Milch", "Brot", "Milch"]  # zweimal Milch OK

# TUPLE  → Reihenfolge wichtig, unveränderlich
#          koordinaten = (48.13, 11.58)

# SET    → Reihenfolge egal, keine Duplikate, schnelle Suche
#          besucher = {"Jan", "Anna", "Tom"}  # jeder nur einmal
