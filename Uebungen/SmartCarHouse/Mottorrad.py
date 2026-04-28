from Übung.SmartCarHouse.Fahrzeug import Fahrzeug

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, preis, hat_beiwagen):
        super().__init__(marke, modell, preis)
        self.hat_beiwagen = hat_beiwagen  # bool
    
    def __str__(self):
        beiwagen_text = "mit Beiwagen" if self.hat_beiwagen else "ohne Beiwagen"
        return f"{super().__str__()} {beiwagen_text}"