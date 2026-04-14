# ============================================================
#  SMART-HOME-STEUERUNG
#  Themen: Funktionen, Standardwerte, *args, **kwargs
# ============================================================


# ==========================
#  TEIL 1: EINFACHE FUNKTION OHNE PARAMETER
# ==========================

# def = Funktion definieren
# system_status = Name der Funktion
# () = keine Parameter nötig

def system_status():
    print("System ist online. Alle Sensoren bereit.")

# Funktion aufrufen:
system_status()
# → System ist online. Alle Sensoren bereit.


# ==========================
#  TEIL 2: FUNKTION MIT PARAMETER & STANDARDWERT
# ==========================

# zimmer = fester Parameter → muss immer angegeben werden
# helligkeit=100 = Standardwert → wird genutzt wenn nichts angegeben wird

def licht_einstellen(zimmer: str, helligkeit: int = 100):
    print(f"Im Zimmer {zimmer} wurde das Licht auf {helligkeit}% gesetzt.")

# Aufruf MIT Helligkeit → eigener Wert wird genutzt
licht_einstellen("Wohnzimmer", 75)
# → Im Zimmer Wohnzimmer wurde das Licht auf 75% gesetzt.

# Aufruf OHNE Helligkeit → Standardwert 100 wird genutzt
licht_einstellen("Küche")
# → Im Zimmer Küche wurde das Licht auf 100% gesetzt.


# ==========================
#  TEIL 3: *ARGS & **KWARGS
# ==========================

# aktion     = fester Parameter (z.B. "Einschalten")
# *geraete   = beliebig viele Gerätenamen → werden als TUPLE gespeichert
# **einstellungen = beliebig viele benannte Werte → werden als DICTIONARY gespeichert

def geraete_befehl(aktion: str, *geraete, **einstellungen):

    # Erste Zeile der Ausgabe
    print(f"\nAktion: {aktion} wird ausgeführt für:")

    # *geraete durchlaufen → jedes Gerät einzeln ausgeben
    for geraet in geraete:
        print(f"  - {geraet}")

    # **einstellungen durchlaufen → Key und Value ausgeben
    if einstellungen:   # nur ausgeben wenn Einstellungen vorhanden
        print("Einstellungen:")
        for key, value in einstellungen.items():
            print(f"  {key}: {value}")

# Aufruf — alles zusammen:
geraete_befehl(
    "Einschalten",              # aktion
    "Fernseher", "Radio",       # *geraete (beliebig viele)
    Modus="Energiesparen",      # **einstellungen
    Lautstaerke=10
)
# → Aktion: Einschalten wird ausgeführt für:
# →   - Fernseher
# →   - Radio
# → Einstellungen:
# →   Modus: Energiesparen
# →   Lautstaerke: 10

# Noch ein Aufruf zum Testen:
geraete_befehl(
    "Ausschalten",
    "Licht", "Heizung", "Alarmanlage"
)