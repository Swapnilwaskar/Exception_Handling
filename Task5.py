# Task 5: Mini Program: Safe Shopping Cart

cart = []

while True:
    price_input = input("Enter price (or 'q' to quit): ")

    if price_input.lower() == 'q':
        break

    try:
        price = float(price_input)
        if price < 0:
            raise ValueError("Price cannot be negative")
        cart.append(price)
    except ValueError as e:
        print(f"Error: {e}")

print(f"Total items: {len(cart)}")
print(f"Total bill: ${sum(cart)}")
