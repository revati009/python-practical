for i in range(1,6):
    for j in range( i):
         print("*", end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()




for i in range(0,10):
    for j in range(i + 1):
        print(j+1, end=" ")
    print()


for i in range(10,0,-1):
    for j in range(i):
        print(j+1, end=" ")
    print()

rows = 8
cols = 35

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

row = 8

for i in range(row):
    for j in range(20):
        print("*",end = " ")
    print()

row = 5

for i in range(1, row + 1):
    for j in range (1,6):
        print(j,end = " ")
    print()


