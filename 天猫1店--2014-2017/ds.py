#coding:utf-8
import xlrd
import re


def xls2list(xlsname):#返回单个列表
	data = xlrd.open_workbook(xlsname)
	table = data.sheet_by_index(0)
	nrows = table.nrows
	# print(nrows)
	list0 = []
	# print(list1)
	for x in range(1,nrows):# 从第二行开始
		text_data = table.cell(x,5).value
		
		list0.append(text_data)
		

	return list0
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
	
def readtxt(filename="ds.txt"):
	f = open(filename)
	line = f.readline()
	inputlist = []
	while line:
		inputlist.append(line)
		line = f.readline()

	print("读数据完成")
	return inputlist

def filterList2list(inputlist):#过滤列表，返回一个没有重复元素的列表
	resultList = []
	for x in range(len(inputlist)):
		if inputlist[x] not in resultList:
			resultList.append(inputlist[x])
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
	fwrite.close()
			
def writeTxtType2(inputlist,filename):#把列表写成txt 注意转码问题
	fwrite = open(filename,"w")#如果已有文件，则覆盖
	# 判断一下编码，然后选择是否要转换格式去写
	if type(inputlist[0])==type(u'abc'):
		for x in range(len(inputlist)):
			tempStr = inputlist[x]
			fwrite.write(tempStr)
	else:
		for x in range(len(inputlist)):
			tempStr = inputlist[x].decode("utf8")
			fwrite.write(tempStr)
	fwrite.close()
def findAndReplace(inputStr):
	pass

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
def extractCupOrBowl(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>(杯盖|平盖|拱盖))"
		s2 = "(?P<capacity>(碗))"
		s3 = "(?P<capacity>(纸杯|杯子|塑料杯|瓦楞杯|白杯|五角星杯))"
		s4 = "(?P<capacity>(吸管))"
		s5 = "(?P<capacity>(勺子|勺))"
		s6 = "(?P<capacity>(筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒))" # 第六个采用了不太一样的方法
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
		
def dsNoRepeatProperty():
	list12 = xls2list("2014年1-2月宝贝报表.xls")
	list34 = xls2list("2014年3-4月宝贝报表.xls")
	list5_12 = xls2list("2014年5月-12月宝贝报表.xls")
	inputlist = list12 + list34 + list5_12
	print(len(inputlist))
	singleList = filterList2list(inputlist)
	print(len(singleList))

	writeTxt(singleList,"dsNoRepeatProperty.txt")
		
def dsNoRepeatCapacity():
	inputList = readtxt("dsNoRepeatProperty.txt")
	print(len(inputList))
	singleList = filterList2list(inputList)
	print(len(singleList))
	capacity = extractCapacity(singleList)

	writeTxt(capacity,"dsNoRepeatCapacity.txt")

def dsCupOrBowl():
	inputList = readtxt("dsNoRepeat.txt")
	print(len(inputList))
	
	capacity = extractCupOrBowl(inputList)

	writeTxt(capacity,"dsCupOrBowl.txt")

# 盎司转毫升
def dsOzToMl():
	inputList = readtxt("dsNoRepeatCapacity&manual.txt")
	resultList = capacityConvert(inputList)
	print(len(resultList))
	writeTxtType2(resultList,"dsOzToMl.txt")

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

