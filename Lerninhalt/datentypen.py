# ============================================================
# DATENTYPEN (Data Types)
# Python erkennt den Typ automatisch — du musst ihn nicht angeben.
# Mit type() kannst du jederzeit nachschauen, welchen Typ ein Wert hat.
# ============================================================


# ============================================================
# 1. ÜBERSICHT DER WICHTIGSTEN TYPEN
# ============================================================

#  int    → ganze Zahl          42, -7, 0
#  float  → Kommazahl           3.14, -0.5
#  str    → Text                "Hallo", 'Welt'
#  bool   → Wahrheitswert       True, False
#  list   → veränderliche Liste [1, 2, 3]
#  tuple  → unveränderlich      (1, 2, 3)
#  set    → keine Duplikate     {1, 2, 3}
#  dict   → Schlüssel → Wert    {"name": "Jan"}
#  None   → kein Wert           None


# ============================================================
# 2. INT (Ganzzahl)
# ============================================================

a = 10
b = -3
c = 0

print(type(a))      # → <class 'int'>
print(a + b)        # → 7
print(a * b)        # → -30
print(a // 3)       # → 3   (Ganzzahldivision — Ergebnis ohne Rest)
print(a % 3)        # → 1   (Modulo — nur der Rest)
print(a ** 2)       # → 100 (Potenz)

# Merkhilfe:
# //  → wie normale Division, aber Nachkommastellen werden abgeschnitten
# %   → gibt nur den REST zurück (z.B. 10 % 3 → 1, weil 3*3=9, Rest=1)


# ============================================================
# 3. FLOAT (Kommazahl)
# ============================================================

x = 3.14
y = -0.5
z = 2.0         # ist ein float, nicht int!

print(type(x))      # → <class 'float'>
print(x + y)        # → 2.64
print(10 / 3)       # → 3.3333...  (/ gibt immer float zurück!)
print(10 // 3)      # → 3          (// gibt int zurück)

# Runden
print(round(3.14159, 2))    # → 3.14   (auf 2 Nachkommastellen)
print(round(3.7))           # → 4      (auf ganze Zahl)


# ============================================================
# 4. STR (Text / String)
# ============================================================

name = "Jan"
stadt = 'Düsseldorf'    # einfache oder doppelte Anführungszeichen — beides OK

print(type(name))       # → <class 'str'>
print(len(name))        # → 3   (Anzahl Zeichen)
print(name[0])          # → J   (erstes Zeichen, Index 0)
print(name[-1])         # → n   (letztes Zeichen)

# f-String — Variablen direkt in Text einbauen
alter = 20
print(f"Ich bin {name} und {alter} Jahre alt.")
# → Ich bin Jan und 20 Jahre alt.

# Strings verbinden
begruessung = "Hallo " + name + "!"
print(begruessung)      # → Hallo Jan!


# ============================================================
# 5. BOOL (Wahrheitswert)
# ============================================================

ist_student = True
hat_auto = False

print(type(ist_student))    # → <class 'bool'>
print(ist_student)          # → True
print(not ist_student)      # → False  (umkehren)

# Bool entsteht bei Vergleichen
print(10 > 5)           # → True
print(10 == 10)         # → True
print(10 != 5)          # → True
print(10 < 3)           # → False

# Bool in if-Bedingungen
if ist_student:
    print("Rabatt!")    # → Rabatt!

# Zahlen als Bool: 0 ist False, alles andere ist True
print(bool(0))          # → False
print(bool(1))          # → True
print(bool(-5))         # → True
print(bool(""))         # → False  (leerer String ist False)
print(bool("Hallo"))    # → True


# ============================================================
# 6. NONE (kein Wert)
# ============================================================

ergebnis = None
print(ergebnis)         # → None
print(type(ergebnis))   # → <class 'NoneType'>

# None prüfen — immer mit "is", nicht mit "=="
if ergebnis is None:
    print("Kein Wert vorhanden")

# Wann tritt None auf?
# → Wenn eine Funktion nichts zurückgibt (kein return)
# → Als Platzhalter für "noch kein Wert"


# ============================================================
# 7. TYPUMWANDLUNG (Type Casting)
# ============================================================

# str → int
zahl_text = "42"
zahl_int = int(zahl_text)
print(zahl_int + 8)     # → 50

# int → str
alter = 20
text = "Ich bin " + str(alter) + " Jahre alt."
print(text)             # → Ich bin 20 Jahre alt.

# int/str → float
print(float(3))         # → 3.0
print(float("3.14"))    # → 3.14

# float → int (Nachkommastellen werden abgeschnitten, nicht gerundet!)
print(int(3.9))         # → 3   (NICHT 4!)
print(int(-3.9))        # → -3  (NICHT -4!)

# Merkhilfe:
# int()   → Umwandlung in ganze Zahl (Nachkommastellen weg)
# float() → Umwandlung in Kommazahl
# str()   → Umwandlung in Text
# bool()  → Umwandlung in True/False


# ============================================================
# 8. VERGLEICH: WELCHER TYP WANN?
# ============================================================

# int    → zählen, indizieren, Ganzzahl-Arithmetik
#          alter = 20, index = 0, anzahl = 5

# float  → Messwerte, Berechnungen mit Komma
#          preis = 9.99, temperatur = 36.6

# str    → Text, Namen, Eingaben, Ausgaben
#          name = "Jan", befehl = "quit"

# bool   → Zustände, Bedingungen, Flags
#          ist_aktiv = True, hat_fehler = False

# None   → "noch kein Wert", optionale Rückgabe
#          ergebnis = None  # wird später gesetzt
