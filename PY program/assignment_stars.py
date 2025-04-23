layer = int(input("請輸入階層數:"))
space = ' '
for i in range (1, layer, 1) :
    print(space * (layer - i) + '*' * (2 * i - 1))

print('*' * (2 * i + 1))    
for j in range (1, layer, 1) :
    print(space * j + '*' * (2 * i - 1))
    i -= 1