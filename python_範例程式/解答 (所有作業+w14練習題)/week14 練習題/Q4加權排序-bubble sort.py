'''
給定一組成績列表 scores 和權重列表 weights，每個成績列表中的元素分別對應一個權重。請計算每組成績的加權平均值，並按照加權平均值的升序對成績進行排序。

範例輸入與輸出
輸入:[80, 90, 100], [70, 85, 95], [88, 92, 76]
第一組成績的加權平均值：
80*0.2+90*0.3+100*0.5 = 92.0
第二組成績的加權平均值：
70*0.2+85*0.3+95*0.5 = 87.5
第三組成績的加權平均值：
88*0.2+92*0.3+76*0.5 = 82.8

根據加權平均數將三組成績做升序的排序，由加權平均值由低到高做排序
輸出:[88, 92, 76], [70, 85, 95], [80, 90, 100]


'''
# 定義一個函式，用於計算加權平均值
def weighted_average(scores, weights):
     # 使用 zip 將成績列表和權重列表配對，並計算每個配對的乘積，再使用 sum 求和
    return sum(score * weight for score, weight in zip(scores, weights))
# 定義冒泡排序函式，用於對成績列表按照加權平均值進行排序
def bubble_sort(scores, weights):
    n = len(scores)
    for i in range(n):
        for j in range(0, n - i - 1):
            if weighted_average(scores[j], weights) > weighted_average(scores[j + 1], weights): # 前數>後數
                scores[j], scores[j + 1] = scores[j + 1], scores[j] # 前後交換(把大的數往後移)
    return scores

# 範例輸入
scores = [[80, 90, 100], [70, 85, 95], [88, 92, 76]]
weights = [0.2, 0.3, 0.5]

# 調用冒泡排序函式，根據加權平均值進行排序
sorted_scores = bubble_sort(scores, weights)

# 輸出排序後的成績列表
print(sorted_scores)
