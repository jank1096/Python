# ============================================================
# TUPLES
# Ein Tuple ist wie eine Liste — aber UNVERÄNDERLICH (immutable).
# Einmal erstellt, kann man Werte weder ändern noch löschen.
# Wann Tuple statt Liste?
# → Daten die sich nie ändern sollen (z.B. Koordinaten, Farben, Wochentage)
# → Tuples sind schneller und speichereffizienter als Listen
# ============================================================


# ============================================================
# 1. TUPLE ERSTELLEN
# ============================================================

t = (1, 2.5, "hallo", True)
#    ↑    ↑      ↑       ↑
# Idx: 0    1      2       3

print(t)            # → (1, 2.5, 'hallo', True)
print(type(t))      # → <class 'tuple'>
print(len(t))       # → 4

# Tuple mit einem Element — Komma ist PFLICHT!
single = (42,)      # ohne Komma wäre es nur eine Zahl in Klammern
print(type(single)) # → <class 'tuple'>
print(type((42)))   # → <class 'int'>  ← KEIN Tuple!

# Tuple ohne Klammern (Packing)
packed = 1, 2, 3
print(packed)       # → (1, 2, 3) — Python erkennt es als Tuple


# ============================================================
# 2. ELEMENTE ABRUFEN (wie bei Listen)
# ============================================================

coords = (10, 20, 30, 40, 50)

print(coords[0])    # → 10   erstes Element
print(coords[2])    # → 30   drittes Element
print(coords[-1])   # → 50   letztes Element
print(coords[-2])   # → 40   vorletztes Element


# ============================================================
# 3. SLICING  →  t[start : end : step]
# Funktioniert genau wie bei Listen
# ============================================================

print(coords[1:4])  # → (20, 30, 40)   Index 1 bis 3
print(coords[:3])   # → (10, 20, 30)   Anfang bis Index 2
print(coords[2:])   # → (30, 40, 50)   ab Index 2 bis Ende
print(coords[::-1]) # → (50, 40, 30, 20, 10)  rückwärts


# ============================================================
# 4. TUPLE METHODEN
# Tuples haben nur 2 Methoden — sie sind unveränderlich!
# ============================================================

farben = ("rot", "blau", "grün", "blau", "rot", "blau")

print(farben.count("blau"))     # → 3   wie oft kommt "blau" vor?
print(farben.index("grün"))     # → 2   an welchem Index ist "grün"?
print(farben.index("blau"))     # → 1   gibt Index des ERSTEN Treffers zurück

# Prüfen ob ein Wert enthalten ist:
print("rot" in farben)          # → True
print("gelb" in farben)         # → False


# ============================================================
# 5. MATHEMATISCHE FUNKTIONEN
# ============================================================

zahlen = (4, 1, 9, 2, 7, 5)

print(len(zahlen))              # → 6     Anzahl Elemente
print(sum(zahlen))              # → 28    Summe
print(min(zahlen))              # → 1     kleinster Wert
print(max(zahlen))              # → 9     größter Wert
print(sum(zahlen) / len(zahlen))# → 4.67  Durchschnitt

# sorted() gibt eine LISTE zurück (kein Tuple — Tuples sind unveränderlich)
print(sorted(zahlen))           # → [1, 2, 4, 5, 7, 9]  ← Liste!
print(type(sorted(zahlen)))     # → <class 'list'>


# ============================================================
# 6. TUPLE UNPACKING
# Werte eines Tuples direkt in Variablen entpacken
# ============================================================

person = ("Jan", 25, "Düsseldorf")

name, alter, stadt = person     # Anzahl Variablen muss exakt passen!
print(name)                     # → Jan
print(alter)                    # → 25
print(stadt)                    # → Düsseldorf

# Mit * den Rest auffangen:
erste, *rest = (1, 2, 3, 4, 5)
print(erste)    # → 1
print(rest)     # → [2, 3, 4, 5]  (wird zur Liste!)

*anfang, letzte = (1, 2, 3, 4, 5)
print(anfang)   # → [1, 2, 3, 4]
print(letzte)   # → 5


# ============================================================
# 7. SCHLEIFEN ÜBER TUPLES
# ============================================================

wochentage = ("Mo", "Di", "Mi", "Do", "Fr", "Sa", "So")

# Variante 1: direkt den Wert
for tag in wochentage:
    print(tag)

# Variante 2: mit Index (enumerate — der Python-Weg)
for i, tag in enumerate(wochentage):
    print(i, ":", tag)


# ============================================================
# 8. TUPLE KOMBINIEREN
# ============================================================

a = (1, 2, 3)
b = (4, 5, 6)

combined = a + b        # → (1, 2, 3, 4, 5, 6)  neues Tuple
print(combined)

repeated = a * 3        # → (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(repeated)


# ============================================================
# 9. KONVERTIERUNG: Tuple ↔ Liste
# ============================================================

mein_tuple = (1, 2, 3, 4)
meine_liste = list(mein_tuple)  # Tuple → Liste (jetzt veränderlich)
meine_liste.append(5)
print(meine_liste)              # → [1, 2, 3, 4, 5]

zurueck = tuple(meine_liste)    # Liste → Tuple (wieder unveränderlich)
print(zurueck)                  # → (1, 2, 3, 4, 5)


# ============================================================
# 10. TUPLE vs. LISTE — Wann was verwenden?
# ============================================================

# LISTE  → wenn sich die Daten ändern können
#          einkaufsliste = ["Milch", "Brot", "Käse"]

# TUPLE  → wenn die Daten fest sind
#          koordinaten = (48.1351, 11.5820)   # München GPS
#          rgb_rot     = (255, 0, 0)
#          wochentage  = ("Mo","Di","Mi","Do","Fr","Sa","So")

# Versuch ein Tuple zu ändern → Fehler!
# t = (1, 2, 3)
# t[0] = 99   # → TypeError: 'tuple' object does not support item assignment


# ============================================================
# 11. VERSCHACHTELTE TUPLES
# ============================================================

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(matrix[0])        # → (1, 2, 3)   erste Zeile
print(matrix[1][2])     # → 6   zweite Zeile, dritter Wert

for zeile in matrix:
    for wert in zeile:
        print(wert, end=" ")
    print()
