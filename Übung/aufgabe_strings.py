# ============================================================
# AUFGABE: Textanalyse
# Konzepte: Strings, Methoden, split(), count(), f-Strings
# ============================================================
#
# Ziel: Du analysierst einen Text und gibst Statistiken aus.
# ============================================================


text = """Python ist eine einfache und mächtige Programmiersprache.
Sie eignet sich ideal für Einsteiger und erfahrene Entwickler.
Python wird in der Datenwissenschaft, Webentwicklung und Automatisierung eingesetzt."""


# ============================================================
# SCHRITT 1: Grundlegende Informationen
# ============================================================

print("--- Textanalyse ---")
print(f"Zeichen gesamt:  {len(text)}")
print(f"Zeichen (ohne Leerzeichen): {len(text.replace(' ', '').replace(chr(10), ''))}")

# Wörter zählen
woerter = text.split()      # teilt bei Leerzeichen und Zeilenumbrüchen
print(f"Wörter:          {len(woerter)}")

# Zeilen zählen
zeilen = text.strip().split("\n")
print(f"Zeilen:          {len(zeilen)}")


# ============================================================
# SCHRITT 2: Suchen & Ersetzen
# ============================================================

# Wie oft kommt "Python" vor?
anzahl_python = text.count("Python")
print(f"\n'Python' kommt {anzahl_python}x vor")

# Text bereinigen: "Programmiersprache" → "Sprache" ersetzen
text_bereinigt = text.replace("Programmiersprache", "Sprache")
print(f"\nBereinigt:\n{text_bereinigt}")


# ============================================================
# SCHRITT 3: Formatierung
# ============================================================

# Ersten Satz extrahieren (bis zum ersten Punkt)
erster_satz = text.split(".")[0].strip()
print(f"\nErster Satz: {erster_satz}")

# Alle Wörter in Großbuchstaben
print(f"Großbuchstaben: {text.upper()[:50]}...")   # nur erste 50 Zeichen

# Jedes Wort mit Großbuchstabe
print(f"Title-Case: {erster_satz.title()}")


# ============================================================
# SCHRITT 4: Wort-Häufigkeit der 5 häufigsten Wörter
# ============================================================

print("\n--- Häufige Wörter ---")

# Wörter bereinigen (Punkte, Kommas entfernen, alles klein)
import string
woerter_bereinigt = []
for wort in woerter:
    wort_sauber = wort.strip(string.punctuation).lower()
    if wort_sauber:     # leere Strings ignorieren
        woerter_bereinigt.append(wort_sauber)

# Häufigkeit zählen
haeufigkeit = {}
for wort in woerter_bereinigt:
    haeufigkeit[wort] = haeufigkeit.get(wort, 0) + 1

# Nach Häufigkeit sortieren und Top 5 ausgeben
sortiert = sorted(haeufigkeit.items(), key=lambda x: x[1], reverse=True)
for wort, anzahl in sortiert[:5]:
    print(f"  {wort}: {anzahl}x")


# ============================================================
# BONUS: Palindrom-Check
# Ist ein Wort vorwärts und rückwärts gleich?
# ============================================================

def ist_palindrom(wort):
    wort = wort.lower()
    return wort == wort[::-1]   # Original == rückwärts?

print("\n--- Palindrom-Check ---")
for wort in ["Rentner", "Anna", "Python", "Lagerregal", "Jan"]:
    status = "✓ Palindrom" if ist_palindrom(wort) else "✗ kein Palindrom"
    print(f"  {wort}: {status}")
