#coding:utf-8
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### cteate tensorflow structure start ###
# 这两步是在随机生成第一个参数，把初始偏差设为0
# 但是必须用tf.Variable tf.函数 的方式生成
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

# 要处理的表达式
y = Weights*x_data + biases

# 计算平方差的公式，要用tf.函数 表示
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)#优化器。参数是学习效率，一般是一个小于1的数
train = optimizer.minimize(loss)# 一个优化器 一个训练表达式

init =  tf.initialize_all_variables()#初始化的固定表达式
### cteate tensorflow structure end ###

sess = tf.Session()
sess.run(init) #激活 init

#开始让神经网络一步步训练
for step in xrange(201):
	sess.run(train)
	if step % 20 == 0:
		print(step,sess.run(Weights),sess.run(biases))