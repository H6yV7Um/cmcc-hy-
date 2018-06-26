# _*_ coding=utf-8 _*_

import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import traceback
from com.fj.src.algorithm.model_predict import DataQingXi
from com.fj.src.algorithm.model_predict import GetLabel1data, DataExtract

projectPath=os.getcwd()
corpus=[]
label=[]
def modelrun():
  DataQingXi.dataQingXi()
  DataExtract.dataExtract()
  with open(projectPath+'/data/vocabulary.txt','r')  as f:
      a = f.read()
      vocabulary = eval(a)


  g=open(projectPath+"/data/unknowndata03.txt","r")
  for cc in g.readlines():
       corpus.append(cc.strip('\r\n'))

  vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,vocabulary=vocabulary)
  tfidf= vectorizer.fit_transform(corpus)

  train_X = tfidf

  try:
       with open(projectPath+"/model/clf.pkl",'rb') as h:
           clf=pickle.load(h)

       predicted = clf.predict(train_X)

       GetLabel1data.getlabel1(predicted)
  except :
    traceback.print_exc()

