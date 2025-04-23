## ex2_power.py ##

# 次方函式
def power_function(base, exp): # 第1個參數:底數 / 第2個參數:次方數
    if exp == 0:
        return 1
    else:
        return base*power_function(base, exp-1)

# 主程式，呼叫次方函式來執行遞迴
print(power_function(2, 3))


'''
------ output ------
8
--------------------
'''