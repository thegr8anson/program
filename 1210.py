import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [0, 1, 4, 9, 16]
# y2 = [0, 1, 8, 27, 64]

# plt.figure()
# plt.plot(x, y, linestyle = '--', marker = 'o', color = 'r')
# plt.plot(x, y)
# plt.plot(x, y2)
# plt.xlabel('x Axis')
# plt.ylabel('y Axis')
# plt.plot(x, y, label='y = x^2')
# plt.plot(x, y2, label='y = x^3')
# plt.xlim(0, 10)
# plt.ylim(0, 10)
# plt.legend() # 有label就要legend()
# plt.grid()
# plt.show()

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
sizes = [20, 50, 100, 200, 500]
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.figure()
for i in range(len(x)):
    plt.text(x[i], y[i], f'({x[i]}, {y[i]})')
plt.scatter(x, y, s=sizes, c=colors)
plt.show()