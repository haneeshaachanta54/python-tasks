#square pattern
rows=4
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()
#Right Triangle
rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()
#number triangle
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
#repeated number triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()
#alphabet triangle
rows = 5
for i in range(rows):
    ch = 65
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
#Inverted Star Triangle
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
#Inverted Number Triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Continuous Number Pattern
rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#Right-Aligned Star Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
#Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()