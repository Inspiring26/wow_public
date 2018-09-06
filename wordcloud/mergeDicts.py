#coding:utf8
import createDict as cd

if __name__ == '__main__':
	undealedList=cd.txt2list("longGoalList.txt")
	undealedList2=cd.txt2list("OnlyAddressList.txt")
	newUndealedList = undealedList + undealedList2
	print(len(newUndealedList))
	dictList = cd.filterList2list(newUndealedList)
	print(len(dictList))
	cd.writeTxtNOTNewline(dictList,"OnlyAddressList.txt")