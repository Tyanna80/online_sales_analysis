from product_manager import ProductManager
from cart import Cart
import random

if __name__ == "__main__":
    # Kreiranje product manager-a i učitavanje proizvoda
    pm = ProductManager()
    pm.load_products()

    print("Dostupni proizvodi:")
    pm.display_products()

    # Kreiranje instance korpe
    cart = Cart()

    # Odabir 3 slučajna proizvoda
    available_products = pm.products
    selected_products = random.sample(available_products, 3)

    print("\nDodajem 3 slučajna proizvoda u korpu...")
    for product in selected_products:
        cart.add_product(product)
        print(f"Dodat proizvod: {product.name}")

    # Prikaz korpe i ukupne cene
    print("\n--- Sadržaj korpe ---")
    cart.display_cart()
