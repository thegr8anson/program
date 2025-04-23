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

print(f"{ans_a}和{ans_b}的最大公因數為: {answer_gcd}")