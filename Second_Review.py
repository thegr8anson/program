# 10 : 59 to 11 : 10

row = int(input())

for i in range(0, row + 1):
    print(i, end = '')

for i in range (1, row + 1):
    for j in range(row - i, - 1, -1):
        print(j, end = '')
    break    
print('')    

for i in range(1, row + 1):
    for j in range(0, row - i + 1):
        print(j, end = '')
    for j in range(1, 2 * i):
        print(' ', end = '')
    for j in range(row - i, - 1, - 1):
        print(j, end = '')
    print('')

for i in range(0, row + 1):
    print(i, end = '')

for i in range (1, row + 1):
    for j in range(row - i, - 1, -1):
        print(j, end = '')
    break    
print('')                            