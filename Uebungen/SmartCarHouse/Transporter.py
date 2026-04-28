from Übung.SmartCarHouse.Fahrzeug import Fahrzeug

class Transporter(Fahrzeug):
    def __init__(self, marke, modell, preis, ladevolumen):
        super().__init__(marke, modell, preis)
        self.ladevolumen = ladevolumen  # in m^3
    
    def __str__(self):
        return f"{super().__str__()} {self.ladevolumen}m³ Ladevolumen"