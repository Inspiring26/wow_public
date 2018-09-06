#coding:utf-8

def gentree():
	tree={}
	for line in open("dict.txt"):
		word,freq = line.split(" ")

		p=tree
		for c in word:
			if c not in p:
				p[c]={}
			p=p[c]#移动光标，1.如果c不在p中的话，存入、移动光标 2.如果在的话，移动光标继续判断
		p[""]=""#一定还有其他的方法
	return tree
print(gentree())

#{'河': {'南': {'潢': {'川': {'': ''}}, '周': {'口': {'': ''}}, '郑': {'州': {'': ''}}}}, '北': {'京': {'': '', '动': {'物': {'园': {'': ''}}}, '天': {'安': {'门': {'': ''}}}}}, '动': {'物': {'园': {'': ''}}}, '天': {'安': {'门': {'': ''}}}}
trie=gentree()
stra = "河南省潢川县"
for word in stra:
	N=len(stra)
	p = trie
	i,j=0,0
	if word in p:
		p = p[word]
		if '' in p:
			print(stra[i:j])
		j+=1
		if j>N:
			i+=1
			j=i
	
			
