#coding:utf-8
'''
制作字典
'''
import xlrd
import numpy as np
import re

def xls2list(xlsname):#返回单个列表
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	# print(list1)
	for x in xrange(1,nrows):# 从第二行开始
		text_data = table.cell(x,1).value
		
		list0.append(text_data)
		

	return list0

def extractAddress(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in xrange(len(inputlist)):
		tempStr = inputlist[x]
		s = ur'(区)(?P<address>[\u4e00-\u9fa5]{2,4}(段|路|巷|街|镇|大道))'
		s2 = ur'(反映|和)(?P<address>[\u4e00-\u9fa5]{2,4}(段|路|巷|街|镇|大道))'
		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append(matchResult.group("address"))
		elif matchResult2:
			resultList.append(matchResult2.group("address"))
	return resultList

def extractAddressAgain(inputlist):#再次匹配，从地址列表中出去不要的地址
	resultList = []
	for x in xrange(len(inputlist)):
		tempStr = inputlist[x]
		#(在|周边|附近)
		s = ur'(?P<address>[\u4e00-\u9fa5]{0,3}(的路|主路|道路|的街|路路|街街|修路))'
		s2 = ur'(?P<address>(在|周边|附近|了|的|与)[\u4e00-\u9fa5]{0,4}(路|巷|街|镇|大道))'
		# 单独添加各种错误街道
		s3 = ur'(?P<address>(大街小巷|了|近期|之前|该街|前往|的|整条))'
		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		matchResult3 = re.search(s3, tempStr)
		if matchResult:
			pass
		elif matchResult2:
			pass
		elif matchResult3:
			pass
		else:
			resultList.append(tempStr)
	return resultList

def filterList2list(inputlist):#过滤列表，返回一个没有重复元素的列表
	resultList = []
	for x in xrange(len(inputlist)):
		if inputlist[x] not in resultList:
			resultList.append(inputlist[x])
	return resultList

def writeTxt(inputlist,filename):#把列表写成txt 注意转码问题
	fwrite = file(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	if type(inputlist[0])==type(u'abc'):
		for x in xrange(len(inputlist)):
			tempStr = inputlist[x].encode("utf8") + "\n"
			fwrite.write(tempStr)
	else:
		for x in xrange(len(inputlist)):
			tempStr = inputlist[x] + "\n"
			fwrite.write(tempStr)

def writeTxtNOTNewline(inputlist,filename):#有时已经有换行符了
	fwrite = file(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	if type(inputlist[0])==type(u'abc'):
		for x in xrange(len(inputlist)):
			tempStr = inputlist[x].encode("utf8")
			fwrite.write(tempStr)
	else:
		for x in xrange(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr)
	
	fwrite.close()	
def assembleList(inputlist1, inputlist2):#把两个列表链接成一个,hahah
	return inputlist1 + inputlist2

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

if __name__ == '__main__':
	xlsFilename = ["sep.xls","企业问题.xls","公开电话.xls","噪音污染.xls",
		"垃圾问题.xls","油烟扰民.xls","物业管理.xls","环境卫生综合整治.xls"]
	mainAddressList=[]
	for xlsname in xlsFilename:
		print("正在处理： "+xlsname)
		list0=xls2list(xlsname)
		addressList = extractAddress(list0)
		mainAddressList += addressList

	dictList = filterList2list(mainAddressList)
	
	#过滤一遍地址列表
	dictList2 = extractAddressAgain(dictList)
	print("dictList长度 "+str(len(dictList2)))
	writeTxt(dictList2,"OnlyAddressList.txt")

	# undealedList = txt2list("longGoalList2.txt")
	# dictList = filterList2list(undealedList)
	# print(len(dictList))
	# writeTxtNOTNewline(dictList,"dictList.txt")







