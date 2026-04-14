import re
from datetime import datetime
from zoneinfo import ZoneInfo

raw_meetings = [
    "MEET: Projekt-Kickoff ; DATE: 2026-05-10 14:00 ; TZ: Europe/Berlin",
    "NOTIZ: Kaffeepause ignorieren",
    "MEET: Update-Call ; DATE: 2026-05-10 10:00 ; TZ: America/New_York",
    "MEET: Tech-Check ; DATE: 2026-05-10 09:00 ; TZ: Asia/Tokyo"
]

muster = r"MEET: (.+?) ; DATE: (.*?) ; TZ: (.*)"

meetings = []
zeitzonen = set()

jetzt = datetime.now(ZoneInfo("UTC"))

for i, zeile in enumerate(raw_meetings):

    treffer = re.match(muster, zeile)

    if not treffer:
        print(f"Zeile {i + 1} wird übersprungen (Kein Meeting-Format).")
        continue   

    name        = treffer.group(1)   
    datum_text  = treffer.group(2)   
    tz_text     = treffer.group(3)   

    dt_naive = datetime.strptime(datum_text, "%Y-%m-%d %H:%M")
    dt_lokal = dt_naive.replace(tzinfo=ZoneInfo(tz_text))

    dt_utc = dt_lokal.astimezone(ZoneInfo("UTC"))

    if dt_lokal < jetzt:
        print(f"Zeile {i + 1} wird übersprungen (Meeting liegt in der Vergangenheit).")
        continue


    region = tz_text.split("/")[0]
    stadt  = tz_text.split("/")[1].replace("_", " ")  

    meetings.append({
        "name":   name,
        "lokal":  dt_lokal,
        "utc":    dt_utc,
        "stadt":  stadt,
        "region": region
    })
    zeitzonen.add(region)


print()
print("--- GEPLANTE EVENTS ---")

print("Anzahl Meetings: %d (%%-Methode)" % len(meetings))

print("Beteiligte Regionen: {} (.format-Methode)".format(zeitzonen))

print()
print(f"{'Name':<20}{'Lokalzeit (Zone)':<28}{'UTC-Zeit'}")
print("-" * 70)

for m in meetings:
    lokal_text = m["lokal"].strftime("%d.%m. %H:%M")
    utc_text   = m["utc"].strftime("%H:%M")

    lokal_spalte = f"{lokal_text} ({m['stadt']})"

    print(f"{m['name']:<20}{lokal_spalte:<28}{utc_text} UTC")