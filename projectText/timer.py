#coding:utf-8

import threading
import time

def fun_timer():
    print ("hello ..")
    global timer
    timer = threading.Timer(5,fun_timer)
    timer.start()

timer = threading.Timer(1,fun_timer)
timer.start()

