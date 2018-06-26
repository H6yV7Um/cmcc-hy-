# -*- coding: utf-8 -*-
import threading
import time
from com.fj.src.spyder.ThreadsClass import MyThread
from .ContentGet_360 import ContentGetHtml1


class MyThread1(MyThread):
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # print "Starting " + self.name
        myThread(self.threadID, self.name, self.url)

        # print "Exiting " + self.name


def myThread(tn, c, data):
    print("start")

    ContentGetHtml1().run(data)
    ContentGetHtml1().run1(data)
    print("end")

