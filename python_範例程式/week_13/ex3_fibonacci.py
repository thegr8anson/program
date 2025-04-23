## ex3_finonacci.py ##

# 使用遞迴計算費式數列
def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
# 主程式，印費式數列1~10
for i in range(1, 11):
    print(f"fibonacci({i}) = {fibonacci(i)}")

