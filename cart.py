class Cart:
    def __init__(self):
        self.cart_items = []  # lista proizvoda u korpi

    def add_product(self, product):
        """Dodaje proizvod u korpu"""
        self.cart_items.append(product)

    def total_price(self):
        """Vraća ukupnu cenu proizvoda u korpi"""
        return sum(product.price for product in self.cart_items)

    def display_cart(self):
        """Prikazuje proizvode u korpi"""
        if not self.cart_items:
            print("Korpa je prazna.")
            return

        print("Proizvodi u korpi:")
        for product in self.cart_items:
            print(f"- {product.name}: {product.price} RSD")

        print(f"\nUkupna cena: {self.total_price()} RSD")