def question2Stat():
	tittle12 = xls2listType2("2014年1-2月宝贝报表.xls",1)
	tittle34 = xls2listType2("2014年3-4月宝贝报表.xls",1)
	tittle5_12 = xls2listType2("2014年5月-12月宝贝报表.xls",1)
	dstitle = tittle12 + tittle34 + tittle5_12
	print("dstitle: "+str(len(dstitle)))

	amount12 = xls2listType2("2014年1-2月宝贝报表.xls",3)
	amount34 = xls2listType2("2014年3-4月宝贝报表.xls",3)
	amount5_12 = xls2listType2("2014年5月-12月宝贝报表.xls",3)
	dsamount = amount12 + amount34 + amount5_12
	print("dsamount: "+str(len(dsamount)))

	property12 = xls2listType2("2014年1-2月宝贝报表.xls",5)
	property34 = xls2listType2("2014年3-4月宝贝报表.xls",5)
	property5_12 = xls2listType2("2014年5月-12月宝贝报表.xls",5)
	dsproperty = property12 + property34 + property5_12
	print("dsproperty: "+str(len(dsproperty)))

	dsNoRepeat = readtxt("dsNoRepeat.txt")
	print("dsNoRepeat: "+str(len(dsNoRepeat)))

	dsCupOrBowl = readtxt("dsCupOrBowl.txt")
	print("dsCupOrBowl: "+str(len(dsCupOrBowl)))


	dsNoRepeatProperty = readtxt("dsNoRepeatProperty.txt")
	print("dsNoRepeatProperty: "+str(len(dsNoRepeatProperty)))

	dsOzToMl = readtxt("dsOzToMl.txt")
	print("dsOzToMl: "+str(len(dsOzToMl)))

	divisionAmountList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	divisionAmountListBowl = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for x in range(len(dstitle)):
		item = dstitle[x]
		item = item +"\n"
		#获取在dsNoRepeat的索引
		pos = dsNoRepeat.index(item)
		# print(pos)
		# 返回类型
		itemType = dsCupOrBowl[pos]
		if itemType=="杯\n":
			colorEtc = dsproperty[x]
			colorEtc = colorEtc + "\n"

			colorPos = dsNoRepeatProperty.index(colorEtc)
			# 容量
			itemCapacity = dsOzToMl[colorPos]

			# 数量
			itemAmount = str(dsamount[x])
			itemAmount = itemAmount.replace("\n","")
			itemAmount = float(itemAmount)
			itemAmount = int(itemAmount)
			# print(itemAmount)
			# print(type(itemAmount))

			if itemCapacity != "\n":
				itemCapacity = itemCapacity.replace("ML\n","")
				# print(itemCapacity)
				# print(type(itemCapacity))
				itemCapacity = float(itemCapacity)
				itemCapacity = int(itemCapacity)
				divisionPos = itemCapacity//100
				divisionAmountList[divisionPos] += itemAmount

	for x in range(len(dstitle)):
		item = dstitle[x]
		item = item +"\n"
		#获取在dsNoRepeat的索引
		pos = dsNoRepeat.index(item)
		# print(pos)
		# 返回类型
		itemType = dsCupOrBowl[pos]
		if itemType=="碗\n":
			colorEtc = dsproperty[x]
			colorEtc = colorEtc + "\n"

			colorPos = dsNoRepeatProperty.index(colorEtc)
			# 容量
			itemCapacity = dsOzToMl[colorPos]

			# 数量
			itemAmount = str(dsamount[x])
			itemAmount = itemAmount.replace("\n","")
			itemAmount = float(itemAmount)
			itemAmount = int(itemAmount)
			# print(itemAmount)
			# print(type(itemAmount))

			if itemCapacity != "\n":
				itemCapacity = itemCapacity.replace("ML\n","")
				# print(itemCapacity)
				# print(type(itemCapacity))
				itemCapacity = float(itemCapacity)
				itemCapacity = int(itemCapacity)
				divisionPos = itemCapacity//100
				divisionAmountListBowl[divisionPos] += itemAmount
	for x in range(len(divisionAmountList)):

		print("卖出的"+str(x*100)+"ML--"+str(x*100+99)+"ML杯子的数量是： "+str(divisionAmountList[x]))
	print("")
	print("")
	for x in range(len(divisionAmountListBowl)):

		print("卖出的"+str(x*100)+"ML--"+str(x*100+99)+"ML碗的数量是： "+str(divisionAmountListBowl[x]))
					
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

def dsMaterial():
	dsNoRepeat = readtxt("dsNoRepeat.txt")
	print("dsNoRepeat: "+str(len(dsNoRepeat)))

	materialInfo = extractMaterialInfo(dsNoRepeat)
	print(len(materialInfo))
	writeTxt(materialInfo,"materialInfo.txt")


	# provinces
