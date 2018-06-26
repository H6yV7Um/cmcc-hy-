# _*_ coding=utf-8 _*_

import re
import os
import jieba
import traceback
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


projectPath=os.getcwd()
if not os.path.exists(projectPath+'/unknown'):
    os.makedirs(projectPath+'/unknown')


f = open(projectPath+"/data/file_list_03.txt", 'r')
for line in f:
    try:
        label, url, file_name = line.strip("\r\n").split(',')
        filepath = file_name.strip("\r\n")
        e = open(projectPath+"/file_02" + "/" + filepath,
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
        c = open(projectPath+"/unknown" + "/" + filepath, "w")

        t = zh.strip().split(",")

        c.write(label + ',' + '\n')
        for i in t:
            c.write(i + '\n')

        e.close()
        c.close()
    except :
        traceback.print_exc()

f.close()