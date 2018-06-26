# -*-coding:utf-8-*-
import chardet
import pymysql
import sys
import os
import re
import time
import datetime
# sys.path.extend(['/home/qianhuhai/Documents/PycharmProjects/com-fj-phishing-2'])
# print(os.getcwd())
projectPath=os.getcwd()
# 打开数据库连接
db = pymysql.connect(host="172.28.19.238", user="AthenaR",
                     password="GYzKyTeB", db="tele_fraud", port=33061, charset='utf8')
cur = db.cursor()
f=open(projectPath+"/web_scan_probe/web-content",'r')
for i in f.readlines():
    hostname, ip, ipBelong, firstVisitTime, lastestVisitTime, userSet, visitNum, similarityValue, imitate,md5_filename,level\
        =i.strip('\r\n').split(',')

    userSet=userSet.strip(' ').replace("'",'')
    visitNum = visitNum.strip(' ').replace("'", '')
    hostname = hostname.strip(' ').replace("'", '')
    ip = ip.strip(' ').replace("'", '')
    imitate=imitate.strip(' ').replace("'", '')
    md5_filename = md5_filename.strip(' ').replace("'", '')
    lastestVisitTime=lastestVisitTime.strip(' ').replace("'", '')

    strUserSet=int(userSet)
    strVisitNum=int(visitNum)
    strHostName=hostname
    strIp=ip
    strImitate=imitate
    strMd5_Filename= 'png/'+md5_filename
    lastestVisitTime=int(lastestVisitTime)
    lastestVisitTime=int(lastestVisitTime/1000)

    found_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    time_local = time.localtime(lastestVisitTime)

    lastTime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    ipBelong=ipBelong.strip(' ').replace("'",'').encode('utf-8').decode('utf-8')

    # strIpBelong=ipBelong.encode('GB2312').decode('utf-8')
    # print(strIpBelong)

    cur.execute("""insert into t_fraud_web_phish(id,domain,ip,ip_belongs,found_time,last_time,user_num,count,imitate,evidence_link)
         values(null,'%s', '%s', '%s', '%s', '%s', '%d', '%d', '%s', '%s')"""
                % ( strHostName, strIp,ipBelong ,found_time ,
                    lastTime, strUserSet, strVisitNum,  strImitate, strMd5_Filename))

    # cur.execute("""insert into t_mcws_web_phishing(id,domain,ip,ip_belongs,found_time,last_time,count,user_count,imitate,evidence_link,handle)
    #  values(NULL ,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')"""
    #             % (hostname, ip, ipBelong, firstVisitTime, lastestVisitTime, userSet, visitNum, similarityValue, imitate,md5_filename))

    db.commit()
cur.close()
db.close()
