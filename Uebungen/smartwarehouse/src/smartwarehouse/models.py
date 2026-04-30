from dataclasses import dataclass
from datetime import date
import json


@dataclass
class Product:
    id: int
    name: str
    price: float

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("ID muss groesser als 0 sein.")
        if not self.name.strip():
            raise ValueError("Name darf nicht leer sein.")
        if self.price < 0:
            raise ValueError("Preis darf nicht negativ sein.")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price:.2f} EUR"


@dataclass
class PhysicalProduct(Product):
    weight: float
    shipping_costs: float
    stock: int = 0

    def __post_init__(self):
        super().__post_init__()
        if self.weight <= 0:
            raise ValueError("Gewicht muss groesser als 0 sein.")
        if self.shipping_costs < 0:
            raise ValueError("Versandkosten duerfen nicht negativ sein.")
        if self.stock < 0:
            raise ValueError("Bestand darf nicht negativ sein.")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "type": "physical",
                "weight": self.weight,
                "shipping_costs": self.shipping_costs,
                "stock": self.stock,
            }
        )
        return data

    def __str__(self):
        return (
            f"{super().__str__()} | Gewicht: {self.weight} kg | "
            f"Versand: {self.shipping_costs:.2f} EUR | Bestand: {self.stock}"
        )


@dataclass
class DigitalProduct(Product):
    key_expiry_date: date

    def __post_init__(self):
        super().__post_init__()
        if self.key_expiry_date < date.today():
            raise ValueError("Ablaufdatum darf nicht in der Vergangenheit liegen.")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "type": "digital",
                "key_expiry_date": self.key_expiry_date.isoformat(),
            }
        )
        return data

    def __str__(self):
        return (
            f"{super().__str__()} | Digital | "
            f"Key gueltig bis: {self.key_expiry_date.isoformat()}"
        )
