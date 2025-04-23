# draw_stars_ex1.py
# 使用巢狀迴圈繪製圖形

n = int(input("輸入star層數: "))

for layer in range(1, n+1, 1): # 外層跑層數
    for starNumber in range(1, layer+1, 1): # 內層跑星星數
        # 數星星的顆數，印到對應層數的顆數才會停
        # 舉例 : 第2層印2顆、第5層印5顆
        # 同一行未印完該層星星數不能換行，所以end設定為""  
        print("*", end="") 
    print() # 每行印完就換行

