import numpy as np
# 矩陣加法
def sumofmatrix(a, b):
    return np.add(a, b)

def f(matrix):
    return matrix[1:-1, 1:-1].flatten() # 先直的 slice 再橫的 slice

def rotatePoint(point, theta_degree):
    rad_angle = (np.pi/180) * theta_degree
    rotate_matrix = np.array([[np.cos(rad_angle), -np.sin(rad_angle)],
                              [np.sin(rad_angle), np.cos(rad_angle)]])
    new_point = rotate_matrix @ point
    return new_point

a = np.arange(1, 10).reshape((3, 3))
b = np.arange(1, 19, 2).reshape((3, 3))
print(a)
print(b)
print(sumofmatrix(a, b))

A = np.arange(25).reshape(5, 5)
print(A) 
print(f(A))

P = np.array([1, 0])
print(rotatePoint(P, 45))