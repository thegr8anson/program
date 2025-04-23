## ex4_gcd.py ##

def gcd(a, b):             
    if b == 0:             # 輾轉相除法的終點
        return a           # 回傳前一個餘數
    else:                  # 如果相除不為 0，表示還沒找到最大公因數
        return gcd(b, a%b) # 使用遞迴，互換位子，進到下一層

print(gcd(9, 3))           # 3
print(gcd(10, 4))          # 2
print(gcd(12, 20))         # 4

