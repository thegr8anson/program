digit = int(input())
int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_dict = {1000 : 'M', 900: 'CM', 500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL',
10 : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I'}

for i in range(1, digit + 1):
    type, num = input().split(' ') # Enter multiple data at a time, seperated by space (' ').
    if (type == '1'):  # roman to int
        total = 0
        num_list = list(num)
        int_list = []
        for j in num_list:
            int_list.append(int_dict[j])

        for j in range(0, len(int_list)):
            if (j == len(int_list) - 1):
                total += int_list[j]
                break
            if (int_list[j] < int_list[j+1]):
                total -= int_list[j]
            else:
                total += int_list[j]    
        print(total)
    else:  # int to roman
        num = int(num)
        total = ''
        for j, k in roman_dict.items():  
            # dict.items()函數會把字典的key和value兩兩一對綁成tuple，並把所有的tuple組成一個list
            # In this case, j (int) is key, and k (str) is value.
            while num >= j:
                num -= j
                total += k
  
        # while (num >= 1000):
        #     total += 'M'
        #     num -= 1000
        # while (num < 1000 and num >= 900):
        #     total += 'CM'
        #     num -= 900
        # while (num < 900 and num >= 500):
        #     total += 'D'
        #     num -= 500
        # while (num < 500 and num >= 400):
        #     total += 'CD'
        #     num -= 400
        # while (num < 400 and num >= 100):
        #     total += 'C'
        #     num -= 100
        # while (num < 100 and num >= 90):
        #     total += 'XC'
        #     num -= 90
        # while (num < 90 and num >= 50):
        #     total += 'L'
        #     num -= 50
        # while (num < 50 and num >= 40):
        #     total += 'XL'
        #     num -= 40    
        # while (num < 40 and num >= 10):
        #     total += 'X'
        #     num -= 10
        # while (num == 9):
        #     total += 'IX'
        #     num -= 9
        # while (num < 9 and num >= 5):
        #     total += 'V'
        #     num -= 5
        # while (num == 4):
        #     total += 'IV'
        #     num -= 4                       
        # while (num < 5 and num > 0):
        #     total += 'I'
        #     num -= 1   
        print(total)        
            