# coding:utf-8
# 获取所有分类名list
# 对一个分类做词云，保存为同名图片 def
# 对centos做了针对处理，可在centos上运行

import xlrd
from xlwt import Workbook
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from os import path
from wordcloud import WordCloud

import numpy as np
from PIL import Image
import jieba
import jieba.analyse

def xls2classList(xlsname):
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)

	list1 = []
	nrows = table.nrows
	for x in xrange(0,nrows):
		cell_data = table.cell(x,3).value
		if cell_data not in list1:
			list1.append(cell_data)
	

	return list1


def class2text(classname,xlsname):
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)


	wb = Workbook(encoding="utf-8")
	sh = wb.add_sheet('A new sheet')


	nrows = table.nrows
	text = ''
	for x in xrange(0,nrows):
		cell_data = table.cell(x,3).value
		if cell_data == classname:
			cell_data2 = table.cell(x,1).value
			text += cell_data2

	return text

def text2wordcloud(text,bg_pic,font,stop_words,classname):#传入的需是unicode类型字符串
	
	
	seg_list = jieba.analyse.extract_tags(text, topK=20, withWeight=False, allowPOS=('ilnv'))
	list1 = []
	#读迭代还是用循环吧，不用next()
	for x in seg_list:
		if x not in stop_words:
			list1.append(x)

	wordcount = {}
	total = 0
	for x in xrange(len(list1)):
		if list1[x] in wordcount.keys():
			wordcount[list1[x]] = wordcount[list1[x]]+1
		else:
			wordcount[list1[x]] = 1

		total += 1

	# print(total)
	sort=sorted(wordcount.items(),key=lambda e:e[1],reverse=True)#按键值排序
	#此时sort的类型时list
	#可以截取前50个

	sort = sort[:200]#unicode类型 
	wc_dict = dict(sort)#unicode类型
	
	#调用wordcloud
	wc = WordCloud(font_path=font,max_font_size=100,
		mask=bg_pic,background_color='white')
	
	wc.generate_from_frequencies(wc_dict) 
	#显示
	plt.figure(figsize=(8,8))#大小
	plt.imshow(wc)#内容
	plt.axis("off")#去掉刻度
	plt.savefig(classname+'.png')
	#plt.show()#显示

if __name__ == '__main__':

	d = path.dirname(__file__)#获取路径
	font=path.join(d, "DroidSansFallbackFull.ttf")#生成字体路径
	#读取图片
	bg_pic = np.array(Image.open("cd1.png"))
	stop_words = [u'']
	list1 = xls2classList("测试数据1.xls")
	#print(list1)
	for x in list1:
		text = class2text(x,"测试数据1.xls")
		text2wordcloud(text,bg_pic,font,stop_words,x)

