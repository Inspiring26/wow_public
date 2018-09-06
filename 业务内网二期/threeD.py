from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
print(len(X))
X, Y = np.meshgrid(X, Y)



Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(- X ** 2 - Y ** 2)
print(len(Z))
print(Z)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
