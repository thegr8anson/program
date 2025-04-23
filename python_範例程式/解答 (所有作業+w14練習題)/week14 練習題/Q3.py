gcd = lambda a, b: a if b == 0 else gcd(b, a % b) # 表達方式同函式，自行參閱函式課程簡報

x = int(input("輸入第一個整數: "))
y = int(input("輸入第二個整數: "))
print(f"{x} 和 {y} 的最大公因數為: {gcd(x, y)}")
