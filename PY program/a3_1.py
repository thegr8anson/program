# 一個由單詞組成的句子（由空格分隔）和一個整數 n，要求提取前 n 個單詞，並用 `-` 符號連接。如果單詞數量少於 n，則返回 "不存在"。

#hint: 使用 join() 來加入分隔符號"-"

sentence = "I love programming in Python"
n = 3
result = None

#--------------------------------------code here
MyList = sentence.split(' ')
if len(MyList) >= n :
    result = '-'.join(MyList[:n])
    print(result)
else :
    print("不存在")
#--------------------------------------code here
