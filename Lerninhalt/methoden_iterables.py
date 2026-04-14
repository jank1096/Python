# ============================================================
#  METHODEN & ITERABLES
#  Themen: zip, enumerate, map, filter, match-case,
#          List Comprehension, Dict Comprehension,
#          break, continue, while
# ============================================================


# ==========================
#  IF / ELIF / ELSE
# ==========================

alter = 18

if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist noch ein Kind!")

note = 2

if note == 1:
    print("Sehr gut!")
elif note == 2:
    print("Gut!")
elif note == 3:
    print("Befriedigend")
else:
    print("Error!")

# Kurzform — Ternary Operator
# "Wert wenn True" if Bedingung else "Wert wenn False"
status = "Erwachsen" if alter >= 18 else "Kind"
print(status)   # → Erwachsen


# ==========================
#  FOR-SCHLEIFE
# ==========================

names = ["Alena", "Rosa", "Mirko", "Ibrahim"]

# Einfach über Liste:
for name in names:
    print(name)

# Mit range() — Zahlen von 1 bis 5:
for i in range(1, 6):
    print(i)

# Mit enumerate() — Index UND Wert gleichzeitig:
# Das zweite Argument (1) = Startnummer
for i, name in enumerate(names, 1):
    print(f"Platz {i}: {name}")


# ==========================
#  ZIP — zwei Listen gleichzeitig durchlaufen
# ==========================

# zip() verbindet zwei Listen paarweise
# Wie ein Reißverschluss — Element 0 mit Element 0, Element 1 mit Element 1 usw.

produkte = ["Tee", "Kaffee"]
preise   = [2.50, 1.80]

for produkt, preis in zip(produkte, preise):
    print(f"{produkt} kostet {preis} €")
# → Tee kostet 2.50 €
# → Kaffee kostet 1.80 €


# ==========================
#  BREAK & CONTINUE
# ==========================

# continue → überspringt den aktuellen Durchlauf, macht weiter
# break    → beendet die Schleife komplett

for zahl in range(1, 10):
    if zahl == 5:
        continue    # 5 überspringen
    if zahl == 8:
        break       # bei 8 aufhören
    print(zahl)     # → 1, 2, 3, 4, 6, 7

# Nur gerade Zahlen ausgeben:
for i in range(1, 20):
    if i % 2 != 0:  # ungerade → überspringen
        continue
    print(i)        # → 2, 4, 6, 8 ...


# ==========================
#  WHILE-SCHLEIFE
# ==========================

# while läuft solange die Bedingung True ist
# while True = läuft unendlich → braucht ein break zum Stoppen!

counter = 0
while True:
    counter += 1
    print(counter)
    if counter == 5:
        break       # → stoppt bei 5


# ==========================
#  MATCH-CASE (ab Python 3.10)
# ==========================

# match-case = wie if/elif, aber übersichtlicher für viele Fälle
# case _ = "alles andere" (wie else)

operator = input("Operator eingeben (+,-,*,/):")

match operator:
    case '+':
        print(f"5 + 4 = {5 + 4}")
    case '-':
        print(f"5 - 4 = {5 - 4}")
    case '*':
        print(f"5 * 4 = {5 * 4}")
    case '/':
        print(f"5 / 4 = {5 / 4}")
    case _:
        print("Nicht verfügbar")


# ==========================
#  LIST COMPREHENSION
# ==========================

# Kurze Schreibweise um eine neue Liste zu erstellen
# Syntax: [Ausdruck for Element in Liste]

# Normal (lang):
ergebnis = []
for name in names:
    ergebnis.append(name.upper())

# Mit List Comprehension (kurz):
ergebnis = [name.upper() for name in names]
print(ergebnis)     # → ['ALENA', 'ROSA', 'MIRKO', 'IBRAHIM']

# Mit Bedingung:
lange_namen = [name for name in names if len(name) > 4]
print(lange_namen)  # → ['Alena', 'Mirko', 'Ibrahim']

# 10x "Hello" in einer Liste:
x_liste = ["Hello" for _ in range(10)]
print(*x_liste)     # * = entpackt die Liste → gibt alle Werte aus


# ==========================
#  DICT COMPREHENSION
# ==========================

# Wie List Comprehension, aber für Dictionaries
# Syntax: {Key: Value for Element in Liste}

namen  = ["Tee", "Kaffee", "Wasser"]
preise = [2.50, 1.80, 0.50]

# Erstellt ein Dictionary aus zwei Listen mit zip():
katalog = {name: preis for name, preis in zip(namen, preise)}
print(katalog)
# → {'Tee': 2.5, 'Kaffee': 1.8, 'Wasser': 0.5}


# ==========================
#  MAP & FILTER
# ==========================

zahlen = [1, 2, 3, 4, 5]

# map() → wendet eine Funktion auf jedes Element an
quadriert = list(map(lambda x: x ** 2, zahlen))
print(quadriert)    # → [1, 4, 9, 16, 25]

# filter() → filtert Elemente nach einer Bedingung
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
print(gerade)       # → [2, 4]

# lambda = anonyme Mini-Funktion
# lambda x: x**2  →  def f(x): return x**2
