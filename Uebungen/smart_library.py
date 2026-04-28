from dataclasses import dataclass
from datetime import datetime

@dataclass
class Autor:
    name: str
    geburtsjahr: int

class Medium:
    bibliotheks_name = "Smart Library"

    def __init__(self, titel, jahr):
        self.titel = titel 
        self._jahr = jahr 
        self.__id = id(self)

    @property
    def jahr(self):
        return self._jahr

    @jahr.setter
    def jahr(self, neues_jahr):
        if neues_jahr > 2026:
            raise ValueError("Jahr darf nicht in der Zukunft liegen")
        self._jahr = neues_jahr


    @staticmethod
    def ist_antik(jahr):
        aktuelles_jahr = datetime.now().year
        return aktuelles_jahr - jahr > 50

    def get_id(self):
        return self.__id


class Buch(Medium):
    def __init__(self, titel, jahr, autor: Autor):
        super().__init__(titel, jahr)
        self.autor = autor

    def __str__(self):
        return f"{self.titel} von {self.autor.name} ({self.jahr})"


    def __eq__(self, other):
        if not isinstance(other, Buch):
            return False
        return self.get_id() == other.get_id()


def print_medien_info(liste):
    for medium in liste:
        print(medium)
        if isinstance(medium, Buch):
            print(f"Autor: {medium.autor.name}")
        print(f"Antik: {Medium.ist_antik(medium.jahr)}")

if __name__ == "__main__":
    autor1 = Autor("George Orwell", 1903)
    autor2 = Autor("J.K. Rowling", 1965)

    buch1 = Buch("1984", 1949, autor1)
    buch2 = Buch("Harry Potter", 1997, autor2)
    buch3 = Buch("1984", 1949, autor1)

    medien_liste = [buch1, buch2, buch3]

    print_medien_info(medien_liste)


    print(f"\nbuch1 == buch2: {buch1 == buch2}") 
    print(f"buch1 == buch3: {buch1 == buch3}") 

    try:
        buch1.jahr = 2030
    except ValueError as e:
        print(f"\nFehler: {e}")

    print(f"\nIst 1949 antik? {Medium.ist_antik(1949)}")

