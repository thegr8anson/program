import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2983, 3092, 3339, 3301, 3198, 3314, 3278, 2687, 2455, 2508, 2733],
                 [1389, 1425, 1473, 1444, 1514, 1508, 1487, 1287, 1200, 1221, 1204]
                ])
A = np.zeros([data.shape[1], 2])
for i in range (data.shape[1]):
    A[i, 0] = data[0, i]
    A[i, 1] = 1
x = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), data[1, :].T)
print(x) # x為迴歸直線的斜率和截距(array)
Xaxis = np.linspace(min(data[0,:]), max(data[0,:]), 1000)
y = x[0] * Xaxis + x[1]

plt.figure()
plt.title("Male and Female correlation")
plt.xlabel("Female")
plt.ylabel("Male")
plt.scatter(data[0, :], data[1, :], color='blue', label='Real Data')
plt.plot(Xaxis, y, color = "red", label = "Fitting Curve")
plt.grid()
plt.legend()
plt.show()
