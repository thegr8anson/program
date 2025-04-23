matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 使用切片提取子矩陣
output = [row[1:3] for row in matrix[1:3]]

print(output)