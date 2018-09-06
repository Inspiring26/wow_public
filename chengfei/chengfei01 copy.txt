from tgrocery import Grocery
import re

def readtxt(filename="ds.txt"):
	f = open(filename)
	line = f.readline()
	inputlist = []
	while line:
		inputlist.append(line)
		line = f.readline()

	print("读数据完成")
	return inputlist

def writeTxtType2(inputlist,filename):#把列表写成txt 注意转码问题
	fwrite = open(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	if type(inputlist[0])==type(u'abc'):
		for x in range(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr)
	else:
		for x in range(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr)
	fwrite.close()

if __name__ == '__main__':
	# 下面这一块是加载模型
	# 这里模型名字需要修改
	new_grocery = Grocery('region')
	new_grocery.load()


	# 下面这一块是读取txt文档，保存到列表raw_input里
	# 这里读取txt的名字需要修改
	raw_input = readtxt("ds.txt")


	# 下面这一块是对列表的每一条信息进行分类，结果保存到result_list里
	result_list = []
	for x in range(len(raw_input)):
		result_list.append(new_grocery.predict(raw_input[x]))


	# 下面这一块是把结果写到txt中
	# 这里写文件的名字可以自己指定
	writeTxtType2(result_list,"result_list.txt")
