#coding:utf-8
'''
提取成都是的地址信息，制作字典

'''
import xlrd
import numpy as np
import pandas as pd
import re
# 读取xls，提取其中要处理的两列
# 这是个常用的功能，我要把它规范化，方便重复使用
def xls2list(xlsname):
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	list1 = []
	# print(list1)
	for x in xrange(1,nrows):
		text_data = table.cell(x,0).value
		userip_data = table.cell(x,1).value
		# print(text_data)
		# print(userip_data)
		list0.append(text_data)
		list1.append(userip_data)

	return list0,list1

# 去掉列表中，每个地点的具体的门牌号，只保留道路信息
def reserveRoadInfo(roadlist):
	dealedList = []
	undealedList = []
	streetInfo = []
	bigRoadInfo = []
	remainInfo = []
	for x in xrange(len(roadlist)):
		roadInfo = roadlist[x]
		goalInfo = re.match(ur"((赵镇)?[\u4e00-\u9fa5]{2,3}路)|((赵镇)?[\u4e00-\u9fa5]{2,3}巷)|((赵镇)?[\u4e00-\u9fa5]{2,3}村)|\
			((赵镇)?[\u4e00-\u9fa5]{2,3}店)|([\u4e00-\u9fa5]{1,3}镇)",roadInfo)
		goalInfoStreet = re.match(ur"(赵镇)?[\u4e00-\u9fa5]{2,3}街",roadInfo)
		InfoBigRoad = re.match(ur"((赵镇)?[\u4e00-\u9fa5]{2,3}大道)|([\u4e00-\u9fa5]{2,3}道)",roadInfo)
		if goalInfo:
			dealedList.append(goalInfo.group().encode("utf8"))
		# goalInfo = re.sub(r'\d+(-|、)',"",goalInfo)
		elif goalInfoStreet:
			streetInfo.append(goalInfoStreet.group().encode("utf8"))
		elif InfoBigRoad:
			bigRoadInfo.append(InfoBigRoad.group().encode("utf8"))
		else:
			remainInfo.append(roadInfo.encode("utf8"))
		
	return dealedList,streetInfo,bigRoadInfo,remainInfo

# 逐行写列表
def writeTxt(infoList,filename):
	fwrite = file(filename,"w")
	for x in xrange(len(infoList)):
		# print(type(infoList[x]))
		tempStr = infoList[x] + "\n"
		fwrite.write(tempStr)
	fwrite.close()
def writeSigleWord(infoList,filename):
	fwrite = file(filename,"w")
	for x in xrange(len(infoList)):
		# print(type(infoList[x]))
		tempStr = infoList[x] + "\n"
		fwrite.write(tempStr)
	fwrite.close()

if __name__ == '__main__':
	list0,list1=xls2list("地址.xlsx")
	print(len(list1))
	dealedList,streetInfo,bigRoadInfo,remainInfo = reserveRoadInfo(list1)
	# print(dealedList)
	writeTxt(dealedList,"roadinfo.txt")
	writeTxt(streetInfo,"streetInfo.txt")
	writeTxt(bigRoadInfo,"bigroadInfo.txt")
	writeTxt(remainInfo,"remainInfo.txt")
	print("已处理条目：")
	print(len(dealedList))
	print(len(streetInfo))
	print(len(bigRoadInfo))
	print("未处理条目：")
	print(len(remainInfo))
	longList=[]
	for name in [dealedList,streetInfo,bigRoadInfo]:
		
		for x in xrange(len(name)):
			longList.append(dealedList[x])
	print("longList长度"+str(len(longList)))
	longGoalList=[]
	for x in xrange(len(longList)):
		if longList[x] not in longGoalList:
			longGoalList.append(longList[x])
	print("longGoalList长度"+str(len(longGoalList)))
	writeTxt(longGoalList,"longGoalList.txt")








