# ============================================================
# OPERATOREN
# Operatoren sind Symbole, mit denen Python Werte verknüpft oder vergleicht.
# ============================================================


# ============================================================
# 1. ARITHMETISCHE OPERATOREN (Rechnen)
# ============================================================

a = 10
b = 3

print(a + b)    # → 13   Addition
print(a - b)    # → 7    Subtraktion
print(a * b)    # → 30   Multiplikation
print(a / b)    # → 3.333...  Division (immer float!)
print(a // b)   # → 3    Ganzzahldivision (Rest wird abgeschnitten)
print(a % b)    # → 1    Modulo (nur der Rest: 10 = 3*3 + 1)
print(a ** b)   # → 1000 Potenz (10 hoch 3)

# Merkhilfe zu // und %:
# 10 // 3  →  wie viele Male passt 3 komplett in 10?  → 3
# 10 %  3  →  was bleibt über?                        → 1
# Probe: 3 * 3 + 1 = 10 ✓


# ============================================================
# 2. VERGLEICHSOPERATOREN (Vergleichen → gibt immer True oder False)
# ============================================================

x = 5
y = 10

print(x == y)   # → False   gleich?
print(x != y)   # → True    ungleich?
print(x < y)    # → True    kleiner?
print(x > y)    # → False   größer?
print(x <= 5)   # → True    kleiner oder gleich?
print(x >= 10)  # → False   größer oder gleich?

# Vergleiche werden oft in if-Bedingungen verwendet:
if x < y:
    print("x ist kleiner")      # → x ist kleiner


# ============================================================
# 3. LOGISCHE OPERATOREN (Bedingungen verknüpfen)
# ============================================================

alter = 20
hat_ausweis = True

# and → BEIDE müssen True sein
if alter >= 18 and hat_ausweis:
    print("Zutritt erlaubt")    # → Zutritt erlaubt

# or → MINDESTENS EINE muss True sein
ist_student = False
hat_rabattcode = True

if ist_student or hat_rabattcode:
    print("Rabatt!")             # → Rabatt!

# not → dreht den Wahrheitswert um
gesperrt = False
if not gesperrt:
    print("Login möglich")       # → Login möglich

# Wahrheitstabelle:
# True  and True  → True
# True  and False → False
# False and False → False

# True  or True   → True
# True  or False  → True
# False or False  → False

# not True  → False
# not False → True


# ============================================================
# 4. ZUWEISUNGSOPERATOREN (Wert ändern und zuweisen)
# ============================================================

n = 10

n += 5      # n = n + 5  → n ist jetzt 15
print(n)    # → 15

n -= 3      # n = n - 3  → n ist jetzt 12
print(n)    # → 12

n *= 2      # n = n * 2  → n ist jetzt 24
print(n)    # → 24

n //= 4     # n = n // 4 → n ist jetzt 6
print(n)    # → 6

n **= 2     # n = n ** 2 → n ist jetzt 36
print(n)    # → 36

n %= 10     # n = n % 10 → n ist jetzt 6
print(n)    # → 6


# ============================================================
# 5. BINÄRE (BITWEISE) OPERATOREN
# Arbeiten auf Bit-Ebene — die Zahlen werden in 0 und 1 umgewandelt
# ============================================================

# Zur Erinnerung: Dezimalzahlen als Binärzahlen
#  5  in Binär: 0101
#  3  in Binär: 0011
#  12 in Binär: 1100
#  10 in Binär: 1010

a = 5   # 0101
b = 3   # 0011

# & (AND) — Bit ist 1 nur wenn BEIDE Bits 1 sind
#   0101
# & 0011
# ------
#   0001  → 1
print(a & b)    # → 1

# | (OR) — Bit ist 1 wenn MINDESTENS EINES der Bits 1 ist
#   0101
# | 0011
# ------
#   0111  → 7
print(a | b)    # → 7

# ^ (XOR) — Bit ist 1 wenn die Bits VERSCHIEDEN sind
#   0101
# ^ 0011
# ------
#   0110  → 6
print(a ^ b)    # → 6

# ~ (NOT) — dreht alle Bits um (Formel: ~n = -(n+1))
print(~a)       # → -6   (-(5+1))
print(~b)       # → -4   (-(3+1))

# << (LEFT SHIFT) — Bits nach links verschieben = * 2 pro Schritt
#   0101 << 1  →  1010  → 10  (= 5 * 2)
#   0101 << 2  →  10100 → 20  (= 5 * 4)
print(a << 1)   # → 10
print(a << 2)   # → 20

# >> (RIGHT SHIFT) — Bits nach rechts verschieben = // 2 pro Schritt
#   0101 >> 1  →  0010  → 2   (= 5 // 2)
print(a >> 1)   # → 2

# Merkhilfe zu bitweisen Operatoren:
# &   → AND:  1 nur wenn BEIDE 1
# |   → OR:   1 wenn MINDESTENS EINES 1
# ^   → XOR:  1 wenn VERSCHIEDENE Bits
# ~   → NOT:  dreht alles um
# <<  → mal 2 (pro Stelle)
# >>  → geteilt durch 2 (pro Stelle)

# Wann werden binäre Operatoren benutzt?
# → Flags und Berechtigungen (z.B. Lesen=1, Schreiben=2, Ausführen=4)
# → Schnelle Multiplikation/Division durch Zweierpotenzen
# → Low-Level-Programmierung, Hardware-Kommunikation


# ============================================================
# 6. IDENTITÄTS- UND ZUGEHÖRIGKEITSOPERATOREN
# ============================================================

# is / is not — prüft ob GLEICHE OBJEKTE (nicht nur gleicher Wert)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # → True   (gleicher WERT)
print(a is b)       # → False  (verschiedene OBJEKTE im Speicher)
print(a is c)       # → True   (c zeigt auf dasselbe Objekt wie a)

# Merkhilfe:
# ==   → gleicher Inhalt?
# is   → dasselbe Objekt? (selbe Adresse im Speicher)
# None immer mit "is" prüfen: if x is None

# in / not in — prüft ob Wert enthalten ist
zahlen = [1, 2, 3, 4, 5]
print(3 in zahlen)          # → True
print(9 in zahlen)          # → False
print(9 not in zahlen)      # → True

text = "Hallo Welt"
print("Hallo" in text)      # → True
print("Python" not in text) # → True


# ============================================================
# 7. OPERATOR PRIORITÄT (Reihenfolge)
# Wie in der Mathematik: Punkt vor Strich, Klammern zuerst
# ============================================================

# Reihenfolge (höchste zuerst):
# ()        Klammern
# **        Potenz
# ~         Bitweise NOT
# * / // %  Multiplikation, Division
# + -       Addition, Subtraktion
# << >>     Shift
# &         Bitweise AND
# ^         Bitweise XOR
# |         Bitweise OR
# == != < > <= >=   Vergleiche
# not       Logisches NOT
# and       Logisches AND
# or        Logisches OR

print(2 + 3 * 4)        # → 14   (* vor +)
print((2 + 3) * 4)      # → 20   (Klammern zuerst)
print(2 ** 3 ** 2)      # → 512  (** von rechts: 3**2=9, dann 2**9=512)

# Im Zweifel: Klammern setzen! Dann ist es immer eindeutig.
