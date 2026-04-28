# ============================================================
# AUFGABE: Taschenrechner & Zahlenspiele
# Konzepte: Arithmetische, logische und Vergleichsoperatoren
# ============================================================


# ============================================================
# SCHRITT 1: Einfacher Taschenrechner
# ============================================================

a = 17
b = 5

print("--- Grundrechenarten ---")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b:.2f}")    # Division → float
print(f"{a} // {b} = {a // b}")        # Ganzzahldivision
print(f"{a} % {b}  = {a % b}")         # Rest
print(f"{a} ** {b} = {a ** b}")        # Potenz


# ============================================================
# SCHRITT 2: Modulo — praktische Anwendungen
# ============================================================

print("\n--- Modulo Anwendungen ---")

# Gerade/Ungerade prüfen
for zahl in range(1, 11):
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade")
    else:
        print(f"{zahl} ist ungerade")

# Jede 3. Zahl aus einer Liste
zahlen = list(range(1, 21))
jede_dritte = [z for z in zahlen if z % 3 == 0]
print(f"\nVielfache von 3 bis 20: {jede_dritte}")

# Tage in Wochen umrechnen
tage = 100
wochen = tage // 7
rest_tage = tage % 7
print(f"\n{tage} Tage = {wochen} Wochen und {rest_tage} Tage")


# ============================================================
# SCHRITT 3: Vergleichs- und logische Operatoren
# ============================================================

print("\n--- Zugangskontrolle ---")

alter = 17
hat_begleitung = True

# Unter 18 UND ohne Begleitung → kein Zugang
if alter >= 18 or hat_begleitung:
    print("Zugang erlaubt")
else:
    print("Kein Zutritt")

# Rabatt-Logik
ist_student = True
ist_mitglied = False
preis = 20.00

if ist_student and ist_mitglied:
    rabatt = 0.30       # 30%
elif ist_student or ist_mitglied:
    rabatt = 0.15       # 15%
else:
    rabatt = 0.00

endpreis = preis * (1 - rabatt)
print(f"Preis: {preis:.2f} € → nach Rabatt: {endpreis:.2f} €")


# ============================================================
# SCHRITT 4: Zuweisungsoperatoren
# ============================================================

print("\n--- Punktekonto ---")

punkte = 0

punkte += 10    # Aufgabe gelöst
print(f"Aufgabe gelöst: {punkte} Punkte")

punkte += 5     # Bonus
print(f"Bonus erhalten: {punkte} Punkte")

punkte -= 3     # Strafe
print(f"Strafe abgezogen: {punkte} Punkte")

punkte *= 2     # Verdopplung
print(f"Doppelt-Event: {punkte} Punkte")


# ============================================================
# SCHRITT 5: Bitweise Operatoren — Berechtigungssystem
# Klassisches Anwendungsbeispiel für & und |
# ============================================================

print("\n--- Berechtigungssystem ---")

# Berechtigungen als Bit-Flags
LESEN     = 0b001   # 1
SCHREIBEN = 0b010   # 2
AUSFUEHREN= 0b100   # 4

# Benutzer mit Lesen + Schreiben
user_rechte = LESEN | SCHREIBEN     # 001 | 010 = 011 = 3
print(f"Benutzerrechte: {bin(user_rechte)} ({user_rechte})")

# Prüfen ob Berechtigung vorhanden (& → Bit ist gesetzt wenn Ergebnis > 0)
print(f"Darf lesen:      {bool(user_rechte & LESEN)}")       # → True
print(f"Darf schreiben:  {bool(user_rechte & SCHREIBEN)}")   # → True
print(f"Darf ausführen:  {bool(user_rechte & AUSFUEHREN)}")  # → False
