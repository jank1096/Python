from medium import medium

class Buch(medium):
    def __init__(self,titel, autor, seiten, kategorie):
        super().__init__(titel)
        self.autor = autor
        self.seiten = seiten
        self.kategorie = kategorie

    def __str__(self):
        return super().__str__()