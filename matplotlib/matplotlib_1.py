import matplotlib.pyplot as plt
import numpy as np
q = 1.6e-19
k = 9e-9
r = np.linspace(0, 0.10, 100)
F = k * q * q / r ** 2
plt.figure()
plt.title('Electrostatic Force as a Function of Distance')
plt.plot(r, F, label = 'Electrostatic Force', color = 'red')
plt.xlabel('Distance (r) [m]')
plt.ylabel('Force (F) [N]')
plt.legend()
plt.grid()
plt.show()