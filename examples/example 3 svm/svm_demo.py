'''from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)  
clf.predict([[2., 2.]])'''


import sys
from class_viz import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel="rbf")
#can be poly,rbf,linear etc...
clf = SVC(C=1000.0)
# more C more training points correct( use in rbf case)
clf = SVC(gamma=1000.0)
# more gamma more training points correct( use in rbf case)

clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data



#### store your predictions in a list named pred





from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)
def submitAccuracy():
    return acc