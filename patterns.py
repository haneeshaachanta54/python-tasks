#create a pattern for a horizontal rectangle using nested loops
n=5
m=3
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()
# create a pattern for a horizontal rectangle using nested loops using '0'
n=5
m=3
for i in range(m):
    for j in range(n):
        print("1", end=" ")
    print()
# create a pattern for a horizontal rectangle using nested loops pattern'11111 22222 33333'
n=5
m=3
for i in range(1,m+1):
    for j in range(n):
        print(i, end=" ")
    print()
# create a pattern for a horizontal rectangle using nested loops pattern'12345 12345 12345'
n=5
m=3
for i in range(m):
    for j in range(1,n+1):
        print(j, end=" ")
    print()
# create a pattern for a horizontal rectangle using nested loops pattern'54321 54321 54321'
n=5
m=3
for i in range(m):
    for j in range(n,0,-1):
        print(j, end=" ")
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'AAAAA BBBBB CCCCC'
n=5
m=3
for i in range(1,m+1):
    for j in range(n):
        print(chr(64+i), end=" ")
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'ABCDE ABCDE ABCDE'
n=5
m=3
for i in range(m):
    for j in range(1,n+1):
        print(chr(65+j-1), end=" ")
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'EDCBA EDCBA EDCBA'
n=5
m=3
for i in range(m): 
    for j in range(n,0,-1):
        print(chr(64+j), end=" ")
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'ABCDE EDCBA ABCDE'
n=5
m=3
for i in range(m):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j), end=" ")
        else:
            print(chr(64+n-j+1), end=" ")
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'ABCDE FGHIJ KLMNO'
n=5
m=3
val=0
for i in range(m):
    for j in range(1,n+1):
        print(chr(65+val), end=" ")
        val+=1
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'ZYXWV UTSRQ PONML'
n=5
m=3
val=0
for i in range(m):
    for j in range(n,0,-1):
        print(chr(90-val), end=" ")
        val+=1
    print()
#create a pattern for a horizontal rectangle using nested loops pattern'ABCDEF FEDCBA ABCDEF FEDCBA'
n=6
m=3
for i in range(m):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j), end=" ")
        else:
            print(chr(64+n-j+1), end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'** ** ** ** ** ** ** ** ** **'
n=2
m=10
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'00 00 00 00 00 00 00 00 00 00'
n=2
m=10
for i in range(m):
    for j in range(n):
        print("0", end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'12 12 12 12 12 12 12 12 12 12'
n=2
m=10
for i in range(m):
    for j in range(1,n+1):
        print(j, end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'21 21 21 21 21 21 21 21 21 21'
n=2
m=10
for i in range(m):
    for j in range(n,0,-1):
        print(j, end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'AB AB AB AB AB AB AB AB AB AB'
n=2
m=10
for i in range(m): 
    for j in range(1,n+1):
        print(chr(65+j-1), end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'BA BA BA BA BA BA BA BA BA BA'
n=2
m=10
for i in range(m):
    for j in range(n,0,-1):
        print(chr(64+j), end=" ")
    print()
#create a pattern for a vertical rectangle using nested loops pattern'AB CD EF GH IJ KL MN OP QR ST'
n=2
m=10
val=0
for i in range(m):
    for j in range(1,n+1):
        print(chr(65+val), end=" ")
        val+=1
    print()
#create a pattern for a vertical rectangle using nested loops pattern'BA DC FE HG JI LK NM PO RQ TS'
n=2
m=10
val=0
for i in range(m):
    for j in range(n,0,-1):
        print(chr(64+val+j), end=" ")
    val+=n
    print()
#create a pattern for a vertical rectangle using nested loops pattern'ABC DEF GHI JKL MNO PQR STU VWX YZ'
n=3
m=9
val=0
for i in range(m):
    for j in range(1,n+1):
        print(chr(65+val), end=" ")
        val+=1
    print()
#create a pattern for a vertical rectangle using nested loops pattern'CBA FED IHG LKJ ONM RQP UTS XWV ZY'
n=3
m=9
val=0
for i in range(m):
    for j in range(n,0,-1):
        print(chr(64+val+j), end=" ")
    val+=n
    print()
# create a pattern for a vertical rectangle using nested loops pattern'ABC CBA ABC CBA ABC CBA ABC CBA ABC CBA'
n=3
m=8
val=0
for i in range(m):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j), end=" ")
        else:
            print(chr(64+n-j+1), end=" ")
    print()
# create a pattern for a vertical rectangle using nested loops pattern'ACE CEG ACE CEG ACE CEG ACE CEG ACE'
n=3
m=8
val=0
for i in range(m):
    for j in range(1,n+1):
        if i%2==0:
            print(chr(64+j*2-1), end=" ")
        else:
            print(chr(64+n*2-j*2+1), end=" ")
    print()