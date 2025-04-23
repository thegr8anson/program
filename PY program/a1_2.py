'''
# 請輸入一個羅馬數字，輸出這個羅馬數字的轉換成阿拉伯數字的結果


Hint:
羅馬數字參照表:{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
}
        
進行加減時的規則:
1.羅馬數字從左到右看過去
2.如果當前字符對應的數值小於右邊字符的數值，則減去當前數值。
3.否則，將當前字符的數值加到結果中。

'''

roman_num=input("請輸入一個羅馬數字")
total = 0

#======================================= code here
roman_list = list(roman_num)
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
int_list = []
for i in roman_list:
    int_list.append(roman_dict[i])

for i in range(0, len(int_list)):
    if (i == len(int_list) - 1):
        total += int_list[i]
        break
    if (int_list[i] < int_list[i+1]):
        total -= int_list[i]
    else:
        total += int_list[i]    
#======================================= code here
print(total)