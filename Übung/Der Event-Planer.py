def plane_event(event_name, *args, **kwargs):
    # Den Namen des Events groß geschrieben ausgeben [cite: 7]
    print(event_name.upper())
    
    # Alle Gäste einzeln auflisten [cite: 8]
    print("Gäste:")
    for gast in args:
        print(f"- {gast}")
    
    # Zusatz-Details im Format „Eigenschaft: Wert" [cite: 9]
    print("Details:")
    for eigenschaft, wert in kwargs.items():
        print(f"{eigenschaft}: {wert}")

# Testaufruf [cite: 10, 11]
plane_event("Geburtstag", "Alice", "Bob", "Charlie", Ort="Garten", Musik="DJ", Kuchen=True)