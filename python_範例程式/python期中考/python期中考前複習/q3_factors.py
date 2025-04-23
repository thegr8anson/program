# 輸入一個正整數
input_num = int(input('輸入一個正整數'))

# 初始化因數總和為0
sum = 0

# 從 1 到 input_num-1 進行迴圈，檢查是否為 input_num 的因數
for i in range(1, input_num, 1):
    if input_num % i == 0:  # 如果 i 能被 input_num 整除 (表示 i 是 input_num 的因數)
        sum += i # 將 i 加到總和中

print(f'{input_num} 所有因數的總和（不包含自己但包含 1）為: {sum}')
