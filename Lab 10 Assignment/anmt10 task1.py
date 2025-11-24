def discount(price, category):
    # discount rules → (threshold, high_rate, low_rate)
    rules = {
        "student": (1000, 0.9, 0.95),   # >1000 → 10% off, else 5% off
        "other":   (2000, 0.85, 1.0)    # >2000 → 15% off, else no discount
    }

    threshold, high_rate, low_rate = rules.get(category, rules["other"])

    # choose the applied rate
    applied_rate = high_rate if price > threshold else low_rate

    # calculate discount percentage
    discount_percent = (1 - applied_rate) * 100

    # calculate final price
    final_price = price * applied_rate

    return discount_percent, final_price


# -------- USER INPUT --------
price = float(input("Enter price: "))
category = input("Enter category (student/other): ").strip().lower()

discount_percent, final_price = discount(price, category)

print(f"Discount Applied: {discount_percent}%")
print(f"Final Price: {final_price}")