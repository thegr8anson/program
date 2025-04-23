# 建立串列的方式 list_ex1.py
# 1) 中括號
x = ['apple', 'bicycle', 'come'] # 文字串列 ['apple', 'bicycle', 'come']
y = [1, 2, 3, 4, 5] # 數字串列 [1, 2, 3, 4, 5]
z = ['apple', 1, 2, ['NSYSU', 'MIS']] # 複合串列 ['apple', 1, 2, ['NSYSU', 'MIS']]
print(x)
print(y)
print(z)
print('-'*50) # 我是分隔線

# 2) list()
a = list() # 空串列 []
b = list('apple') # 字元串列 ['a', 'p', 'p', 'l', 'e']
c = list(x) # 文字串列 ['apple', 'bicycle', 'come']
print(a)
print(b)
print(c)
print('-'*50) # 我是分隔線

# 3) str.split() -> 可以將一個字串斷開為許多不同的片段，並組成list
strA = "how do you turn this on"
print(strA.split(" ")) # ['how', 'do', 'you', 'turn', 'this', 'on'] (讀取字串時以空格做區隔)
strB = "1,2,3,4,5,6,7"
print(strB.split(",")) # ['1', '2', '3', '4', '5', '6', '7'] (讀取字串時以逗點做區隔)


