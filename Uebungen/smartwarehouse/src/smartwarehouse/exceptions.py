class InventoryError(Exception):
    pass


class OutOfStockError(InventoryError):
    pass
