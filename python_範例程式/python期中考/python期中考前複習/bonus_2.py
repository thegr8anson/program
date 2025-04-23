n=int(input("請輸入層數"))

for i in range(1,n+1,1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(1,i*2,1):
        if k%2==0:
            print("0",end="")
        else:
            print("*",end="")
        
    print()