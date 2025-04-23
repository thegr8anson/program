# continue_ex1.py
# 使用continue跳過某次迴圈

for i in range(10, 1, -1):
    if (i % 3 == 0):
        # 如果i為3的倍數，就跳過此次迴圈執行
        # 直接進行下一輪迴圈
        continue

    print(f"i = {i}")

print("程式結束")



'''
--------output--------
i = 10
i = 8   
i = 7   
i = 5   
i = 4   
i = 2   
程式結束
----------------------
'''

