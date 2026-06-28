num = int(input("Enter a number: "))
temp = num
length = 0
while temp > 0:
    length += 1
    temp //= 10
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp //= 10
if total == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")