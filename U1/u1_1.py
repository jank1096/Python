# ============================================================
# GRUNDLAGEN — Variablen, Datentypen, Operatoren
# ============================================================


# ============================================================
# 1. DATENTYPEN
# ============================================================

PI = 3.14               # float  — Kommazahl
x = 3                   # int    — ganzzahlig
z = 5.4                 # float
c = 3 + 4j              # complex — komplexe Zahl (j = imaginäre Einheit)
isWahr = True           # bool   — True oder False
ss = "Hello"            # str    — Text

t = (1, 2, 3)           # tuple  — unveränderlich
l = [2, "hi", 3, False] # list   — veränderlich
set_var = {1, 2, 3, 4}  # set    — keine Duplikate, keine Reihenfolge

# dictionary: Schlüssel → Wert
person = {"name": "Ali", "age": 39, "isAlive": True}


# ============================================================
# 2. VARIABLEN VERÄNDERN (Zuweisungsoperatoren)
# ============================================================

number = 5
number += 7     # number = number + 7  → 12
number -= 2     # → 10
number *= 3     # → 30
number /= 10    # → 3.0   (Division ergibt immer float!)
print(number)   # → 3.0


# ============================================================
# 3. VERGLEICHSOPERATOREN
# Geben immer True oder False zurück
# ============================================================

print(number == 4)   # → False  (gleich?)
print(number != 4)   # → True   (ungleich?)
print(number > 3)    # → False  (größer?)
print(number < 2)    # → False  (kleiner?)
print(number <= 3)   # → True   (kleiner gleich?)
print(number >= 4)   # → False  (größer gleich?)


# ============================================================
# 4. IDENTITÄTSOPERATOREN: is, is not
# is prüft ob BEIDE auf dasselbe Objekt im Speicher zeigen (nicht nur gleicher Wert!)
# ============================================================

num = number            # num zeigt auf dasselbe Objekt wie number
print(num is number)    # → True   (gleiche Speicheradresse)
print(id(num), id(number))

num += 5                # num zeigt jetzt auf ein NEUES Objekt (3.0 + 5 = 8.0)
print(num is not number)# → True   (verschiedene Speicheradressen)
print(id(num), id(number))


# ============================================================
# 5. MITGLIEDSCHAFTSOPERATOR: in
# Prüft ob ein Wert in einem Container (Liste, String, Tuple, ...) enthalten ist
# ============================================================

vari = "hio"
print(vari in l)        # → False  ("hio" ist nicht in l)

s = "Hello World"
print("Text" in s)      # → False
print("Hello" in s)     # → True


# ============================================================
# 6. LOGISCHE OPERATOREN: and, or, not
#
# and → BEIDE Bedingungen müssen True sein
# or  → EINE Bedingung reicht
# not → kehrt das Ergebnis um
#
# Wahrheitstabelle and:  T+T=T | T+F=F | F+T=F | F+F=F
# Wahrheitstabelle or:   T+T=T | T+F=T | F+T=T | F+F=F
# ============================================================

print(5 > 3 and "a" in l)   # → False  (True and False)
print(5 > 4 and "hi" in l)  # → True   (True and True)

print(5 > 3 or "a" in l)    # → True   (True or False)
print(1 > 4 or "hi" in l)   # → True   (False or True)

print(not(5 > 3 or "a" in l))  # → False  (not True)


# ============================================================
# 7. FUNKTIONEN
# def = definiert eine Funktion
# Funktion mit Rückgabewert (return) → "Funktion"
# Funktion ohne Rückgabewert         → "Prozedur"
# Typannotationen: num1:int → erwartet int, -> int → gibt int zurück
# ============================================================

def print_hw():
    print("Hello World!")


def calculate(num1: int, num2: int) -> int:
    return num1 + num2


print(calculate(1, 2))  # → 3


# ============================================================
# 8. EINFACHER RECHNER (Eingabe + if/elif/else)
# int(input(...)) → Eingabe einlesen und direkt zu int umwandeln
# ============================================================

# Auskommentiert, da input() interaktiv ist:
# num1 = float(input("Erste Zahl: "))
# num2 = float(input("Zweite Zahl: "))
# operator = input("Operator (+, -, *, /): ")
#
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "*":
#     print(num1 * num2)
# else:
#     print("Ungültiger Operator!")


# ============================================================
# 9. LOGIN-BEISPIEL (for-Schleife + if/else + not)
# ============================================================

login_user = ["user123", "admin"]

for user in login_user:
    if not user == "admin":
        print("Access denied!")
    else:
        print("Access granted!")
