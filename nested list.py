n = 1011
decimal = 0
base = 1
while n > 0:
    digit = n % 10
    decimal += digit * base
    base = base * 2
    n = n // 10
print(decimal)