def dsProvinces():
	# provinces12 = xls2listType2("2014年1-2月订单报表.xls",13)
	# provinces34 = xls2listType2("2014年3-4月订单报表.xls",13)
	# provinces5_12 = xls2listType2("2014年5月-12月订单报表.xls",13)
	# provinces1_9 = xls2listType2("2015年1-9月订单报表.xls",13)
	# provinces10_9 = xls2listType2("2015年10-2016年9月订单列表.xls",13)
	# provinces10_7 = xls2listType2("2016年10月-2017年7月20日订单报表.xls",13)
	# provinces = provinces12 + provinces34 + provinces5_12 + provinces1_9 + provinces10_9 + provinces10_7
	# print("provinces: "+str(len(provinces)))
	# dsNoRepeatAddress = filterList2list(provinces)
	# print("dsNoRepeatAddress: "+str(len(dsNoRepeatAddress)))
	# writeTxt(dsNoRepeatAddress,"dsNoRepeatAddress.txt")

	dsNoRepeatAddress = readtxt("dsNoRepeatAddress.txt")
	print(len(dsNoRepeatAddress))
	# 提取省
	# provincesAddress = extractProvinces(dsNoRepeatAddress)
	# writeTxt(provincesAddress,"provincesAddress.txt")
	# 提取市
	# cityAddress = extractCity(dsNoRepeatAddress)
	# writeTxt(cityAddress,"cityAddress.txt")

	# 提取县、区、市级县
	countyAddress = extractCounty(dsNoRepeatAddress)
	writeTxt(countyAddress,"countyAddress.txt")


def extractProvinces(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>(上海|北京|天津|重庆|广西壮族自治区|新疆维吾尔自治区|内蒙古自治区|西藏自治区))"
		s2 = "(?P<capacity>[\u4e00-\u9fa5]{2,3}省)"
		# s3 = "(?P<capacity>牛皮)"
		# s4 = "(?P<capacity>瓦楞)"
		# s5 = "(?P<capacity>(纸杯[^盖]))"
		# s6 = "(?P<capacity>(筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒))" # 第六个采用了不太一样的方法
		# s7 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		# matchResult3 = re.search(s3, tempStr)
		# matchResult4 = re.search(s4, tempStr)
		# matchResult5 = re.search(s5, tempStr)
		# matchResult6 = re.search(s6, tempStr)
		# matchResult7 = re.search(s7, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append(matchResult.group("capacity"))
		elif matchResult2:
			resultList.append(matchResult2.group("capacity"))
		# elif matchResult3:
		# 	resultList.append("牛皮纸")
		# elif matchResult4:
		# 	resultList.append("瓦楞纸")
		# elif matchResult5:
		# 	resultList.append("纸杯")
		# elif matchResult6:
		# 	resultList.append(matchResult6.group("capacity"))
		# elif matchResult7:
		# 	resultList.append("饭盒")
		else:
			resultList.append("")
	return resultList

