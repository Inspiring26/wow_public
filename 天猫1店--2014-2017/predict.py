from sklearn import linear_model
import matplotlib.pyplot as plt
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

def linreg():
	reg = linear_model.LinearRegression()
	

	reg.fit (months, sales)
	print(reg.coef_)
	print(reg.intercept_)

	y_pred = reg.predict(months)
	for x in range(7,13):
		newsales = x*reg.coef_[0] + reg.intercept_
		print("第"+str(x)+"个月销售额： "+str(int(newsales)))


	plt.scatter(pltmonths, sales, color='black')
	plt.plot(pltmonths, y_pred, color='blue', linewidth=3)
	# plt.xticks(())
	# plt.yticks(())
	plt.show()

def polynomial_regression(): # 不怎么好
	from sklearn.preprocessing import PolynomialFeatures
	months = [[1],[2],[3],[4],[5],[6]]
	poly = PolynomialFeatures(degree=2)
	print(poly.fit_transform(months))

def polynomial_regression2():
	from sklearn.preprocessing import PolynomialFeatures
	from sklearn.linear_model import LinearRegression
	from sklearn.pipeline import Pipeline
	import numpy as np
	fig=plt.figure()
	model = Pipeline([('poly', PolynomialFeatures(degree=6)),
		('linear', LinearRegression(fit_intercept=False))]) 
	model = model.fit(month_all + month_all +month_all, sales_2015_all+sales_2014_all+sales_2016_all)
	mycoef_ = model.named_steps['linear'].coef_
	print("mycoef_: "+ str(mycoef_))
	# print(model.named_steps['linear'].intercept_)

	# p1=fig.add_subplot(211)
	p1=plt
	p1.scatter(month_all2, sales_2015_all, color='black')
	p1.scatter(month_all2, sales_2016_all, color='red')
	p1.scatter(month_all2, sales_2014_all, color='blue')
	xline = np.arange(1.0, 12.0, 0.01)
	yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5 + mycoef_[6]*xline**6
	p1.plot(xline, yline, color='cyan', linewidth=3)
	
	for x in range(7,13):
		xline = x
		yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5 + mycoef_[6]*xline**6
		print("第"+str(x)+"个月销售额： "+str(int(yline)))
	# p2=fig.add_subplot(212)
	# model = model.fit(month_all, sales_2016_all)
	# mycoef_ = model.named_steps['linear'].coef_
	# p2.scatter(month_all2, sales_2016_all, color='black')
	# xline = np.arange(1.0, 12.0, 0.01)
	# yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5
	# p2.plot(xline, yline, color='blue', linewidth=3)


	plt.show()

def polynomial_regression3(month_all3, list3,month_all3_2):
	from sklearn.preprocessing import PolynomialFeatures
	from sklearn.linear_model import LinearRegression
	from sklearn.pipeline import Pipeline
	import numpy as np
	fig=plt.figure()
	model = Pipeline([('poly', PolynomialFeatures(degree=6)),
		('linear', LinearRegression(fit_intercept=False))]) 
	model = model.fit(month_all3, list3)
	mycoef_ = model.named_steps['linear'].coef_
	print("mycoef_: "+ str(mycoef_))
	p1=plt
	p1.scatter(month_all3_2[:12], list3[:12], color='black')
	p1.scatter(month_all3_2[12:24], list3[12:24], color='red')
	p1.scatter(month_all3_2[24:], list3[24:], color='blue')
	xline = np.arange(1.0, 12.0, 0.01)
	yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5 + mycoef_[6]*xline**6
	p1.plot(xline, yline, color='cyan', linewidth=3)
	
	for x in range(7,13):
		xline = x
		yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5 + mycoef_[6]*xline**6
		print("第"+str(x)+"个月人数： "+str(int(yline)))
	
	plt.show()

def polynomial_regression4():
	from sklearn.preprocessing import PolynomialFeatures
	from sklearn.linear_model import LinearRegression
	from sklearn.pipeline import Pipeline
	import numpy as np
	fig=plt.figure()
	model = Pipeline([('poly', PolynomialFeatures(degree=2)),
		('linear', LinearRegression(fit_intercept=False))]) 
	model = model.fit(months, sales)
	mycoef_ = model.named_steps['linear'].coef_
	print("mycoef_: "+ str(mycoef_))
	# print(model.named_steps['linear'].intercept_)

	# p1=fig.add_subplot(211)
	p1=plt
	
	p1.scatter(pltmonths, sales, color='blue')
	xline = np.arange(1.0, 6.0, 0.01)
	yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 
	p1.plot(xline, yline, color='cyan', linewidth=3)
	
	# for x in range(7,13):
	# 	xline = x
	# 	yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5 + mycoef_[6]*xline**6
	# 	print("第"+str(x)+"个月销售额： "+str(int(yline)))
	# p2=fig.add_subplot(212)
	# model = model.fit(month_all, sales_2016_all)
	# mycoef_ = model.named_steps['linear'].coef_
	# p2.scatter(month_all2, sales_2016_all, color='black')
	# xline = np.arange(1.0, 12.0, 0.01)
	# yline = mycoef_[0] + mycoef_[1]*xline + mycoef_[2]*xline**2 + mycoef_[3]*xline**3 + mycoef_[4]*xline**4 + mycoef_[5]*xline**5
	# p2.plot(xline, yline, color='blue', linewidth=3)


	plt.show()



if __name__ == '__main__':
	months = [[1],[2],[3],[4],[5],[6]]
	month_all = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]
	month_all2 = [1,2,3,4,5,6,7,8,9,10,11,12]
	pltmonths = [1, 2, 3, 4, 5, 6]
	sales = [597547.23, 695798.43, 736183.06, 617787.83, 482578.12, 413010.58]
	sales_2016_all = [844502.04,483095.43,807709.8,752466.97,873828.93,868251.13,898105.85,897510.72,844974.83,904996.17,1334920.82,816388.18]
	sales_2015_all = [808697.07,446200.07,421299.16,434614.8,423182.9,391980.78,516134.66,622733.87,691361.69,697784.58,891524.1,862011.53]
	sales_2014_all = [375448.62,386128.67,462792.55,480231.5,451894.06,569854.67,543491.03,578835.31,554923.86,441160.46,1645048.43,510417.82]
	orders = [8130, 9765, 7905, 6272, 5200, 4460]
	items = [9877, 11765, 10091, 8509, 7105, 6168]
	productnum = [25919, 28540, 29072, 24567, 20091, 19308]
	number_of_people = [7550, 9039, 7001, 5494, 4544, 3916]

	# polynomial_regression2()

	list3 = xls2listType2("2017后半年预算(1).xls",6)
	list3 = list3[:36]
	print(list3)
	month_all3 = month_all * 3
	month_all3_2 = month_all2 *3
	print(month_all3_2)
	polynomial_regression3(month_all3, list3,month_all3_2)
	# polynomial_regression4()
	# polynomial_regression()




