def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)

def main():
    count = 0
    for i in range(1, 100001):
        sum = 0
        tmp = i
        while (tmp != 0):
            sum += factorial(int(tmp % 10))
            tmp //= 10
        if (i == sum):
            print(f"{i} is a factorion")
            count += 1
    print("Total factorions found:", count)
        

if __name__ == "__main__":
    main()