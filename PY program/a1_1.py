#一個非空的整數陣列 nums，其中每個元素都出現兩次，只有一個元素只出現一次。找出這個唯一的元素，並print出來。

nums=[4,4,2,2,3,3,1]
result = None

#--------------------------------------code here
# 找出出現過一次的元素
for result in nums:
    if (nums.count(result) == 1):
        print(result)

#--------------------------------------code here


#--------------------------------------code here
# 輸出檔案成output.txt
f = open("output.txt", 'a', encoding = "utf-8")
f.write(str(result))
f.close()

#--------------------------------------code here
