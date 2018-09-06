#coding:utf-8
import xlrd
import numpy as np
import pandas as pd
import re
from xlwt import Workbook
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

def txt2list(txtname):
	f = open(txtname)
	line = f.readline()
	rowNumber = 1
	inputlist = []
	print("读取数据")
	while line:
		inputlist.append(line)
		line = f.readline()
		rowNumber += 1

	print("读数据完成")
	return inputlist

def mainDeal(inputlist,roadNameList):
	resultList = []
	lenOfInput = len(inputlist)
	for x in xrange(lenOfInput):
		resultList.append("")
	lenOfRoadName = len(roadNameList)
	for x in xrange(lenOfRoadName):
		roadname = roadNameList[x].decode("utf8").replace("\n","")
		displayStr = "处理进度  "+str(x+1)+"/"+str(lenOfRoadName)
		print(displayStr)#单行跳动显示,但是需要是python3，python3呢又要改xrange
		for y in xrange(lenOfInput):
			inputcontent = inputlist[y]
			judge = re.search(roadname,inputcontent)
			tempStr = resultList[y]
			if judge:
				tempStr = tempStr + roadname + ','
			else:
				tempStr = tempStr + ''
			resultList[y]=tempStr

	return resultList

def writeTxt(infoList,filename):
	fwrite = file(filename,"w")
	for x in xrange(len(infoList)):
		# print(type(infoList[x]))
		tempStr = infoList[x].encode("utf8") + "\n"
		fwrite.write(tempStr)
	fwrite.close()

def writeXls(infoList,filename):
	wb = Workbook(encoding="utf-8")
	sh = wb.add_sheet('A new sheet')
	for x in xrange(len(infoList)):
		cell_data = infoList[x].encode("utf8")
		sh.write(x, 0, cell_data)
	wb.save(filename)


	
	

if __name__ == '__main__':
	list0,list1=xls2list("环境卫生综合整治.xls")
	print(len(list1))
	roadNameList = txt2list("OnlyAddressList.txt")
	print(len(roadNameList))
	# print(roadNameList)
	resultList = mainDeal(list1,roadNameList)
	# writeTxt(resultList,"classify.txt")
	writeXls(resultList,"环境卫生综合整治result.xls")
