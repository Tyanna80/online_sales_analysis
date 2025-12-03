from typing import List, Optional
from product import Product

class ProductManager:
    """
    Upravljanje listom proizvoda.
    - add_product: dodaje proizvod ili uvećava količinu ako proizvod sa istim imenom postoji
    - list_products: vraća listu proizvoda
    - total_inventory_value: izračunava ukupnu vrednost inventara
    - remove_by_name: uklanja proizvod po imenu (prvi pogodak)
    """
    def __init__(self):
        self.products: List[Product] = []

    def find_by_name(self, name: str) -> Optional[Product]:
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def add_product(self, product: Product) -> None:
        existing = self.find_by_name(product.name)
        if existing:
            # Uvećaj količinu i osveži cenu demonstrativno (zadržava staru cenu ako je 0)
            existing.update_quantity(product.quantity)
            if product.price > 0:
                existing.price = product.price
        else:
            self.products.append(product)

    def list_products(self) -> List[Product]:
        return list(self.products)

    def total_inventory_value(self) -> float:
        return sum(p.total_value() for p in self.products)

    def remove_by_name(self, name: str) -> bool:
        """
        Uklanja proizvod po imenu. Vraća True ako je uklonjen, False ako nije nađen.
        """
        for i, p in enumerate(self.products):
            if p.name.lower() == name.lower():
                del self.products[i]
                return True
        return False

    def __repr__(self) -> str:
        lines = [p.display() for p in self.products]
        lines.append(f"Total inventory value: {self.total_inventory_value():.2f}")
        return "\n".join(lines)
