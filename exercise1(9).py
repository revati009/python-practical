transactions = []

for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: "))
    transactions.append(amount)

largest_transaction = max(transactions)
average_spend = sum(transactions) / len(transactions)

print("Largest transaction:", largest_transaction)
print("Average spend:", average_spend)
