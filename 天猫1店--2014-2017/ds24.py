#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import xlrd


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

def cluster(pricelist, amountlist, X1, n_clusters):
	
	plt.rcParams['font.sans-serif']=['SimHei']
	plt.rcParams['axes.unicode_minus']=False
	plt.figure(figsize=(12, 6))

	random_state = 170
	# X, y = make_blobs(n_samples=n_samples, random_state=random_state)


	y_pred = KMeans(n_clusters=n_clusters, random_state=random_state).fit_predict(X1)

	print(len(y_pred))
	plt.scatter(pricelist, amountlist,  c=y_pred)
	plt.xlabel("price")
	plt.ylabel("amount")
	# print(X[:, 0])
	plt.title(u"ds")
	plt.show()

if __name__ == '__main__':
	pricelist = xls2listType2("不同价格销量统计.xls",0)
	amountlist = xls2listType2("不同价格销量统计.xls",1)
	# pricelist = pricelist[:100]
	# amountlist = amountlist[:100]
	X1 = []
	for x in range(len(pricelist)):
		templist = []
		templist.append(pricelist[x]*10)
		templist.append(amountlist[x]/3750)
		X1.append(templist)
	print(len(pricelist))
	print(len(amountlist))
	print(len(X1))
	X, y = make_blobs(n_samples=50, random_state=170)
	x_0 =X[:,0]
	x_1 =X[:,1]
	# cluster(x_0, x_1, X, 3)
	cluster(pricelist, amountlist, X1, 4)



