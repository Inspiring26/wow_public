#coding:utf-8
from tgrocery import Grocery


grocery = Grocery('region')
grocery.train('taggeddata.txt')
grocery.save()

print("模型保存成功")


new_grocery = Grocery('region')
new_grocery.load()
teststr = "来话人反映当地政府在金牛区金房苑横街81号设立分类垃圾站，反映：1、垃圾桶入口处有隔板，但口径过小，市民投放垃圾时存在不便；2、之前通知可以回收任何垃圾，但近期又被告知只回收旧衣服，认为不合理。希望部门协调加强管理。"
print(new_grocery.predict(teststr))

# 测试准确率
#new_grocery = Grocery('region')
#new_grocery.load()
print(new_grocery.test("taggeddata2.txt"))
