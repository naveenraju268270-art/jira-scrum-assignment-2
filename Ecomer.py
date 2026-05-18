orders = [
    [
        (101, "Laptop", 999.99, 1),
        (102, "Mouse", 25.50, 2),
        (103, "Keyboard", 75.00, 1)
    ],

    [
        (101, "Laptop", 999.99, 2),
        (104, "Monitor", 299.99, 1),
        (105, "Webcam", 89.99, 1)
    ],

    [
        (102, "Mouse", 25.50, 3),
        (103, "Keyboard", 75.00, 2),
        (106, "Headphones", 199.99, 1)
    ]
]

threshold_value = 1000.00
print("Order Totals:")

order_totals = []

for index, order in enumerate(orders, start=1):
    total = sum(price * quantity for _, _, price, quantity in order)
    order_totals.append(total)

    print(f"Order {index} Total: ${total:.2f}")

all_items = [item for order in orders for item in order]

most_expensive = max(all_items, key=lambda item: item[2])

print("\nMost Expensive Item:")
print(f"{most_expensive[1]} (${most_expensive[2]:.2f})")

product_summary = {}

for order in orders:
    for product_id, product_name, price, quantity in order:

        if product_name in product_summary:
            product_summary[product_name] += quantity
        else:
            product_summary[product_name] = quantity

print("\nProduct Quantity Summary:")

for product, quantity in product_summary.items():
    print(f"{product}: {quantity} units")

print(f"\nOrders Exceeding ${threshold_value:.2f}:")

for index, total in enumerate(order_totals, start=1):
    if total > threshold_value:
        print(f"Order {index}: ${total:.2f}")

unique_products = {}

for order in orders:
    for product_id, product_name, price, quantity in order:
        unique_products[product_id] = product_name

print("\nUnique Products Ordered:")

for product_id, product_name in unique_products.items():
    print(f"{product_id}: {product_name}")