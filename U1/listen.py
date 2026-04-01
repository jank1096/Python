# ============================================================
# LISTEN (Lists)
# Eine Liste ist wie ein Regal mit nummerierten Fächern.
# Sie kann alles enthalten: Zahlen, Text, Boolean, andere Listen.
# ============================================================

l = [2, 3.5, 'hi', False, [1, 2, 5]]  # noqa: E741
#    ↑     ↑     ↑     ↑       ↑
# Index: 0     1     2     3       4

print(len(l))   # Anzahl der Elemente → 5


# ============================================================
# ELEMENTE ABRUFEN
# ============================================================

print(l[0])     # 2        → erstes Element (Index 0)
print(l[3])     # False    → viertes Element (Index 3)

# Negative Indizes: zählen von HINTEN
print(l[-1])    # [1,2,5]  → letztes Element
print(l[-6])    # 2        → 6. von hinten = erstes Element


# ============================================================
# LIST SLICING  →  l[start : end : step]
# start = ab hier, end = bis hier (NICHT dabei), step = Schrittweite
# ============================================================

print(l[2:4])   # ['hi', False]          → Index 2 bis 3
print(l[:4])    # [2, 3.5, 'hi', False]  → Anfang bis Index 3
print(l[::2])   # [2, 'hi', [1,2,5]]     → jedes 2. Element
print(l[::-1])  # [[1,2,5], False, 'hi', 3.5, 2] → Liste rückwärts
print(l[3:])    # [False, [1,2,5]]       → ab Index 3 bis Ende


# ============================================================
# LISTE VERÄNDERN
# ============================================================

l.append(6)             # fügt 6 ans ENDE an
print(l)                # [2, 3.5, 'hi', False, [1,2,5], 6]

l.insert(2, "Halina")   # fügt "Halina" bei Index 2 ein
                        # alles dahinter rutscht einen Platz nach rechts
print(l)

mylist = [2, 4, 6]
l.extend(mylist)        # hängt eine ganze andere Liste ans Ende an
                        # (anders als append: kein [2,4,6] als Block, sondern einzeln)

l[1] = 3.14             # überschreibt Index 1 direkt (3.5 → 3.14)

l.append("Maria")       # "Maria" ans Ende


# ============================================================
# ELEMENTE LÖSCHEN
# ============================================================

l.remove('hi')          # löscht das ERSTE Vorkommen von 'hi'
                        # Fehler wenn der Wert nicht existiert!

# Alle 6er entfernen:
for _ in l:             # _ = "den Wert brauche ich nicht"
    if 6 in l:          # solange 6 noch in der Liste ist...
        l.remove(6)     # ...lösche die erste 6

print(l)


# ============================================================
# SCHLEIFEN ÜBER LISTEN
# ============================================================

# Variante 1: einfach — gibt direkt den Wert aus
for item in l:
    print(item)

# Variante 2: mit Index — gibt Position UND Wert aus
for i in range(0, len(l)):
    print(i, ":", l[i])

# Wann welche?
# → Variante 1: wenn du nur den WERT brauchst
# → Variante 2: wenn du auch die POSITION brauchst
