#coding:utf-8
import numpy as np
from qxlist import df_format
from qxcf import input2numlist
import sys

def nxqx(fileName="records_2017-10-16.txt",recmdIp="192.168.216.222"):
	
	f = open(fileName)
	line = f.readline()
	rowNumber = 1
	inputlist = []
	print("读取数据")
	while line:
		inputlist.append(line)
		line = f.readline()
		rowNumber += 1

	print("读数据完成")
	# print(inputlist)
	mainList = []
	for x in xrange(len(inputlist)):
		tempArray = inputlist[x]
		splittedArray = tempArray.split(",")
		# print(splittedArray)
		mainList.append(splittedArray)

		# print(splittedArray)
		# mainArray = np.append(mainArray,[splittedArray])


	# print(mainList)
	print(len(mainList))
	print(len(mainList[0]))
	# print(mainList[0])
	item_id = []
	user_id = []
	item_link = []

	for x in xrange(len(mainList)):
		if mainList[x][0].decode("utf-8") == u"basic":
			
			item_id.append(mainList[x][2])
			user_id.append(mainList[x][6])
			item_link.append(mainList[x][3])

	# print(item_id)
	# print(len(item_id))
	# print(len(user_id))
	# print(len(item_link))
	recmdList = input2numlist(item_id,user_id,recmdIp)
	# print(recmdList)
	recmdLinkList = []
	for x in xrange(len(recmdList)):
		pos = item_id.index(recmdList[x])
		# print(pos)
		recmdLinkList.append(item_link[pos])


	# print(recmdLinkList)
	return recmdList,recmdLinkList

if __name__ == '__main__':
	fileName = sys.argv[1]
	recmdIp = sys.argv[2]
	print(fileName,recmdIp)
	recmdList,recmdLinkList=nxqx()
	fwrite = file("result.txt","a+")
	for x in xrange(len(recmdList)):
		tempStr = str(recmdList[x]) + "," +str(recmdLinkList[x]) + "\n"
		fwrite.write(tempStr)
	fwrite.close()













