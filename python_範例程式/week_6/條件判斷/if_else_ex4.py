# if_else_ex4.py
# 成績判斷程式，判斷是否要重修

score = int(input("請輸入成績: "))

if score < 60:
    if score >= 50:
        print("請參加補考")
    else:
        print("必須重修")
else:
    print("本科及格")

'''
------output1------
請輸入成績: 60
本科及格
------output2------
請輸入成績: 59
請參加補考
------output3------
請輸入成績: 40
必須重修
'''


