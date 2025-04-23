# 輸入兩數
a=int(input('輸入一個正整數: '))
b=int(input('輸入一個正整數: '))

# 保存輸入原始值
ans_a=a
ans_b=b

# 輾轉相除法
# 當 a 除以 b 的餘數不等於 0 時，繼續迴圈
# 更新 a 和 b 的值，直到找到最大公因數
while a % b !=0:
    temp=b     # 暫存 b 的值
    b= a % b   # 更新 b 為 a 除以 b 的餘數
    a=temp     # 將 a 更新為之前的 b 值

# 當迴圈結束時，b 就是 a 和 b 的最大公因數
print(f"{ans_a}和{ans_b}的最大公因數為: {b}")
