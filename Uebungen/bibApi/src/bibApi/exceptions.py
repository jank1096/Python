class MediumNichtVerfuegbarError(Exception):
    def __init__(self, titel):
        super().__init__(titel + " ist leider schon ausgeliehen!")