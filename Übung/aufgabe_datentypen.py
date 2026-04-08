# ============================================================
# AUFGABE: Persönliches Profil
# Konzepte: Datentypen, Typumwandlung, f-Strings, bool
# ============================================================
#
# Ziel: Du liest simulierte Nutzereingaben (als Strings) ein,
# wandelst sie in die richtigen Typen um und gibst ein
# formatiertes Profil aus.
#
# Alle Eingaben kommen "als String" — so wie bei input()
# ============================================================


# ============================================================
# SCHRITT 1: Eingaben (simuliert — stell dir vor, der User tippt das ein)
# ============================================================

eingabe_name  = "Jan"
eingabe_alter = "20"         # String! Muss zu int umgewandelt werden
eingabe_groesse = "182.5"    # String! Muss zu float umgewandelt werden
eingabe_student = "True"     # String! Muss zu bool umgewandelt werden


# ============================================================
# SCHRITT 2: Typumwandlung
# Wandle jede Eingabe in den richtigen Typ um
# ============================================================

name    = eingabe_name                  # bleibt str
alter   = int(eingabe_alter)            # str → int
groesse = float(eingabe_groesse)        # str → float
# Achtung: bool("True") gibt IMMER True zurück — auch für "False"!
# Richtige Umwandlung für einen bool-String:
student = eingabe_student == "True"     # Vergleich → True oder False

print(type(name))       # → <class 'str'>
print(type(alter))      # → <class 'int'>
print(type(groesse))    # → <class 'float'>
print(type(student))    # → <class 'bool'>


# ============================================================
# SCHRITT 3: Profil ausgeben
# ============================================================

print("\n--- Dein Profil ---")
print(f"Name:    {name}")
print(f"Alter:   {alter} Jahre")
print(f"Größe:   {groesse:.1f} cm")     # 1 Nachkommastelle
print(f"Student: {student}")


# ============================================================
# SCHRITT 4: Einfache Berechnung mit den Werten
# ============================================================

# Renteneintritt in wie vielen Jahren?
renten_alter = 67
jahre_bis_rente = renten_alter - alter
print(f"\nNoch {jahre_bis_rente} Jahre bis zur Rente.")

# Studenten-Rabatt
if student:
    preis_original = 15.00
    preis_rabatt   = preis_original * 0.8   # 20% Rabatt
    print(f"Ticket: {preis_original:.2f} € → mit Studentenrabatt {preis_rabatt:.2f} €")
else:
    print("Kein Studentenrabatt.")


# ============================================================
# BONUS: Was passiert bei falscher Umwandlung?
# ============================================================

# int("abc")    → ValueError: invalid literal
# int("3.14")   → ValueError: can't convert float string to int
# int(float("3.14"))  → erst zu float, dann zu int → 3  (Lösung!)

print(int(float("3.14")))   # → 3
