n=int(input("請輸入層數"))

for i in range(1,n+1,1):
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(i,i*2,1):
        print(k,end="")
    for q in range(k-1,i-1,-1):
        print(q,end="")
    print()