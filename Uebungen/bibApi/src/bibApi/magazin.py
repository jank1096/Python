from .medium import Medium

class Magazin(Medium):
    def __init__(self, titel, ausgabe_nummer):
        super().__init__(titel)
        self.ausgabe_nummer = ausgabe_nummer

    def __str__(self):
        basis = super().__str__()
        return basis + " | Ausgabe Nr. " + str(self.ausgabe_nummer)