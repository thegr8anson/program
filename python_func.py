def fibonachi(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)
      
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power (x, n - 1)

for i in range(1, 11):
    print(fibonachi(i), end = ' ')

print('')    
    
for i in range(1, 11):
    for j in range(0, 5):
        print(power(i, j), end = ' ')
    print('')    
    