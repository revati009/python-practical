Score=float(input("Enter Graduation Score (%):"))
Backlogs=int(input("Enter Number of Active Backlogs:"))

if Score >= 70 and Backlogs == 0:
    print("***Candidate Eligible For Placement***")
else:
     print("***Candidate is Not Eligible For Placement***")
    