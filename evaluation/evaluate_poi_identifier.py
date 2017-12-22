#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features, labels)
print clf.score(features, labels)

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)
clf.fit(x_train, y_train)
print clf.score(x_test, y_test)
print x_test, y_test
print len(x_test), len(y_test)

pred = clf.predict(x_test)
count = 0
for i in range(len(y_test)):
	if pred[i] == y_test[i]:
		count += 1

print count		

from sklearn import metrics
print metrics.precision_score(y_test, pred)
print metrics.recall_score(y_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]	
print metrics.confusion_matrix(predictions, true_labels)
print metrics.precision_score(true_labels, predictions)
print metrics.recall_score(true_labels, predictions)
