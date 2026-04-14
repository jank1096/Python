import re

raw_logs = [
    "2026-04-09 10:01:22 [ERROR] User: ID_425 - Verbindung fehlgeschlagen",
    "Anmerkung: Wartung wurde durchgeführt",
    "2026-04-09 10:05:15 [INFO] User: ID_102 - Login erfolgreich",
    "2026-04-09 10:10:45 [ERROR] User: ID_425 - Timeout beim Laden",
    "KRITISCHER FEHLER: Stromausfall",
    "2026-04-09 10:15:00 [ERROR] User: ID_999 - Datenbank nicht erreichbar"
]

#1 Regex
muster = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(ERROR|INFO)\] User: ID_(\d+) - (.+)"

#2 Loop & Aufzählungen
fehler_liste = []
fehler_zaehler = {}   

for i, zeile in enumerate(raw_logs):

    treffer = re.match(muster, zeile)
    if not treffer:
        print(f"Zeile {i} wird übersprungen: {zeile}")
        continue    

#3 Daten sammeln & Filtern
    zeitstempel = treffer.group(1) 
    level       = treffer.group(2)    
    user_id     = treffer.group(3)    
    nachricht   = treffer.group(4)    

    if level == "ERROR":
        fehler_liste.append({
            "zeit": zeitstempel,
            "user": user_id,
            "nachricht": nachricht
        })
        fehler_zaehler[user_id] = fehler_zaehler.get(user_id, 0) + 1

#4 FORMATIERTE AUSGABE
print()
print("FEHLER-BERICHT")
print("Insgesamt %d Zeilen analysiert." % len(raw_logs))
fehler_ids = list(fehler_zaehler.keys())
print("Gefundene Fehler-IDs: {}".format(fehler_ids))


print()
print("Details:")
for f in fehler_liste:
    uhrzeit = f["zeit"][11:]
    print(f"[{uhrzeit}] User {f['user']} meldete: {f['nachricht']}")