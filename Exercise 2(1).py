items = []
for i in range(3):
    print("\nEnter details for item", i + 1)

    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))

    total = quantity * price

    items.append([name, quantity, price, total])

print("\n" + "=" * 55)
print("                 GROCERY BILL")
print("=" * 55)

print(f"{'Item':<15}{'Quantity':<10}{'Price':<12}{'Total':<10}")
print("-" * 55)

for item in items:
    print(f"{item[0]:<15}{item[1]:<10}{item[2]:<12.2f}{item[3]:<10.2f}")

grand_total = sum(item[3] for item in items)

print("-" * 55)
print(f"{'GRAND TOTAL':<37}₹{grand_total:.2f}")
print("=" * 55)
