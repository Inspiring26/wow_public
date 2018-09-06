#coding:utf-8

from wordcloud import WordCloud
from os import path
import json

# 读excel
import xlrd
data = xlrd.open_workbook('sep.xls')
table = data.sheets()[0]
nrows = table.nrows
total = 0
wordcount = {}
for i in range(nrows):
	cell_A1 = table.cell(i,3).value
	# print(cell_A1)
	if cell_A1.encode('utf-8')=="公交车、出租车管理":
		cell_A0 = table.cell(i,0).value
		cell_A0 = cell_A0.encode('utf-8') 
		if cell_A0 in wordcount.keys():
			# print(cell_A0)
			wordcount[cell_A0] = wordcount[cell_A0]+1 
		else:
			wordcount[cell_A0] = 1



		total += 1

print(total)
import chardet
print(wordcount)
# print(chardet.detect(wordcount))
wordcount = json.dumps(wordcount, encoding="utf-8")
print(wordcount)
print(chardet.detect(wordcount))
wordcount = json.loads(wordcount)
wordcount = json.dumps(wordcount, encoding="utf-8")
print(chardet.detect(wordcount))
wordcount = json.loads(wordcount)
# print(repr(wordcount).decode('unicode-escape'))
	



d = path.dirname(__file__)
font=path.join(d, "DroidSansFallbackFull.ttf")

import matplotlib.pyplot as plt
txtFreq = {'中国': 100,'四川': 50,'成都':10}
txtFreq = json.dumps(txtFreq, encoding="utf-8")
print(chardet.detect(txtFreq))
txtFreq = json.loads(txtFreq)

wc = WordCloud(font_path=font,max_font_size=40)

wc.generate_from_frequencies(wordcount) 

# 生成图片  

plt.imshow(wc)
#去掉坐标显示
plt.axis("off")
plt.show()
