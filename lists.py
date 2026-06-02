#sum of the lists without built in function
l=[1,2,3,4,5]
sum=0
for val in l:
    sum+=val
print(sum)
#product of the lists without built in function
l=[1,2,3,4,5]
prd=1
for val in l:
    prd*=val
print(prd)
#Maximium of the lists without built in function
l=[1,2,3,4,5]
max1=0
for val in l:
    if(max1<val):
        max1=val
print(max1)
#Minimum of the lists without built in function
l=[1,2,3,4,5]
min1=l[0]
for val in l:
    if(min1>val):
        min1=val
print(min1)
#count of the lists without built in function
l=[1,2,3,4,5,6]
cnt=0
for val in l:
    cnt+=1
print(cnt)
