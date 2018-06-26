#!/usr/bin/env python

__author__ = 'qianhuhai'
import os


projectPath=os.getcwd()
def getlabel1(param):
     l=[]
     c=[]
     for i,j in enumerate(param):
          if j=="1":
              l.append(i)

     with open(projectPath+"/data/web-content","r") as G:
               for m,n in  enumerate(G.readlines()):
                   if m in l:
                       c.append(n)
     with open(projectPath+"/data/"+"/"+"putsql.txt","w") as F:
                        for x in c:
                           F.write(x.strip()+'\n')
