# 一個由單詞組成的句子（由空格分隔）和一個整數 n，要求提取前 n 個單詞，並用 `-` 符號連接。如果單詞數量少於 n，則返回 "不存在"。

#hint: 使用 join() 來加入分隔符號"-"

sentence = "I love programming in Python"
n = 3
result = None

#--------------------------------------code here
# 使用 split() 將句子分割成單詞的列表
words = sentence.split()

# 檢查單詞數量是否小於 n
if len(words) < n:
    result = "不存在"
else:
    # 提取前 n 個單詞並用 `-` 連接
    result = '-'.join(words[:n])
#--------------------------------------code here

print(result)