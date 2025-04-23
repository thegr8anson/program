# 迴圈從 1000 到 9999，依序檢查每個數字是否符合題目條件
for n in range(1000, 10000):
    # 檢查輸入值 n 是否為質數
    is_prime_n = True
    for i in range(2, n):
        if n % i == 0:
            is_prime_n = False
            break

    if is_prime_n == True:  # 如果 n 是質數
        # 將 n 分為兩個兩位數
        first_half = n // 100  # 取前兩位數
        second_half = n % 100  # 取後兩位數

        # 檢查 first_half 是否為質數
        is_prime_first_half = True
        for i in range(2, first_half):
            if first_half % i == 0:
                is_prime_first_half = False
                break

        # 檢查 second_half 是否為質數
        is_prime_second_half = True
        for i in range(2, second_half):
            if second_half % i == 0:
                is_prime_second_half = False
                break

        # 如果前後兩部分都是質數，將兩個兩位數對調，形成新的數字
        if is_prime_first_half and is_prime_second_half:
            reversed_number = second_half * 100 + first_half

            # 檢查對調後的數字是否不是質數
            is_prime_swapped = True
            for i in range(2, reversed_number):
                if reversed_number % i == 0:
                    is_prime_swapped = False
                    break

            # 如果對調後的數字不是質數，則輸出 n
            if is_prime_swapped == False:
                print(n)