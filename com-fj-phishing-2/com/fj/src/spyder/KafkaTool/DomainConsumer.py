# -*-coding:utf-8-*-
# !/usr/bin/env python
import threading
from DetectData import DetectData

from kafka import KafkaConsumer


class DomainConsumer(threading.Thread):
    def __init__(self, threadName, keyName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.keyName = keyName

    def run(self):
        receiveinfo(self.threadName, self.keyName)


def receiveinfo(threadName, keyName):
    queues = []
    print("fyi")

    consumerUrl = KafkaConsumer("domain",
                                bootstrap_servers=['172.23.26.222:9091', '172.23.26.222:9092', '172.23.26.223:9091',
                                                   '172.23.26.223:9092'])



    container = DetectData().readUrl(consumerUrl)
