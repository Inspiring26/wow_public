#coding:utf-8
import os

_curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) )  )
print(_curpath)

def gen_trie():
	trie = {}
	for line in open("dict.txt"):
		word,freq = line.strip().split(" ")
		
		p = trie
		for c in word:
			if not c in p:
				p[c] ={}
			p = p[c]
		p['']='' #ending flag
	return trie


trie = gen_trie()
print(trie)
sentence="河南潢川在楚地"

mytrie = {'河': {'南': {'潢': {'川': {'': ''}}}}}
print("故" in trie)
N = len(sentence)
i,j=0,0
p=mytrie
while i<N:
	c = sentence[j]
	if c in p:
		p = p[c]
		if "" in p:
			print(sentence[i:j+1])
			break;
		j+=1



def __cut(sentence):
	N = len(sentence)
	i,j=0,0
	p = trie
	while i<N:
		c = sentence[j]
		# print(c)
		# print(p)
		if c in p:
			p = p[c]
			if '' in p:
				print(sentence[i:j+1])
				# yield sentence[i:j+1]
			j+=1
			if j>=N:
				i+=1
				j=i
		else:
			p = trie
			i+=1
			j=i


__cut(sentence)




