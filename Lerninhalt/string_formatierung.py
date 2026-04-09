# ============================================================
# String-Formatierung in Python
# ============================================================
# Es gibt 3 Wege, Werte in Strings einzusetzen:
#   1. %-Operator       (alt, aber gut zu kennen)
#   2. .format()        (moderner, flexibler)
#   3. f-Strings        (neueste, kürzeste Variante)
# ============================================================


# ────────────────────────────────────────────────────────────
# 1. %-OPERATOR (wie printf in C)
# ────────────────────────────────────────────────────────────
# Platzhalter im String → Werte werden mit % am Ende eingesetzt
#
#   %s  = String (Text)
#   %d  = Dezimalzahl (ganze Zahl)
#   %f  = Float (Kommazahl)
#   %x  = Hexadezimal (kleinbuchstaben)
#   %X  = Hexadezimal (Großbuchstaben)
#   %o  = Oktal (Basis 8)

name = "Lina"
age = 18

print("Hallo, ich bin %s und %d Jahre alt." % (name, age))
# → Hallo, ich bin Lina und 18 Jahre alt.


# Kommazahlen begrenzen mit %.Nf (N = Nachkommastellen)
PI = 3.141592
print("Pi: %f" % PI)           # → Pi: 3.141592  (Standard: 6 Stellen)
print("Pi: %.2f" % PI)         # → Pi: 3.14      (nur 2 Stellen)


# Spalten ausrichten mit Breiten-Angabe
# %-10s = linksbündig, 10 Zeichen breit
# %5d   = rechtsbündig, 5 Zeichen breit
print("%-10s | %5d" % ("Rosa", 30))     # → Rosa       |    30
print("%-10s | %5d" % ("Steven", 20))   # → Steven     |    20


# Dictionary-Werte einsetzen mit %(key)s
daten = {"stadt": "Koeln", "temp": 22.5}
print("In %(stadt)s sind %(temp).1f Grad." % daten)
# → In Koeln sind 22.5 Grad.


# Hexadezimal: Zahlen als Hex-Werte ausgeben
zahl = 255
print("Hex klein: %x" % zahl)    # → ff
print("Hex gross: %X" % zahl)    # → FF
print("Mit Prefix: %#x" % zahl)  # → 0xff
print("Mit Prefix: %#X" % zahl)  # → 0XFF

# Praxis-Beispiel: RGB-Farbcode zusammenbauen
# %02X = 2 Stellen, mit führender Null, Großbuchstaben
r, g, b = 255, 165, 0
print("Farbe: #%02X%02X%02X" % (r, g, b))  # → #FFA500 (Orange!)


# ────────────────────────────────────────────────────────────
# 2. .format() (ab Python 2.6)
# ────────────────────────────────────────────────────────────
# Platzhalter: {} im String → .format() setzt Werte ein
# Vorteil: Flexibler als %, Reihenfolge änderbar

# Einfach: Reihenfolge wie angegeben
print("Ich bin {} und {} Jahre alt.".format("Lina", 18))

# Mit Index: {0} = erstes Argument, {1} = zweites
print("{1} ist älter als {0}".format("Ali", "Salma"))
# → Salma ist älter als Ali

# Wiederholung: gleichen Wert mehrfach nutzen
print("{0} {0} {0}!".format("Stopp"))
# → Stopp Stopp Stopp!

# Hex-Formatierung auch hier möglich
print("Hex: {:#x}".format(255))  # → Hex: 0xff

# Benannte Argumente (wie Variablen)
print("{name} ist {alter} Jahre alt".format(name="Rosa", alter=20))

# Dictionary & Tuple-Zugriff direkt im Platzhalter
person = {"name": "Max", "alter": 15}
punkt = (20, 10)

print("Name: {p[name]}".format(p=person))       # → Name: Max
print("X-Koordinate: {pt[0]}".format(pt=punkt))  # → X-Koordinate: 20


# ────────────────────────────────────────────────────────────
# 3. f-STRINGS (ab Python 3.6) — der beste Weg!
# ────────────────────────────────────────────────────────────
# f vor dem String → Python-Code direkt in {} schreiben
# Kürzer, lesbarer, schneller als die anderen Methoden

print(f"Ich bin {name} und {age} Jahre alt.")
print(f"Pi auf 2 Stellen: {PI:.2f}")
print(f"Hex: {255:#X}")
print(f"RGB: #{r:02X}{g:02X}{b:02X}")

# Rechnen direkt im f-String
preis = 19.99
print(f"Mit MwSt: {preis * 1.19:.2f} Euro")  # → 23.79 Euro


# ============================================================
# MERKSATZ
# ============================================================
# %-Operator  → kennen (kommt in altem Code vor)
# .format()   → kennen (kommt in Libraries vor)
# f-Strings   → BENUTZEN (kürzer, schneller, lesbarer)
#
# Formatierung:  :.2f = 2 Nachkommastellen
#                :02X = 2-stellig Hex mit führender Null
#                :>10 = rechtsbündig, 10 Zeichen breit
# ============================================================
