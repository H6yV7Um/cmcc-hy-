# _*_ coding=utf-8 _*_
import os

box=[]
boxes=[]


projectPath=os.getcwd()
def dataExtract():
    f=open(projectPath+"/data/unknowndata03.txt",'w')
    for dirs,dirlist,filelist in os.walk(projectPath+"/html2/"):
      for file in filelist:
        box=[]
        filename=os.path.join(dirs+file)
        e = open(filename, 'r')
        text=e.readlines()
        for i in text:
            box.append(i.strip("\n\r"))
        a=' '.join(box)
        boxes.append(a)
    #


    for i in boxes:
        f.write(i+'\n')
    f.close()