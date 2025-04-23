# break_ex1.py
# 使用break結束迴圈

count = 3 

# 從10開始，數3下就停
for i in range(10, 1, -1):
    if count <= 0:
        # 如果剩餘的count <= 0 代表數完了
        # 所以使用 break 離開迴圈
        print("count <= 0，結束迴圈")
        break

    # 如果剩餘的count > 0 繼續執行以下敘述
    print(f"i = {i}")
    count = count - 1

print("程式結束")

'''
--------output--------
i = 10
i = 9
i = 8
count <= 0，結束迴圈
程式結束
----------------------
'''


