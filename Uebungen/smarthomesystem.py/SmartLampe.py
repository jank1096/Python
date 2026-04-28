from Geraet import Geraet


class SmartLampe(Geraet):

    def __init__(self, name: str, stromverbrauch: float, helligkeit: float):
        super().__init__(name, stromverbrauch)  # Eltern-Konstruktor aufrufen
        self.helligkeit: float = helligkeit  # extra Attribut (0–100)

    # Überschreibt schalte_aus() – setzt zusätzlich Helligkeit auf 0
    def schalte_aus(self):
        super().schalte_aus()  # erst die Eltern-Methode ausführen
        self.helligkeit = 0  # dann noch die Helligkeit zurücksetzen

    # Überschreibt __str__ – hängt Helligkeit an den Text von Geraet an
    def __str__(self) -> str:
        info = super().__str__()  # Text von Geraet holen
        return f"{info} | Helligkeit: {self.helligkeit}%"
