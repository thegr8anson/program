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
roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
}
    


    
for i in range(len(roman_num)):
      
    if i < len(roman_num) - 1 and roman_values[roman_num[i]] < roman_values[roman_num[i + 1]]:
        total -= roman_values[roman_num[i]]
    else:
        
        total += roman_values[roman_num[i]]



#======================================= code here
print(total)