#coding:utf-8
'''
由于使用的是pymysql 需要用python3运行
'''

import pymysql
import re


def filterList2list(inputlist):#过滤列表，返回一个没有重复元素的列表
	resultList = []
	for x in range(len(inputlist)):
		if inputlist[x] not in resultList:
			resultList.append(inputlist[x])
	return resultList
def extractCupOrBowl(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>(杯盖|平盖|拱盖))"
		s2 = "(?P<capacity>(碗))"
		s3 = "(?P<capacity>(纸杯|杯子|塑料杯|瓦楞杯|白杯|五角星杯|冷饮杯|热饮杯|苓膏杯|敞口杯|圣代杯|果冻杯|酸奶杯|试吃杯|品尝杯|试饮杯))"
		s4 = "(?P<capacity>(吸管))"
		s5 = "(?P<capacity>(勺子|勺))"
		s6 = "(?P<capacity>(调料盒|酱料盒筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒|竹筷|方便筷|一次性筷子|竹卫生筷子|打9.5折|金属钢丝球|洗浴用品))" # 第六个采用了不太一样的方法
		s7 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		matchResult3 = re.search(s3, tempStr)
		matchResult4 = re.search(s4, tempStr)
		matchResult5 = re.search(s5, tempStr)
		matchResult6 = re.search(s6, tempStr)
		matchResult7 = re.search(s7, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append("盖子")
		elif matchResult2:
			resultList.append("碗")
		elif matchResult3:
			resultList.append("杯")
		elif matchResult4:
			resultList.append("吸管")
		elif matchResult5:
			resultList.append("勺子")
		elif matchResult6:
			resultList.append(matchResult6.group("capacity"))
		elif matchResult7:
			resultList.append("饭盒")
		else:
			resultList.append("")
	return resultList
def extractCupCap(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>(不带盖|盖子单拍|盖单拍))"
		s2 = "(?P<capacity>带盖)"
		s3 = "(?P<capacity>盖)"
		s4 = "(?P<capacity>杯)"
		# s5 = "(?P<capacity>(纸杯|杯子|塑料杯|瓦楞杯|白杯|五角星杯|冷饮杯|苓膏杯|敞口杯|圣代杯|果冻杯|酸奶杯|试吃杯|品尝杯|试饮杯))"
		s5 = "(?P<capacity>(吸管))"
		s6 = "(?P<capacity>(勺子|勺))"
		s7 = "(?P<capacity>(调料盒|杯套|酱料盒筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|棉签|牙签|外卖盒|竹筷|方便筷|一次性筷子|竹卫生筷子))" # 第六个采用了不太一样的方法
		s8 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		matchResult3 = re.search(s3, tempStr)
		matchResult4 = re.search(s4, tempStr)

		matchResult5 = re.search(s5, tempStr)
		matchResult6 = re.search(s6, tempStr)
		matchResult7 = re.search(s7, tempStr)
		matchResult8 = re.search(s8, tempStr)
		if matchResult5:
			# resultList.append(matchResult5.group("capacity"))
			if matchResult2:
				resultList.append("杯子--带盖")
			else:
				resultList.append("")
		elif matchResult6:
			# resultList.append(matchResult6.group("capacity"))
			resultList.append("")
		elif matchResult7:
			# resultList.append(matchResult7.group("capacity"))
			resultList.append("")
		elif matchResult8:
			# resultList.append(matchResult8.group("capacity"))
			resultList.append("")
		elif matchResult4:
			if matchResult:
				resultList.append("杯子--无盖")
			elif matchResult2:
				resultList.append("杯子--带盖")
			elif matchResult3:
				resultList.append("盖子")
			else:
				resultList.append("杯子")			
		
		else:
			resultList.append("")
	return resultList
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
			
		
	
# def writeTxtType2(inputlist,filename):#把列表写成txt 注意转码问题
# 	fwrite = open(filename,"w")#如果已有文件，则覆盖
# 	# 判断一下编码，然后选择是否要转换格式去写
# 	if type(inputlist[0])==type(u'abc'):
# 		for x in range(len(inputlist)):
# 			tempStr = inputlist[x]
# 			fwrite.write(tempStr)
# 	else:
# 		for x in range(len(inputlist)):
# 			tempStr = inputlist[x]
# 			fwrite.write(tempStr)
def extractMaterialInfo(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>塑料)"
		s2 = "(?P<capacity>(PET|pet))"
		s3 = "(?P<capacity>牛皮)"
		s4 = "(?P<capacity>瓦楞)"
		s5 = "(?P<capacity>(纸杯[^盖]))"
		# s6 = "(?P<capacity>(筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒))" # 第六个采用了不太一样的方法
		# s7 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		matchResult3 = re.search(s3, tempStr)
		matchResult4 = re.search(s4, tempStr)
		matchResult5 = re.search(s5, tempStr)
		# matchResult6 = re.search(s6, tempStr)
		# matchResult7 = re.search(s7, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append("塑料")
		elif matchResult2:
			resultList.append("PET")
		elif matchResult3:
			resultList.append("牛皮纸")
		elif matchResult4:
			resultList.append("瓦楞纸")
		elif matchResult5:
			resultList.append("纸杯")
		# elif matchResult6:
		# 	resultList.append(matchResult6.group("capacity"))
		# elif matchResult7:
		# 	resultList.append("饭盒")
		else:
			resultList.append("")
	return resultList

def extractCapacity(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>\d{1,4}(ml|ML|Ml|毫升|盎司))"

		matchResult = re.search(s, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			undealStr = matchResult.group("capacity")
			dealedStr = undealStr.replace("毫升", "ML")
			dealedStr = dealedStr.replace("ml", "ML")
			dealedStr = dealedStr.replace("Ml", "ML")
			resultList.append(dealedStr)
		else:
			resultList.append("")
	return resultList


def capacityConvert(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>\d{1,4}(盎司))"
		s2 = "(?P<capacity>\d{1,2})盎司"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			amount = matchResult2.group("capacity")
			# print(amount)
			amount = (float)(amount) * 29.27
			resultList.append(str(amount)+"ML\n")
		else:
			resultList.append(tempStr)
	return resultList

def getdatafrom_mysql():
	
# 打开数据库连接
# db = MySQLdb.connect("172.18.100.39","report","report","analysis_report")
	conn = pymysql.connect(host='172.18.100.39', port=3306, user='report', passwd='report',db='analysis',charset="utf8")
	# 使用cursor()方法获取操作游标 
	# cursor = db.cursor()
	cur = conn.cursor()

	# 创建数据表SQL语句
	sql0 = """CREATE TABLE EMPLOYEE (
	         FIRST_NAME  CHAR(20) NOT NULL,
	         LAST_NAME  CHAR(20),
	         AGE INT,  
	         SEX CHAR(1),
	         INCOME FLOAT )"""
	sql1 = """SELECT name FROM analysis_commodity LIMIT 100"""
		
	# 使用execute方法执行SQL语句
	cur.execute("SELECT name FROM analysis_order")
	# 使用 fetchone() 方法获取一条数据
	data = cur.fetchall()
	conn.close()
	print(len(data))

# 	print(type(data))
# # print(data[0:5][0])
# print(data[0:5][0][0])
# print(data)

	resultList = []
	for x in range(len(data)):
		if data[x][0] not in resultList:
			resultList.append(data[x][0])
		# if x%1000==0:
		# 	print(x)
		
		
	print(len(resultList))
	return resultList

if __name__ == '__main__':
	resultList = getdatafrom_mysql()
	cupbowllist = extractCupOrBowl(resultList)
	writeTxt(resultList,"cupbowlnamelist.txt")
	writeTxt(cupbowllist,"cupbowllist.txt")

	
	







