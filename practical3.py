print("***college admission Eligibility checker***")

age=int(input("Enter age:"))
marks=float(input("Enter marks:"))

if age>=18:
  if marks>=65:
    print("Eligible for admission")

    if marks>=85:
      print("Eligible for AIML admission")

    elif marks>=75:
      print("Eligible for CS admission")

    elif marks>=70:
      print("Eligible for other stream")

    else:
     print("Eligible for general stream")

else:
  print("Not Eligible for admission")