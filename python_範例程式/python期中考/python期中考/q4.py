n = int(input("Input an integer:"))
if n <= 0:
    print("Invalid input!")
else:
    for i in range(1, n+1, 1):
        if i%7==0 or i%11==0:
            print("FizzBuzz", end=" ")
        elif i%2==0:
            print("even", end=" ")
        else:
            print(i, end=" ")
