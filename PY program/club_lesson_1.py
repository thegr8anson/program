print("Hello world")    #Hello world
print("Hello","world")  #Hello world
print(1,2,3,sep = "\n", end = "\n")    #1
                                       #2
                                       #3
print(1,2,3, sep = ',', end = "\n")    #1,2,3
#In python, complex number should be written in a + bj
#Multi-line comments can be done by selecting code fragments and press ctrl + /
#list: [] tuple: () set: {}
print(type(1))  #int
print(type(0.1))    #float
print(type('1'))    #str
print(type("1"))    #str
print(type('''1'''))    #str
print(type(5+2j))   #complex
print(type([1, 2, 3, 4]))   #list
print(type((1, 2, 3, 4)))   #tuple
print(type({1, 2, 3, 4}))   #set
print(type({"apple":1, "banana":2}))    #dict
print(type({1, 2, 3, 4, 5} == {1, 2, 3, 4, 5, 5}))  #bool
#強制轉型: x = new data type (original data) 
#ex: x = int(5.4)
print(int(5.5)) #5(無條件捨去)
print(int(5.4)) #5(無條件捨去)
print(list("hello world")) #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'](空格也算)
print(set("hello world")) #{'e', 'd', 'r', 'l', 'w', 'h', ' ', 'o'}(順序為random,且會刪除重複資料)
#special operators: "/" floating-point division "//" integer division "**" 次方 ex: 2**3 = 8 
#compound statement: += -= *= /= //= **= %=
#conditional: == (equal) != (not equal) ^ (xor) > >= < <= and or not 
#  in (for container, see if the element on the left exists in the container on the right)
#  is (see if two variables are in the same place in the memory)(not recommended)
#xor : a ^ b (either a or b is true --> true ; both a and b is true --> false; neither a nor b is true --> false)
#ex: 5 in [1,2,3,4,6] --> false 
#ex: x = y 
#    x is y --> true
print("Hi" + " " + "Friend") # add strings together
print([1, 2, 3]+[4, 5, 6]) # add lists together
print((1,)+(2,)+(3,)) #If only one element exists in the tuple, it's necessary to add a comma before ).
print("hi"*3) #repeat string
print([1, 2, 3]*3) #repeat list
print((1,)*3) #repeat tuple
print("hello" > "World") # compare ASCII unicode
print([1, 2, 3] > [1, 2, 4]) # same as above
print((1, 2, 3) > (1, 2, 4)) # same as above
#The default data type for input() is string.
ID = input("What's your student ID: ") #What's your student ID: (B123040012)
print("Your student ID is", ID) #Your student ID is B123040012
print(f"Your student ID is {ID}") #Your student ID is B123040012
var1 = input("var1: ") #var1: 1                                  
var2 = input("var2: ") #var2: 2
print(f"var1 + var2 = {var1 + var2}") #var1 + var2 = 12 (string addition)
print(f"var1 + var2 = {int(var1)+int(var2)}") #var1 + var2 = 3 (轉型, integer addition)
list1 = [0, 1, 2, 3, 4]
list2 = [0, 1.5, "hi", 6+7j]
list3 = [ ] #(empty list)
print(list1, list2, list3, sep = '\n')
myList = [1, 2, 3, 4, 5]
print(myList)
myList[0] = 1.1 #change the first element
print(myList)
myList[-1] = 5.5 #change the last element
print(myList)
NewList = [1, 2, 3, 4, 5]
print(NewList)
#python 為左閉右開，即[  ,  ) ，也就是 a <= x < b
print(NewList[0:1]) # = myList[0]
print(NewList[0:5]) # = myList[0] + ... + myList[4]
print(NewList[1:-1]) # = myList[1] + ... + myList[3]
print(NewList[2:]) # = myList[2] + ... + myList[4] (from 2nd to the last element)
print(NewList[:]) # = myList[0] + ... + myList[4] (print the whole list)