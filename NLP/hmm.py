# 用pyhton实现hmm，并把它封装成一个类
class HMM(object):
	"""docstring for HMM"""
	# 初始化一些全局信息，初始化一些成员变量
	def __init__(self):
		import os
		# 主要用于存取算法中间结果，不用每次都训练模型
		self.model_file = './data/hmm_model.pkl'

		# 状态值集合
		self.state_list = ['B','M','E','S']

		# 加载参数，用于判断是否需要加载model_file
		self.load_para = False

	# 接收一个参数，用于判断是否加载中间文件结果
	# 当需要重新训练时，需初始化清空结果
	def try_load_model(self,trained):
		if trained:
			import pickle
			with open(self.model_file,'rb') as f:
				self.A_dic = pickle.load(f)
				self.B_dic = pickle.load(f)
				self.Pi_dic = pickle.load(f)
				self.load_para = True
		else:
			# 
	def train(self,path):
		pass
	def viterbi(self,text,states,start_p,trans_p,emit_p):
		pass
	def cut(self,text):
		pass
