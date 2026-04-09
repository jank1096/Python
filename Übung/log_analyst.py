import re

# ============================================================
# DER AUTOMATISIERTE LOG-DATEI-ANALYST
# ============================================================
# Aufgabe: Eine "schmutzige" Log-Datei säubern und einen
#          Fehlerbericht erstellen.
# Themen:  Regex, enumerate, Dictionaries, 3 Formatierungsarten
# ============================================================


# ────────────────────────────────────────────────────────────
# DIE ROHDATEN (unsere "schmutzige" Log-Datei)
# ────────────────────────────────────────────────────────────
# Manche Zeilen haben das richtige Format, manche nicht.
# Unser Job: die guten erkennen, die schlechten überspringen.

raw_logs = [
    "2026-04-09 10:01:22 [ERROR] User: ID_425 - Verbindung fehlgeschlagen",
    "Anmerkung: Wartung wurde durchgeführt",
    "2026-04-09 10:05:15 [INFO] User: ID_102 - Login erfolgreich",
    "2026-04-09 10:10:45 [ERROR] User: ID_425 - Timeout beim Laden",
    "KRITISCHER FEHLER: Stromausfall",
    "2026-04-09 10:15:00 [ERROR] User: ID_999 - Datenbank nicht erreichbar"
]


# ────────────────────────────────────────────────────────────
# SCHRITT 1: DAS REGEX-MUSTER BAUEN
# ────────────────────────────────────────────────────────────
# Wir wollen dieses Format erkennen:
#   "2026-04-09 10:01:22 [ERROR] User: ID_425 - Verbindung fehlgeschlagen"
#
# Zerlegt in Teile:
#   2026-04-09 10:01:22    → Datum + Uhrzeit  (Zeitstempel)
#   [ERROR]                → Level in eckigen Klammern
#   ID_425                 → User-ID (Zahl nach ID_)
#   Verbindung fehlgeschl. → Nachricht (alles nach " - ")
#
# Das Muster mit Gruppen (...):
#
#   (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})   ← Gruppe 1: Zeitstempel
#       \d{4}  = 4 Ziffern (Jahr)
#       -      = Bindestrich
#       \d{2}  = 2 Ziffern (Monat, Tag, Stunde, Minute, Sekunde)
#
#   \[(ERROR|INFO)\]                           ← Gruppe 2: Level
#       \[     = echte eckige Klammer (\ weil [ sonst Regex-Syntax ist)
#       ERROR|INFO = entweder "ERROR" oder "INFO"
#
#   ID_(\d+)                                   ← Gruppe 3: User-ID (nur die Zahl)
#       \d+    = eine oder mehr Ziffern
#
#   - (.+)                                     ← Gruppe 4: Nachricht (alles danach)
#       .+     = ein oder mehr beliebige Zeichen

muster = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(ERROR|INFO)\] User: ID_(\d+) - (.+)"


# ────────────────────────────────────────────────────────────
# SCHRITT 2: LOGS DURCHGEHEN MIT ENUMERATE
# ────────────────────────────────────────────────────────────
# enumerate(liste) gibt uns: (index, wert) für jedes Element
#
# Beispiel:
#   for i, zeile in enumerate(["a", "b", "c"]):
#       print(i, zeile)
#   → 0 a
#   → 1 b
#   → 2 c

fehler_liste = []     # Hier sammeln wir alle ERROR-Einträge als Dictionaries
fehler_zaehler = {}   # Hier zählen wir Fehler pro User-ID

for i, zeile in enumerate(raw_logs):

    # re.match() prüft ob die Zeile zum Muster passt
    treffer = re.match(muster, zeile)

    # Kein Treffer? → Zeile überspringen und Warnung ausgeben
    if not treffer:
        print(f"Zeile {i} wird übersprungen: {zeile}")
        continue    # continue = Rest der Schleife überspringen, nächste Zeile

    # ────────────────────────────────────────────────────────
    # SCHRITT 3: DATEN EXTRAHIEREN
    # ────────────────────────────────────────────────────────
    # treffer.group(1) = erste Klammer  → Zeitstempel
    # treffer.group(2) = zweite Klammer → Level
    # treffer.group(3) = dritte Klammer → User-ID
    # treffer.group(4) = vierte Klammer → Nachricht

    zeitstempel = treffer.group(1)    # "2026-04-09 10:01:22"
    level       = treffer.group(2)    # "ERROR" oder "INFO"
    user_id     = treffer.group(3)    # "425"
    nachricht   = treffer.group(4)    # "Verbindung fehlgeschlagen"

    # Nur ERROR-Einträge sammeln (INFO ignorieren wir)
    if level == "ERROR":

        # Als Dictionary in die Liste packen
        fehler_liste.append({
            "zeit": zeitstempel,
            "user": user_id,
            "nachricht": nachricht
        })

        # Fehler pro User zählen
        # .get(key, 0) → gibt den Wert zurück, oder 0 wenn der Key nicht existiert
        fehler_zaehler[user_id] = fehler_zaehler.get(user_id, 0) + 1


# ────────────────────────────────────────────────────────────
# SCHRITT 4: FORMATIERTE AUSGABE (alle 3 Methoden)
# ────────────────────────────────────────────────────────────

print()
print("--- FEHLER-BERICHT ---")

# %-Formatierung: Gesamtzahl der Zeilen
print("Insgesamt %d Zeilen analysiert." % len(raw_logs))

# .format(): Liste der User-IDs die Fehler hatten
# list(fehler_zaehler.keys()) → alle Keys aus dem Zähler-Dict als Liste
fehler_ids = list(fehler_zaehler.keys())
print("Gefundene Fehler-IDs: {}".format(fehler_ids))

# f-Strings: Saubere Tabelle der Fehler
print()
print("Details:")
for f in fehler_liste:
    # Nur die Uhrzeit extrahieren (ab Zeichen 11, also nach "2026-04-09 ")
    uhrzeit = f["zeit"][11:]
    print(f"[{uhrzeit}] User {f['user']} meldete: {f['nachricht']}")

# Bonus: Fehler pro User anzeigen
print()
print("Fehler pro User:")
for uid, anzahl in fehler_zaehler.items():
    print(f"  User {uid}: {anzahl}x")
