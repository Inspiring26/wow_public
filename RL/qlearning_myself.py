#coding:utf-8
import numpy as np
import pandas as pd

ACTIONS = ['left', 'right'] 

table = pd.DataFrame(np.zeros((6,2)),columns = ['left', 'right'])
# print(table)
def choose_action(S, table):
	if (np.random.uniform() > 0.9) or (table.loc[S,'left']==table.loc[S,'right']):
		action = np.random.choice(ACTIONS)
		print("action1: "+str(action))
	else:
		if table.loc[S,'left'] > table.loc[S,'right']:

			action = ACTIONS[0]
		else:
			action = ACTIONS[1]
		print("action2: "+str(action))
	return action

# # A是当前的位置 宝藏在第6个位置，也就是说坐标是5
# A = action
# S = 0
# # 如果此时在宝藏的旁边，并且动作是向右，则获得一个奖励1
def feedback(S, A):# 根据位置和动作，进行奖励返回，和下一步的位置返回
	if A == "right" :
		if S == 4:
			S_ = 'gold'
			R = 1
		else:
			S_ = S + 1
			R = 0
	else:
		R = 0
		if S == 0:
			S_ = 0
		else:
			S_ = S -1
	return S_, R

	

# print("S_: "+str(S_))
# print("R: "+str(R))


# # 在终端下不断显示所处状态
# print("")
# 在终端下不断显示所处状态 end

# 主控制程序
# qpredict = table.ix[S,A]
# print("S: "+str(S))
# print("A: "+str(A))
# print(qpredict)
# print(table.loc[S_, :].max())
# R = 1
# if S_ != 'gold':
# 	qtarget = R + 0.9*table.loc[S_, :].max()
# else:
# 	qtarget = R
# 	is_terminated = True
# table.ix[S, A] += 0.1*(qtarget - qpredict)

# print("")
# print(table)


def rl():
	for x in range(1,10):
		print("第"+str(x)+"代：")
		# 每一代开始，位置要设置为0
		S = 0
		counter = 0

		is_terminated = False
		while not is_terminated:
			print("S: "+str(S))
			A = choose_action(S, table)
			S_, R = feedback(S, A)
			qnow = table.ix[S,A] # qpredict是当前的，qtarget是下一个的
			if S_ != 'gold':
				qnext = R + 0.9*table.loc[S_, :].max() # 参考下一步的数据
			else:
				qnext = R
				is_terminated = True

			table.ix[S, A] += 0.1*(qnext - qnow)
			S = S_
			counter += 1

		print("counter: "+str(counter))
		print(table)

	


rl()


env_list = ["-"]*5 +["T"]
env_list[2] = 'o'
interaction = ''.join(env_list)
print('\r{}'.format(interaction), end='')#其中'{}'是占位符
env_list = ["-"]*5 +["T"]
env_list[3] = 'o'
interaction = ''.join(env_list)
print('\r{}'.format(interaction), end='')

























