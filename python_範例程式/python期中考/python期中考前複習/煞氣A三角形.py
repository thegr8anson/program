n=int(input("請輸入層數"))

#最上面的一層
for i in range(0,n+1,1):
    print(i,end="")
for i in range(n-1,-1,-1):
    print(i,end="")

for i in range(1,n+1,1):#中間的三角形層數
    print()
    for j in range(0,n-i+1,1):
        print(j,end="")
    for j in range(1,2*i):
         print(" ",end="")
    for j in range(n-i,-1,-1):
         print(j,end="")
print()

#最下面的一層
for i in range(0,n+1,1):
    print(i,end="")
for i in range(n-1,-1,-1):
    print(i,end="")