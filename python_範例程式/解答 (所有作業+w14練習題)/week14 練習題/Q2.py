matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 提取主對角線元素
main_diagonal = [matrix[i][i] for i in range(len(matrix))]  # 左上到右下

# 提取反對角線元素
anti_diagonal = [matrix[i][-i-1] for i in range(len(matrix))]  # 右上到左下

print("主對角線:", main_diagonal)
print("反對角線:", anti_diagonal)
