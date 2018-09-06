#coding:utf-8
from tgrocery import Grocery
import numpy as np
import pandas as pd 


df = pd.read_excel("测试数据1.xls")
print(df)
print(len(df))

# grocery = Grocery('region')
# grocery.train('region_1.txt')
# grocery.save()




# 测试准确率
#new_grocery = Grocery('region')
#new_grocery.load()
#print new_grocery.test("区域-内容_2.txt")
