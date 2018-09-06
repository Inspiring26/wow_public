#coding:utf-8

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from scipy.misc import imread
import numpy as np
from PIL import Image
import matplotlib.image as im
import json
import jieba
# import jieba.analyse

def text2wordcloud(text,bg_pic,font,stop_words):#传入的需是unicode类型字符串
	
	#读取文件、字体、形状图
	# d = path.dirname(__file__)#获取路径
	# font=path.join(d, "DroidSansFallbackFull.ttf")#生成字体路径
	# bg_pic = imread('disney.png')#读取图片
	# text = open(path.join(d, 'idf.txt')).read().decode('utf-8')#内容转换为utf8编码的字符串

	# print(type(text))
	#对字符串进行处理，自己统计词频


	# str1 = "成华区	 来话人反映161122T00028相同问题，\
	# 	建设路56号在建的地铁口，在11月21日施工至深夜，噪音扰民。\
	# 	来话人再次来电称噪音问题未得到解决，希望部门调查处理。"
	

	#jieba分词没有停用词功能，
	#只有在关键词抽取时可以用停用词
	#于是，我打算先自己写，然后用关键词抽取方式来进行这一步
	#jieba.analyse.set_stop_words("/Users/huangyong/Downloads/stop_words.txt")

	#停用词表
	seg_list = jieba.cut(text,cut_all = False)
	list1 = []
	#读迭代还是用循环吧，不用next()
	for x in seg_list:
		if x not in stop_words:
			list1.append(x)

	wordcount = {}
	total = 0
	for x in xrange(len(list1)):
		if list1[x] in wordcount.keys():
			wordcount[list1[x]] = wordcount[list1[x]]+1
		else:
			wordcount[list1[x]] = 1

		total += 1

	# print(total)
	sort=sorted(wordcount.items(),key=lambda e:e[1],reverse=True)#按键值排序
	#此时sort的类型时list
	#可以截取前50个

	sort = sort[:200]#unicode类型 
	wc_dict = dict(sort)#unicode类型
	# txtFreq = {'中国': 100,'四川': 50,'成都':90}
	# txtFreq = json.dumps(txtFreq, encoding="utf-8")
	# txtFreq = json.loads(txtFreq)
	# print("wc_dict:")
	# print(type(wc_dict))
	# print(wc_dict)
	# print("txtFreq:")
	# print(type(txtFreq))
	# print(txtFreq)

	#调用wordcloud
	wc = WordCloud(font_path=font,max_font_size=100,
		mask=bg_pic,background_color='white')
	# wordcloud.generate_from_frequencies(wc_dict)
	# wordcount = json.dumps(wordcount, encoding="utf-8")
	# wordcount = json.loads(wordcount)
	# wc = WordCloud(font_path=font,max_font_size=100)
	wc.generate_from_frequencies(wc_dict) 
	#显示
	plt.figure(figsize=(8,8))#大小
	plt.imshow(wc)#内容
	plt.axis("off")#去掉刻度
	# plt.savefig('test18.png')
	plt.show()#显示




if __name__ == '__main__':
	#读取文件、字体、形状图
	d = path.dirname(__file__)#获取路径
	font=path.join(d, "DroidSansFallbackFull.ttf")#生成字体路径
	#读取图片
	bg_pic = np.array(Image.open("cd1.png"))
	
	text = open(path.join(d, 'idf.txt')).read()#内容转换为utf8编码的字符串

	stop_words = [u"，",u"。",u' ',u'\t',u'来话',u'反映',u'人',u'的',u'请',u'在',u'号'
		,u'（',u'）',u'(',u')',u':',u'：',u'"',u'“',u'\n',u'6',
		u'00',u'25',u'24',u'5',u'2',u'3',u'8',u'&',u'4',u'、',u'1',
		u'20',u'30',u'部门',u'来电',u'相关',u'希望',u'问题',u'年',u'月']
	

	#传入字符串需是utf-8或者unicode
	text2wordcloud(text,bg_pic,font,stop_words)





