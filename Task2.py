# Task 2: Bill calculator with error handling

prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Value is not a number")
        if price < 0:
            raise ValueError("Negative price not allowed")
        if price > 0:
            total += price
        print(f"Running total: ${total}")
    except TypeError as e:
        print(f"Error: {e}. Skipping invalid item.")
    except ValueError as e:
        print(f"Error: {e}. Skipping invalid item.")

print(f"Final total: ${total}")