from Geraet import Geraet
from Klimaanlage import Klimaanlage
from SmartLampe import SmartLampe


def menu():
    print("=== Willkommen im Smart-Home-System ===\n")

    # Objekte erstellen
    lampe = SmartLampe("Nachttischlampe", 15.0, 75)
    klima = Klimaanlage("Wohnzimmer Klima", 2000.0, 21)
    klima2 = Klimaanlage("Keller Klima", 1500.0, 15)  # löst Warnung aus

    print("\n--- Ausgangszustand (alle AUS) ---")
    print(lampe)
    print(klima)
    print(klima2)

    print("\n--- Geräte einschalten ---")
    lampe.schalte_an()
    klima.schalte_an()
    print(lampe)
    print(klima)

    print("\n--- Lampe ausschalten (Helligkeit geht auf 0) ---")
    lampe.schalte_an()
    print(lampe)

    print(f"\nGeräte insgesamt im System: {Geraet.anzahl_geraete}")


if __name__ == "__main__":
    menu()
