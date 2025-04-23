n=int(input("請輸入層數"))

print("*")
for i in range(1,n-2+1,1):
    print("*",end="")
    for j in range(1,i):
        print(" ",end="")
    print("*",end="")
    print()

for i in range(1,n+1):
    print("*",end="")

