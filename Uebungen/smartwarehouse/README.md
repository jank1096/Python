# Smart Warehouse

Smart Warehouse ist ein kleines Python-Projekt zum Ueben von objektorientierter
Programmierung. Es simuliert eine einfache Lagerverwaltung mit physischen und
digitalen Produkten, Bestand, Verkauf, Historie und JSON-Export.

Das Projekt ist bewusst kompakt gehalten: Es soll nicht wie ein fertiges
Enterprise-System wirken, sondern die wichtigsten Python-Konzepte in einem
ueberschaubaren Beispiel verbinden.

## Features

- Produktklassen mit Vererbung und `@dataclass`
- Physische Produkte mit Gewicht, Versandkosten und Bestand
- Digitale Produkte mit Ablaufdatum fuer Lizenz-Keys
- Eigene Exceptions fuer Inventarfehler
- Warehouse-Klasse zum Verwalten, Verkaufen und Filtern
- History mit Zeitstempel fuer wichtige Aktionen
- JSON-Export des aktuellen Inventars
- Einfaches Terminal-Menue in `main.py`

## Gelernte Konzepte

| Thema | Umsetzung im Projekt |
| --- | --- |
| OOP | Basisklasse `Product`, Unterklassen `PhysicalProduct` und `DigitalProduct` |
| Vererbung | Gemeinsame Produktlogik wird in den Unterklassen erweitert |
| Dataclasses | Weniger Boilerplate bei den Produktklassen |
| Exceptions | `InventoryError` und `OutOfStockError` fuer klare Fehlerfaelle |
| Dictionaries | Produkte werden ueber ihre ID im Warehouse gespeichert |
| Lambda | Preisfilter nutzt eine Lambda-Funktion |
| JSON | Inventar kann als strukturierte Datei exportiert werden |
| Datum & Zeit | History-Eintraege erhalten Zeitstempel |

## Projektstruktur

```text
smartwarehouse/
├── main.py
├── pyproject.toml
├── README.md
└── src/
    └── smartwarehouse/
        ├── __init__.py
        ├── exceptions.py
        ├── models.py
        └── warehouse.py
```

## Installation und Start

```bash
cd Uebungen/smartwarehouse
python3 main.py
```

Optional kann das Package im Entwicklungsmodus installiert werden:

```bash
cd Uebungen/smartwarehouse
python3 -m pip install -e .
python3 main.py
```

## Beispiel

```text
--- Smart Warehouse ---
1 Bestand anzeigen
2 Produkt verkaufen
3 Historie anzeigen
4 Guenstige Produkte anzeigen
5 Inventar als JSON exportieren
6 Beenden
Auswahl:
```

Ein Produkt wird in der Konsole lesbar ausgegeben:

```text
354 | Dell X500 | 979.99 EUR | Gewicht: 1.5 kg | Versand: 15.00 EUR | Bestand: 5
```

## Naechste Ideen

- Produkte ueber das Menue hinzufuegen
- Inventar beim Programmstart aus JSON laden
- Tests fuer Produktvalidierung und Verkauf schreiben
- Suche nach Produktname oder ID ergaenzen
- Sortierung nach Preis oder Name einbauen
