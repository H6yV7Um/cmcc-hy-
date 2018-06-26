
# _*_ coding=utf-8 _*_

import re
import os
import jieba
import traceback

projectPath=os.getcwd()
def getChineseContent(raw_page_content):
    raw_page_content_1 = raw_page_content.decode("utf-8").encode('unicode_escape').decode('unicode_escape') #str

    content_list_encode = []
    content_list = re.findall(u"[\u4e00-\u9fa5]+", raw_page_content_1)

    for line in content_list:


          if len(line)>6: #如果词语长度大于１０，则进行分词，
                smallLine=jieba.cut(line)
                text=','.join(smallLine)

          else:
                text=line

          content_list_encode.append(text)

    return ",".join(content_list_encode)


if not os.path.exists(projectPath+'/html2'):
    os.makedirs(projectPath+'/html2')
def dataQingXi():
    f = open(projectPath+"/data/web-content", 'r')
    for line in f.readlines():
        try:
            hostname, ip, ipBelong, firstVisitTime, lastestVisitTime, userSet, visitNum, similarityValue, imitate,\
                     md5_filename= line.strip("\r\n").split(',')
            filepath = md5_filename.strip("\r\n").replace("'","").replace(" ","")
            e = open(projectPath+"/html" + "/" + filepath,
                     'rb')

            zh = getChineseContent(e.read())

            # zh1 = jieba.cut(zh)
            # text = ','.join(zh1)
            # # print label,id,text
            # c = open("I:\Users\qianhuhai\PycharmProjects\com-fj-phishing-1.0\com\\fj\data\\unknown" + "\\" + filepath, "wb")
            # t = text.strip().split(",")
            # c.write(label.encode('utf-8') + ',' + '\n')
            # for i in t:
            #     c.write(i.encode("utf-8") + '\n')
            c = open(projectPath+"/html2" + "/" + filepath, "w")

            t = zh.strip().split(",")


            for i in t:
                c.write(i + '\n')

            e.close()
            c.close()
        except :
            traceback.print_exc()

    f.close()