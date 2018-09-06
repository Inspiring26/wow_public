#coding:utf-8
from tgrocery import Grocery

new_grocery = Grocery('region')
new_grocery.load()
print new_grocery.test("cf_testdata.txt")