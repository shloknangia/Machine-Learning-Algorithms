#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# training on only 1% of the full training set
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
clf = SVC(kernel="rbf")
clf = SVC(C = 10000.0)
t0 = time()
clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")
t1 = time()
pred = clf.predict(features_test)
print ("predicting time:", round(time()-t1, 3), "s")
# to count no of 1's
count = 0
for i in range(len(pred)):
	if(pred[i] == 1):
		count = count + 1

print(count)
from sklearn.metrics import accuracy_score
print (accuracy_score(pred,labels_test))
#########################################################
### your code goes here ###

#########################################################


