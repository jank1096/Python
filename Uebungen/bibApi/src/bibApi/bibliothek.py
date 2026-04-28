from datetime import datetime, timedelta
from .buch import Buch
from .exceptions import MediumNichtVerfuegbarError


class Bibliothek:
    def __init__(self, name):
        self.name = name
        self.inventar = {}
        self.ausleih_verlauf = []
        self.kategorien = set()

    def medium_hinzufuegen(self, medium):
        self.inventar[medium.id] = medium
        if isinstance(medium, Buch):
            self.kategorien.add(medium.kategorie)
        print(f"'{medium.titel}' (ID: {medium.id}) wurde hinzugefügt.")

    def ausleihen(self, medium_id):
        try:
            if medium_id not in self.inventar:
                raise KeyError(medium_id)

            medium = self.inventar[medium_id]

            if medium.ist_ausgeliehen:
                raise MediumNichtVerfuegbarError(medium.titel)

            medium.ist_ausgeliehen = True
            ausleih_datum = datetime.now()
            rueckgabe_datum = ausleih_datum + timedelta(days=14)

            self.ausleih_verlauf.append((medium_id, medium.titel, ausleih_datum, rueckgabe_datum))

            print(f"'{medium.titel}' wurde ausgeliehen.")
            print(f"  Ausgeliehen am: {ausleih_datum.strftime('%d.%m.%Y %H:%M')}")
            print(f"  Rückgabe bis:   {rueckgabe_datum.strftime('%d.%m.%Y')}")

        except KeyError:
            print(f"Fehler: Kein Medium mit ID '{medium_id}' gefunden.")
        except MediumNichtVerfuegbarError as e:
            print(f"Fehler: {e}")

    def zurueckgeben(self, medium_id):
        try:
            if medium_id not in self.inventar:
                raise KeyError(medium_id)

            medium = self.inventar[medium_id]

            if not medium.ist_ausgeliehen:
                print(f"'{medium.titel}' war gar nicht ausgeliehen.")
                return

            medium.ist_ausgeliehen = False
            print(f"'{medium.titel}' wurde erfolgreich zurückgegeben.")

        except KeyError:
            print(f"Fehler: Kein Medium mit ID '{medium_id}' gefunden.")

    def suche_medium(self, suchbegriff):
        treffer = [m for m in self.inventar.values() if suchbegriff.lower() in m.titel.lower()]
        if treffer:
            print(f"\nSuchergebnisse für '{suchbegriff}':")
            for medium in treffer:
                print(f"  {medium}")
        else:
            print(f"Keine Medien mit '{suchbegriff}' gefunden.")

    def zeige_inventar(self):
        print(f"\nInventar der '{self.name}':")
        if not self.inventar:
            print("  Keine Medien vorhanden.")
            return
        for medium in self.inventar.values():
            print(f"  {medium}")
        if self.kategorien:
            print(f"\nKategorien: {', '.join(sorted(self.kategorien))}")

    def zeige_ausleih_verlauf(self):
        print(f"\nAusleih-Verlauf ({len(self.ausleih_verlauf)} Einträge):")
        if not self.ausleih_verlauf:
            print("  Noch keine Ausleihen.")
            return
        for medium_id, titel, ausleih_dat, rueckgabe_dat in self.ausleih_verlauf:
            print(f"  [{medium_id}] '{titel}' – ausgeliehen: {ausleih_dat.strftime('%d.%m.%Y')}, "
                  f"Rückgabe: {rueckgabe_dat.strftime('%d.%m.%Y')}")
