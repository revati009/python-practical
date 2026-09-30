responses = [
    "Mobile",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile",
    "Tablet",
    "Laptop",
    "Mobile",
    "Laptop"
]
votes = {
    "Mobile": 0,
    "Laptop": 0,
    "Tablet": 0
}
for response in responses:
    if response in votes:
        votes[response] += 1
    else:
        votes[response] = 1

print("========== SURVEY RESULTS ==========")

for category, count in votes.items():
    print(category, ":", count, "votes")

winner = max(votes, key=votes.get)
winning_votes = votes[winner]

print("\n========== WINNER ==========")
print("Winning Product :", winner)
print("Total Votes     :", winning_votes)
