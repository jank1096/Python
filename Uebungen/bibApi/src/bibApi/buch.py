from .medium import Medium

class Buch(Medium):
    def __init__(self, titel, autor, seitenanzahl, kategorie):
        super().__init__(titel)
        self.autor = autor
        self.seitenanzahl = seitenanzahl
        self.kategorie = kategorie

    def __str__(self):
        basis = super().__str__()
        return f"{basis} | Buch von {self.autor} ({self.seitenanzahl} Seiten, {self.kategorie})"
