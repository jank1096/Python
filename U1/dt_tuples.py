# ============================================================
# TUPLES — Schulbeispiel
# ============================================================

tup = ("Jan", 25, "Düsseldorf")
#       ↑      ↑        ↑
#    Index 0   1        2

print(tup)              # → ('Jan', 25, 'Düsseldorf')

# Unpacking — Werte direkt in Variablen entpacken
# Anzahl Variablen muss exakt mit Tuple-Länge übereinstimmen!
name, age, city = tup

print(name)             # → Jan
print(age)              # → 25
print(city)             # → Düsseldorf

print(len(tup))         # → 3 (Anzahl Elemente)

# Schleife Variante 1 — direkt den Wert
for item in tup:
    print(item)

# Schleife Variante 2 — mit Index
for i in range(len(tup)):
    print(i, ":", tup[i])
