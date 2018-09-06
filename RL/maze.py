#coding:utf-8
'''
洗澡时突发灵感
可以自己写一个迷宫的RL
'''
import numpy as np 
# 创建迷宫
def createMaze():
	
	mazeTable = np.zeros((6,6))
	# print(mazeTable)

	for x in range(6):
		mazeTable[0][x]=mazeTable[5][x]=-1
		mazeTable[x][0]=mazeTable[x][5]=-1

	# print(mazeTable)
	mazeTable[2][2]=mazeTable[3][2]=mazeTable[2][3]=-1
	mazeTable[3][3]=1
	print(mazeTable)
	return mazeTable
# 动作
def actions(action, position):
	if action=="up":
		position[0]=position[0]-1

	if action=="down":
		position[0]=position[0]+1

	if action=="left":
		position[1]=position[1]-1

	if action=="right":
		position[1]=position[1]+1

	return position
# qtable每个点存四个信息
def createQTable():
	qtable=np.zeros((6,6,4))
	qtable[3][3]=1
	# print(qtable)
	return qtable

# 采取动作的策略
def policy(position, mazeTable,qtable):

	chosedAction=-1#0 1 2 3
	# 上下左右
	# 可选区域
	# policyArea=[1,1,1,1]#不可去为0
	
	# if position[0]-1 < 0:
	# 	policyArea[0]=0
	# if position[0]+1 < 0:
	# 	policyArea[1]=0
	# if position[1]-1 < 0:
	# 	policyArea[2]=0
	# if position[1]+1 < 0:
	# 	policyArea[3]=0
	# random_num=np.random.random_sample((4,))
	# for x in xrange(4):
	# 	policyArea[x]policyArea = policyArea[x]*random_num[x]
	# 现在的policy就已经是有权重的了，或者为0
	# 90%的概率选权重最大的10%的概率从权重不是最大的那几个里面随机的选取一个
	# 如果所有的权重都为0，则进行随机选择
	weight=qtable[position[0]][position[1]]==[0,0,0,0]
	if weight[0]==weight[0]==weight[0]==weight[0]==True:
		print("随机选择")
		while True:
			randINT = np.random.random_integers(4)-1
			# 随机选择一个区域，如果这个区域可以走，就返回结果
			empL = position[:]
			# print(empL)
			if (randINT == 0)&(mazeTable[empL[0]-1][empL[1]]>-0.5):
					return randINT
			if (randINT == 1)&(mazeTable[empL[0]+1][empL[1]]>-0.5):
					return randINT
			if (randINT == 2)&(mazeTable[empL[0]][empL[1]-1]>-0.5):
					return randINT
			if (randINT == 3)&(mazeTable[empL[0]][empL[1]+1]>-0.5):
					return randINT

			
		print("选动作出错")
		return chosedAction
		# 以上出来一个选择结果
	elif np.random.random_sample()<0.8:
		print("非随机选择0")
		# 当前位置的权重列表
		valueList = qtable[position[0]][position[1]]
		# 获取列表中最大值
		listMaxValue = np.max(valueList)
		valueListListed = list(valueList)
		pos = valueListListed.index(listMaxValue)
		return pos
	else:
		print("非随机选择1")
		# 从除了最大的那个之外的里面随机选，并且保证是能移动的
		flag=True
		
		valueList = qtable[position[0]][position[1]]
		listMaxValue = np.max(valueList)
		valueListListed = list(valueList)
		pos = valueListListed.index(listMaxValue)
		while flag:
			randINT = np.random.random_integers(4)-1
			if (randINT!=pos)&(qtable[position[0]][position[1]][randINT]!=0.0):
				return randINT
			else:
				return pos
		print("选动作出错2")
		return chosedAction

def policy2(position, mazeTable,qtable):

	chosedAction=-1#0 1 2 3
	
	weight=qtable[position[0]][position[1]]==[0,0,0,0]
	
		# 以上出来一个选择结果
	if np.random.random_sample()<1.1:
		print("非随机选择0")
		# 当前位置的权重列表
		valueList = qtable[position[0]][position[1]]
		# 获取列表中最大值
		listMaxValue = np.max(valueList)
		valueListListed = list(valueList)
		pos = valueListListed.index(listMaxValue)
		return pos
	else:
		print("非随机选择1")
		# 从除了最大的那个之外的里面随机选，并且保证是能移动的
		flag=True
		
		valueList = qtable[position[0]][position[1]]
		listMaxValue = np.max(valueList)
		valueListListed = list(valueList)
		pos = valueListListed.index(listMaxValue)
		while flag:
			randINT = np.random.random_integers(4)-1
			if (randINT!=pos)&(qtable[position[0]][position[1]][randINT]!=0.0):
				return randINT
			else:
				return pos
		print("选动作出错2")
		return chosedAction
			
def updateWeight(position,position_,qtable,chosedAction):
	# if mazeTable[position_[0]][position_[1]]==1.0:
	# 	maxWeight_ = 1.0
		
	# else:
		# maxWeight_ = np.max(qtable[position_[0]][position_[1]])
	# 更新了当前位置，做这个选择的权重
	maxWeight_ = np.max(qtable[position_[0]][position_[1]])
	qtable[position[0]][position[1]][chosedAction] += 0.1*(0.9*maxWeight_ - qtable[position[0]][position[1]][chosedAction])

def computePosition_(position,chosedAction):
	position_=position[:]
	if chosedAction==0:
		position_[0]=position_[0]-1
	elif chosedAction==1:
		position_[0]=position_[0]+1
	elif chosedAction==2:
		position_[1]=position_[1]-1
	else:
		position_[1]=position_[1]+1

	return position_


		



if __name__ == '__main__':
	# 创建迷宫
	mazeTable=createMaze()
	# 创建qtable
	qtable=createQTable()
	# 起始位置
	# position=[1,1]
	# 动作列表
	actionName=["上","下","左","右"]

	for x in range(500):
		position=[1,1]
		
		print("第"+str(x)+"回合")
		for y in range(1000):

			# print("position"+str(position))
			# 选择动作
			chosedAction=policy(position, mazeTable,qtable)
			print("第"+str(y)+"步.  "+"当前位置： "+str(position)+"选择的方向：  向"+actionName[chosedAction])
			
			
			
			# 下一步的地点
			# print("当前位置2： "+str(position))
			position_=computePosition_(position,chosedAction)
			# 更新权重
			# print("position: "+str(position)+"  position_: "+str(position_))
			updateWeight(position,position_,qtable,chosedAction)
			position=position_
			if position==[3,3]:
				break
			print("")
		
		print("")
		print("")

	print(qtable)
	print(mazeTable)
	position=[1,1]
	for y in range(1000):

		# print("position"+str(position))
		# 选择动作
		chosedAction=policy2(position, mazeTable,qtable)
		print("第"+str(y)+"步.  "+"当前位置： "+str(position)+"选择的方向：  向"+actionName[chosedAction])
		
		
		
		# 下一步的地点
		# print("当前位置2： "+str(position))
		position_=computePosition_(position,chosedAction)
		# 更新权重
		# print("position: "+str(position)+"  position_: "+str(position_))
		# updateWeight(position,position_,qtable,chosedAction)
		position=position_
		if position==[3,3]:
			break
		print("")
		
		
#其实可以先把价值矩阵写为一个空的
#等它能正确运行以后再考虑价值矩阵的迭代更新

	



