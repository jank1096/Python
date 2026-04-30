from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "src"))

from smartwarehouse.exceptions import InventoryError, OutOfStockError
from smartwarehouse.warehouse import Warehouse


def show_products(store: Warehouse):
    print("\nBestand:")
    for product in store.products.values():
        print(product)


def sell_product(store: Warehouse):
    try:
        product_id = int(input("Produkt-ID: "))
        quantity = int(input("Menge: "))
        store.sell_product(product_id, quantity)
        print("Produkt wurde verkauft.")
    except OutOfStockError as error:
        print(f"Nicht genug Bestand: {error}")
    except (InventoryError, ValueError) as error:
        print(f"Fehler: {error}")


def show_history(store: Warehouse):
    print("\nHistorie:")
    if not store.history:
        print("Noch keine Eintraege.")
        return

    for entry in store.history:
        print(entry)


def show_cheap_products(store: Warehouse):
    try:
        max_price = float(input("Maximaler Preis: "))
    except ValueError:
        print("Bitte eine gueltige Zahl eingeben.")
        return

    products = store.filter_products(max_price)
    print("\nGuenstige Produkte:")
    if not products:
        print("Keine Produkte gefunden.")
        return

    for product in products:
        print(product)


def export_json(store: Warehouse):
    file_path = "warehouse_export.json"
    store.save_to_json_file(file_path)
    print(f"JSON-Datei erstellt: {file_path}")


def main():
    my_store = Warehouse.create_warehouse_and_products()

    while True:
        print("\n--- Smart Warehouse ---")
        print("1 Bestand anzeigen")
        print("2 Produkt verkaufen")
        print("3 Historie anzeigen")
        print("4 Guenstige Produkte anzeigen")
        print("5 Inventar als JSON exportieren")
        print("6 Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            show_products(my_store)
        elif choice == "2":
            sell_product(my_store)
        elif choice == "3":
            show_history(my_store)
        elif choice == "4":
            show_cheap_products(my_store)
        elif choice == "5":
            export_json(my_store)
        elif choice == "6":
            print("Programm beendet.")
            break
        else:
            print("Ungueltige Auswahl.")


if __name__ == "__main__":
    main()
