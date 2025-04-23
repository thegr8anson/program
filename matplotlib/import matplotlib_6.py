import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection = "3d")

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

ax.scatter(x, y, z)
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()