# _*_ coding=utf-8 _*_

import re

f=open("/home/qianhuhai/Documents/PycharmProjects/com-fj-phishing-2/com/fj/src/white_list/result.txt",'r')
L=[]
with open("/home/qianhuhai/Documents/PycharmProjects/com-fj-phishing-2/com/fj/src/white_list/white_list.txt",
          'w') as g:
   for i in f.readlines():
       j=i.strip('\r\n')
       l2=re.search('[0-9A-Za-z]+\.[0-9A-Za-z]+\.[0-9A-Za-z]+', j)
       l3 = re.search('[0-9A-Za-z]+\.[0-9A-Za-z]+', j)
       l1 = re.search('[0-9A-Za-z]+\.[0-9A-Za-z]+\.[0-9A-Za-z]+\.[0-9A-Za-z]+', j)
       if l1 :
           print(l1.group())

           L.append(l1)
       elif l2:
               print(l2.group())

               L.append(l2)
       elif l3:
           print(l3.group())
           L.append(l3)
       else:
           print("no urls")
   for l in L:

       url=l[0]
       # print(url)
       g.write(url+'\n')

f.close()