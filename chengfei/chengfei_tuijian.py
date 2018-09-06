#!/usr/local/bin/python3
#coding:utf-8

import xlrd
import xlwt
import re
import pandas as pd 
import numpy as np

# 读excel，仅支持xls格式
def read_excel(excel_name, column_number):
	data = xlrd.open_workbook(excel_name)
	table = data.sheet_by_index(0)
	out_list = table.col_values(column_number)
	return out_list
def read_excel(excel_name, column_number_1, column_number_2):
	data = xlrd.open_workbook(excel_name)
	table = data.sheet_by_index(0)
	out_list_1 = table.col_values(column_number_1)
	out_list_2 = table.col_values(column_number_2)
	return out_list_1, out_list_2
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
# 一般要在main函数里展开了写，这里只是一个示例
def write_excel():
	file = xlwt.Workbook()
	table = file.add_sheet('info',cell_overwrite_ok=True) 
	table.write(0,0,'hahah')
	file.save('file.xls')

def write_txt(inlist, txt_name):
	fwrite = open(txt_name,"w")#如果已有文件，则覆盖
	out_str = ""
	for x in inlist:
		out_str += x + "\n"
	fwrite.write(out_str)
	fwrite.close
def read_txt(txt_name):
	f = open(txt_name)
	line = f.readline()
	inputlist = []
	while line:
		inputlist.append(line)
		line = f.readline()
	return inputlist

def cos(vector1,vector2):
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)
if __name__ == '__main__':
	issue_list,slove_list = read_excel("issue_slove.xls", 0, 1)
	# test_list = read_excel_type2("issue_slove.xls", 0)
	

	issue_list = list(set(issue_list))
	slove_list = list(set(slove_list))
	# print(issue_list)
	# print(slove_list)
	df = pd.DataFrame(np.zeros((len(issue_list),len(slove_list))),index=issue_list,columns=slove_list)
	
	for x in range(read_excel_numbers("issue_slove.xls")):
		temp_list = read_excel_type2("issue_slove.xls", x)
		df.loc[temp_list[0],temp_list[1]] += 1
	print(df)
	# print(df.T)
	# print(df[0:1])
	issue_relation = pd.DataFrame(np.zeros((len(issue_list),len(issue_list))),index=issue_list,columns=issue_list)
	# print("issue_relation")
	# print(issue_relation)
	slove_relation = pd.DataFrame(np.zeros((len(slove_list),len(slove_list))),index=slove_list,columns=slove_list)
	# print("slove_list")
	# print(slove_relation)

	for x in issue_list:
		for y in issue_list:
			issue_relation.loc[x,y]=cos(df.T[x],df.T[y])
	# print("issue_relation:")
	# print(issue_relation)

	for x in slove_list:
		for y in slove_list:
			slove_relation.loc[x,y]=cos(df[x],df[y])
	# print("slove_relation:")
	# print(slove_relation)
	# slove_relation.sort_values(by=["slove01"])
	# print("slove_relation:")
	temp_list = slove_relation.sort_values(by=["slove01","slove02"],ascending=False)
	temp_list = temp_list["slove01"]
	interception_len = 0
	if len(temp_list)<100:
		interception_len = int(len(temp_list)*0.9)
	else:
		interception_len = 100
	temp_list = temp_list[:interception_len]
	# print(temp_list)

	recommed_weight = pd.DataFrame(np.zeros((len(issue_list),len(slove_list))),index=issue_list,columns=slove_list)
	# print("recommed_weight:")
	# print(recommed_weight)

	print("")
	for issue in recommed_weight.index:
		# print(issue)
		# 选出最相关的几个问题，保留本身作为100%相关
		temp_l = issue_relation.sort_values(by=[issue],ascending=False)
		temp_l = temp_l[issue]
		temp_l = temp_l[:interception_len]
		# print("temp_l")
		# print(temp_l)
		# 计算最相关的问题和各个解决方案的权重，直接加到权重矩阵
		for ngb_issue in temp_l.index:
			for slove in recommed_weight.columns:
				# 权重分为 问题之间的关系 和 问题与解决方法的关系
				# print(issue)
				# print(ngb_issue)
				# print(issue_relation.loc[issue,ngb_issue])
				recommed_weight.loc[issue,slove] += issue_relation.loc[issue,ngb_issue] * df.loc[ngb_issue,slove]

	print(recommed_weight)
	# 权重最大值
	# print(recommed_weight.values.max())

	print("")
	print(recommed_weight.T.sort_values(by=["issue01"],ascending=False)["issue01"][:5])
	# print(len(temp_list))
	# print(temp_list.index)
	# print(temp_list.index[1])

	# print(df.sort_values(by=["slove01"]))
	# 推荐三个 设定为3列
	recommed_matrix = pd.DataFrame(np.zeros((len(issue_list),3)),index=issue_list,columns=["1","2","3"])
	recommed_matrix_weight = pd.DataFrame(np.zeros((len(issue_list),3)),index=issue_list,columns=["1","2","3"])
	# print(recommed_matrix)
	# recommed_matrix.loc["issue01","1"]="hahah"
	# print(recommed_matrix)
	for x in recommed_weight.index:
		columns_list=["1","2","3"]
		for y in columns_list:
			recommed_matrix.loc[x,y]=recommed_weight.T.sort_values(by=[x],ascending=False)[x].index[int(y)-1]
			recommed_matrix_weight.loc[x,y]=recommed_weight.T.sort_values(by=[x],ascending=False)[x][int(y)-1]*100/(recommed_weight.values.max()*1.011)
	print(recommed_matrix)	
	print(recommed_matrix_weight)

	file = xlwt.Workbook()
	table = file.add_sheet('info',cell_overwrite_ok=True)
	for x in range(len(recommed_matrix.index)):
		table.write(x+1,0,recommed_matrix.index[x])
		for y in range(len(recommed_matrix.columns)):
			table.write(x+1,2*y+1,recommed_matrix.iloc[x,y])
			table.write(x+1,2*y+2,recommed_matrix_weight.iloc[x,y])
			if x == 0:
				table.write(x,2*y+1,"解决方案")
				table.write(x,2*y+2,"方案权重")

	file.save('file.xls')
	

	