def extractCity(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "(?P<capacity>[\u4e00-\u9fa5]{2,3}市)"
		s2 = "(?P<capacity>[\u4e00-\u9fa5]{2,7}自治州)"
		s3 = "(?P<capacity>(阿克苏地区|神农架林区))"
		s4 = "(?P<capacity>[\u4e00-\u9fa5]{2,5}盟)"
		# s5 = "(?P<capacity>(纸杯[^盖]))"
		# s6 = "(?P<capacity>(筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒))" # 第六个采用了不太一样的方法
		# s7 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		matchResult3 = re.search(s3, tempStr)
		matchResult4 = re.search(s4, tempStr)
		# matchResult5 = re.search(s5, tempStr)
		# matchResult6 = re.search(s6, tempStr)
		# matchResult7 = re.search(s7, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append(matchResult.group("capacity"))
		elif matchResult2:
			resultList.append(matchResult2.group("capacity"))
		elif matchResult3:
			resultList.append(matchResult3.group("capacity"))
		elif matchResult4:
			resultList.append(matchResult4.group("capacity"))
		# elif matchResult5:
		# 	resultList.append("纸杯")
		# elif matchResult6:
		# 	resultList.append(matchResult6.group("capacity"))
		# elif matchResult7:
		# 	resultList.append("饭盒")
		else:
			resultList.append("")
	return resultList
def extractCounty(inputlist):#传入列表，返回地址列表
	resultList = []
	for x in range(len(inputlist)):
		tempStr = inputlist[x]
		s = "\ (?P<capacity>[\u4e00-\u9fa5]{1,3}县)"
		s2 = "\ (?P<capacity>[\u4e00-\u9fa5]{1,3}区)"
		# s3 = "(?P<capacity>(阿克苏地区|神农架林区))"
		# s4 = "(?P<capacity>[\u4e00-\u9fa5]{2,5}盟)"
		# s5 = "(?P<capacity>(纸杯[^盖]))"
		# s6 = "(?P<capacity>(筷|打包桶|卷纸|纸袋|餐巾纸|打包袋|垃圾袋|清洁袋|手套|纸盘|补邮费|优惠券|优惠劵|餐叉|餐刀|保鲜膜|保鲜袋|桌布|料理棒|定制产品|棉签|牙签|外卖盒))" # 第六个采用了不太一样的方法
		# s7 = "(?P<capacity>(餐盒|饭盒))"

		matchResult = re.search(s, tempStr)
		matchResult2 = re.search(s2, tempStr)
		# matchResult3 = re.search(s3, tempStr)
		# matchResult4 = re.search(s4, tempStr)
		# matchResult5 = re.search(s5, tempStr)
		# matchResult6 = re.search(s6, tempStr)
		# matchResult7 = re.search(s7, tempStr)
		# matchResult2 = re.search(s2, tempStr)
		if matchResult:
			resultList.append(matchResult.group("capacity"))
		elif matchResult2:
			resultList.append(matchResult2.group("capacity"))
		# elif matchResult3:
		# 	resultList.append(matchResult3.group("capacity"))
		# elif matchResult4:
		# 	resultList.append(matchResult4.group("capacity"))
		# elif matchResult5:
		# 	resultList.append("纸杯")
		# elif matchResult6:
		# 	resultList.append(matchResult6.group("capacity"))
		# elif matchResult7:
		# 	resultList.append("饭盒")
		else:
			resultList.append("")
	return resultList


def dsProvincesType2():
	# provinces12 = xls2listType2("2014年1-2月订单报表.xls",13)
	# provinces34 = xls2listType2("2014年3-4月订单报表.xls",13)
	# provinces5_12 = xls2listType2("2014年5月-12月订单报表.xls",13)
	# provinces1_9 = xls2listType2("2015年1-9月订单报表.xls",13)
	# provinces10_9 = xls2listType2("2015年10-2016年9月订单列表.xls",13)
	# provinces10_7 = xls2listType2("2016年10月-2017年7月20日订单报表.xls",13)
	# provinces = provinces12 + provinces34 + provinces5_12 + provinces1_9 + provinces10_9 + provinces10_7
	# print("provinces: "+str(len(provinces)))
	# dsNoRepeatAddress = filterList2list(provinces)
	# print("dsNoRepeatAddress: "+str(len(dsNoRepeatAddress)))
	# writeTxt(dsNoRepeatAddress,"dsNoRepeatAddress.txt")

	dsNoRepeatAddress = readtxt("dsNoRepeatAddress.txt")
	print(len(dsNoRepeatAddress))
	provincesList=[]
	cityList=[]
	countyList=[]
	for x in range(len(dsNoRepeatAddress)):
		
		tempStr = dsNoRepeatAddress[x].split(" ")
		provincesList.append(tempStr[0])
		cityList.append(tempStr[1])
		countyList.append(tempStr[2])
	writeTxt(provincesList,"provincesList.txt")
	writeTxt(cityList,"cityList.txt")
	writeTxt(countyList,"countyList.txt")
	# 提取省
	# provincesAddress = extractProvinces(dsNoRepeatAddress)
	# writeTxt(provincesAddress,"provincesAddress.txt")
	# 提取市
	# cityAddress = extractCity(dsNoRepeatAddress)
	# writeTxt(cityAddress,"cityAddress.txt")

	
if __name__ == '__main__':
	# dsCupOrBowl()
	# dsOzToMl()
	# question2Stat()
	# dsMaterial()
	# 提取省份
	dsProvincesType2()









