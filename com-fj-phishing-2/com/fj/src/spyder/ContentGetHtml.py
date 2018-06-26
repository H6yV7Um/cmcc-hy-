# -*- coding: utf-8 -*-

#这是通过splash的方式
from urllib import request
import re
import hashlib
import traceback
import socket
import os
import threading

timeout = 5
socket.setdefaulttimeout(timeout)  #设置超时
projectPath=os.getcwd()
#
#源码分析类
#
class ContentGetHtml():
    def __init__(self):
        #对输入的list进行格式化，去除http://,https://
        self.url_format = []
        self.html_vector = []
        self.result = []
        self.record=[]
        self.count=0
        self.l = []
#
#对比源码内容，查看敏感词
#
    def run(self,param):

      #获取相应的根目录
      if not os.path.exists(projectPath + '/data'):
          os.makedirs(projectPath + '/data')
      if not os.path.exists(projectPath+'/html'):
            os.makedirs(projectPath+'/html')
      if not os.path.exists(projectPath+'/png'):
          os.makedirs(projectPath+'/png')
          
      for i in param:
        hostname, ip, ipBelong, firstVisitTime,lastestVisitTime, userSet, visitNum ,similarityValue,imitate= i.strip('\r\n').split(";")
        print(hostname)
        try:
              detect_url = "url=http://" + hostname.strip('\n\r')  ###
              params_html = "&wait=0.5"  ###

              splash_url_html = "http://172.18.2.67:8050/render.html?"###
              oneUrlHtml = splash_url_html + detect_url +params_html                          ###

              url_request = request.Request(oneUrlHtml)
              html = request.urlopen(url_request).read().decode("utf-8")  # str
              html1 = html.encode("unicode_escape")  # bytes
              

              params_png = "&render_all=0&wait=0.5"  ###
              splash_url_png = "http://172.18.2.67:8050/render.png?"  ###
              oneUrlPng = splash_url_png + detect_url + params_png  ###
              url_request = request.Request(oneUrlPng)  ###query下载图片
              png=request.urlopen(url_request).read()
              print(type(png))



              if html1 != '':  # 如果文本非空，才保存

              # found_sensitive_words=keyword_processor.extract_keywords(returned_url_request_unicode)
              # found_sensitive_words_len=len(found_sensitive_words)
                  hostname_encode = hostname.encode("unicode_escape")  # bytes
                  hmd = hashlib.md5()  #
                  hmd.update(hostname_encode)  # 生成文件的MD5值，MD5是一种哈希算法
                  md5_filename = hmd.hexdigest()  #
                  with open(projectPath+"/html" + "/" + md5_filename,
                            "w") as K:
                      K.write(html)
           #       with open("/home/hadoop/qianhuhai/com-fj-phishing-2/png" + "/" + md5_filename,
           #                 "w") as J:
           #           J.write(png.content)


                  with open(projectPath+"/png" + "/" + md5_filename,
                            "wb") as J:
                      J.write(png)
                  self.l.append([hostname, ip, ipBelong, firstVisitTime, lastestVisitTime, userSet, visitNum,
                             similarityValue, imitate, md5_filename])
              # if found_sensitive_words_len>1:
              #         self.result.append(1)
              # else:
              #         self.result.append(0)
              #for black_word in black_words:     ###
              #  word=black_word.strip('\n\r')###
              #  regex=unicode(word,"utf-8")###
              #  if  re.findall(regex,unicode(returned_url_request_unicode,"utf-8")) :###正则匹配的方法
              #      result.append(1)###
              #  result.append(0)###
        except :
               traceback.print_exc()
              # self.result.append(0)
      ###result=[0,1,0,1,...]  len(result)=len(self.url_list)
      with open(projectPath+"/data/web-content", "a") as L:
          for i in self.l:
              L.write(str(i).strip("[]") + '\n')
      return "scrapy end"


#
# if __name__ == '__main__':
#         param=["tk.haotibang.com;101.200.86.162:80;其他;0;1526426870510;1;18;0.5625;taobao.com"
#             ,"zs.ylzpay.com;202.101.157.200:8060;其他;0;1526426405595;1;4;0.61538464;alipay.com"
#                ,"zf.crv.com.cn;120.192.82.239:80;其他;0;1526427860332;1;5;0.61538464;cmbc.com.cn"
#                ,"tech.cpic.com.cn;117.131.74.128:80;其他;0;1526428690318;5;18;0.625;epicc.com.cn"
#                ,"www.100585.cn;47.90.53.47:80;其他;0;1526427560271;3;46;0.53846157;10086.cn"]
#         ContentGetHtml().cmpWebHtml(param=param)