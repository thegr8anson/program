a = int(input("a = "))
b = int(input("b = "))

if(a > b):
    print(f"{a} is larger than {b}.")
    
if(a <= b):
    if(a < b):
        print(f"{a} is smaller than {b}.")
    if(a == b):
        print(f"{a} is equal to {b}.")
    print("This line will be printed only when a <= b.")
    
print("This line will be printed anyway")
print("because it is not in the body of if.")
