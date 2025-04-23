# 計算加權分數總合

def sum(scores, weights):
    w_scores = []
    for i in range(0, 3):
        sum = 0
        for j in range(0, 3):
            sum += scores[i][j] * weights[j]
        w_scores.append(sum)
    return w_scores    

# 氣泡排序法(同時排兩個)

def BubbleSort(scores, w_scores):
    for i in range(1, len(w_scores)):
        for j in range(0, len(w_scores) - 1):
            if (w_scores[j] > w_scores[j + 1]):
                s_tmp = scores[j + 1]
                w_tmp = w_scores[j + 1]
                scores[j + 1] = scores[j]
                w_scores[j + 1] = w_scores[j]
                scores[j] = s_tmp
                w_scores[j] = w_tmp
    return scores

# 小朋友下樓梯

def steps(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    return steps(n - 1) + steps(n - 2)

#九九乘法表(遞迴 ver. + 對齊)

def time_table(a = 1, b = 1):
    print(f"{a} * {b} = {a * b :2d}", end = "  ")
    if(a <= 9 and b < 9):
        return time_table(a, b + 1)
    elif(a < 9 and b == 9):
        print()
        return time_table(a + 1, 1)


# 提取中心矩陣

# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
# print([row [1:-1] for row in a[1:-1]])

# 提取主對角線和反對角線

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# my_list = []
# for i in range(0, 3):
#     my_list.append(matrix[i][i])
# print(my_list)

# my_list.clear()

# for i in range(0, 3):
#     my_list.append(matrix[i][2 - i])        
# print(my_list)

# GCD(最大公因數) (lambda, recursion)

# a = int(input("輸入第一個整數: "))
# b = int(input("輸入第二個整數: "))
# GCD = lambda a, b: a if b == 0 else GCD(b, a % b)
# print(GCD(a, b))

# 帶權重的排序 (Bubble_Sort)

# scores = [[80, 90, 100],
#           [70, 85, 95],
#           [88, 92, 76]]
# weights = [0.2, 0.3, 0.5]
# w_scores = sum(scores, weights)
# print(BubbleSort(scores, w_scores))

# 帶權重的排序 (sorted)





# 小朋友下樓梯

# print(steps(5))

#九九乘法表(遞迴 ver. + 對齊)

# time_table()
    
'''
Bubble Sort

input未排序的 list 
output排序的 list 
1. 設定 n 為 list size 
2. 重複執⾏以下步驟直到列表排序完成:
      設定變數 swapped = false，紀錄本次迴圈是否有進行過交換
      從 0 跑到 n-2:
          i. 如果 list[i] > list[i+1]，則交換 list[i] 和 list[i+1] 
          ii.將swapped 標記為 true
      如果 swapped 為 false，表示列表已排序break
      否則將 n 減 1（縮⼩排序範圍）
'''

'''
Binary Search

input: 排列好的列表 nums，⽬標值 target 
output: ⽬標值的 index（如果找到），否則返回 -1   
1. 初始化
    left ← 0                 // 左邊界           
    right ← nums 的⻑度 - 1  // 右邊界       
2. 當 left ⼩於或等於 right時，重複以下步驟:
      計算中間位置mid ←  ( left + right ) // 2    
      比較 nums[mid] 和 target:       
          i. 如果 nums[mid] == target，回傳 mid      
          ii. 如果 nums[mid] > target，更新右邊界right ← mid - 1  
          iii. 如果 nums[mid] < target，更新左邊界left ← mid + 1        
3. 如果迴圈結束仍未找到⽬標值，返回 -1
'''
