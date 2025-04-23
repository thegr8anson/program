# 請寫一個程式判斷輸入的年份是否是閏年
# Hint: 
# 1.可被4整除 "且" 不為100整除者為閏年
# 2."或" 可被400整除為閏年

year = int(input())
remainder_1 = year % 4
remainder_2 =  year % 100
remainder_3 = year % 400
if remainder_1 == 0 and remainder_2 != 0 or remainder_3 == 0 :
    print("Leap year : True")
else :
    print("Leap year : False")