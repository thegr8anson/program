# 迴圈從 1000 到 9999，依序檢查每個數字是否為質數
for n in range(1000, 10000, 1):
    is_prime = True # 假設當前數字 n 是質數，初始化為 True

    # 檢查 n 是否有除了1和自己的其他因數 (從 2 開始一直到 n-1做檢查)
    for i in range(2, n):  
        if  n % i == 0: # 如果 n 能被 i 整除，表示 n 不是質數
            is_prime = False # 將 is_prime 設為 False
            break # 找到一個因數後，立即跳出內層迴圈
    
    # 如果 is_prime 維持為 True，代表 n 是質數
    if is_prime == True:
        print(n)
