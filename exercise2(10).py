# Inventory Catalog Manager

products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]

item = input("Enter the product name to search: ")

if item in products:
    index = products.index(item)
    print(f"{item} is available in the inventory.")
    print(f"Index location: {index}")
else:
    print(f"{item} is not available in the inventory.")
