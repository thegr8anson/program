# 輸入兩數
a=int(input('輸入一個正整數: '))
b=int(input('輸入一個正整數: '))

# 比較 a 和 b，將較大的數字存入 greater 變數
if a > b :
    greater = a
else :
    greater = b

# 使用無窮迴圈來尋找最小公倍數
while True:
    # 如果 greater 能同時被 a 和 b 整除，則找到最小公倍數
    if greater % a == 0 and greater % b == 0:
        break # 跳出迴圈，因為找到了最小公倍數
    else :
        greater+=1 # 如果還沒找到，將 greater 加 1，繼續尋找

print(f'{a}和{b}的最小公倍數為: {greater}')
