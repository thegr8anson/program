def bubble_sort(list):
    n = len(list)

    for i in range(n):  # 外層迴圈

        swapped = False  # 檢查是否有發生 swap

        for j in range(n - 1 - i):  # 每次進行內層迴圈時都有縮小範圍
            
            if list[j] > list[j + 1]:  # 比較相鄰元素
                list[j], list[j + 1] = list[j + 1], list[j]  # 交換元素
                swapped = True

        if not swapped:  # 若無 swap，表示排序完成
            break

    return list  # 回傳排序後的 list

# test
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data)
print("排序後的列表:", sorted_data)    # 排序後的列表: [11, 12, 22, 25, 34, 64, 90]