#coding:utf-8
from tgrocery import Grocery

grocery = Grocery('region')
grocery.train('cf_testdata.txt')
grocery.save()