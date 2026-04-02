# Python – Fachinformatiker Lernprojekte

Dieses Repository enthält alle Python-Übungen und Projekte aus meiner Ausbildung zum Fachinformatiker.

## Setup

- Python 3.13
- Editor: VS Code mit Black Formatter, Ruff, Pylance
- Virtuelle Umgebung: `.venv/`

```bash
# Virtuelle Umgebung aktivieren
source .venv/bin/activate

# Skript ausführen
python3 U1/listen.py
```

## Dateiübersicht

### U1/ — Grundlagen

| Datei | Thema |
|-------|-------|
| `u1_1.py` | Variablen, Datentypen, Operatoren, if/else, Funktionen |
| `Binäre Operatoren.py` | AND, OR, XOR, NOT, Left/Right Shift |
| `listen.py` | Listen: Erstellen, Slicing, Methoden, Schleifen, Verschachtelt, List Comprehensions |
| `tuples.py` | Tuples: Vollständige Referenz mit allen Methoden |
| `dt_tuples.py` | Tuples: Schulbeispiel nach Dozenten-Vorlage (Unpacking, id(), any/all, nested) |
| `aufgabe_filme.py` | Aufgabe: Filmdaten mit Tuple & Liste |
| `speisekarte.py` | Aufgabe: Restaurant-Speisekarte mit Funktionen, Tuple & Liste |

### Uebungen/ — Buchaufgaben

| Datei | Thema |
|-------|-------|
| `umsatz_visualisierung.py` | Pandas + Matplotlib: Kuchendiagramme aus CSV |
| `umsatz.csv` | Beispieldaten: Umsatz 5 Städte 2020–2023 |

## Struktur

```
Python/
├── U1/                   # Grundlagen & Unterrichtsmaterial
├── Uebungen/             # Buchaufgaben & Projekte
└── .venv/                # Virtuelle Umgebung (nicht in Git)
```
