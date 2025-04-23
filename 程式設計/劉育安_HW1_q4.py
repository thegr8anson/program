def squareOddsum(num):
    # please finish your function here
    if (num == []):
        return 0
    if (num[0] % 2):
        return num[0] ** 2 + squareOddsum(num[1:])
    else:
        return squareOddsum(num[1:])
        
def main():
    try:
        num_list = list(map(int, input("Please enter a list of integers separated by space: ").split()))
        print("Squares of all odd:", squareOddsum(num_list)) 
    except ValueError:
        print("Invalid input. Please enter integers only.") 
        
if __name__ == "__main__":
    main()