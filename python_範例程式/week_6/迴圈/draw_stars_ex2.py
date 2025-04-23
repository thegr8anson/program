# draw_stars_ex2.py
# 不使用巢狀迴圈繪製圖形

n = int(input("輸入star層數: "))

for layer in range(1, n+1, 1):
    # 用"*"印出要重複印幾次星星
    # 舉例 : 第2層印2顆、第5層印5顆
    print("*"*layer) 

