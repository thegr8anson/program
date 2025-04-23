#input output 
print("apple","banana","coconut")
print("apple","banana","coconut",sep="&")
print("apple","banana","coconut",sep=";",end=".")#用end會導致下一行接在同一行後面
print("\napple,banana,%s" % "coconut")#用\n來換行
massage = input("Please enter a sentence you want to repeat:")
print(massage)
name = input("Please enter your name:")
number = input("Please enter your number:")
a = "Hi {}. Your number is {}"
b = a.format(name,number)
print(b)
c = "Welcome to {1}. I'm {0}."
d = c.format("Anson","python")
print(d)
e = "I hate {error_type}, and it happens {frequency}."
f = e.format(error_type = "FileNotFoundError",frequency = "all the time") 
print(f)
g = "weather"
h = "nice"
i = f"The {g} is so {h} today."
print(i)