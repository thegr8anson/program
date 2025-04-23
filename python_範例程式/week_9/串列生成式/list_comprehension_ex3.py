# list_comprehension_ex3.py

# 原本寫法
# a = input().split(' ') # 用空格分開
# b = []
# for i in a:
#     b.append(int(i))
# print(b)

# 使用生成式
a = [int(i) for i in input().split(' ')]
print(a)