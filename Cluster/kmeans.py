#coding:utf-8
#本程序实现的是使用kmeans聚类的功能

#part one
#use jieba to divide Chinese words

import jieba
import numpy as np

fr = open("sk.txt")
fr_list = fr.read()
dataList = fr_list.split("\n")
data = []
for oneline in dataList:
    data.append(" ".join(jieba.cut(oneline)))

#part two
#feature selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

stop_words = ["，","。","（","）"," 来话人","来话","2017",
        '希望','部门','核实','处理',"认为"," 不合理"]
#将得到的词语转换为词频矩阵
freWord = CountVectorizer(stop_words=stop_words)
#freWord.fit_transform()显示的信息是：
#按行显示，比如(0, 30)	1
#指低0篇文章，用到了词频里的第30号词，在第0篇文章里出现1次
fre = freWord.fit_transform(data[:50])

word = freWord.get_feature_names()
print(repr(word).decode('unicode-escape'))
print(len(word))
#print(fre)
#加入tf-idf
transformer = TfidfTransformer()
#tf-idf和上面的fre是差不多的结果，只不过，频次变成了小数
tfidf = transformer.fit_transform(fre)
#得到权重
#print(tfidf)
weight = tfidf.toarray()
#这一步把权重变成数组了，按词频里的顺序排列，没有的词权重为0
#print(weight)

from sklearn.cluster import KMeans
import numpy as np
kmeans = KMeans(n_clusters=5, random_state=0).fit(weight)
print(kmeans.labels_)
label = kmeans.labels_
print(len(label))
for i in range(5):
	print("")
	print("")
	print("第"+str(i)+"类有：")
	for x in range(len(label)):
		if(label[x]==i):
			print(dataList[x])

#from sklearn.cluster import AffinityPropagation
#ap = AffinityPropagation().fit(weight)
#print(ap.labels_)
#label = ap.labels_
#for i in range(10):
#    print("第"+str(i)+"类有：")
#    for x in range(len(label)):
#        if(label[x]==i):
#            print(dataList[x])

# meanshift 分出来的只有一类，不知道为什么
# from sklearn.preprocessing import StandardScaler
# from sklearn import cluster
# X = StandardScaler().fit_transform(weight)
# print(X)
# bandwidth = cluster.estimate_bandwidth(X)
# ms = cluster.MeanShift(bandwidth=15, bin_seeding=True)
# ms.fit(X)
# print(ms)
# print(ms.labels_)



#不能用
#from sklearn.cluster import DBSCAN
#from sklearn.preprocessing import StandardScaler
#X = StandardScaler().fit_transform(weight)
#db = DBSCAN(eps=0.3, min_samples=10).fit(X)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
#labels = db.labels_
## Number of clusters in labels, ignoring noise if present.
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#print('Estimated number of clusters: %d' % n_clusters_)

#from sklearn.cluster import Birch
#brc = Birch(branching_factor=50, n_clusters=None, threshold=0.5,
#    compute_labels=True)
#brc.fit(weight)
#print(brc.labels_)






