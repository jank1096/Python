from Übung.SmartCarHouse.Fahrzeug import Fahrzeug

class PKW(Fahrzeug):
    def __init__(self, marke, modell, preis, sitze):
        super().__init__(marke, modell, preis)  # Basisklasse initialisieren
        self.sitze = sitze
    
    def __str__(self):
        return f"{super().__str__()} {self.sitze} Sitze"