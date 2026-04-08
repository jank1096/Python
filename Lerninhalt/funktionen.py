# ============================================================
# FUNKTIONEN (Functions)
# Eine Funktion ist ein wiederverwendbarer Codeblock.
# Du definierst sie einmal — und kannst sie beliebig oft aufrufen.
#
# Warum Funktionen?
#   → Kein doppelter Code (DRY: Don't Repeat Yourself)
#   → Code wird lesbarer und strukturierter
#   → Fehler nur einmal fixen, nicht 10-mal
# ============================================================


# ============================================================
# 1. FUNKTION DEFINIEREN & AUFRUFEN
# ============================================================

# Definieren — mit "def"
def begruessung():
    print("Hallo!")

# Aufrufen — mit dem Namen + ()
begruessung()       # → Hallo!
begruessung()       # → Hallo!  (beliebig oft)


# ============================================================
# 2. PARAMETER (Eingaben)
# Parameter sind Platzhalter für Werte, die beim Aufruf übergeben werden
# ============================================================

def begruessung_mit_name(name):
    #                     ↑
    #              Parameter — wie eine Variable, nur für diese Funktion
    print(f"Hallo, {name}!")

begruessung_mit_name("Jan")     # → Hallo, Jan!
begruessung_mit_name("Anna")    # → Hallo, Anna!

# Mehrere Parameter
def addiere(a, b):
    print(a + b)

addiere(3, 5)       # → 8
addiere(10, -2)     # → 8


# ============================================================
# 3. RETURN (Rückgabewert)
# Mit return gibt die Funktion ein Ergebnis zurück
# ============================================================

def addiere(a, b):
    return a + b    # Ergebnis zurückgeben

ergebnis = addiere(3, 5)    # Rückgabewert in Variable speichern
print(ergebnis)             # → 8

# Ohne return gibt eine Funktion None zurück:
def ohne_return():
    x = 5 + 3      # wird berechnet, aber nicht zurückgegeben

print(ohne_return())        # → None

# Merkhilfe:
# print() → gibt auf dem Bildschirm aus (nur für Menschen sichtbar)
# return  → gibt den Wert an den Aufrufer zurück (kann weiterverwendet werden)


# ============================================================
# 4. STANDARDWERTE FÜR PARAMETER
# Wenn kein Wert übergeben wird, wird der Standardwert verwendet
# ============================================================

def begruessung(name, sprache="de"):
    #                         ↑
    #               Standardwert — wird benutzt wenn kein Argument übergeben
    if sprache == "de":
        print(f"Hallo, {name}!")
    elif sprache == "en":
        print(f"Hello, {name}!")

begruessung("Jan")              # → Hallo, Jan!   (Standardwert "de")
begruessung("Anna", "en")       # → Hello, Anna!  (Standardwert überschrieben)

# Wichtig: Parameter mit Standardwert IMMER nach denen ohne!
# def f(a=1, b):  → SyntaxError!  ← FALSCH
# def f(b, a=1):  → OK            ← RICHTIG


# ============================================================
# 5. KEYWORD ARGUMENTE
# Du kannst Parameter beim Aufruf mit Namen ansprechen
# ============================================================

def person_vorstellen(name, alter, stadt):
    print(f"{name}, {alter} Jahre, aus {stadt}")

# Normale Reihenfolge
person_vorstellen("Jan", 20, "Düsseldorf")

# Mit Keyword-Argumenten — Reihenfolge egal!
person_vorstellen(alter=20, stadt="Düsseldorf", name="Jan")
person_vorstellen("Jan", stadt="Düsseldorf", alter=20)


# ============================================================
# 6. *args — BELIEBIG VIELE ARGUMENTE
# Wenn du nicht weißt, wie viele Werte übergeben werden
# ============================================================

def summe(*zahlen):
    #      ↑
    #  * = sammelt alle Argumente in einem Tuple
    print(zahlen)           # → (1, 2, 3) — ein Tuple
    return sum(zahlen)

print(summe(1, 2, 3))       # → 6
print(summe(10, 20))        # → 30
print(summe(5))             # → 5


# ============================================================
# 7. **kwargs — BELIEBIG VIELE KEYWORD-ARGUMENTE
# Sammelt Schlüssel=Wert Paare in einem Dictionary
# ============================================================

def profil(**daten):
    #        ↑
    #  ** = sammelt alle key=value Paare in einem Dict
    for key, wert in daten.items():
        print(f"{key}: {wert}")

profil(name="Jan", alter=20, stadt="Düsseldorf")
# → name: Jan
# → alter: 20
# → stadt: Düsseldorf


# ============================================================
# 8. SCOPE (Gültigkeitsbereich)
# Variablen innerhalb einer Funktion existieren nur dort
# ============================================================

x = 10          # globale Variable — überall erreichbar

def zeige():
    y = 5       # lokale Variable — nur INNERHALB der Funktion
    print(x)    # → 10  (globales x ist sichtbar)
    print(y)    # → 5   (lokales y)

zeige()
print(x)        # → 10  (global OK)
# print(y)      → NameError! y existiert nur innerhalb der Funktion

# Merkhilfe:
# Lokale Variable  → nur innerhalb der Funktion
# Globale Variable → überall, aber Funktionen sollten sie nicht verändern


# ============================================================
# 9. FUNKTIONEN ALS RÜCKGABEWERT
# Eine Funktion kann mehrere Werte zurückgeben (als Tuple)
# ============================================================

def min_max(zahlen):
    return min(zahlen), max(zahlen)     # gibt Tuple zurück

kleinste, groesste = min_max([4, 1, 9, 2, 7])  # Tuple Unpacking
print(kleinste)     # → 1
print(groesste)     # → 9


# ============================================================
# 10. LAMBDA — KLEINE ANONYME FUNKTIONEN
# Für einfache Einzeiler — kein def, kein Name
# ============================================================

# Normale Funktion
def verdoppeln(x):
    return x * 2

# Dasselbe als Lambda
verdoppeln_lambda = lambda x: x * 2

print(verdoppeln(5))            # → 10
print(verdoppeln_lambda(5))     # → 10

# Lambda mit mehreren Parametern
addiere = lambda a, b: a + b
print(addiere(3, 4))            # → 7

# Wann Lambda?
# → Kurze Einzeiler, z.B. beim Sortieren
namen = ["Zara", "Anna", "Jan", "Mike"]
namen.sort(key=lambda name: len(name))  # nach Namenslänge sortieren
print(namen)    # → ['Jan', 'Anna', 'Zara', 'Mike']


# ============================================================
# 11. DOCSTRING — FUNKTION DOKUMENTIEREN
# ============================================================

def berechne_flaeche(laenge, breite):
    """
    Berechnet die Fläche eines Rechtecks.

    Parameter:
        laenge (float): Länge des Rechtecks
        breite (float): Breite des Rechtecks

    Rückgabe:
        float: Fläche in Quadratmetern
    """
    return laenge * breite

print(berechne_flaeche(5, 3))   # → 15
print(berechne_flaeche.__doc__) # → zeigt den Docstring an
