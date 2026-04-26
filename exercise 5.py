# Shop Inventory System

# Store products in a dictionary
shop = {
    "apple": {"price": 2, "quantity": 10},
    "banana": {"price": 1, "quantity": 15},
    "orange": {"price": 3, "quantity": 8},
    "milk": {"price": 5, "quantity": 5}
}

total_price = 0

print("Welcome to the Shop!")
print("Type 'exit' to finish your order.\n")

# Take orders
while True:
    item = input("Enter product name: ").lower()

    if item == "exit":
        break

    # Check if item exists
    if item not in shop:
        print("❌ Item does not exist.\n")
        continue

    try:
        qty = int(input("Enter quantity: "))

        # Check if enough stock
        if qty > shop[item]["quantity"]:
            print("❌ Not enough stock available.\n")
            continue

        # Calculate price
        cost = shop[item]["price"] * qty
        total_price += cost

        # Reduce quantity
        shop[item]["quantity"] -= qty

        print(f"✅ Added {qty} {item}(s). Cost: {cost}\n")

    except ValueError:
        print("❌ Please enter a valid number.\n")

# Show total price
print("\n🧾 Total Price:", total_price)

# Show remaining inventory
print("\n📦 Remaining Inventory:")
for name, details in shop.items():
    print(f"{name} - Price: {details['price']}, Quantity: {details['quantity']}")