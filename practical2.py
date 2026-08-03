print("========== GROCERY SHOP BILLING CALCULATOR ==========")

Paneer_price = float(input("Enter price of Paneer: "))
Paneer_qty = int(input("Enter quantity of Paneer: "))

Noodles_price = float(input("Enter price of Noodles: "))
Noodles_qty = int(input("Enter quantity of Noodles: "))

Shampoo_price = float(input("Enter price of Shampoo: "))
Shampoo_qty = int(input("Enter quantity of Shampoo: "))

Dal_price = float(input("Enter price of Dal: "))
Dal_qty = int(input("Enter quantity of Dal: "))

Sugar_price = float(input("Enter price of Sugar: "))
Sugar_qty = int(input("Enter quantity of Sugar: "))

Paneer = Paneer_price * Paneer_qty
Noodles = Noodles_price * Noodles_qty
Shampoo = Shampoo_price * Shampoo_qty
Dal = Dal_price * Dal_qty
Sugar = Sugar_price * Sugar_qty

total = Paneer + Noodles + Shampoo + Dal + Sugar
if total >= 1000:
    discount = total * 0.10

elif total >= 500:
    discount = total * 0.05

else:
    discount = 0
final_amount = total - discount

print("\n<<<<<<<<<< BILL DETAILS >>>>>>>>>>")
print("Paneer Total:", Paneer)
print("Noodles Total:", Noodles)
print("Shampoo Total:", Shampoo)
print("Dal Total:", Dal)
print("Sugar Total:", Sugar)

print("-----------------------------")
print("Total =", total)
print("Discount =", discount)
print("Final Amount =", final_amount)
