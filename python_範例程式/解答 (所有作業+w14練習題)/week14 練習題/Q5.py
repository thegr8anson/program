## Q5 : 小朋友上樓梯

def count_ways(n):
    # 如果是 0 階或 1 階，只有 1 種走法
    if n == 0 or n == 1:
        return 1
    # 利用遞迴計算
    return count_ways(n - 1) + count_ways(n - 2)

n = 3
print(f"小朋友走到 {n} 階共有 {count_ways(n)} 種走法")
