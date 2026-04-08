# ============================================================
# AUFGABE: Filmdaten mit Tuple & Liste
# ============================================================


# ============================================================
# 1. TUPLE ERSTELLEN
# Ein Tuple weil sich Filmdaten nicht ändern sollen
# ============================================================

film_a = ("Die Matrix", 1999, "Science-Fiction")
#              ↑           ↑          ↑
#           Index 0     Index 1    Index 2


# ============================================================
# 2. TITEL AUSGEBEN (per Index)
# ============================================================

print(film_a[0])    # → Die Matrix


# ============================================================
# 3. LISTE ERSTELLEN UND BEFÜLLEN
# Die Sammlung ist eine Liste — weil wir Filme hinzufügen/entfernen können sollen
# ============================================================

film_b = ("Der Pate", 1972, "Drama")
film_c = ("Inception", 2010, "Science-Fiction")

filmsammlung = [film_a, film_b, film_c]

print(filmsammlung)


# ============================================================
# 4. NEUEN FILM AN INDEX 1 EINFÜGEN
# insert(index, wert) — schiebt alles ab Index 1 einen Platz nach rechts
# ============================================================

film_neu = ("Interstellar", 2014, "Science-Fiction")

filmsammlung.insert(1, film_neu)

print(filmsammlung)

# Zur Kontrolle — alle Filme schön ausgeben:
for film in filmsammlung:
    print(f"Titel: {film[0]} | Jahr: {film[1]} | Genre: {film[2]}")


# ============================================================
# 5. BONUS: Kann man das Jahr von "Die Matrix" ändern?
# ============================================================

# NEIN — Tuples sind unveränderlich!
# Dieser Code würde einen Fehler geben:
# filmsammlung[0][1] = 2000  → TypeError!

# Warum?
# filmsammlung[0]    → gibt film_a zurück → das ist ein Tuple
# film_a[1] = 2000   → Tuple kann nicht geändert werden!

# Wenn man es trotzdem ändern müsste:
# → Tuple in Liste umwandeln, ändern, zurück in Tuple
film_a_liste = list(filmsammlung[0])    # Tuple → Liste
film_a_liste[1] = 2000                  # Jahr ändern
filmsammlung[0] = tuple(film_a_liste)   # Liste → Tuple, zurück in Sammlung

print(filmsammlung[0])  # → ('Die Matrix', 2000, 'Science-Fiction')
