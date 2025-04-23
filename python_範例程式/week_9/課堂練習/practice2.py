words = [] # 建立一個空的串列來存放單字

# 使用迴圈讓使用者連續輸入 5 個單字
for i in range(5):
    word = input(f"請輸入第 {i+1} 個英文單字: ")
    words.append(word)

# 印出結果
print(words)