Name=input("Enter Your Name:")
Age=int(input("Enter Your Age:"))
Income=float(input("Enter Your Family annual Income:"))
Cast=input("Enter your Cast (SC/ST/OBC/OPEN):").upper()

if Age < 25 and Income<300000 and Cast=="OBC":
    print("CONGRATULATION! You Qualify For The Scholarship ")
else:
        print("SORRY! You Do Not Qualify For Scholarship")
