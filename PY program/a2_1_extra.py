word=input("請輸入一個英文單字判斷是否有迴文")
result=None
a = list(word)
b = a.copy()
b.reverse()
print(a)
print(b)
if (a == b):
    result = True
else:
    result = False        
print(result)
