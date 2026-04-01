# ============================================================
# TUPLES — Schulbeispiel
# ============================================================

tup = ("Jan", 20, "Düsseldorf")
#       ↑      ↑        ↑
#    Index 0   1        2

print(tup)              # → ('Jan', 20, 'Düsseldorf')

# Unpacking — Werte direkt in Variablen entpacken
# Anzahl Variablen muss exakt mit Tuple-Länge übereinstimmen!
name, age, city = tup

print(name)             # → Jan
print(age)              # → 20
print(city)             # → Düsseldorf

print(len(tup))         # → 3 (Anzahl Elemente)

# Schleife Variante 1 — direkt den Wert
for item in tup:
    print(item)

# Schleife Variante 2 — mit Index
for i in range(len(tup)):
    print(i, ":", tup[i])

# Direkter Zugriff per Index
print(tup[1])           # → 20        positiver Index
print(tup[-1])          # → Düsseldorf  letztes Element (von hinten)

# Slicing
print(tup[:1])          # → ('Jan',)   nur erstes Element als Tuple

# index(wert) — gibt Position des Wertes zurück
print(tup.index(20))        # → 1   wo ist 20 im Tuple?

# index(wert, start, end) — sucht nur zwischen start und end
print(tup.index(20, 1, 2))  # → 1   suche 20 zwischen Index 1 und 1
                             # start=1, end=2 → nur Index 1 wird durchsucht
