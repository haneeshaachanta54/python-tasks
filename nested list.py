# CONVERT BINARY TO DECIMAL
n = int(input("Enter a binary number: "))
d = 0
i = 0
while n != 0:
    r = n % 10
    d = d + r * (2 ** i)
    n = n // 10
    i += 1
print(d)