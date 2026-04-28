class Fahrzeug:
    def __init__(self, marke, modell, preis):
        self.marke = marke
        self.modell = modell           
        self.__preis = preis

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, neuer_preis):
        if neuer_preis < 0:
            raise ValueError("Preis darf nicht negativ sein")
        self.__preis = neuer_preis

    @staticmethod
    def berechne_rabatt(preis, prozent):
        return preis * (1 - prozent / 100)

    def __str__(self):
        return f"{self.marke} {self.modell}"