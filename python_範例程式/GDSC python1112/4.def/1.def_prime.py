def isPrime(num):
    if(num <= 1):
        return False
    if(num == 2):
        return True
    if(num%2 == 0):
        return False
    for i in range(3, num, 2): # This works because num here must be an odd number.
        if num%i == 0:
            return False
    return True

while(True):
    num = int(input("Input a number(-1 to exit): "))
    if(num == -1):
        break
    if(isPrime(num)):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")