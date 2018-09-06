#coding:utf-8
#获取文本，存为列表
import jieba
fr = open('svc.txt')
fr_list = fr.read()
dataList = fr_list.split('\n')
data = []
for oneline in dataList:
	data.append(" ".join(jieba.cut(oneline)))

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(stop_words=["，","。","（","）"],max_features=10)
X = vectorizer.fit_transform(data)
#查看选取的特征
print ("选取的特征:")
print (repr(vectorizer.get_feature_names()).decode('unicode-escape'))
print ("训练集的向量:")
print X.toarray()[-1:]
X_data = X.toarray()

# from sklearn.feature_extraction.text import TfidfTransformer
# transformer = TfidfTransformer(smooth_idf=False)
# tfidf = transformer.fit_transform(X)
# print tfidf.toarray()

from sklearn.svm import LinearSVC
clf = LinearSVC()
# clf.fit(X_data[:9], [0,0,0,1,1,1,2,2,2])
clf.fit(X_data[:9], [u"环境保护",u"环境保护",u"环境保护",u"交通管理",u"交通管理",u"交通管理",u"城市管理",u"城市管理",u"城市管理"])
print ("拟合的系数:")
print(clf.coef_)
print ("拟合的常数项:")
print(clf.intercept_)


print(repr(clf.predict(X_data[-1:])).decode('unicode-escape'))
# print X2.toarray()
# X2_data = X2.toarray()
# print(clf.predict(X2_data))


