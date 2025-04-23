# 移除串列元素

a = [1, 3, 5, 7, 9, 3]

# 使用 remove()
# 移除指定值的第一個元素，若重複則只會刪除第一個
a.remove(3)
print(a)  # [1, 5, 7, 9, 3]

# 使用 pop() 
# 移除指定索引(預設為最後一個)的元素，並回傳該元素
removed_element = a.pop(2)  # 移除索引為 2 的元素
print(a)               # [1, 5, 9, 3]
print(removed_element) # 7

# 使用 clear() 
# 將所有元素移除，讓 list 變為空串列
a.clear()

print(a)  # []


