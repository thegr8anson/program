'''
算術運算範例
'''

# 1. 整數 (Integer) 運算
a = 10
b = 3

# 加法
addition = a + b
print("整數加法 (a + b):", addition)  # 結果為 13

# 減法
subtraction = a - b
print("整數減法 (a - b):", subtraction)  # 結果為 7

# 乘法
multiplication = a * b
print("整數乘法 (a * b):", multiplication)  # 結果為 30

# 除法 (Python 3 中的 "/" 會返回浮點數)
division = a / b
print("整數除法 (a / b):", division)  # 結果為 3.3333333333333335

# 整數除法 (只取整數部分)
integer_division = a // b
print("整數整除 (a // b):", integer_division)  # 結果為 3

# 取餘數 (Modulo)
modulus = a % b
print("取餘數 (a % b):", modulus)  # 結果為 1

# 次方 (Exponentiation)
exponentiation = a ** b
print("次方 (a ** b):", exponentiation)  # 結果為 1000

# 先乘除後加減，括號內先算
arithmetic_rule = a*(a+b)
print("四則運算(先乘除後加減，括號內先算):", arithmetic_rule) # 結果為130

# 2. 浮點數 (Floating Point) 運算
x = 5.5
y = 2.3

# 加法
float_addition = x + y
print("浮點數加法 (x + y):", float_addition)  # 結果為 7.8

# 減法
float_subtraction = x - y
print("浮點數減法 (x - y):", float_subtraction)  # 結果為 3.2

# 乘法
float_multiplication = x * y
print("浮點數乘法 (x * y):", float_multiplication)  # 結果為 12.65

# 除法
float_division = x / y
print("浮點數除法 (x / y):", float_division)  # 結果為 2.391304347826087


# 3. 整數與浮點數混合運算
mixed_addition = a + x
print("整數與浮點數相加 (a + x):", mixed_addition)  # 結果為 15.5

mixed_multiplication = b * y
print("整數與浮點數相乘 (b * y):", mixed_multiplication)  # 結果為 6.8999999999999995