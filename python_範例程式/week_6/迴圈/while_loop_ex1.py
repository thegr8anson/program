# while_loop_ex1.py
# 要幾張1000元，才夠付帳單?

bill = 45163
count = 0

while (count * 1000) < bill:
    count = count + 1

print(f"最少需要 {count} 張1000元，才夠付 {bill} 元的帳單") 

'''
------output------
最少需要 46 張1000元，才夠付 45163 元的帳單。
------------------
'''

