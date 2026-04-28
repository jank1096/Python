from Geraet import Geraet


class Klimaanlage(Geraet):

    def __init__(self, name: str, stromverbrauch: float, ziel_temperatur: int):
        super().__init__(name, stromverbrauch)  # Eltern-Konstruktor aufrufen

        # Validierung – Warnung wenn Temperatur zu niedrig
        if ziel_temperatur < 18:
            print(f"WARNUNG: Zieltemperatur {ziel_temperatur}°C ist unter 18°C!")

        self.ziel_temperatur: int = ziel_temperatur  # extra Attribut

    # Überschreibt __str__ – hängt Temperatur an den Text von Geraet an
    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Zieltemperatur: {self.ziel_temperatur}°C"
