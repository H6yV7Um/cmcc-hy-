# _*_ coding=utf-8 _*_


# load_jieba('/Users/qianhuhai/PycharmProjects/com-fj-model-02/src/data/finance.txt')
import re
import os

projectPath=os.getcwd()
corpus=[]
g=open(projectPath+"/data/unknowndata01.txt",'w')
with open(projectPath+"/data/unknowndata.txt",'r') as f:
     for i in f.readlines():
         label,value=i.split(',')
         if value.strip()!='':
           if label=='1':
             corpus.append("1," + value)
             corpus.append("1," + value)
           else:
             corpus.append("0," + value)
for i in corpus:

    g.write(i)