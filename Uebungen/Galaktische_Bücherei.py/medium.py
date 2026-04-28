import random

class medium:
    def __init__(self,titel):
        self.titel = titel
        self.id = random.randint(0000,9999)
        self.ist_ausgeliehen = False

    def __str__(self):
        if self.ist_ausgeliehen:
            status = "ausgeliehen"
        else: 
            status = "verfügbar"
        return f"[{self.id}] {self.titel} - {status}"