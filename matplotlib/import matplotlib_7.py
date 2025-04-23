import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection = "3d")

z = np.linspace(0, 10, 100)
x = np.sin(z)
y = np.cos(z)

ax.plot(x, y, z)
ax.set_title("3D Line Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()
