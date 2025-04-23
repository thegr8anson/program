'''
字串操作範例程式
'''

# 1. 字串相加
str1 = "Hello"
str2 = "NSYSU"
# 使用 "+" 將兩個字串相加
concatenated_str = str1 + " " + str2 # 中間以空白做連接
print("字串相加: ", concatenated_str)  # Hello World

# 2. 重複字串
# 使用 "*" 重複字串
repeated_str = "Apple" * 3
print("重複字串: ", repeated_str)  # AppleAppleApple

# 3. 計算字串長度 
# 使用內建函數 len() 來計算字串相加後的長度
length_of_str = len(concatenated_str)
print("字串長度: ", length_of_str)  # 結果為 11，包含空格

# 4. 轉義/跳脫字元 (Escape Characters)
# 使用反斜線 '\' 來插入特殊字元，像是雙引號、換行符號等等
escaped_str = "The teacher said, \"Hello!\"\nHow are you?"
print("跳脫字元: ")
print(escaped_str)  # 顯示兩行: The teacher said, "Hello!" 和 How are you?