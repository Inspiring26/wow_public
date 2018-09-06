from matplotlib import pyplot as plt
import numpy as np

def f(x, y):
	return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)




X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)


Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(- X ** 2 - Y ** 2)

plt.contour(X, Y, f(X,Y),alpha = 0.75, cmap = plt.cm.hot)
# 去除坐标轴
plt.xticks(())
plt.yticks(())

plt.show()