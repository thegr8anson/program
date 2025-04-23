'''
請製作一個幾A幾B的小遊戲
使用者輸入四個數字
輸出  "?A?B" ex.3A1B

hint:
generate_secret(): 
生成一組隨機的四位數字組合，數字不重複
可以利用 random 的函式完成

calculate_ab(secret,gusess)
secret: 隨機生成的答案
gusess: 使用者猜的答案
輸出 A,B 為A的數量及B的數量
'''


import random

def generate_secret():
    # code here
    sample_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    secret = random.sample(sample_number, 4)
    return secret
    # code here
def calculate_ab(secret, guess)-> tuple[int, int]:
    # code here
    A = 0
    B = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if (secret[i] == guess[j]):
                if (i == j):
                    A += 1
                    continue
                else:
                    B += 1
                    continue               
    return A,B
    # code here


def game():
    """生成一個隨機的四位數字組合，數字不重複"""
    secret = generate_secret()
    attempts = 0
    print("歡迎來到幾A幾B小遊戲！請猜一個四位數字，每位數字不重複。")

    while True:
        guess = input("請輸入你的猜測：ex.1234\n")
        
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("請輸入四位不重複的數字！")
            continue

        attempts += 1
        """計算幾A幾B"""
        A, B = calculate_ab(secret, guess)
        print(f"{A}A{B}B")

        if A == 4:
            print(f"恭喜你！猜對了！總共猜了 {attempts} 次。")
            break

# 開始遊戲
game()

