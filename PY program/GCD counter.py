#輸入兩個正整數，輸出兩數的最大公因數
# hint:
# 輾轉相除法
a,b=map(int,input('輸入兩個正整數: ').split())
#a, b = input().split()
ans_a=int(a)
ans_b=int(b)
answer_gcd = None

while (b != 0) :
    temp = a % b
    a = b
    b = temp
answer_gcd = a   

print(f"{ans_a}和{ans_b}的最大公因數為: {answer_gcd}")