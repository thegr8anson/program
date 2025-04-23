# list_comprehension_ex1.py

lst = [1, 2, 3, 4, 5]

# for loop
lst_sq = []
for num in lst:
    lst_sq.append(num ** 2)

# list comprehension
lst_sq_c = []   
lst_sq_c = [num**2 for num in lst]
print(lst_sq_c)

