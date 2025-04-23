# first example (奇數*三角形)

# row_1 = int(input())
# for i in range (1, row_1 + 1, 1):
#     for j in range (1, (row_1 - i) + 1, 1):
#         print (' ', end= '')
#     for j in range (1, 2 * i, 1):
#         print ('*', end = '')
#     print("\n") 

#second example (煞氣A三角形)

# row_2 = int(input())
# for k in range(0, row_2 * 2 + 1, 1):
#     if (k <= row_2):
#         print(k, end = '')
#     else:
#         print(row_2 * 2 - k , end = '')
# print("")

# for k in range(1, row_2 + 1, 1):
#     for l in range(0, row_2 - k + 1, 1):
#         print(l, end = '')
#     for l in range(1, 2 * k, 1):
#         print(' ',end = '')
#     for l in range(row_2 - k, -1, -1):
#         print(l,end = '')
#     print('')

# for k in range(0, row_2 * 2 + 1, 1):
#     if (k <= row_2):
#         print(k, end = '')
#     else:
#         print(row_2 * 2 - k , end = '')
# print("")        
  
#third example (橫的數字三角形)
#如果有下半迴圈變成相反的情況，則可將上半迴圈的第1、2的控制變數變為2、1放在下半    

# row_3 = int(input())
# for m in range(1, row_3 + 1, 1):
#     for n in range(1, row_3 - m + 1, 1):
#         print(' ', end = '')
#     for n in range(1 , m + 1, 1): 
#         print (n, end = '') 
#     print('')

# for m in range(1, row_3, 1):
#     for n in range(1, m + 1, 1):
#         print(' ', end = '')
#     for n in range(1, row_3 - m + 1, 1): 
#         print (n, end = '')
#     print('')

# number example(因數)

# number = int(input())
# sum = 0

# for o in range(1, number, 1):
#     if (number % o == 0):
#         sum += o
# print(sum)

#number example(prime number)

# for p in range(1000 , 10000, 1):
#     count = 0  #count要放這裡，否則會於for迴圈外消滅
#     for q in range(2, int(p ** 1 / 2 + 1), 1): 
#         if (p % q == 0):
#             count += 1
#     if (count == 0):
#         print(p,end = ' ')

#number example(prime number exchange)

# for r in range(0, 100, 1):   #front two numbers 0 to 99
#     count = 1
#     for s in range(0, 100, 1):   #rear two numbers 0 to 99   
#         normal_number = r * 100 + s
#         reverse_number = s * 100 + r
#         if (normal_number < 1000):
#             continue
#         for t in range(2, int(reverse_number ** 1 / 2 + 1), 1):
#             if(reverse_number % t == 0):
#                 count = 0                    # not prime = very good
#         for t in range(2, normal_number, 1):
#             if(normal_number % t == 0):
#                 count += 1
#         for t in range(2, r, 1):
#             if(r % t == 0):
#                 count += 1
#         for t in range(2, s, 1):
#             if(s % t == 0):
#                 count += 1
#         if (count == 0):
#             print(normal_number, end = '\t')

# prime number exchange (array) (存在note裡)

# for n in range(1000,10000):



# prime number exchange (function)

# def check_prime_number(number): #檢查質數
#     a=2
#     prime_number=True
#     if(number==1):
#         prime_number=False    
#     while(a<number):
#         if(number%a==0):
#             prime_number=False
#         a+=1
#     return prime_number


# def check_prime_number_premium(number): #檢查交換後的質數
#     a=2
#     prime_number1=False

#     first_number=number%100 #我first跟second打反了超好笑
#     second_number=number//100

#     swap_number=first_number*100+second_number

#     if(check_prime_number(first_number)==True and check_prime_number(second_number)==True and check_prime_number(number)==True and check_prime_number(swap_number)==False):
#     #檢查所有條件
#         prime_number1=True
#     return prime_number1

# b=1000
# while(b<=9999):
#     if(check_prime_number_premium(b)==True):
#         print(b, end = '\t')
#     b+=1

# 水仙花數

# for u in range(1, 10, 1):
#     for v in range(0, 10, 1):
#         for w in range(0, 10, 1):
#             number = u * 100 + v * 10 + w
#             if (number == u ** 3 + v ** 3 + w ** 3):
#                 print(number)

# 找錢程式

# price = int(input("請輸入價格："))
# money = int(input("請輸入金額："))
# return_money = money - price
# bill_10000 = return_money // 10000
# return_money %= 10000
# bill_5000 = return_money // 5000
# return_money %= 5000
# bill_1000 = return_money // 1000
# return_money %= 1000
# coin_500 = return_money // 500
# return_money %= 500
# coin_100 = return_money // 100
# return_money %= 100
# coin_50 = return_money // 50
# return_money %= 50
# coin_10 = return_money // 10
# print(f"找回10000元{bill_10000}張，5000元{bill_5000}張，1000元{bill_1000}張，500元硬幣{coin_500}個，\
# 100元硬幣{coin_100}個，50元硬幣{coin_50}個，10元硬幣{coin_10}個")

#合體1=菱形

# row_4 = int(input())
# for x in range (1, row_4 + 1):
#     for y in range (1, row_4 - x + 1) :
#         print(' ',end = '')
#     for y in range (1, 2 * x) :
#         print('*', end = '')
#     print('')
# for x in range (1, row_4):
#     for y in range (1, x + 1):
#         print(' ', end = '')
#     for y in range (1, row_4 * 2 - 2 * x) :
#         print('*', end = '')
#     print('')                   

#合體2=漏斗

# row_5 = int(input())

# for z in range (1, row_5 + 1):
#     for a in range (1, z):
#         print(' ', end ='')
#     for a in range (1, 2 * row_5 - 2 * z + 2):
#         print('*', end = '')
#     print('')

# for z in range (1, row_5):
#     for a in range (1, row_5 - z):
#         print(' ', end = '')
#     for a in range (1, 2 * z + 2):
#         print('*', end = '')
#     print('')

#星爆金字塔

# row_6 = int(input())
# for b in range (1, row_6 + 1):
#     for c in range (1, row_6 - b + 1):
#         print(' ', end = '')
#     for c in range (b, 2 * b):
#         print(c, end ='')
#     for c in range (2 * b - 2, b - 1, - 1):   
#         print(c, end = '')
#     print('')                                    
 
# 混合金字塔

# row_7 = int(input())
# for d in range (1, row_7 + 1):
#     for e in range(1,row_7 - d + 1):
#         print(' ',end = '')
#     for f in range (1, 2 * d):
#         if (f % 2 != 0):
#             print ('*', end = '')
#         else:
#             print('0', end = '')
#     print('')            