# 輸入商品價格和付款金額，並轉換為整數
price = int(input("請輸入商品價格: "))
paid = int(input("請輸入付款金額: "))

# 記錄找零的數量
coins_10000 = 0
coins_5000 = 0
coins_1000 = 0
coins_500 = 0
coins_100 = 0
coins_50 = 0
coins_10 = 0

# 紀錄找零金額
change = paid - price

while(change > 0):
    if(change >= 10000):
        coins_10000 += 1
        change -= 10000
    elif(change >= 5000):
        coins_5000 += 1
        change -= 5000
    elif(change >= 1000):
        coins_1000 += 1
        change -= 1000
    elif(change >= 500):
        coins_500 += 1
        change -= 500
    elif(change >= 100):
        coins_100 += 1
        change -= 100
    elif(change >= 50):
        coins_50 += 1
        change -= 50
    elif(change >= 10):
        coins_10 += 1
        change -= 10

print(f"""需要找零：{paid - price} 日幣
            
      找零明細：
      {coins_10000} 張一萬元
      {coins_5000} 張五千元
      {coins_1000} 張一千元
      {coins_500} 個五百元
      {coins_100} 個一百元
      {coins_50} 個五十元
      {coins_10} 個十元
      """)
