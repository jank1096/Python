from .geraet import Geraet


class SmartLampe(Geraet):

    def __init__(self, name: str, stromverbrauch: float, helligkeit: float):
        super().__init__(name, stromverbrauch)
        self.helligkeit: float = helligkeit  # 0–100

    def schalte_aus(self):
        super().schalte_aus()
        self.helligkeit = 0

    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Helligkeit: {self.helligkeit}%"
