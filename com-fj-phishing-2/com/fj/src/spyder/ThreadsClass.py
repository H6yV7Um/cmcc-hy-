# -*- coding: utf-8 -*-
#!/usr/bin/env python
import threading
import time
from  .ContentGetHtml import ContentGetHtml
url1=[]
url2=[]
returned_p_result_filter=[]
threadLock = threading.Lock()
class MyThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # print "Starting " + self.name
        myThread(self.threadID, self.name, self.url)

        # print "Exiting " + self.name

def myThread(tn,c,data):
    print("start")

    ContentGetHtml().run(data)
    print("end")