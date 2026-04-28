from Übung.SmartCarHouse.Fahrzeug import Fahrzeug
from Übung.SmartCarHouse.PKW import PKW
from Übung.SmartCarHouse.Transporter import Transporter
from Übung.SmartCarHouse.Mottorrad import Motorrad
from Übung.SmartCarHouse.dataclass import Kunde

def fahrzeug_praesentation(fahrzeug):

    print(fahrzeug)
    
    if isinstance(fahrzeug, PKW):
        print(f"Dieser PKW bietet Platz für {fahrzeug.sitze} Personen.")
    elif isinstance(fahrzeug, Transporter):
        print(f"Dieser Transporter bietet {fahrzeug.ladevolumen}m³ Platz.")
    elif isinstance(fahrzeug, Motorrad):
        if fahrzeug.hat_beiwagen:
            print("Dieses Motorrad hat einen Beiwagen für zusätzlichen Transport.")
        else:
            print("Dieses Motorrad ist ohne Beiwagen - purer Fahrspaß.")
    print(f"Preis: {fahrzeug.preis}€")
    print("")

if __name__ == "__main__":
    kunde1 = Kunde("Max Mustermann", 1001)
    kunde2 = Kunde("Anna Schmidt", 1002)
    print(f"Kunden: {kunde1}, {kunde2}\n")
    
    golf = PKW("VW", "Golf", 25000, 5)
    sprinter = Transporter("Mercedes", "Sprinter", 45000, 15)
    harley = Motorrad("Harley-Davidson", "Sportster", 12000, False)
    bmw_mit = Motorrad("BMW", "R1250GS", 18000, True)
    
    fahrzeuge = [golf, sprinter, harley, bmw_mit]
    
    for fz in fahrzeuge:
        fahrzeug_praesentation(fz)
    
    print(f"Golf mit 10% Rabatt: {Fahrzeug.berechne_rabatt(golf.preis, 10)}€")
    
    try:
        golf.preis = -5000
    except ValueError as e:
        print(f"\nFehler beim Setzen des Preises: {e}")