# 合併串列

a = [1, 2, 3]
b = [4, 5, 6]

# 使用 "+"
# 將串列 a 和 b 合併為一個新的串列，不會改變原始串列 a, b 的內容。
merged_list = a + b
print(merged_list)  # [1, 2, 3, 4, 5, 6]


# 使用 extend()
# 將 b 的每個元素逐一添加到 a 中，會直接改變串列 a 的內容。
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]




