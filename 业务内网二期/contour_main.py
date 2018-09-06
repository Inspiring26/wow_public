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
# 图片分辨率
resolution = 100
# 循环遍历part_one_1填充三个表
for x in range(len(part_one_1)):
	templist = part_one_1[x].split(",")

	longitude.append(float(templist[0]))
	latitude.append(float(templist[1]))
	temperature.append(float(templist[2]))


plt.figure(figsize=(10,6))

x = np.linspace(101.48, 115.05, resolution)
y = np.linspace(17.9, 29.39, resolution)
X, Y = np.meshgrid(x, y)

# 创建Z的二维矩阵
Z = np.zeros((resolution,resolution))


step_len1 = (115.05-101.48)/resolution
step_len2 = (29.39-17.9)/resolution

temperature_standard = [-20.0,-16.0,-12.0,-8.0,-4.0,0.0,4.0,8.0,12.0,16.0,20.0,24.0,28.0,32.0,36.0,40.0,44.0]
temperature_dealed = []
for x in range(len(temperature)):
	# 把温度化成指定规格的
	temperature_dealed.append(temperature_standard[int((temperature[x]+20)//4)])
for x in range(len(longitude)):
	pos_i = (longitude[x]-101.48)//step_len1
	pos_j = (latitude[x]-17.9)//step_len2
	Z[int(pos_i)-1][int(pos_j)-1] = temperature_dealed[x]
print(Z)
# 建立一个标示数组

Zflag = np.zeros((resolution,resolution))
for x in range(len(Z)):
	for y in range(len(Z[0])):
		if Z[x][y] == 0.0:
			Zflag[x][y] = -1
		else:
			Zflag[x][y] = 1
print(Zflag)
for num in range(1,2):

	for x in range(len(Zflag)):
		for y in range(len(Zflag[0])):
			if Zflag[x][y] == 1.0 and x*y*(resolution-1-x)*(resolution-1-y)>0.0:
				if Zflag[x-num][y-num] == -1 and Z[x-num][y-num]==0.0:
					Z[x-num][y-num] = Z[x][y]
					# Zflag[x-1][y-1] = 1
				if Zflag[x-num][y]== -1 and Z[x-num][y]==0.0:
					Z[x-num][y]=Z[x][y]
					# Zflag[x-1][y]=1
				if Zflag[x-num][y+num]== -1 and Z[x-num][y+num]==0.0:
					Z[x-num][y+num]=Z[x][y]
					# Zflag[x-1][y+1]=1
				if Zflag[x][y-num]== -1 and Z[x][y-num]==0.0:
					Z[x][y-num]=Z[x][y]
					# Zflag[x][y-1]=1
				if Zflag[x][y+num]== -1 and Z[x][y+num]==0.0:
					Z[x][y+num]=Z[x][y]
					# Zflag[x][y+1]=1
				if Zflag[x+num][y-num]== -1 and Z[x+num][y-num]==0.0:
					Z[x+num][y-num]=Z[x][y]
					# Zflag[x+1][y-1]=1
				if Zflag[x+num][y]== -1 and Z[x+num][y]==0.0:
					Z[x+num][y]=Z[x][y]
					# Zflag[x+1][y]=1
				if Zflag[x+num][y+num]== -1 and Z[x+num][y+num]==0.0:
					Z[x+num][y+num]=Z[x][y]
					# Zflag[x+1][y+1]=1
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# plt.show()
plt.contour(X, Y, Z, alpha = 0.75, cmap = plt.cm.hot)
plt.show()






