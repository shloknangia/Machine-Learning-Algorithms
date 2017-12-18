'''from sklearn import tree
X = [[0,0],[1,1]]
Y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

clf.predict([[2.,2.]])'''


#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_viz import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


from sklearn import tree
### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!

clf = tree.DecisionTreeClassifier(min_samples_split = 50)
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)





#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())


from sklearn.metrics import accuracy_score
print(accuracy_score(pred,labels_test))
