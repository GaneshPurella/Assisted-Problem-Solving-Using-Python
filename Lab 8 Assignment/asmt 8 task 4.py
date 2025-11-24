class ShoppingCart:
    def __init__(self):
        self.items = {}  # store items as {name: price}

    def add_item(self, name, price):
        """Add an item with its price"""
        self.items[name] = price
        print(f"✅ {name} added to cart (₹{price})")

    def remove_item(self, name):
        """Remove an item by name"""
        if name in self.items:
            del self.items[name]
            print(f"🗑️ {name} removed from cart")
        else:
            print(f"⚠️ {name} not found in cart")

    def total_cost(self):
        """Return total cost of all items"""
        return sum(self.items.values())


# --- Main Program with User Input ---
cart = ShoppingCart()

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View total cost")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter item name: ")
        try:
            price = float(input("Enter item price: "))
            cart.add_item(name, price)
        except:
            print("❌ Invalid price! Please enter a number.")
    
    elif choice == "2":
        name = input("Enter item name to remove: ")
        cart.remove_item(name)
    
    elif choice == "3":
        print(f"💰 Total cost of items in cart: ₹{cart.total_cost()}")
    
    elif choice == "4":
        print("🛒 Thank you for shopping! Goodbye 👋")
        break
    
    else:
        print("⚠️ Invalid choice, please enter 1–4.")