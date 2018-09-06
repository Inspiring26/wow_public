#coding:utf-8
# 多进程模式
# 使用四个cpu同时处理，把数据分成4个部分
import xlrd
import numpy as np
import pandas as pd
import pickle
import math
import re

def xls2listType2(xlsname,n):#返回单个列表
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	# print(list1)
	for x in range(1,nrows):# 从第二行开始
		text_data = table.cell(x,n).value
		
		list0.append(text_data)
	return list0
def filterList2list(inputlist):#过滤列表，返回一个没有重复元素的列表
	resultList = []
	for x in range(len(inputlist)):
		if inputlist[x] not in resultList:
			resultList.append(inputlist[x])
	return resultList
def common_amount(inputlist,m,n):
	num = 0
	for x in range(len(inputlist)):
		if inputlist[x][m] == inputlist[x][n]:
			num += 1
	return num
def save_pickle():
	titles = xls2listType2("商品名称用户ID.xls",0)
	usrs = xls2listType2("商品名称用户ID.xls",1)

	titles_unique = filterList2list(titles)
	usrs_unique = filterList2list(usrs)

	maintable = np.zeros((len(usrs_unique),len(titles_unique)))
	for x in range(len(titles)):
		titles_ = titles[x]
		usrs_ = usrs[x]

		x_ = usrs_unique.index(usrs_)
		y_ = titles_unique.index(titles_)

		maintable[x_][y_] = 1.0

	# print(len(maintable))
	# 生成数据分布表maintable结束

	# 下面生成物品间的交集数
	items_items = np.zeros((len(titles_unique),len(titles_unique)))
	print(len(maintable)==len(usrs_unique))
	print("共"+str(len(titles_unique))+"列")
	print("共"+str(len(maintable))+"行")
	for x in range(len(titles_unique)):
		print("处理到第"+str(x)+"列")
		for y in range(x+1,len(titles_unique)):# 选中了两个物品x,y
			for z in range(len(maintable)):# 对于两列，从上往下遍历
				if maintable[z][x] == 1.0:
					if maintable[z][y] == 1.0:
						items_items[y][x]+=1
						items_items[x][y]=items_items[y][x]

	# 生成物品间的交集数矩阵结束
	file = open('items_items.pickle', 'wb')
	pickle.dump(items_items, file)
	file.close()
def cosine_similarity(two_axis_list):
	# 计算每两行的相似度
	molecular = 0.0
	denominator1 = 0.0
	denominator2 = 0.0
	denominator = 0.0
	listlen = len(two_axis_list)
	return_two_axis_list = np.zeros((listlen,listlen))

	for x in range(listlen):
		print("计算第"+str(x)+"/"+str(listlen)+"个矩阵的余弦")
		for y in range(x+1,listlen):
			for z in range(len(two_axis_list[0])):
				molecular += two_axis_list[x][z]*two_axis_list[y][z]
				denominator1 += two_axis_list[x][z]**2
				denominator2 += two_axis_list[y][z]**2
		
		denominator = math.sqrt(denominator1)*math.sqrt(denominator2)
		if denominator == 0.0:
			return_two_axis_list[x][y] = 0.0
			return_two_axis_list[y][x] = return_two_axis_list[x][y]
		else:
			return_two_axis_list[x][y] = molecular/denominator
			return_two_axis_list[y][x] = return_two_axis_list[x][y]

		molecular = 0.0
		denominator1 = 0.0
		denominator2 = 0.0
		denominator = 0.0

	return return_two_axis_list
def writeTxt(inputlist,filename):#把列表写成txt 注意转码问题
	fwrite = open(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	s="\n"
	if type(inputlist[0])==type(u'abc'):
		for x in range(len(inputlist)):
			matchResult = re.search(s, inputlist[x])
			if matchResult:
				tempStr = inputlist[x]
				fwrite.write(tempStr)
			else:
				tempStr = inputlist[x] + "\n"
				fwrite.write(tempStr)





if __name__ == '__main__':
	titles = xls2listType2("商品名称用户ID.xls",0)
	usrs = xls2listType2("商品名称用户ID.xls",1)

	titles_unique = filterList2list(titles)
	usrs_unique = filterList2list(usrs)

	maintable = np.zeros((len(usrs_unique),len(titles_unique)))
	for x in range(len(titles)):
		titles_ = titles[x]
		usrs_ = usrs[x]

		x_ = usrs_unique.index(usrs_)
		y_ = titles_unique.index(titles_)

		maintable[x_][y_] = 1.0

	# print(len(maintable))
	# 生成数据分布表maintable结束

	# 下面生成物品间的交集数
	sw1 = 1
	if sw1 == 0:	
		items_items = np.zeros((len(titles_unique),len(titles_unique)))
		print(len(maintable)==len(usrs_unique))
		print("共"+str(len(titles_unique))+"列")
		print("共"+str(len(maintable))+"行")
		for x in range(len(titles_unique)):
			print("处理到第"+str(x)+"列")
			for y in range(x+1,len(titles_unique)):# 选中了两个物品x,y
				for z in range(len(maintable)):# 对于两列，从上往下遍历
					if maintable[z][x] == 1.0:
						if maintable[z][y] == 1.0:
							items_items[y][x]+=1
							items_items[x][y]=items_items[y][x]

		# 生成物品间的交集数矩阵结束
		file = open('items_items.pickle', 'wb')
		pickle.dump(items_items, file)
		file.close()
	else:
		with open('items_items.pickle', 'rb') as file:
	 		items_items =pickle.load(file)

	# print(items_items)
	# list_1axis = []
	# for x in range(len(items_items)):
	# 	list_1axis.append(str(items_items[x]))
	# writeTxt(list_1axis,"list_1axis.txt")


	sw2 = 0
	if sw2 == 0:
		cos_list = cosine_similarity(maintable.T)
		file = open('cos_list.pickle', 'wb')
		pickle.dump(cos_list, file)
		file.close()
	else:
		with open('cos_list.pickle', 'rb') as file:
	 		cos_list =pickle.load(file)

	print(cos_list)

	maintext = ""
	for x in range(len(cos_list)):
		temp = cos_list[x].max()
		temp = list(cos_list[x]).index(temp)
		# print(str(titles_unique[x])+"\n&\n"+str(titles_unique[temp])+"\n"+str(items_items[x][temp])+"个同时购买\n\n")
		maintext = maintext+str(titles_unique[x])+"\n&\n"+str(titles_unique[temp])+"\n"+str(items_items[x][temp])+"个同时购买\n\n"



	fwrite = open("关联规则.txt","w")#如果已有文件，则覆盖
	fwrite.write(maintext)









		