n=int(input("請輸入層數"))

for i in range(1,n+1,1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(1,2*i,1):
        print("*",end="")
    print()

for i in range(1,n,1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(2*(n-i)-1,0,-1):
        print("*",end="")
    print()