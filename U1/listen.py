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

popped = l.pop()        # entfernt das LETZTE Element und gibt es zurück
print(popped)           # man kann den entfernten Wert also noch verwenden
popped2 = l.pop(1)      # entfernt Element an Index 1 und gibt es zurück
print(popped2)

# Unterschied remove vs pop:
# remove("hi") → sucht nach dem WERT, löscht erstes Vorkommen
# pop(1)       → löscht nach INDEX, gibt den Wert zurück

del l[2:4]              # löscht alle Elemente von Index 2 bis 3
                        # funktioniert wie Slicing — end-Index ist NICHT dabei
                        # gibt nichts zurück (kein Rückgabewert wie pop)

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


# ============================================================
# WEITERE NÜTZLICHE METHODEN
# ============================================================

# index() — gibt die POSITION eines Wertes zurück
l.append("Maria")           # erst "Maria" wieder hinzufügen
print(l.index("Maria"))     # → gibt den Index von "Maria" aus
                            # Fehler wenn der Wert nicht in der Liste ist!

# clear() — löscht ALLE Elemente, Liste bleibt aber bestehen
l.clear()
print(l)                    # → [] (leere Liste)


# ============================================================
# LISTEN ZUSAMMENFÜHREN & KOPIEREN
# ============================================================

l = [2, 3.5, False]         # Liste neu befüllen zum Weitermachen
mylist = [2, 4, 6]

new_list = l + mylist       # + verbindet zwei Listen zu einer neuen
print(new_list)             # → [2, 3.5, False, 2, 4, 6]

# ACHTUNG: Referenz vs. Kopie!
new_1_2 = new_list          # keine echte Kopie — beide zeigen auf DIESELBE Liste
                            # ändert man new_list, ändert sich auch new_1_2!

new_list.pop()              # entfernt letztes Element (6) aus new_list
print(new_list)             # → [2, 3.5, False, 2, 4]
print(new_1_2)              # → [2, 3.5, False, 2, 4]  ← AUCH verändert!

# Echte Kopie (unabhängig) erstellt man so:
new_copy = new_list.copy()  # jetzt sind beide unabhängig voneinander


# ============================================================
# MATHEMATISCHE FUNKTIONEN AUF LISTEN
# sum() und len() kennen wir schon — kombiniert ergibt das den Durchschnitt
# ============================================================

num_l = [10, 20, 30, 40, 50]

print(sum(num_l))               # → 150  (alle Werte addiert)
print(len(num_l))               # → 5    (Anzahl Elemente)
print(sum(num_l) / len(num_l))  # → 30.0 (Durchschnitt = Summe / Anzahl)


# ============================================================
# all() und any() — prüfen ob Werte True oder False sind
# Wichtig: 0 und False gelten als False, alles andere als True
# ============================================================

list_1 = [0, 1, True, False]    # enthält 0 und False → nicht alle True
list_2 = [1, 1, True]           # alles ungleich 0 → alle True

# all() → True nur wenn ALLE Elemente True sind
print(all(list_1))  # → False  (weil 0 und False dabei sind)
print(all(list_2))  # → True   (1, 1, True sind alle "truthy")

# any() → True wenn MINDESTENS EIN Element True ist
print(any(list_1))  # → True   (1 und True sind dabei)
print(any(list_2))  # → True   (alle sind True)

# Merkhilfe:
# all() = UND-Verknüpfung (alle müssen True sein)
# any() = ODER-Verknüpfung (mindestens eines muss True sein)


# ============================================================
# VERSCHACHTELTE LISTEN (Liste in einer Liste)
# Zugriff: n_list[äußerer_index][innerer_index]
# ============================================================

n_list = [[1, 3, 4, 2], [5, 6, 7, 8, 9]]
#          ↑ Index 0       ↑ Index 1

print(n_list[0])        # → [1, 3, 4, 2]   erste innere Liste
print(n_list[1])        # → [5, 6, 7, 8, 9] zweite innere Liste

print(n_list[1][1])     # → 6
# Schritt 1: n_list[1]   → [5, 6, 7, 8, 9]
# Schritt 2: [5,6,7,8,9][1] → 6  (Index 1 dieser Liste)
