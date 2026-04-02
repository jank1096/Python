# ============================================================
# TUPLES — Schulbeispiel (erweitert nach Dozenten-Vorlage)
# ============================================================

tup = ("Maria", 20, "Köln")
#       ↑         ↑     ↑
#    Index 0    Index 1  Index 2

print(tup)              # → ('Maria', 20, 'Köln')

# Unpacking — Werte direkt in Variablen entpacken
# Anzahl Variablen muss exakt mit Tuple-Länge übereinstimmen!
name, age, city = tup

print(name)             # → Maria
print(age)              # → 20
print(city)             # → Köln

print(len(tup))         # → 3 (Anzahl Elemente)

# Schleife Variante 1 — direkt den Wert
for item in tup:
    print(item)

# Schleife Variante 2 — mit Index
for i in range(len(tup)):
    print(i, ":", tup[i])

# Direkter Zugriff per Index
print(tup[1])           # → 20         positiver Index
print(tup[-1])          # → Köln       letztes Element (von hinten)

# Slicing
print(tup[:1])          # → ('Maria',)   nur erstes Element als Tuple

# index(wert) — gibt Position des Wertes zurück
print(tup.index(20))          # → 1  wo ist 20?

# index(wert, start, end) — sucht nur zwischen start und end
# start=1, end=2 → nur Index 1 wird durchsucht
print(tup.index(20, 1, 2))    # → 1

# in-Operator — prüft ob ein Wert enthalten ist
print("Köln" in tup)          # → True
print("Berlin" in tup)        # → False


# ============================================================
# TUPLE ÄNDERN — über Umweg via Liste
# Tuples selbst sind unveränderlich!
# tup[1] = 25  → würde einen TypeError geben!
# ============================================================

# Lösung: Tuple → Liste → ändern → zurück zu Tuple
tup_list = list(tup)    # Tuple in Liste umwandeln (jetzt veränderlich)
tup_list[1] = 25        # Wert an Index 1 überschreiben
tup = tuple(tup_list)   # Liste zurück in Tuple umwandeln
print(tup_list)         # → ['Maria', 25, 'Köln']
print(tup)              # → ('Maria', 25, 'Köln')
print(tup.count(25))    # → 1   wie oft kommt 25 vor?


# ============================================================
# REFERENZ vs. KOPIE mit id()
# id() gibt die Speicheradresse eines Objekts zurück.
# Wenn id gleich → selbes Objekt. Wenn anders → anderes Objekt.
# ============================================================

tup1 = (1, 2, 3, 6)
tup2 = tup1             # KEINE Kopie — beide zeigen auf dasselbe Tuple

tup1_list = list(tup1)
tup1_list.append(8)
tup1 = tuple(tup1_list) # tup1 zeigt jetzt auf ein NEUES Tuple

print(id(tup1))         # anderer Wert als id(tup2)
print(tup1)             # → (1, 2, 3, 6, 8)
print(id(tup2))         # original Speicheradresse
print(tup2)             # → (1, 2, 3, 6)  unverändert!


# ============================================================
# TUPLES VERBINDEN (Konkatenation)
# + erstellt ein neues Tuple aus zwei Tuples
# ============================================================

tup3 = tup + tup1
print(tup3)             # → ('Maria', 25, 'Köln', 1, 2, 3, 6, 8)


# ============================================================
# MATHEMATISCHE FUNKTIONEN
# ============================================================

print(sum(tup1))        # → 21    Summe aller Zahlen
print(min(tup1))        # → 1     kleinster Wert
print(max(tup1))        # → 8     größter Wert


# ============================================================
# VERSCHACHTELTE TUPLES
# Zugriff: n_tup[äußerer_index][innerer_index]
# ============================================================

n_tup = ((1, 2, 3), (6, 8, 10))
#         ↑ Index 0    ↑ Index 1

print(n_tup[1][1])      # → 8
# Schritt 1: n_tup[1]       → (6, 8, 10)
# Schritt 2: (6, 8, 10)[1]  → 8


# ============================================================
# any() UND all() mit Boolean-Tuples
# 0 und False gelten als False, alles andere als True
# ============================================================

b_tup_1 = (1, 0, False, True)   # enthält 0 und False
b_tup_2 = (1, 1, True, True)    # alles "truthy"

# any() = ODER → mindestens EINES muss True sein
print(any(b_tup_1))     # → True   (1 und True sind truthy)
print(any(b_tup_2))     # → True

# all() = UND → ALLE müssen True sein
print(all(b_tup_1))     # → False  (0 und False sind falsy)
print(all(b_tup_2))     # → True
