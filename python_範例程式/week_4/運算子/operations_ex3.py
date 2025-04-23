'''
Boolean 比較運算範例
'''

# 1. 相等運算符 (==)
x = 10
y = 20
print("x == y:", x == y)  # False，因為 x 不等於 y

# 2. 不相等運算符 (!=)
print("x != y:", x != y)  # True，因為 x 不等於 y

# 3. 大於運算符 (>)
print("x > y:", x > y)  # False，因為 x 小於 y

# 4. 小於運算符 (<)
print("x < y:", x < y)  # True，因為 x 確實小於 y

# 5. 大於等於運算符 (>=)
z = 10
print("x >= z:", x >= z)  # True，因為 x 等於 z

# 6. 小於等於運算符 (<=)
print("x <= z:", x <= z)  # True，因為 x 等於 z

# 7. 使用布林值進行比較
is_raining = True
is_sunny = False

# 相等比較
print("is_raining == is_sunny:", is_raining == is_sunny)  # False，因為 True 不等於 False

# 不相等比較
print("is_raining != is_sunny:", is_raining != is_sunny)  # True，因為 True 與 False 不相等

# 8. 比較數字與布林值
# True 相當於數字 1，False 相當於數字 0
print("is_raining == 1:", is_raining == 1)  # True，因為 True 相當於 1
print("is_sunny == 0:", is_sunny == 0)      # True，因為 False 相當於 0