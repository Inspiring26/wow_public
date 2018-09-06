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

# 专用函数，提取想要的数据组成三个列表
def llt():
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
	resolution = 200
	# 循环遍历part_one_1填充三个表
	for x in range(len(part_one_1)):
		templist = part_one_1[x].split(",")

		longitude.append(float(templist[0]))
		latitude.append(float(templist[1]))
		temperature.append(float(templist[2]))
	return longitude,latitude,temperature