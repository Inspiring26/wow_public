#coding:utf-8

from tgrocery import Grocery
import xlrd
from xlwt import Workbook
import sys
#reload(sys)
#sys.setdefaultencoding("utf8")


#print "传入参数为："
#print sys.argv[1]
tempstr = str(sys.argv[1])+str(sys.argv[2])
data = xlrd.open_workbook(tempstr)
table = data.sheet_by_index(0)

wb = Workbook(encoding="utf-8")
sh = wb.add_sheet('A new sheet')




nrows = table.nrows
xf = 0 # 扩展的格式化

print "加载训练模型中..."
new_grocery = Grocery('/root/apache-tomcat-7.0.79/apache-tomcat-7.0.79/webapps/Upload/WEB-INF/classes/com/analysis/cuit')
new_grocery.load()


# 单独处理第一行
cell_data = table.cell(0,0).value
sh.write(0, 0, cell_data)
sh.write(0, 1, "大类")
sh.write(0, 2, "小类")

for x in xrange(1,nrows):
	
	cell_data = table.cell(x,0).value
	# 写入表格
	result = str(new_grocery.predict(cell_data))
	print x
	sh.write(x, 0, cell_data)
	sh.write(x, 1, result.split("|")[0])
	sh.write(x, 2, result.split("|")[1])


	

tempstr2 = str(sys.argv[1])+"_step1_"+str(sys.argv[2]) 
wb.save(tempstr2)
print "分类完成!"
#print "传入参数为："
#print sys.argv[1]
# grocery = Grocery('cuit1')
# grocery.train('train1.txt')
# grocery.save()
# print "the train is over!"


# new_grocery = Grocery('cuit1')
# new_grocery.load()
# print new_grocery.test('train_test1.txt')
