

def __cut_DAG(sentence):
	N = len(sentence)
	i,j=0,0
	p = trie
	DAG = {}
	while i<N:
		c = sentence[j]
		if c in p:
			p = p[c]
			if '' in p:
				if not i in DAG:
					DAG[i]=[]
				DAG[i].append(j)
			j+=1
			if j>=N:
				i+=1
				j=i
				p=trie
		else:
			p = trie
			i+=1
			j=i
	for i in range(len(sentence)):
		if not i in DAG:
			DAG[i] =[i]
	#pprint.pprint(DAG)
	route ={}
	calc(sentence,DAG,0,route=route)
	x = 0
	buf =u''
	while x<N:
		y = route[x][1]+1
		l_word = sentence[x:y]
		if y-x==1:
			buf+= l_word
		else:
			if len(buf)>0:
				if len(buf)==1:
					yield buf
					buf=u''
				else:
					regognized = finalseg.cut(buf)
					for t in regognized:
						yield t
					buf=u''
			yield l_word		
		x =y

	if len(buf)>0:
		if len(buf)==1:
			yield buf
		else:
			regognized = finalseg.cut(buf)
			for t in regognized:
				yield t

def calc(sentence,DAG,idx,route):
	if idx in route:
		return route[idx]
	if idx>=len(sentence):
		return (1.0,'')
	next = DAG[idx]
	best = max([ ( FREQ.get(sentence[idx:x+1],min_freq) * calc(sentence,DAG,x+1,route=route)[0],x )for x in next ])
	route[idx]=best
	return best

if __name__ == '__main__':
	trie = {'河': {'南': {'潢': {'川': {'': ''}}, '周': {'口': {'': ''}}, '郑': {'州': {'': ''}}}}, '北': {'京': {'': '', '动': {'物': {'园': {'': ''}}}, '天': {'安': {'门': {'': ''}}}}}, '动': {'物': {'园': {'': ''}}}, '天': {'安': {'门': {'': ''}}}}
	outp = __cut_DAG("河南潢川")
	for x in outp:
		print(x)





