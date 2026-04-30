from datetime import date, datetime
import json

from .exceptions import InventoryError, OutOfStockError
from .models import DigitalProduct, PhysicalProduct, Product


class Warehouse:
    def __init__(self):
        self.products = {}
        self.history = []

    def add_product(self, product: Product):
        self.products[product.id] = product
        self._add_history(f"Produkt hinzugefuegt: {product.name}")

    def sell_product(self, product_id: int, quantity: int):
        if quantity <= 0:
            raise ValueError("Menge muss groesser als 0 sein.")

        product = self.products.get(product_id)
        if product is None:
            raise InventoryError("Produkt nicht gefunden.")

        if isinstance(product, PhysicalProduct):
            if quantity > product.stock:
                raise OutOfStockError(
                    f"Nur noch {product.stock} Stueck von {product.name} vorhanden."
                )
            product.stock -= quantity

        self._add_history(f"Verkauf: {quantity}x {product.name}")

    def filter_products(self, max_price: float) -> list[Product]:
        return list(
            filter(lambda product: product.price <= max_price, self.products.values())
        )

    def to_dict(self) -> dict:
        return {
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "products": [product.to_dict() for product in self.products.values()],
            "history": self.history,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def save_to_json_file(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.to_json())
        self._add_history(f"JSON-Datei erstellt: {file_path}")

    @classmethod
    def create_warehouse_and_products(cls):
        warehouse = cls()

        warehouse.add_product(
            PhysicalProduct(
                id=354,
                name="Dell X500",
                price=979.99,
                weight=1.5,
                shipping_costs=15,
                stock=5,
            )
        )

        warehouse.add_product(
            DigitalProduct(
                id=632,
                name="Hausmeister Kurs",
                price=20.0,
                key_expiry_date=date(2029, 10, 30),
            )
        )

        return warehouse

    @staticmethod
    def calculate_tax(amount: float, tax_rate: float = 0.19) -> float:
        return round(amount * tax_rate, 2)

    def _add_history(self, message: str):
        timestamp = datetime.now().isoformat(timespec="seconds")
        self.history.append(f"{timestamp} | {message}")
