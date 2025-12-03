from dataclasses import dataclass

@dataclass
class Product:
    """
    Predstavlja proizvod u inventaru.
    Atributi:
    - name: ime proizvoda (str)
    - price: cena po jedinici (float)
    - quantity: dostupna količina (int)
    """
    name: str
    price: float
    quantity: int = 0

    def display(self) -> str:
        """Vrati formatiran opis proizvoda."""
        return f"Product(name='{self.name}', price={self.price:.2f}, quantity={self.quantity})"

    def update_quantity(self, delta: int) -> None:
        """
        Ažurira količinu proizvoda.
        delta može biti pozitivan (dodavanje) ili negativan (oduzimanje).
        Podigni ValueError ako bi količina postala negativna.
        """
        new_qty = self.quantity + delta
        if new_qty < 0:
            raise ValueError(f"Ne može se postaviti negativna količina za '{self.name}'.")
        self.quantity = new_qty

    def total_value(self) -> float:
        """Vrati ukupnu vrednost ovog proizvoda (price * quantity)."""
        return self.price * self.quantity

    def __repr__(self) -> str:
        return self.display()

