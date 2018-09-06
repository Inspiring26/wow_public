#!/usr/local/bin/python3
#coding:utf-8

import xlrd
import re
import xlwt
# 读excel，仅支持xls格式
def read_excel(excel_name, column_number):
	data = xlrd.open_workbook(excel_name)
	table = data.sheet_by_index(0)
	out_list = table.col_values(column_number)
	return out_list

def writeTxtType2(inputlist,filename):#把列表写成txt 注意转码问题
	fwrite = open(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	if type(inputlist[0])==type(u'abc'):
		for x in range(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr+"\n")
	else:
		for x in range(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr)
	fwrite.close()

# 读excel的一行
def read_excel_type2(excel_name, row_number):
	data = xlrd.open_workbook(excel_name)
	table = data.sheet_by_index(0)
	out_list = table.row_values(row_number)
	return out_list
# 获取excel的行数
def read_excel_numbers(excel_name):
	data = xlrd.open_workbook(excel_name)
	table = data.sheet_by_index(0)
	return table.nrows


if __name__ == '__main__':
	# name_list = read_excel("需要导入到数据库的数据.xlsx",4)
	# name_list = list(set(name_list))
	# print(name_list)
	# print(len(name_list))
	# writeTxtType2(name_list,"name_list.txt")
	name_list = []
	file = xlwt.Workbook()
	table = file.add_sheet('info',cell_overwrite_ok=True)
	counter = 0
	for x in range(read_excel_numbers("需要导入到数据库的数据.xls")):
		temp_list = read_excel_type2("需要导入到数据库的数据.xls",x)
		if temp_list[4] not in name_list:
			name_list.append(temp_list[4])
			for y in range(len(temp_list)):
				table.write(counter,y,temp_list[y])
				if y==len(temp_list)-1:
					counter += 1
		

	file.save('file.xls')
