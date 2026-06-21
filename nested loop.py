# Sum of Digits 
n=int(input("Enter a number: "))
sum=0
while n>0:
    digit=n%10    
    sum+=digit
    n=n//10 
print(sum)
# Reverse a Number
n=int(input("Enter a number: "))
reverse=0
while n>0:
    digit=n%10    
    reverse=reverse*10+digit
    n=n//10
print(reverse)
# Count Digits in a Number
n=int(input("Enter a number: "))
count=0
while n>0:
    n=n//10
    count+=1
print(count)
#Check Even or Odd   
n=int(input("Enter a number: "))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")
#Check Prime Number 
n=int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime")
            break
    else:
        print(n,"is prime")
else:
    print(n,"is not prime")
#Find Factorial of a Number
n=int(input("Enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
#Find Factors of a Number
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)
#Check Palindrome Number
n=int(input("Enter a number: "))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if original==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
#Check Armstrong Number 
n=int(input("Enter a number: "))
original=n
digits=len(str(n))
total=0
while n>0:
    digit=n%10
    total+=digit**digits
    n=n//10
if total==original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
#Find GCD (HCF) of Two Numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD =",gcd)

