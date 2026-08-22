
asset_costs = [1250.50, 875.25, 3200.75, 450.00, 2100.40, 975.80]

asset_costs.sort(reverse=True)

print("Top 3 priciest assets:")

for price in asset_costs[:3]:
    print(f"{price:.2f}")
