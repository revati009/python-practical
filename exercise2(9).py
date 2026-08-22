
grades = [75, 82, 68, 91, 88]

print("Current grades:", grades)

index = int(input("Enter the index position to update: "))

new_grade = int(input("Enter the new grade: "))

if 0 <= index < len(grades):
    grades[index] = new_grade
    print("Corrected grades:", grades)
else:
    print("Invalid index position.")
