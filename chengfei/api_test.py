
'''
os.system("curl -i -H \"Content-Type: application/json\" -X PUT -d '{\"question\":\"来话人是成龙大道蓝润锦江春天小区的业主，反映小区8栋附近有一垃圾处理厂，经常在深夜处理垃圾，机器产生严重噪音，请处理。\"}' http://172.18.0.171:8000/todo/api/v1.0/tasks/1")
'''
import time
t1 = time.time()
for x in xrange(1000):
	os.system("curl -i -H \"Content-Type: application/json\" -X PUT -d '{\"question\":\"来话人是成龙大道蓝润锦江春天小区的业主，反映小区8栋附近有一垃圾处理厂，经常在深夜处理垃圾，机器产生严重噪音，请处理。\"}' http://172.18.0.171:8000/todo/api/v1.0/tasks/1")

t2 = time.time()
print(t2-t1)
