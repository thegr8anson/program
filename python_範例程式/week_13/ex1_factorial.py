## ex1_factorial.py ##

# 階層函式
def factorial(number):
    if number >= 1:     
        return number*factorial(number-1)
    else:
        return 1

# 主程式，呼叫階層函式來執行遞迴
print(factorial(4))



'''
------ output ------
24
--------------------
'''

