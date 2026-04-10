import re
from datetime import datetime
from zoneinfo import ZoneInfo

# ============================================================
# DAS GLOBALE EVENT-MANAGEMENT-SYSTEM
# ============================================================
# Aufgabe: Unsaubere Meeting-Strings säubern, in echte
#          datetime-Objekte umwandeln, in UTC umrechnen und
#          als Tabelle ausgeben.
# Themen:  Regex, enumerate, datetime, ZoneInfo,
#          3 Formatierungsarten (%, .format(), f-Strings)
# ============================================================


# ────────────────────────────────────────────────────────────
# DIE ROHDATEN (unsere "schmutzige" Meeting-Liste)
# ────────────────────────────────────────────────────────────
# Manche Zeilen passen zum Muster, manche nicht.
# Unser Job: die guten erkennen, die schlechten überspringen.

raw_meetings = [
    "MEET: Projekt-Kickoff ; DATE: 2026-05-10 14:00 ; TZ: Europe/Berlin",
    "NOTIZ: Kaffeepause ignorieren",  # Ungültig
    "MEET: Update-Call ; DATE: 2026-05-10 10:00 ; TZ: America/New_York",
    "MEET: Tech-Check ; DATE: 2026-05-10 09:00 ; TZ: Asia/Tokyo"
]


# ────────────────────────────────────────────────────────────
# SCHRITT 1: DAS REGEX-MUSTER BAUEN
# ────────────────────────────────────────────────────────────
# Wir wollen dieses Format erkennen:
#   "MEET: Projekt-Kickoff ; DATE: 2026-05-10 14:00 ; TZ: Europe/Berlin"
#
# Zerlegt in Teile:
#   Projekt-Kickoff        → Name des Meetings
#   2026-05-10 14:00       → Datum + Uhrzeit
#   Europe/Berlin          → Zeitzone
#
# Das Muster mit Gruppen (...):
#
#   MEET: (.+?)            ← Gruppe 1: Name (so wenig wie möglich, bis ";")
#       .+?  = ein oder mehr Zeichen, "lazy" (nicht gierig)
#
#   ; DATE: (.*?)          ← Gruppe 2: Datum/Uhrzeit
#       .*?  = beliebig viele Zeichen, ebenfalls lazy
#
#   ; TZ: (.*)             ← Gruppe 3: Zeitzone (alles bis zum Ende)
#       .*   = beliebig viele Zeichen (gierig, bis Zeilenende)

muster = r"MEET: (.+?) ; DATE: (.*?) ; TZ: (.*)"


# ────────────────────────────────────────────────────────────
# SCHRITT 2: MEETINGS DURCHGEHEN MIT ENUMERATE
# ────────────────────────────────────────────────────────────
# enumerate(liste) gibt uns: (index, wert) für jedes Element.
# Den Index brauchen wir, um in der Warnung sagen zu können,
# WELCHE Zeile übersprungen wurde.

meetings = []     # Hier sammeln wir alle gültigen Meetings als Dictionaries
zeitzonen = set() # Set → Duplikate werden automatisch entfernt

# "jetzt" brauchen wir später, um zu prüfen ob ein Meeting in der Zukunft liegt.
# WICHTIG: datetime.now(ZoneInfo("UTC")) → "aware" (mit Zeitzone),
# damit wir es später mit unseren aware-Meetings vergleichen können.
jetzt = datetime.now(ZoneInfo("UTC"))

