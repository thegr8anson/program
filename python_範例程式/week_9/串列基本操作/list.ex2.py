# 讀取字串 list_ex2.py
# 使用索引讀取串列內容

a = ['apple', 'banana', 'orange']
print(a[0]) # apple
print(a[1]) # banana
print(a[2]) # orange
print(a[-1]) # orange (負的從後面數回來，最後是-1)

a = [['apple', 'banana'], ['dog', 'cat']] # apple, banana
                                          # dog, cat
print(a[0][1]) # banana
print(a[1][1]) # cat

