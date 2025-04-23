n = int(input())

for i in range(1, n+1, 1):
    print("*", end=" ")
print()

for i in range(1, int(n/2)+1, 1):
    # star
    for j in range(int(n/2)-i+1, 0, -1):
        print("*", end=" ")
    
    # space
    for j in range(1, 2*i, 1):
        print(" ", end=" ")

    # star
    for j in range(int(n/2)-i+1, 0, -1):
        print("*", end=" ")

    print()

for i in range(1, int(n/2), 1):
    # star
    for j in range(1, i+2, 1):
        print("*", end=" ")

    
    # space
    for j in range(1, (n-2*i)-1, 1):
        print(" ", end=" ")

    # star
    for j in range(1, i+2, 1):
        print("*", end=" ")
    print()
    

for i in range(1, n+1, 1):
    print("*", end=" ")