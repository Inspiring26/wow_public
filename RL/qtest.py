#coding:utf-8
import time
for x in range(1,10):
	line = ['-']*10
	line[x%10] = 'o'
	str1 = ''.join(line)
	print('\r{}'.format(str1),end='')
	time.sleep(1)
print('\r          ',end='')# 这个的空格长度必须和上面的列表长度一样或多于，才能覆盖。我测试了
print("")# 这一句是为了换行显示