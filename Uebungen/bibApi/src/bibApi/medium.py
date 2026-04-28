import random


class Medium:
    def __init__(self, titel):
        self.titel = titel
        self.id = random.randint(1000, 9999)
        self.ist_ausgeliehen = False

    def __str__(self):
        status = "ausgeliehen" if self.ist_ausgeliehen else "verfügbar"
        return f"[{self.id}] '{self.titel}' – {status}"
