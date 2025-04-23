'''
- b的值賦予給變數a
- c的值賦予給變數b
- a的值賦予給變數c
'''
a = 1
b = 2
c = 3
print(a, b, c) # 1, 2, 3
a, b, c = b, c, a # 交換內容
print(a, b, c) # 2, 3, 1