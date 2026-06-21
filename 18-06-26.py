# # #even or odd
# # n=7
# # if n%2==0:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #even or odd using and operation only
# # n=6
# # if n&1==0:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #even or odd using bitwise operation
# # n=5
# # if n^1==n+1:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #even or odd using // operator
# # n=4
# # if n//2*2==n:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #even or odd using << operator
# # n=2
# # if n<<1==n*2:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #even or odd using >> operator
# # n=4
# # if n>>1==n/2:
# #     print(n,"is even")
# # else:
# #     print(n,"is odd")
# # #multiple of 4 using >> operator
# # n=8
# # if n>>2==n/4:
# #     print(n,"is multiple of 4")
# # else:
# #     print(n,"is not multiple of 4")
# # #multiple of 4 using xor operator
# # n=12
# # if n^2==n+2:
# #     print(n,"is multiple of 4")
# # else:
# #     print(n,"is not multiple of 4")
# # #swap 2 number using xor operator
# # a=5
# # b=10
# # a=a^b
# # b=a^b
# # a=a^b
# # print("a:",a)
# # print("b:",b)
# # #count number of 1 digits in a binary number getting binary number with quotient and remainder
# # n=int(input("Enter a number: "))
# # count=0
# # while n!=0:
# #     if n%2==1:
# #         count+=1
# #     n=n//2
# # print(count)
# # print(bin(1010110))
# # 1010110->find decimal
# n=1010110
# decimal=int(str(n),2)
# print("Decimal equivalent:", decimal)
# #power of 2 using & operator
# n=8
# if n&(n-1)==0:
#     print(n,"is a power of 2")
# else:
#     print(n,"is not a power of 2")
# #count number of 1 and 0 digits in a binary number
# n=int(input("Enter a number: "))
# count1=0
# count0=0
# while n!=0:
#     if n%2==1:
#         count1+=1
#     else:
#         count0+=1
#     n=n//2
# print("Number of 1 digits:", count1)
# print("Number of 0 digits:", count0)
# #find postions of 1 digits in a binary number
# n=int(input("Enter a number: "))
# positions=[]
# i=0
# while n!=0:
#     if n%2==1:
#         positions.append(i)
#     n=n//2
#     i+=1
# print("Positions of 1 digits:", positions)
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        result[i][j]=l1[i][j]+l2[i][j]
    print(result[i])
 # 1010110->find decimal
n=1010110
d=0
for i in range(len(str(n))):
    if str(n)[i]=='1':
        d+=2**(len(str(n))-1-i)
print("Decimal equivalent:", d)
