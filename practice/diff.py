#coding:utf-8
import xlrd
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
	list_a = xls2listType2("正式数据a.xls",0)
	list_b = xls2listType2("临时数据b.xls",0)
	inBnotInA = []
	inAnotInB = []
	# 属于B不属于A的
	for x in range(len(list_b)):
		if list_b[x] not in list_a:
			inBnotInA.append(list_b[x])

	# 属于A不属于B的
	for x in range(len(list_a)):
		if list_a[x] not in list_b:
			inAnotInB.append(list_a[x])
	writeTxt(inBnotInA,"inBnotInA.txt")
	writeTxt(inAnotInB,"inAnotInB.txt")