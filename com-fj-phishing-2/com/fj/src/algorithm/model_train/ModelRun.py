# _*_ coding=utf-8 _*_

from sklearn.model_selection import train_test_split
import pickle
from xgboost import XGBClassifier
from sklearn import metrics
import os
from sklearn.naive_bayes import MultinomialNB

projectPath=os.getcwd()
if not os.path.exists(projectPath+'/model'):
    os.makedirs(projectPath+'/model')
def  ModelRun(x,y):

   train_X,test_X, train_y, test_y = train_test_split(x,
                                                   y,
                                                   test_size = 0.2,
                                                   random_state = 0)

   x = 0
   for i, j in enumerate(test_y):
       if j == '1':
           x = x + 1

   nb=MultinomialNB(alpha=0.001)
   clf=nb.fit(train_X,train_y)
   predicted = clf.predict(test_X)

   metrics_result(test_y,predicted)
   print(metrics.confusion_matrix(test_y, predicted))

   with open(projectPath+"/model/clf.pkl", 'wb') as K:
       pickle.dump(clf, K)

def metrics_result(actual, predict):
    print('精度:{0:.3f}'.format(metrics.precision_score(actual, predict,average='weighted')))
    print('召回:{0:0.3f}'.format(metrics.recall_score(actual, predict,average='weighted')))
    print('f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict,average='weighted')))


