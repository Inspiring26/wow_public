import math
import jieba
import jieba.posseg as psg
from gensim import corpora,models
from jieba import analyse
import functools

# gensim包含多种主题模型算法

def get_stopword_list():
	stop_word_path = './stopword.txt'
	stopword_list = [sw.replace('\n','') for sw in open(stop_word_path).readlines()]
	return stopword_list

# 使用jieba分词获取分词后的list
def seg_to_list(sentence,pos=False):
	if not pos:
		# 使用不标注词性的分词法
		seg_list = jieba.cut(sentence)
	else:
		seg_list = psg.cut(sentence)
	return seg_list

# 去除干扰词
def word_filter(seg_list,pos=False):
	stopword_list = get_stopword_list()
	filter_list = []
	# 根据pos决定是否进行词性过滤
	for seg in seg_list:
		if not pos:
			word = seg
			flag = 'n'
		else:
			word = seg.word
			flag = seg.flag
		# not word in 等价于 word not in 
		if not word in stopword_list and len(word)>1:
			filter_list.append(word)
	return filter_list

# 数据加载
def load_data(pos=False,corpus_path='./corpus.txt'):
	doc_list = []
	for line in open(corpus_path,'r'):
		content = line.strip()
		seg_list = seg_to_list(content,pos)
		filter_list = word_filter(seg_list,pos)
		doc_list.append(filter_list)
	return doc_list

# idf值统计方法
def train_idf(doc_list):
	idf_dic = {}
	# 总文档数
	tt_count = len(doc_list)

	# 每个词出现的文档数
	for doc in doc_list:
		for word in set(doc):
			idf_dic[word] = idf_dic.get(word,0.0) + 1.0

	# 按公式转化成idf值，分母加1进行平滑处理
	for k,v in idf_dic.items():
		idf_dic[k]=math.log(tt_count/(1.0+v))

	# 对于没有在字典中的词，默认其尽在一个文档出现，得到默认idf值
	default_idf = math.log(tt_count/(1.0))
	return idf_dic,default_idf

def train_lsi(self):
	lsi = models.LsiModel(sel.corpus_tfidf,id2word=self.dictionary,num_topics=sel.num_topics)
	return lsi

def train_lda(self):
	pass





















