import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 50, 1000)
S = 3 * np.cos(0.5 * t + 1) + 4 * np.sin(t + 8)
v = np.gradient(S)
a = np.gradient(v)
plt.figure()
plt.plot(t, S)
plt.plot(t, v)
plt.plot(t, a)
plt.grid()
plt.show()