# ============================================================
# LISTEN (Lists)
# Eine Liste ist wie ein Regal mit nummerierten Fächern.
# Sie kann alles enthalten: Zahlen, Text, Boolean, andere Listen.
# Reihenfolge: Erstellen → Abrufen → Slicing → Verändern →
#              Suchen → Löschen → Mathe → all/any → Schleifen →
#              Kombinieren → Verschachtelt
# ============================================================


# ============================================================
# 1. LISTE ERSTELLEN
# ============================================================

l = [2, 3.5, "hi", False, [1, 2, 5]]
#    ↑    ↑     ↑      ↑       ↑
# Idx: 0    1     2      3       4

print(len(l))   # → 5 (Anzahl Elemente)


# ============================================================
# 2. ELEMENTE ABRUFEN
# ============================================================

print(l[0])     # → 2         erstes Element
print(l[2])     # → 'hi'      drittes Element
print(l[-1])    # → [1,2,5]   letztes Element (von hinten)
print(l[-2])    # → False     vorletztes Element


# ============================================================
# 3. LIST SLICING  →  l[start : end : step]
# start = ab hier | end = bis hier (NICHT dabei) | step = Schrittweite
# ============================================================

print(l[1:3])   # → [3.5, 'hi']              Index 1 bis 2
print(l[:3])    # → [2, 3.5, 'hi']           Anfang bis Index 2
print(l[2:])    # → ['hi', False, [1,2,5]]   ab Index 2 bis Ende
print(l[::2])   # → [2, 'hi', [1,2,5]]       jedes 2. Element
print(l[::-1])  # → [[1,2,5], False, 'hi', 3.5, 2]  rückwärts


# ============================================================
# 4. LISTE VERÄNDERN
# ============================================================

l.append(6)             # fügt 6 ans ENDE an
print(l)                # → [2, 3.5, 'hi', False, [1,2,5], 6]

l.insert(2, "Halina")   # fügt "Halina" bei Index 2 ein
                        # alles dahinter rutscht einen Platz nach rechts
print(l)

l[1] = 99               # überschreibt Index 1 direkt
print(l)

mylist = [7, 8, 9]
l.extend(mylist)        # hängt mylist Element für Element ans Ende
                        # append würde [7,8,9] als Block hinzufügen — extend nicht!
print(l)


# ============================================================
# 5. SUCHEN & PRÜFEN
# ============================================================

l.append("hi")                  # zweites "hi" hinzufügen zum Testen

print("hi" in l)                # → True   (ist "hi" enthalten?)
print("xyz" in l)               # → False

print(l.index("hi"))            # → gibt Index des ERSTEN Treffers zurück
                                # Fehler wenn Wert nicht existiert!

print(l.count("hi"))            # → 2   (wie oft kommt "hi" vor?)
print(l.count(6))               # → 1


# ============================================================
# 6. LÖSCHEN
# ============================================================

l.remove("hi")          # löscht ERSTES Vorkommen von "hi" (sucht nach Wert)
print(l)

popped = l.pop()        # entfernt LETZTES Element und gibt es zurück
print(popped)           # → "hi" (das zweite, das wir oben ergänzt hatten)

popped2 = l.pop(2)      # entfernt Element an Index 2 und gibt es zurück
print(popped2)

del l[1:3]              # löscht Index 1 und 2 (end-Index 3 ist NICHT dabei)
print(l)

# Übersicht: Wann was verwenden?
# remove(wert) → wenn du den WERT kennst
# pop(index)   → wenn du den INDEX kennst + Rückgabewert brauchst
# del l[i]     → wenn du schnell per Index oder Bereich löschen willst
# clear()      → wenn du ALLES löschen willst (Liste bleibt bestehen)

l.clear()
print(l)                # → []


# ============================================================
# 7. MATHEMATISCHE FUNKTIONEN
# ============================================================

num_l = [4, 1, 7, 2, 9, 3]

