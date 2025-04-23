import numpy as np

def rMatrix(arr):
    arr = arr.T
    print("Rotated Matrix:")
    print(arr[:,::-1])

n = int(input("Enter the matrix size n: "))
print("Original Matrix:")
arr = np.arange(1, n ** 2 + 1)
arr = arr.reshape(n, n) 
print(arr)
rMatrix(arr)