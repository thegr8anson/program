#  輸入兩個正整數，輸出最小公倍數
#  Hint:
#  1.GCD
#  or
#  2.一個迴圈，遞增倍數，直到找到能同時被兩個數整除的數 

a=int(input('輸入一個正整數: '))
b=int(input('輸入一個正整數: '))
ans_a=a
ans_b=b
answer_gcd = None

while (b != 0) :
    temp = a % b
    a = b
    b = temp
answer_gcd = a    

greater = abs(ans_a * ans_b) / answer_gcd

print(f'{ans_a}和{ans_b}的最小公倍數為: {greater}')