def recursion99(i, j): 
    if i <= 9 and j <= 9: # i和j皆在9範圍內，印出相乘結果 (終止條件)
        print(f'{i}*{j}={i*j}',end='  ')

    if j < 9: # j小於9，i要不變，j要一直遞加到9為止
        return recursion99(i, j+1) 
    
    if j == 9 and i < 9: # j已經到9了，i要往下一個數走，然後j要變回1
        print() # 換行
        return recursion99(i+1, 1)

recursion99(1, 1)