# 02 : 47 to 02 : 56

#Bert的三角形(1)

# n = int(input())
# for i in range (1, n + 1):
#     for j in range (1, i + 1):
#         print('*', end = '')
#     print("")    

#Bert的三角形(2)

# n = int(input())
# for i in range(1, n + 1):
#     for j in range (1, n - i + 1):
#         print('_', end = '')
#     for j in range (1, i + 1):
#         print('*', end = '')
#     print('')  

#Bert的三角形(3)

# n = int(input())
# for i in range (1, n + 1):
#     for j in range (1, n - i + 1):
#         print('_', end = '')
#     for j in range (1, 2 * i):
#         print('*', end = '')
#     for j in range (1, n - i + 1):
#         print('_', end = '')
#     print('')

#數字三角形(一直做直到0)

# n = int(input())

# while(n != 0):
#     for i in range (1, n + 1):
#         for j in range (1, n - i + 1):
#             print('_', end = '')
#         for j in range (1, i + 1):
#             print('+', end = '')
#         print('')
#     n = int(input())
          
# 數字翻轉

# n_original = int(input())
# n_reverse = 0

# while (n_original > 0):
#     n_reverse *= 10
#     n_reverse += n_original % 10
#     n_original //= 10
# print(n_reverse)                     