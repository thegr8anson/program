for number in range(100, 1000, 1):
    # 將當前數字轉換為字串，並計算其位數（長度）
    length_of_number = len(str(number)) # 這裡 length_of_number 為 3，因為範圍是 100 到 999
    
    sum = 0 # 初始化變數 sum 為 0，用於計算每個位數的三次方之和

    # 將數字轉換為字串，逐一處理每個位數
    for each_number in str(number):
        # 將每個位數轉換回整數，計算其次方，並累加到 sum 中
        sum += int(each_number) ** length_of_number 
    
    # 如果三次方之和等於原數字，則為水仙花數
    if sum == number:
        print(number) 