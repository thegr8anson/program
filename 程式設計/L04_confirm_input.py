def convert_roman(roman_dict, s): 
    if not s:
        return None
    s = s.upper()
    result = 0
    i = 0
    subtractive_patterns = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    used_subtractive = []

    while(i < len(s)):
        # 只有一個字元或剩下一個字元，並確保該字元合法
        if (i == len(s) - 1):
            if (s[i] in roman_dict):
                # 確保沒有較小數值跟在減法組合後（如 XLX）
                if used_subtractive and roman_dict[s[i]] < roman_dict[used_subtractive[-1]]:
                    return None
                result += roman_dict[s[i]]
                return result
            else:
                return None

        # 確保四字元以上時，沒有非法的連續字元(防止如'IIII'等輸入)
        if (len(s) >= 4 and s[i:i+4].count(s[i]) == 4):
            return None

        # 確保沒有沒進位的非法字元(如'VV'應為'X')
        elif ('VV' in s or 'LL' in s or 'DD' in s):
            return None

        # 確保無連續的遞減型字元（不能有兩個 IX, XL, 等）
        for j in subtractive_patterns:
            if (s.count(j) > 1):
                return None

        # 檢查兩字元數字，若剛好剩兩字元則回傳
        if (s[i] + s[i + 1] in roman_dict):
            # 如果之前使用過減法組合，不能再接更小的數字（防 XLX）
            if used_subtractive and roman_dict[s[i] + s[i + 1]] < roman_dict[used_subtractive[-1]]:
                return None
            result += roman_dict[s[i] + s[i + 1]]
            used_subtractive.append(s[i] + s[i + 1])
            i += 2
            if (i == len(s)):
                return result

        # 檢查一字元數字，並確保合法
        elif (s[i] in roman_dict and s[i + 1] in roman_dict):
            # 確保合法輸入 (防止如'IC'等輸入)
            if (roman_dict[s[i]] >= roman_dict[s[i + 1]]):
                # 如果之前使用過減法組合，不能再加更小的數（如 XLX）
                if used_subtractive and roman_dict[s[i]] < roman_dict[used_subtractive[-1]]:
                    return None
                result += roman_dict[s[i]]
                i += 1
            else:
                return None
        else:
            return None

    return result


roman_dict = {
    'I':1, 'IV':4,'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50,
    'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000
}

s = input()
result = convert_roman(roman_dict, s)
if (result == None):
    print('Invalid input.')
else:
    print(result)

