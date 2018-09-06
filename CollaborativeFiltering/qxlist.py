#coding:utf-8
# 先实现一个读取xls，返回list的功能
import  xlrd
import numpy as np
import pandas as pd

# 读取xls，提取其中要处理的两列
def xls2list(xlsname):
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	list1 = []
	# print(list1)
	for x in xrange(0,nrows):
		text_data = table.cell(x,2).value
		userip_data = table.cell(x,5).value
		# print(text_data)
		# print(userip_data)
		list0.append(text_data)
		list1.append(userip_data)

	return list0,list1

# 返回df格式数据
def df_format(list0,list1):
	df = pd.DataFrame({'item_id':list0,'user_id':list1})
	return df

list0,list1 = xls2list("log.xls")
df = df_format(list0,list1)







