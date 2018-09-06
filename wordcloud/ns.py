#coding:utf-8
import jieba.posseg as pseg
import jieba

sentence = "来话人2017年6月24日23：40在武侯区兆景路508号中铁骑士公馆乘坐车牌为川ATN685的出租车前往成华区昭觉寺南路金科一城（6月25日00:28下车），打表支付73元.但以前乘坐相同路线支付65元。来话人认为司机手动调节计价器。希望 部门核实处理。"

# jieba.suggest_freq(('金科一城'), True)
words = pseg.cut(sentence)
for w in words:
	if w.flag in ['ns','nr','nrt','nz']:
		print(w.word.encode("utf-8"))

