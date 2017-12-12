#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0 )
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.xlim(0, 0.5e7)
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.ylim(-0.2e7, 0.4e8)
matplotlib.pyplot.show()


# for k in data_dict:
#     if (data_dict[k]['bonus'] > 5000000 and data_dict[k]['bonus'] != 'NaN') and (data_dict[k]['salary'] > 1000000 and data_dict[k]['salary'] != 'NaN'):
#         print k


max1 = 0
max2 = 0
k = ' '
for i in data_dict:
	if (data_dict[i]['bonus'] > max1 and data_dict[i]['bonus'] != 'NaN') and (data_dict[i]['salary'] > max2 and data_dict[i]['salary'] != 'NaN'):
		max1 = data_dict[i]['bonus']
		max2 = data_dict[i]['salary']
		k = i
print k
