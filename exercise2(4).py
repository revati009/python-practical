status=input("Enter Atmospheric status:").lower()

if status == "hot":
    print("Recommendation: Turn on AC.")
elif status == "cold":
    print("Recommendation: Activate Heater.")
elif status == "normal":
    print("Recommendation: Idle.")
else:
    print("invalid atmospheric status.")