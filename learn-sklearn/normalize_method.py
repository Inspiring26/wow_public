#归一化处理
from sklearn import preprocessing
a=[3/4,1/8,1/441,56/3,252]
b = preprocessing.normalize(a)
print(b)
