# -*- coding: utf-8 -*-


from com.fj.src.spyder.ThreadsClass import MyThread
import os,sys

projectPath=os.getcwd()
sys.path.append(projectPath)

from com.fj.src.spyder.AsynchronousCrawler import AsynchronousCrawlerTxt


class WebScanProbe (AsynchronousCrawlerTxt):
    def readUrl(self, domainInfo):
        container = []
        threads = []

        url1 = []
        url2 = []
        url3 = []
        url4 = []
        url5 = []
        url6 = []
        url7 = []
        url8 = []
        url9 = []
        url10 = []
        url11 = []
        url12 = []
        url13 = []
        url14 = []
        url15 = []
        url16 = []
        url17 = []
        url18 = []
        url19 = []
        url0 = []

        infoLen=len(domainInfo)

         #domainInfo=["a","b","c"]


        for id, urls in enumerate(domainInfo):
            threadsNumber=int(id %20)
            print(threadsNumber)
            if threadsNumber==1:
              url1.append(urls)
            elif threadsNumber==2:
              url2.append(urls)
            elif threadsNumber==3:
              url3.append(urls)
            elif threadsNumber==4:
              url4.append(urls)
            elif threadsNumber==5:
              url5.append(urls)
            elif threadsNumber==6:
              url6.append(urls)
            elif threadsNumber==7:
              url7.append(urls)
            elif threadsNumber==8:
              url8.append(urls)
            elif threadsNumber==9:
              url9.append(urls)
            elif threadsNumber==9:
              url9.append(urls)
            elif threadsNumber==10:
              url10.append(urls)
            elif threadsNumber==11:
              url11.append(urls)
            elif threadsNumber==12:
              url12.append(urls)
            elif threadsNumber==13:
              url13.append(urls)
            elif threadsNumber==14:
              url14.append(urls)
            elif threadsNumber==15:
              url15.append(urls)
            elif threadsNumber==16:
              url16.append(urls)
            elif threadsNumber==17:
              url17.append(urls)
            elif threadsNumber==18:
              url18.append(urls)
            elif threadsNumber==19:
              url19.append(urls)
            else :
              url0.append(urls)

        thread = MyThread(1, "Thread-1", url1)
        threads.append(thread)
        thread = MyThread(2, "Thread-2", url2)
        threads.append(thread)
        thread = MyThread(3, "Thread-3", url3)
        threads.append(thread)
        thread = MyThread(4, "Thread-4", url4)
        threads.append(thread)
        thread = MyThread(5, "Thread-5", url5)
        threads.append(thread)
        thread = MyThread(6, "Thread-6", url6)
        threads.append(thread)
        thread = MyThread(7, "Thread-7", url7)
        threads.append(thread)
        thread = MyThread(8, "Thread-8", url8)
        threads.append(thread)
        thread = MyThread(9, "Thread-9", url9)
        threads.append(thread)
        thread = MyThread(10, "Thread-10", url10)
        threads.append(thread)
        thread = MyThread(11, "Thread-11", url11)
        threads.append(thread)
        thread = MyThread(12, "Thread-12", url12)
        threads.append(thread)
        thread = MyThread(13, "Thread-13", url13)
        threads.append(thread)
        thread = MyThread(14, "Thread-14", url14)
        threads.append(thread)
        thread = MyThread(15, "Thread-15", url15)
        threads.append(thread)
        thread = MyThread(16, "Thread-16", url16)
        threads.append(thread)
        thread = MyThread(17, "Thread-17", url17)
        threads.append(thread)
        thread = MyThread(18, "Thread-18", url18)
        threads.append(thread)
        thread = MyThread(19, "Thread-19", url19)
        threads.append(thread)
        thread = MyThread(0, "Thread-0", url0)
        threads.append(thread)

        for i in threads:
            i.start()

        for i in threads:
            i.join()


if __name__ == '__main__':
    g = open(projectPath+"/data/part-r-00000", 'r')
    param = []
    for i in g.readlines():
        ki, vl = i.split('\t')

        param.append(vl.strip("\r\n"))
    print(param)
    # param=["tk.haotibang.com;101.200.86.162:80;其他;0;1526426870510;1;18;0.5625;taobao.com"
    # ,"zs.ylzpay.com;202.101.157.200:8060;其他;0;1526426405595;1;4;0.61538464;alipay.com"
    #    ,"zf.crv.com.cn;120.192.82.239:80;其他;0;1526427860332;1;5;0.61538464;cmbc.com.cn"
    #    ,"tech.cpic.com.cn;117.131.74.128:80;其他;0;1526428690318;5;18;0.625;epicc.com.cn"
    #    ,"www.100585.cn;47.90.53.47:80;其他;0;1526427560271;3;46;0.53846157;10086.cn"
    #    ]
    WebScanProbe().readUrl(domainInfo=param)

    g.close()