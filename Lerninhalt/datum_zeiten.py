# ============================================================
#  DATUM & ZEITEN IN PYTHON
#  Themen: datetime, date, time, timedelta, timezone, ZoneInfo
# ============================================================

from datetime import datetime, time, date, timedelta, timezone
from zoneinfo import ZoneInfo


# ==========================
#  SCHRITT 1: AKTUELLES DATUM & UHRZEIT
# ==========================

# datetime.now() gibt uns das aktuelle Datum + Uhrzeit als Objekt zurück
now = datetime.now()
print(now)              # → 2026-04-10 14:30:00.123456

# Einzelne Teile abrufen
print(now.year)         # → 2026
print(now.month)        # → 4
print(now.isoformat())  # → "2026-04-10T14:30:00" (internationales Format)


# ==========================
#  SCHRITT 2: STRFTIME — datetime in Text umwandeln
# ==========================

# strftime() = "string format time"
# Du gibst ein Format an, Python wandelt das datetime-Objekt in Text um

print(now.strftime("%d.%m.%Y %H:%M"))      # → "10.04.2026 14:30"
print(now.strftime("%A, %d. %B %Y"))       # → "Friday, 10. April 2026"

# Die wichtigsten Platzhalter:
# %d = Tag (01-31)
# %m = Monat als Zahl (01-12)
# %Y = Jahr vierstellig (2026)
# %H = Stunden 24h (00-23)
# %M = Minuten (00-59)
# %A = Wochentag ausgeschrieben (Monday, Tuesday...)
# %B = Monat ausgeschrieben (January, February...)


# ==========================
#  SCHRITT 3: STRPTIME — Text in datetime umwandeln
# ==========================

# strptime() = "string parse time" → das GEGENTEIL von strftime()
# Du hast einen Text und willst damit rechnen → erst in datetime umwandeln

datum_text = "24.10.2025"
datum_obj = datetime.strptime(datum_text, "%d.%m.%Y")
# datum_obj ist jetzt ein echtes datetime-Objekt
print(datum_obj.year)   # → 2025


# ==========================
#  SCHRITT 4: DATE, TIME, DATETIME
# ==========================

# date → nur das Datum (kein Uhrzeit)
today = date.today()
print(today)            # → 2026-04-10
print(now.date())       # → 2026-04-10  (aus datetime nur den Datumsteil holen)

# time → nur die Uhrzeit (kein Datum)
uhr = now.time()
print(uhr)              # → 14:30:00.123456

# Eigene time/date/datetime Objekte erstellen:
tea_time = time(12, 30, 30)             # 12:30:30 Uhr
tea_date = date(2026, 4, 10)            # 10. April 2026
tea_dt   = datetime(2026, 4, 10, 12, 30, 30)  # beides zusammen

print(tea_time.isoformat())             # → "12:30:30"
print(tea_date.isoformat())             # → "2026-04-10"
print(tea_dt.isoformat())              # → "2026-04-10T12:30:30"

# combine() → date + time zu datetime zusammenfügen
zusammen_dt = datetime.combine(today, uhr)
print(zusammen_dt)


# ==========================
#  SCHRITT 5: TIMEDELTA — mit Zeiten rechnen
# ==========================

# timedelta = eine Zeitspanne (kein Zeitpunkt, sondern eine Dauer)
# Du kannst damit addieren (+) und subtrahieren (-)

heute = datetime.now()

# Zukunft: heute + X Tage/Wochen/Stunden
morgen = heute + timedelta(days=1)
print(morgen)

# Vergangenheit: heute - X Tage/Wochen
letzte_woche = heute - timedelta(weeks=1)
print(letzte_woche)

# Differenz zwischen zwei Daten berechnen
bis_weihnachten = datetime(2026, 12, 24) - heute
print(f"Noch {bis_weihnachten.days} Tage bis Weihnachten")


# ==========================
#  SCHRITT 6: ZEITZONEN
# ==========================

# UTC = koordinierte Weltzeit — der internationale Standard
utc_zeit = datetime.now(timezone.utc)
print(utc_zeit)

# ZoneInfo → Zeitzonen per Name (z.B. "Europe/Berlin", "Asia/Tokyo")
# Verfügbar ab Python 3.9

berlin_jetzt = datetime.now(ZoneInfo("Europe/Berlin"))
print(f"Berlin: {berlin_jetzt}")

la_jetzt = datetime.now(ZoneInfo("America/Los_Angeles"))
print(f"LA: {la_jetzt}")

# WICHTIG: "naive" vs "aware" datetime
# naive  → kennt keine Zeitzone → kann NICHT umrechnen
dt_naive = datetime(2026, 4, 10, 10, 0)

# aware  → kennt seine Zeitzone → kann umrechnen mit .astimezone()
dt_aware = datetime(2026, 4, 10, 10, 0, tzinfo=ZoneInfo("Europe/Berlin"))

# .astimezone() rechnet in eine andere Zeitzone um
termin_berlin = datetime(2026, 4, 20, 15, 0, tzinfo=ZoneInfo("Europe/Berlin"))
termin_ny     = termin_berlin.astimezone(ZoneInfo("America/New_York"))

print(f"Meeting Berlin: {termin_berlin.strftime('%H:%M')}")
print(f"Meeting NY:     {termin_ny.strftime('%H:%M')}")
