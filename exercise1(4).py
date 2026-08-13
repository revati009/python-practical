Status=input("Enter Order Status:").lower()

if Status == "shipped":
    print("Your Ordered Has Been Shipped and is on the way....")
elif Status == "delivered":
    print("Your Order Has Been Delivered Successfully.")
elif Status == "pending":
    print("Your Order is Pending and will be Processed soon.")
else:
    print("Invalid Status.Please Enter Shipped,Delivered or Pending.")