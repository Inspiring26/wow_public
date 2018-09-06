#coding:utf-8

import numpy as np#numpy真的很有用，哈哈哈
import heapq
import pandas as pd
from sklearn import cross_validation as cv
import matplotlib.pyplot as plt
from qxlist import xls2list
from qxlist import df_format

# 计算相似度
# 使用sklearn的pairwise_distances函数来计算余弦相似性
from sklearn.metrics.pairwise import pairwise_distances

#把这个功能做成一个可复用的函数
#它的作用就是把文字转换为数字id
def text2num(textlist):
	listlen = len(textlist)
	subnum = 1
	tittledict = {}
	for x in xrange(listlen):
		data = textlist[x]
		if data not in tittledict.keys():
			tittledict[data] = subnum
			subnum += 1
	key_list = []
	value_list = []
	for key,value in tittledict.items():
		key_list.append(key)
		value_list.append(value)
	return [tittledict,key_list,value_list]

def input2numlist(inputip="10.160.170.28",id=119):
	header = [ 'item_id','user_id']
	# df = pd.read_csv('qx.data', sep='\t', names=header)
	# 把获取的数据组装成pandas
	list0,list1 = xls2list("log.xls")
	df = df_format(list0,list1)
	print(df)
	len_df = len(df)
	n_users = df.user_id.unique().shape[0]
	n_items = df.item_id.unique().shape[0]
	train_data_matrix = np.zeros((len_df, 2))
	item_id_list = []
	user_id_list = []
	#这个pandas需要通过这种for循环来读
	for line in df.itertuples():
		
		item_id_list.append(line[1])
		user_id_list.append(line[2])

	
	item_id_dict = text2num(item_id_list)[0]
	item_id_dict_keylist = text2num(item_id_list)[1]
	item_id_dict_valuelist = text2num(item_id_list)[2]

	user_id_dict = text2num(user_id_list)[0]
	user_id_dict_keylist = text2num(user_id_list)[1]
	user_id_dict_valuelist = text2num(user_id_list)[2]
	
	# 根据输入ip，显示指定的这个ip的推荐信息
	inputip_unicode = inputip.decode("gbk")
	id = user_id_dict[inputip_unicode]
	
	dict_i = 0
	for line in df.itertuples():
		temp = item_id_dict.get(line[1])
		temp2 = user_id_dict.get(line[2])
		# 调整为第一列是用户，第二列是"物品"
		train_data_matrix[dict_i,1] = int(temp)
		train_data_matrix[dict_i,0] = int(temp2)

		dict_i += 1
	
	# 用户-商品 为坐标轴 所有的对应信息表
	big_matrix = np.zeros((n_users, n_items))#n_users: 31 n_items: 488, 新的数据源，这个不对
	print("n_users"+str(n_users))
	print("n_items"+str(n_items))
	#n_users217 n_items823

	for x in xrange(len(train_data_matrix)):
		col = train_data_matrix[x]
		# print(col)
		# print(int(col[0]-1))
		temp = big_matrix[int(col[0]-1),int(col[1]-1)]
		big_matrix[int(col[0]-1),int(col[1]-1)] = temp + 1
		# 下面这句话，打印的是已经有权重的词
		# print(big_matrix[int(col[0]-1),int(col[1]-1)])
		
	# print(big_matrix)
	user_similarity = pairwise_distances(big_matrix, metric='cosine')
	print(user_similarity[id])
	for x in xrange(len(user_similarity[id])):
		if user_similarity[id][x]==1.0:
			user_similarity[id][x]=0.0
		
	# print(user_similarity[id])
	list2 = heapq.nlargest(30, range(len(user_similarity[id])), user_similarity[id].__getitem__)
	# print("user_similarity[id]"+str(len(user_similarity)))
	# print("list2"+str(list2))

	likelist = np.zeros((1,n_items))#为了不处理下标，直接按商品个数来组建数组
	likelist = likelist[0]#因为np生成的是两层方括号的，比如[[ 0.  0.  0. 0.  0. 0.]]
	# print(likelist)
	
	for x in xrange(len(list2)): # x是用户坐标x
		uid = int(list2[x])
		for y in xrange(n_items): # y是商品坐标y
			# 把和用户相似的这20个用户（记作v）, 每一个做如下处理
			# 把v对物品y的好感度乘以和用户u的好感度，加到likelist[y]
			# v对物品y的好感度：big_matrix
			# v对用户u的好感度：user_similarity
			if user_similarity[id,uid] < 1:
				likelist[y] += user_similarity[id,uid]*big_matrix[uid,y]

	# print(likelist) #查看喜爱列表
	
	
	favorite = heapq.nlargest(10, range(len(likelist)), likelist.__getitem__)
	favorite_item_name = []

	print("编号2用户最值得推荐的5个链接的编号："+str(favorite))
	print("")
	print("")
	print("链接名及权重如下：")
	print("")
	# 添加num，if，beak等是为了过滤掉无用关键字后，依然输出前五个内容
	num=1
	for x in xrange(1,len(favorite)):
		pos = item_id_dict_valuelist.index(favorite[x])
		favorite_item_name.append(item_id_dict_keylist[pos])
		if item_id_dict_keylist[pos] not in ('text',u'首页',u'\n\t\t\t\t\t\t\t登录\n\t\t\t\t\t\t'):
			
			print(item_id_dict_keylist[pos])
			print(likelist[favorite[x]])
			if num==5:
				break
			num +=1
	

	
	print("")
	print("")

	# 可视化一下
	likelistpd = pd.Series(likelist)
	likelistpd.plot()
	plt.show()
	
	return user_similarity





if __name__ == '__main__':
	user_similarity = input2numlist("10.158.46.179")
	


	
	

	

