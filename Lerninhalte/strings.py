# ============================================================
# STRINGS (Zeichenketten)
# Ein String ist eine Folge von Zeichen — Text in Python.
# Strings sind UNVERÄNDERLICH — jede Methode gibt einen NEUEN String zurück.
# ============================================================


# ============================================================
# 1. STRING ERSTELLEN
# ============================================================

s1 = "Hallo Welt"        # doppelte Anführungszeichen
s2 = 'Hallo Welt'        # einfache — beides gleich
s3 = """Erster Satz.     # mehrzeiliger String (drei Anführungszeichen)
Zweiter Satz.
Dritter Satz."""

print(type(s1))          # → <class 'str'>
print(len(s1))           # → 10  (Anzahl Zeichen inkl. Leerzeichen)


# ============================================================
# 2. ZEICHEN ABRUFEN & SLICING
# Funktioniert wie bei Listen — Strings haben Indizes
# ============================================================

s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5   (positiv)
#   -6 -5 -4 -3 -2 -1   (negativ)

print(s[0])             # → P    erstes Zeichen
print(s[-1])            # → n    letztes Zeichen
print(s[2])             # → t    drittes Zeichen

# Slicing — s[start : end : step]
print(s[1:4])           # → yth    Index 1 bis 3
print(s[:3])            # → Pyt    Anfang bis Index 2
print(s[3:])            # → hon    ab Index 3 bis Ende
print(s[::-1])          # → nohtyP rückwärts


# ============================================================
# 3. GROSS/KLEIN SCHREIBEN
# ============================================================

text = "hallo welt"

print(text.upper())         # → HALLO WELT    alles groß
print(text.lower())         # → hallo welt    alles klein
print(text.capitalize())    # → Hallo welt    nur erstes Zeichen groß
print(text.title())         # → Hallo Welt    jedes Wort groß

# Merke: der ORIGINAL-String bleibt unverändert!
print(text)                 # → hallo welt  (unverändert)


# ============================================================
# 4. SUCHEN & PRÜFEN
# ============================================================

s = "Ich lerne Python programmieren"

print("Python" in s)            # → True   (ist enthalten?)
print("Java" in s)              # → False

print(s.startswith("Ich"))      # → True   (beginnt mit "Ich"?)
print(s.endswith("ieren"))      # → True   (endet mit "ieren"?)

print(s.find("Python"))         # → 11     (Position des ersten Treffers)
print(s.find("Java"))           # → -1     (nicht gefunden → -1, kein Fehler)

print(s.count("e"))             # → 3      (wie oft kommt "e" vor?)

# find() vs. index():
# find()  → gibt -1 zurück wenn nicht gefunden
# index() → gibt Fehler wenn nicht gefunden


# ============================================================
# 5. ERSETZEN & BEREINIGEN
# ============================================================

s = "  Hallo Welt  "

# Leerzeichen entfernen
print(s.strip())        # → "Hallo Welt"    links und rechts
print(s.lstrip())       # → "Hallo Welt  "  nur links
print(s.rstrip())       # → "  Hallo Welt"  nur rechts

# Ersetzen
s2 = "Ich mag Äpfel. Äpfel sind lecker."
print(s2.replace("Äpfel", "Birnen"))
# → Ich mag Birnen. Birnen sind lecker.  (alle Vorkommen!)

print(s2.replace("Äpfel", "Birnen", 1))
# → Ich mag Birnen. Äpfel sind lecker.  (nur erstes Vorkommen)


# ============================================================
# 6. AUFTEILEN & VERBINDEN
# ============================================================

# split() — String in Liste aufteilen
satz = "Jan,Anna,Tom,Sara"
namen = satz.split(",")
print(namen)            # → ['Jan', 'Anna', 'Tom', 'Sara']

satz2 = "Ich lerne Python"
woerter = satz2.split()     # ohne Argument → trennt bei Leerzeichen
print(woerter)          # → ['Ich', 'lerne', 'Python']

# join() — Liste zu String zusammenfügen
# Muster: "Trennzeichen".join(liste)
print(", ".join(namen))     # → Jan, Anna, Tom, Sara
print(" | ".join(namen))    # → Jan | Anna | Tom | Sara
print("".join(namen))       # → JanAnnaTomSara  (kein Trennzeichen)


# ============================================================
# 7. F-STRINGS (empfohlen ab Python 3.6)
# Variablen und Ausdrücke direkt in Text einbauen
# ============================================================

name = "Jan"
alter = 20
preis = 9.987

print(f"Ich bin {name} und {alter} Jahre alt.")
# → Ich bin Jan und 20 Jahre alt.

print(f"Doppeltes Alter: {alter * 2}")
# → Doppeltes Alter: 40

# Zahlenformatierung in f-Strings
print(f"Preis: {preis:.2f} €")      # → Preis: 9.99 €   (2 Nachkommastellen)
print(f"Preis: {preis:.0f} €")      # → Preis: 10 €     (keine Nachkommastellen)
print(f"Zahl: {1234567:,}")         # → Zahl: 1,234,567 (Tausender-Trennzeichen)


# ============================================================
# 8. NÜTZLICHE PRÜFMETHODEN
# ============================================================

print("123".isdigit())          # → True    (nur Ziffern?)
print("abc".isalpha())          # → True    (nur Buchstaben?)
print("abc123".isalnum())       # → True    (Buchstaben oder Ziffern?)
print("   ".isspace())          # → True    (nur Leerzeichen?)
print("Hallo".islower())        # → False   (alles klein?)
print("HALLO".isupper())        # → True    (alles groß?)


# ============================================================
# 9. SONDERZEICHEN (Escape Sequences)
# ============================================================

print("Zeile 1\nZeile 2")       # \n → Zeilenumbruch
print("Spalte1\tSpalte2")       # \t → Tabulator
print("Er sagt: \"Hallo\"")     # \" → Anführungszeichen im String
print("Backslash: \\")          # \\ → ein Backslash

# Raw String — Backslashes werden nicht interpretiert
pfad = r"C:\Users\Jan\Dokumente"
print(pfad)         # → C:\Users\Jan\Dokumente  (kein \U oder \J als Sonderzeichen)


# ============================================================
# 10. STRINGS SIND UNVERÄNDERLICH
# Jede Methode gibt einen NEUEN String zurück — der Original bleibt gleich!
# ============================================================

original = "hallo"
gross = original.upper()    # gibt neuen String zurück

print(original)     # → hallo   (unverändert!)
print(gross)        # → HALLO   (neuer String)

# Wenn du den Wert ändern willst, überschreibe die Variable:
original = original.upper()
print(original)     # → HALLO
