# -*- coding:utf-8 -*-
'''
	弹出页面即关闭，原版本 16212个数据块 耗时55.8011910915秒
	弹出页面即关闭，优化后 9892个数据块 耗时32.6869959831秒
	mac 主频1.6 直接保存图片 耗时32.5647268295秒 (2017-10-16)
'''
import numpy as np

# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 添加计时功能，为优化做对比
import time
# 处理速度缓慢，考虑组织成五个数组，然后调用一次bar，这样应该能提升效率
timeStart = time.time()
theX = np.array([])
theHeight = np.array([])
theWidth = np.array([])
theBottom = np.array([])
theColors = np.array([])
 

colors = np.array(["#ffffff","#00ACA4","#C0C0FE","#7A72EE","#1E26D0","#A6FCA8",
	"#00EA00","#10921A","#FCF464","#C8C802","#8C8C00","#FEACAC","#FE645C",
	"#EE0230","#D48EFE","#AA24FA"])



f = open("ld.txt")
line = f.readline()
inputlist = []
print("读取数据")
while line:
	# print line
	inputlist.append(line)
	line = f.readline()
print("读数据完成")

npinputlist=np.array(inputlist)
plt.figure(figsize=(8,8)) 
# 
ax =plt.subplot(111, projection='polar');
#projection='polar' 投影成极坐标

for x in xrange(len(npinputlist)):
	print("第"+str(x)+"条处理中...")
	# pre = npinputlist[x]
	twoPart = npinputlist[x].split(";")
	partOne = twoPart[0]
	#起始的弧度和跨越的弧度
	start = int(partOne.split(",")[0])
	width = int(partOne.split(",")[1])

	parttwo = twoPart[1]
	# b=parttwo.split(",")
	posAndColor=np.array(parttwo.split(","))
	sum=0
	for y in xrange(len(posAndColor)-1):

		dataPair = posAndColor[y]
		
		# csp = dataPair.split(" ")
		
		distanceFromPolar = dataPair.split(" ")[0]
		blockColor = dataPair.split(" ")[1]

		distance=int(distanceFromPolar)
		blockColor=int(blockColor)
		if blockColor != 0:
			theX = np.append(theX,[start*np.pi/1800.0 + 3*np.pi/2.0])
			theHeight = np.append(theHeight,[distance])
			theWidth = np.append(theWidth,[width*np.pi/1800.0])
			theBottom = np.append(theBottom,[sum])
			theColors = np.append(theColors,[colors[blockColor]])
		sum += int(distance)
		

print("共有"+str(len(theBottom))+"个数据块")
print("制作效果图中...")
ax.bar(theX,theHeight,theWidth,theBottom,color=theColors)




ax.grid(False)
# No ticks
ax.set_xticks([])
ax.set_yticks([])
# 这个是我自己尝试出来的哈哈哈哈，原来是没有polar这个参数的
ax.spines["polar"].set_color('none')

   
# plt.show()
plt.savefig("雷达图.png")

timeEnd = time.time()
print("耗时"+str(timeEnd - timeStart)+"秒")

