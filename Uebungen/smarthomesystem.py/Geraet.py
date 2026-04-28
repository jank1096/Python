class Geraet:
    anzahl_geraete: int = 0  # Klassenattribut – zählt alle erstellten Geräte

    def __init__(self, name: str, stromverbrauch: float):
        self.name: str = name                       # public
        self.__status: bool = False                 # private   – nur über schalte_an/aus änderbar
        self._stromverbrauch: float = stromverbrauch  # protected – Kinder dürfen drauf zugreifen

        Geraet.anzahl_geraete += 1                  # jedes neue Gerät erhöht den Zähler

    # ---------- Methoden ----------

    def schalte_an(self):
        self.__status = True

    def schalte_aus(self):
        self.__status = False

    def get_status(self) -> bool:
        return self.__status

    def __str__(self) -> str:
        status_text = "AN" if self.__status else "AUS"
        return f"Gerät: {self.name} | Status: {status_text} | Verbrauch: {self._stromverbrauch}W"
