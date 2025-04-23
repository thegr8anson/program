import random

def generate_secret():
    # code here
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))
    # code here
def calculate_ab(secret, guess)-> tuple[int, int]:
    # code here
    A = sum(1 for s, g in zip(secret, guess) if s == g)
    B = sum(1 for g in guess if g in secret) - A
    return A, B
    # code here


def game():
    """生成一個隨機的四位數字組合，數字不重複"""
    secret = generate_secret()
    attempts = 0
    print("歡迎來到幾A幾B小遊戲！請猜一個四位數字，每位數字不重複。")

    while True:
        guess = input("請輸入你的猜測且：")
        
        
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