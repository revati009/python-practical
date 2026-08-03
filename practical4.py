
print(""""""""""TRAFFIC SIGNALS""""""""""")


signal = input("Enter signal color (RED/YELLOW/GREEN): ").lower()

if signal == "red":
    print("ACTION:STOP")

elif signal == "yellow":
    print("ACTION:READY")

elif signal == "green":
    print("ACTION:GO")  

else:
    print("Invalid signal color")





