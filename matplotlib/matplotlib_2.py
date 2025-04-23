import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 11, 1000)
v = np.zeros(len(x))

for i in range(len(x)):
    if 0 <= x[i] <= 8:
        v[i] = 133.75 - 40 * x[i]
    else:
        v[i] = 20    

plt.figure()
plt.xlabel('V (kN)')
plt.ylabel('M (kN * m)')
plt.plot(x, v)
plt.grid()
plt.show()