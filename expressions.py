#Arthemetic Operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
#Relational Operations
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)
# LOGICAL EXPRESSIONS 
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# ASSIGNMENT EXPRESSIONS 
num = 20
print("Initial:", num)
num += 5
print("+= :", num)
num -= 2
print("-= :", num)
num *= 3
print("*= :", num)
num /= 2
print("/= :", num)
num //= 2
print("//= :", num)
num %= 4
print("%= :", num)
num **= 2
print("**= :", num)
#  BITWISE EXPRESSIONS 
a = 5
b = 3
print("AND:", a & b)
print("OR :", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

#  MEMBERSHIP EXPRESSIONS 
numbers = [10,20,30,40]
print("20 in list:", 20 in numbers)
print("50 not in list:", 50 not in numbers)

# IDENTITY EXPRESSIONS 
l1 = [1,2]
l2 = l1
l3 = [1,2]
print("l1 is l2:", l1 is l2)
print("l1 is l3:", l1 is l3)
print("l1 is not l3:", l1 is not l3)

#  CONDITIONAL (TERNARY) 
age = 20
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)


#  BOOLEAN EXPRESSIONS 
print(True and False)
print(True or False)
print(not True)
print(10 > 5)
print(8 == 8)

#  MATHEMATICAL FORMULAS 

length = 10
breadth = 5
print("Area of Rectangle:", length * breadth)
print("Perimeter of Rectangle:", 2 * (length + breadth))
side = 6
print("Area of Square:", side ** 2)
print("Perimeter of Square:", 4 * side)
radius = 7
pi = 3.14159
print("Area of Circle:", pi * radius ** 2)
print("Circumference:", 2 * pi * radius)
P = 10000
R = 10
T = 2
print("Simple Interest:", (P * R * T) / 100)
amount = P * (1 + R/100) ** T
print("Compound Interest:", amount - P)
marks = 450
total = 500
print("Average:", (10 + 20 + 30) / 3)
print("Percentage:", (marks / total) * 100)
weight = 70
height = 1.75
print("BMI:", weight / (height ** 2))
distance = 120
time = 2
print("Speed:", distance / time)
cost_price = 500
selling_price = 650
print("Profit:", selling_price - cost_price)
print("Loss:", cost_price - selling_price)
profit = selling_price - cost_price
print("Profit Percentage:", (profit / cost_price) * 100)
marked_price = 800
discount = marked_price - selling_price
print("Discount:", discount)
print("Discount Percentage:", (discount / marked_price) * 100)
n = 10
print("Sum of First N Natural Numbers:", n * (n + 1) // 2)
print("Sum of Squares:", n * (n + 1) * (2*n + 1) // 6)
celsius = 30
fahrenheit = 86
print("Celsius to Fahrenheit:", (celsius * 9/5) + 32)
print("Fahrenheit to Celsius:", (fahrenheit - 32) * 5/9)
#SWAP TWO NUMBERS 
a = 10
b = 20
print("Before Swap:", a, b)
a, b = b, a
print("After Swap:", a, b)
