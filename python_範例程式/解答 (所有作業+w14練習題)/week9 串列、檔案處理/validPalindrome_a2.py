# 判斷一個英文單字是否為迴文
# 迴文是指正讀和反讀都相同的字串，例如 "level" 或 "radar"。


# 測試範例
#輸入 level 輸出: True
#輸入 hello 輸出: True

word=input("請輸入一個英文單字判斷是否有迴文")

result=None
#----------------------------------------code here


result=word==word[::-1]


#----------------------------------------code here

print(result)


