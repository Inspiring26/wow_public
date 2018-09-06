from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def read_txt(txt_name):
	f = open(txt_name)
	line = f.readline()
	inputlist = []
	while line:
		inputlist.append(line)
		line = f.readline()
	return inputlist

inlist = read_txt("inputdata.txt")
# 第一次分割,去掉括号
inlist_1 = inlist[0][1:-1]
# 第二次分割，以引号为分割点
inlist_2 = inlist_1.split("'")
part_one = inlist_2[1]
part_two = inlist_2[3]
part_three = inlist_2[5]
# 把第一部分的数据以雷达站为单位分成，一个个的数据单元
part_one_1 = part_one.split(";")
# 建立关系对应的经度表、纬度表、温度表
# 经度表
longitude = []
# 纬度表
latitude = []
# longitude, latitude = np.meshgrid(longitude, latitude)
# 温度表
temperature = []
# Z的值用不用np.meshgrid转，区别不大
# temperature, temperature1 = np.meshgrid(temperature, temperature)

# 循环遍历part_one_1填充三个表
for x in range(len(part_one_1)):
	templist = part_one_1[x].split(",")

	longitude.append(float(templist[0]))
	latitude.append(float(templist[1]))
	temperature.append(float(templist[2]))


# print(longitude)
print(len(longitude))
print(len(latitude))
print(len(temperature))
longitude, latitude = np.meshgrid(longitude[:100], latitude[:100])
temperatureU,temperatureU2 = np.meshgrid(temperature[:100],temperature[:100])
# fig = plt.figure()
# ax = Axes3D(fig)

# # Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(- X ** 2 - Y ** 2)

# ax.plot_surface(longitude, latitude, temperature[:100], rstride=1, cstride=1, cmap='rainbow')
# plt.show()



plt.contour(longitude, latitude, temperatureU,alpha = 0.75, cmap = plt.cm.hot)
# 去除坐标轴
plt.xticks(())
plt.yticks(())

plt.show()

# ax = plt.subplot(111, projection='3d')
# ax.scatter(longitude, latitude, temperature, c='r')
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

# 画出各个点分布的三维曲面图
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(longitude, latitude, temperature)
# plt.show()