print(len(num_l))               # → 6     Anzahl Elemente
print(sum(num_l))               # → 26    Summe aller Werte
print(min(num_l))               # → 1     kleinster Wert
print(max(num_l))               # → 9     größter Wert
print(sum(num_l) / len(num_l))  # → 4.33  Durchschnitt

print(sorted(num_l))            # → [1,2,3,4,7,9]  neue sortierte Liste
print(num_l)                    # → [4,1,7,2,9,3]  ORIGINAL unverändert!

num_l.sort()                    # sortiert die Liste direkt (in-place)
print(num_l)                    # → [1,2,3,4,7,9]  ORIGINAL verändert!

num_l.sort(reverse=True)        # absteigend sortieren
print(num_l)                    # → [9,7,4,3,2,1]

# Merkhilfe:
# sorted(l) → gibt neue Liste zurück, Original bleibt
# l.sort()  → verändert Original, kein Rückgabewert


# ============================================================
# 8. all() UND any()
# 0 und False gelten als False, alles andere als True ("truthy")
# ============================================================

list_1 = [0, 1, True, False]    # enthält 0 und False
list_2 = [1, 1, True]           # alles ungleich 0

print(all(list_1))  # → False  (ALLE müssen True sein — 0 und False sind es nicht)
print(all(list_2))  # → True   (alle Werte sind "truthy")

print(any(list_1))  # → True   (MINDESTENS EINES muss True sein — 1 und True sind es)
print(any(list_2))  # → True

# Merkhilfe:
# all() = UND → alle müssen True sein
# any() = ODER → mindestens eines muss True sein


# ============================================================
# 9. SCHLEIFEN ÜBER LISTEN
# ============================================================

fruits = ["Apfel", "Banane", "Kirsche"]

# Variante 1: for-in — einfachste Form, direkt den Wert
for item in fruits:
    print(item)

# Variante 2: enumerate() — gibt Index UND Wert zurück (Pythonic!)
for i, item in enumerate(fruits):
    print(i, ":", item)

# Variante 3: range/len — nur wenn Index-Manipulation nötig
for i in range(len(fruits)):
    print(i, ":", fruits[i])

# Wann welche?
# → Variante 1: nur der WERT gebraucht wird
# → Variante 2: INDEX und WERT gebraucht werden (bevorzugt!)
# → Variante 3: wenn du den Index zum Schreiben brauchst (z.B. fruits[i] = ...)


# ============================================================
# 10. LISTEN KOMBINIEREN & KOPIEREN
# ============================================================

a = [1, 2, 3]
b = [4, 5, 6]

combined = a + b        # + erstellt eine neue kombinierte Liste
print(combined)         # → [1, 2, 3, 4, 5, 6]

# ACHTUNG: Referenz vs. echte Kopie!
ref = combined          # KEINE Kopie — beide zeigen auf DIESELBE Liste
copy = combined.copy()  # ECHTE Kopie — unabhängig

combined.pop()
print(ref)              # → [1,2,3,4,5]  MIT verändert (gleiche Referenz!)
print(copy)             # → [1,2,3,4,5,6] unverändert (echte Kopie)


# ============================================================
# 11. VERSCHACHTELTE LISTEN
# Zugriff: n_list[äußerer_index][innerer_index]
# ============================================================

n_list = [[1, 3, 4, 2], [5, 6, 7, 8, 9]]
#          ↑ Index 0        ↑ Index 1

print(n_list[0])        # → [1, 3, 4, 2]
print(n_list[1])        # → [5, 6, 7, 8, 9]
print(n_list[1][1])     # → 6
# Schritt 1: n_list[1]      → [5, 6, 7, 8, 9]
# Schritt 2: [5,6,7,8,9][1] → 6

# Verschachtelt mit Schleife durchlaufen:
for inner in n_list:
    for value in inner:
        print(value, end=" ")   # end=" " verhindert Zeilenumbruch
    print()     
    
                # Zeilenumbruch nach jeder inneren Liste
