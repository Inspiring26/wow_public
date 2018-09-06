#!/usr/local/bin/python3
#coding:utf-8

import xlrd
import xlwt
import re
import pandas as pd 
import numpy as np
from tgrocery import Grocery

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
	# issue_list,slove_list = read_excel("issue_slove.xls", 0, 1)
	category_list = read_excel("in_list.xls",1)
	print(len(category_list))

	







