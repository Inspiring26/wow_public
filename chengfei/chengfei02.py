#coding:utf-8
import re
def readtxt(filename):
	f = open(filename)
	line = f.readline()
	inputlist = []
	s="\n"
	while line:
		inputlist.append(line.replace(s,""))
		line = f.readline()

	return inputlist
def oneList2twoList(inlist):
	list_one = []
	list_two = []
	for x in range(len(inlist)):
		temp_list = inlist[x].split(" ")
		list_one.append(temp_list[0])
		list_two.append(temp_list[1])
	return list_one,list_two
def slove_way(inlist1, inlist2, toSlovedList):
	return_list = []
	for x in range(len(toSlovedList)):
		pos = inlist1.index(toSlovedList[x])
		return_list.append(inlist2[pos])

	return return_list
def writeTxt(inlist, filename):
	fwrite = open(filename,"w")
	s="\n"
	for x in xrange(len(inlist)):
		matchResult = re.search(s, inlist[x])
		if matchResult:
			fwrite.write(inlist[x])
		else:
			fwrite.write(inlist[x]+"\n")
	fwrite.close
if __name__ == '__main__':
	issue_slove = readtxt("issue_slove.txt")
	in_data = readtxt("in_data.txt")
	
	list_one,list_two = oneList2twoList(issue_slove)
	
	out_data = slove_way(list_one,list_two,in_data)
	print("输入信息：")
	print(in_data)
	print("输出方案：")
	print(out_data)
	writeTxt(out_data,"out_data.txt")
