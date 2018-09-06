import numpy as np
import matplotlib.pyplot as plt 

m,n = 5,3
# x是有5个元素的数组
# y是有3个元素的数组
x = np.linspace(0,1,m)
y = np.linspace(0,1,n)

# X、Y都是3行5列的矩阵，他们分别是3*5个元素的x轴y轴坐标
# 为什么是3行5列？
# 因为x轴上有5个刻度，y轴方向有3个刻度所以高为3
X,Y = np.meshgrid(x,y)

# 打印出这些点
plt.plot(X, Y, marker='.', color='blue', linestyle='none')
plt.show()
