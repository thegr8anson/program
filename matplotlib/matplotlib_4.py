import matplotlib.pyplot as plt
import numpy as np
def Rotate_M(theta, point):
    x = point[0] * np.cos(theta) - point[1] * np.sin(theta)
    y = point[0] * np.sin(theta) + point[1] * np.cos(theta)
    return np.array([x, y]) 

x = np.array([1, 2, 3, 4, 5])
y = 3 * x + 2
theta = 45 * np.pi / 180 
r_point = Rotate_M(theta, np.array([x, y]))
plt.figure()
plt.scatter(x, y, color = "blue", label = "Original Points")
plt.scatter(r_point[0], r_point[1], color = "red", label = "Rotated Points")
plt.hlines(0, - 20, 20) # hlines(水平線的y座標, xmin, xmax)
plt.vlines(0, 0, 20) # vlines(垂直線的x座標, ymin, ymax)
plt.grid()
plt.legend()
plt.show()