for i, zeile in enumerate(raw_meetings):

    # re.match() prüft ob die Zeile zum Muster passt
    treffer = re.match(muster, zeile)

    # Kein Treffer? → Zeile überspringen und Warnung ausgeben
    if not treffer:
        print(f"Zeile {i + 1} wird übersprungen (Kein Meeting-Format).")
        continue    # continue = Rest der Schleife überspringen, nächste Zeile

    # ────────────────────────────────────────────────────────
    # SCHRITT 3: DATEN EXTRAHIEREN
    # ────────────────────────────────────────────────────────
    # treffer.group(1) = erste Klammer  → Name
    # treffer.group(2) = zweite Klammer → Datum/Uhrzeit als Text
    # treffer.group(3) = dritte Klammer → Zeitzone als Text

    name        = treffer.group(1)   # "Projekt-Kickoff"
    datum_text  = treffer.group(2)   # "2026-05-10 14:00"
    tz_text     = treffer.group(3)   # "Europe/Berlin"

    # ────────────────────────────────────────────────────────
    # SCHRITT 4: ZEIT-MAGIE (Text → datetime → aware → UTC)
    # ────────────────────────────────────────────────────────
    # 4a) strptime() wandelt Text in ein datetime-Objekt um.
    #     Das Format muss genau zum Text passen:
    #     "2026-05-10 14:00"  →  "%Y-%m-%d %H:%M"
    dt_naive = datetime.strptime(datum_text, "%Y-%m-%d %H:%M")

    # 4b) "naive" Datetime kennt noch keine Zeitzone.
    #     Mit replace(tzinfo=...) machen wir es "aware".
    dt_lokal = dt_naive.replace(tzinfo=ZoneInfo(tz_text))

    # 4c) astimezone() rechnet das aware-Datetime in UTC um.
    dt_utc = dt_lokal.astimezone(ZoneInfo("UTC"))

    # ────────────────────────────────────────────────────────
    # SCHRITT 5: VALIDIERUNG — liegt das Meeting in der Zukunft?
    # ────────────────────────────────────────────────────────
    # Wenn das Meeting schon vorbei ist, überspringen wir es.
    if dt_lokal < jetzt:
        print(f"Zeile {i + 1} wird übersprungen (Meeting liegt in der Vergangenheit).")
        continue

    # ────────────────────────────────────────────────────────
    # SCHRITT 6: SAUBERE DATEN ALS DICTIONARY SAMMELN
    # ────────────────────────────────────────────────────────
    # "Europe/Berlin".split("/") → ["Europe", "Berlin"]
    # [0] = Region ("Europe"), [1] = Stadt ("Berlin")
    region = tz_text.split("/")[0]
    stadt  = tz_text.split("/")[1].replace("_", " ")  # "New_York" → "New York"

    meetings.append({
        "name":   name,
        "lokal":  dt_lokal,
        "utc":    dt_utc,
        "stadt":  stadt,
        "region": region
    })

    # Region ins Set legen (Duplikate fliegen automatisch raus)
    zeitzonen.add(region)


# ────────────────────────────────────────────────────────────
# SCHRITT 7: FORMATIERTE AUSGABE (alle 3 Methoden)
# ────────────────────────────────────────────────────────────

print()
print("--- GEPLANTE EVENTS ---")

# %-Formatierung: Anzahl der gefundenen Meetings
# %d = ganze Zahl (Integer)
print("Anzahl Meetings: %d (%%-Methode)" % len(meetings))

# .format(): Liste der beteiligten Regionen als Set
# {} ist der Platzhalter, .format(wert) füllt ihn
print("Beteiligte Regionen: {} (.format-Methode)".format(zeitzonen))

# f-Strings: Tabellen-Ausgabe
# :<20 = linksbündig, 20 Zeichen breit  → saubere Spalten
print()
print(f"{'Name':<20}{'Lokalzeit (Zone)':<28}{'UTC-Zeit'}")
print("-" * 70)

for m in meetings:
    # strftime() wandelt datetime zurück in Text mit unserem Wunsch-Format:
    #   %d = Tag, %m = Monat, %H = Stunde, %M = Minute
    lokal_text = m["lokal"].strftime("%d.%m. %H:%M")
    utc_text   = m["utc"].strftime("%H:%M")

    # "Lokalzeit (Stadt)" als einen String bauen, damit die Spalte sauber bleibt
    lokal_spalte = f"{lokal_text} ({m['stadt']})"

    print(f"{m['name']:<20}{lokal_spalte:<28}{utc_text} UTC")
