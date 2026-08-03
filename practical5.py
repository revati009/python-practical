print("==========MONTHLY EXPENSE TRACKER==========")
n=int(input("Enter The Number Of Expense:"))

expense=[]
total=0

for i in range(n):
    amount=float(input(f"Enter Expense{i + 1}:"))
    expense.append(amount)
    total+=amount

while True:
    print("\n_ _ _ _ _EXPENSE TRACKER MENU_ _ _ _ _ ") 
    print("1. Show All Expenses ")
    print("2. Show Total Expenses ")
    print("3. Add New Expense ")
    print("4. Delete Expense")
    print("5. EXIT")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
       print("\nExpense List:")
       for i in range(len(expense)):
         print(f"Expense {i + 1}:{expense[i]}")

    elif choice==2:
     print("Total Monthly Expense =" , total)

    elif choice==3:
      new_expense = float(input("Enter New Expense:"))
      expense.append(new_expense)
      total+=new_expense
      print("^^^^^^^^Expense Added Succesfully^^^^^^^^")

    elif choice == 4:
     index = int(input("Enter expense number to delete: ")) - 1
     if 0 <= index < len(expense):
        total -= expense[index]
        expense.pop(index)
        print("Expense deleted successfully.")
   
    elif choice==:
      print("Thank you for")

    else:
      print("Invalid Choice,Try again Later")
 