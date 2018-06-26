# _*_ coding=utf-8 _*_

import sys
import os
projectPath=os.getcwd()
# sys.path.append(projectPath)
from sklearn.feature_extraction.text import TfidfVectorizer
from com.fj.src.algorithm.model_train import ModelRun




corpus=[]
L=[]
g=open(projectPath+"/data/unknowndata01.txt","r")

for cc in g.readlines():
     l, words = cc.strip('\n\r').split(',')
     corpus.append(words)
     L.append(l)
vectorizer = TfidfVectorizer(sublinear_tf=True,max_df=0.5,max_features=1000)

tfidf = vectorizer.fit_transform(corpus)

vocabulary=vectorizer.vocabulary_

with open(projectPath+"/data/vocabulary.txt", "w") as h:
    h.write(str(vocabulary))

ModelRun.ModelRun(tfidf, L)

g.close()