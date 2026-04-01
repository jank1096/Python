import pandas as pd
import matplotlib.pyplot as plt
import os

# __file__ = der Pfad dieser .py Datei
# dirname = der Ordner in dem sie liegt
# so findet Python die CSV immer, egal von wo du das Skript startest
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# CSV einlesen
# pd.read_csv liest die Datei, sep=';' weil Semikolon als Trennzeichen
# index_col=0 setzt die erste Spalte (Stadt) als Zeilenindex
# ============================================================
df = pd.read_csv(os.path.join(BASE_DIR, "umsatz.csv"), sep=";", index_col=0)

print(df)           # Tabelle in der Konsole ausgeben zur Kontrolle
print(df.columns)   # zeigt alle Spalten (= Jahre)

# ============================================================
# Letzte 4 Jahre extrahieren
# df.columns gibt alle Spaltenüberschriften zurück
# [-4:] → Slicing: nur die letzten 4 nehmen
# ============================================================
letzte_4_jahre = df.columns[-4:]
print(letzte_4_jahre)

# ============================================================
# Subplots erstellen — 2x2 Raster (4 Diagramme)
# figsize=(10,10) → Größe des gesamten Fensters in Zoll
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# axes ist ein 2D-Array:
# axes[0][0] = oben links   | axes[0][1] = oben rechts
# axes[1][0] = unten links  | axes[1][1] = unten rechts

# axes.flatten() macht daraus eine einfache Liste [ax0, ax1, ax2, ax3]
# so können wir mit enumerate() einfach durchloopen
for i, jahr in enumerate(letzte_4_jahre):
    ax = axes.flatten()[i]          # das passende Diagramm-Feld auswählen

    ax.pie(
        df[jahr],                   # die Umsatzzahlen für dieses Jahr
        labels=df.index,            # Städtenamen als Beschriftung
        autopct="%1.1f%%",          # Prozentzahl mit 1 Nachkommastelle anzeigen
    )

    ax.set_title(f"Umsatzverteilung {jahr}")   # Titel mit Jahreszahl

# ============================================================
# Layout & Anzeige
# tight_layout() verhindert, dass sich Diagramme überlappen
# ============================================================
plt.tight_layout()
plt.show()
