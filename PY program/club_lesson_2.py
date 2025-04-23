# name = input("Please enter your name:")
# age = int(input("Please enter your age:"))
# print(f"Hello, {name}! Next year, you will be {age + 1} years old.") 


# a = int(input("Please enter the first integer:"))
# b = int(input("Please enter the second integer:"))
# print(f"{a} divided by {b} gives a quotient of {a // b} and a remainder of {a % b}.")

# myList = [1, 2, 3, 4, 5]
# print(myList)
# print(myList[0:1]) # = myList[0]
# print(myList[0:5]) # = myList[0] + ... + myList[4]
# print(myList[1:-1]) # = myList[1] + ... + myList[3]
# print(myList[2:]) # = myList[2] + ... + myList[4]
# print(myList[:]) # = myList[0] + ... + myList[4]


# myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list slicing: list[a:b:c], if any one of a, b, c is not specified,
#                                              # the default is [index 0, last index + 1, step = 1]. 
# start = 2
# end = 8
# step = 2
# print(myList[start:end:step]) # myList[2] + myList[4] + myList[6] (no 8)
# print(myList[start::step]) # myList[2] + ... + myList[10]
# print(myList[:end:step]) # myList[0] + myList[2] + ... + myList[6]
# print(myList[start:end:]) # myList[2] + myList[3] + ... + myList[7]


# myList = [1, 3.14, "hello", [3, 4]]
# print(myList[0:4:1])
# myList.append(7)
# print(myList)
# myList.append((8, 7))
# print(myList)
# print(myList[::-1])  # Tip: Set step to -1 can reverse the list.
# myList.pop() # Tip: The default of pop() is the last index.
# print(myList)
# myList.pop(0)
# print(myList)

# myList = [35, 2, 53, 61, 4, 70, 41, 9, 12]
# print(myList)
# myList.sort()
# print(myList)
# myList.sort(reverse = True)
# print(myList)

# tuple1 = (0, 1, 2, 3, 4)
# tuple2 = (0, 1.5, "hi", 6+7j)
# tuple3 = ( )
# tuple4 = (1) # It's not a tuple, just a integer.
# tuple5 = (1, ) # If you want to create a tuple containing only one element, then add a comma(,) at the end of the element.
# print(tuple1, tuple2, tuple3, tuple4, tuple5, sep = '\n')

# myTuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(myTuple[3])
# print(myTuple[1:5])
# print(myTuple[::3])


# print("Hi" + " " + "Friend")
# print([1, 2, 3]+[4, 5, 6])  # Combine list
# print((1,)+(2,)+(3,)) #Combine tuple
# print("hi"*3)
# print([1, 2, 3]*3) # Repeat the content 3 times, and form a new list.
# print((1,)*3) # Same as above but in the case of tuple.
# print("hello" > "World")  # Compare Unicode
# print([1, 2, 3] > [1, 2, 4])
# print((1, 2, 3) > (1, 2, 4))


# myTuple = (0, 1, 2, 3, 4)
# print(myTuple)
# myTuple = (5,) + myTuple[1:] # but you can do this
# print(myTuple)

# Operator for set: | (union 聯集) & (intersection 交集) - (difference 差集) 
#                   ^ (symmetric difference 反差集 XOR) > >= (superset 包含) < <= (subset 包含於)

# empty list [] empty tuple () empty dict {} empty set set()
# Set deletes repeated elements.  

myDict = {"name":"Dyson","age":19,"C":"C-","Python":"A+"}
print(myDict["name"], myDict["age"])   # The key is the index for its value

myDict["Calculus"] = "A+"        # add new keys and values to dict
myDict["Data Structure"] = "A+"
print(myDict)

del myDict["C"]       # del means delete
del myDict["Python"]
print(myDict)

print(myDict.keys())   # Shows all keys of the dict

print(myDict.values())  # Shows all values of the dict

print(myDict.items())  # Shows all keys and values in pair in form of tuple

