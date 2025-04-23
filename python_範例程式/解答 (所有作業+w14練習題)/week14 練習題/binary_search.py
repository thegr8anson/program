def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid  # 找到目標值
        elif nums[mid] > target:
            right = mid - 1  # 縮小搜尋範圍至左半部分
        else:
            left = mid + 1  # 縮小搜尋範圍至右半部分
    
    return -1  # 若未找到目標值，返回 -1


# 測試資料
examples = [
    ([1, 3, 5, 7, 9], 7),         # target 7 在 [1, 3, 5, 7, 9] 中的 index：3
    ([1, 3, 5, 7, 9], 2),         # target 2 在 [1, 3, 5, 7, 9] 中的 index：-1
    ([10, 20, 30, 40, 50], 40),     # target 40 在 [10, 20, 30, 40, 50] 中的 index：3
    ([10, 20, 30, 40, 50], 25),     # target 25 在 [10, 20, 30, 40, 50] 中的 index：-1
    ([5], 5),                  # target 5 在 [5] 中的 index：0
    ([5], 3)                   # target 3 在 [5] 中的 index：-1
]

# 執行測試
for nums, target in examples:
    result = binary_search(nums, target)
    print(f"target {target} 在 {nums} 中的 index：{result}")
