a=int(input('輸入一個正整數: '))
b=int(input('輸入一個正整數: '))
greater = 1

while (greater % a != 0 or greater % b != 0):
    greater = greater + 1

print(f'{a}和{b}的最小公倍數為: {greater}')