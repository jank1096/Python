from .geraet import Geraet


class Klimaanlage(Geraet):

    def __init__(self, name: str, stromverbrauch: float, ziel_temperatur: int):
        super().__init__(name, stromverbrauch)

        if ziel_temperatur < 18:
            print(f"WARNUNG: Zieltemperatur {ziel_temperatur}°C ist unter 18°C!")

        self.ziel_temperatur: int = ziel_temperatur

    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Zieltemperatur: {self.ziel_temperatur}°C"
