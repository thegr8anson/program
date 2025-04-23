# for_loop_ex2.py
# 計算丟骰子的機率
# 丟10000次骰子，印出點數為三的次數和機率

import random # 引用random模組

count = 0 # 用來儲存丟到三的次數

for i in range(1, 10001, 1):
    if random.randint(1, 6) == 3:
        # 使用randint(a, b)，產生骰子隨機點數值
        # randint(a, b) -> Return a number between a and b (both included)
        count = count + 1

print(f"丟10,000次骰子，出現3的次數為 : {count}\n")
print(f"機率為 : {float(count/10000)}\n")

