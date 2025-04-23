#sum 是保留字，要避免使用
summ = 0
for i in range(11):
    summ += i


# how it runs
# 0(original) + 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(summ)