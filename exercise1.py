Marks1=float(input("Enter marks for subject 1:"))
Marks2=float(input("Enter marks for subject 2:"))
Marks3=float(input("Enter marks for subject 3:"))

Total=Marks1+Marks2+Marks3
Average=Total/3

print("********** STUDENT SCORE CARD**********")


print("Subject1:",Marks1)
print("Subject2:",Marks2)
print("Subject3:",Marks3)
print("Total",Total)
print("Average:",round(Average,2))