import matplotlib
import numpy as np 
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt 

def read_txt(txt_name):
	f = open(txt_name)
	line = f.readline()
	inputlist = []
	while line:
		inputlist.append(line)
		line = f.readline()
	return inputlist

# 定义等高线高度函数
def f(x, y):
	return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)

# 接下来参考usage_of_meshgrid.py中meshgrid的用法就好了
# 数据个数
n = 256
# 定义x,y
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 生成网格数据
X, Y = np.meshgrid(x, y)
# print(X)
# print(Y)

# plt.plot(X, Y, marker='.', color='blue', linestyle='none')
# plt.show()

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
# 温度表
temperature = []

# 循环遍历part_one_1填充三个表
for x in range(len(part_one_1)):
	templist = part_one_1[x].split(",")

	longitude.append(templist[0])
	latitude.append(templist[1])
	temperature.append(templist[2])

print(f(1,2))

# X, Y = np.meshgrid(longitude, latitude)



# plt.figure(figsize=(10,6))

# print(f(X, Y))
# alpha表示透明度 cmap表示渐变标准 
plt.contour(X, Y, f(X,Y),alpha = 0.75, cmap = plt.cm.hot)
# 去除坐标轴
plt.xticks(())
plt.yticks(())

plt.show()





