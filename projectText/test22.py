import xlrd
import xlwt
import jieba.analyse
import jieba.posseg

# 读txt
def readtext(filename):
	f = open(filename)
	list1 = []
	line = f.readline()
	while line:
		list1.append(line)
		line = f.readline()
	return list1
# 读xls
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
def word_ate(sentence):
	words = jieba.posseg.cut(sentence)
	stop_words = []
	str2 = ""
	atelist = ["ns","nr","i","nt"]
	for word, flag in words:
		if flag in atelist:
			if word not in stop_words:
									
				if str2 == "":
					str2 = word
				else:
						
					str2 = str2+","+word
		print('%s %s' % (word, flag),end=" ")

	print(" ")
	print(" ")
	return str2
# 提取关键词
def extract_words(sentence):
	seg_list = jieba.analyse.textrank(sentence, topK=20, withWeight=False,allowPOS=('ns',"nr","i",'n',"nt")) 
	str1 = ""
	stop_words = []
	#读迭代还是用循环吧，不用next()
	for x in seg_list:
		# print(x)
		if x not in stop_words:
			if x != "":
				if str1 == "":
					str1 = x
				else:
						
					str1 = str1+","+x
	return str1

# 写xls
def writeexcel03(path, inputlist):  
  
    wb=xlwt.Workbook()  
    sheet=wb.add_sheet("xlwt3数据测试表")  
    # inputlist = [["名称", "hadoop编程实战", "hbase编程实战", "lucene编程实战"], ["价格", "52.3", "45", "36"], ["出版社", "机械工业出版社", "人民邮电出版社", "华夏人民出版社"], ["中文版式", "中", "英", "英"]]  
    for i in range(len(inputlist)):  
        for j in range(0,len(inputlist[i])):  
            sheet.write(i,j,inputlist[i][j])  
    wb.save(path)  
    print("写入数据成功！")  
  

if __name__ == '__main__':
	# list1 = readtext("test.txt")
	# print(list1)

	list1 = xls2listType2("测试数据1.xls",1)
	list1 = list1[:10]
	
	list2=[]
	for x in range(len(list1)):
		# print(list1[x])
		# x_ = extract_words(list1[x])
		# str2 = word_ate(list1[x])
		# print(x_)
		templist=[]
		templist.append(list1[x])
		templist.append(x)
		templist.append(x**2)
		list2.append(templist)


	# print(list2)

	writeexcel03("test.xls", list2)




